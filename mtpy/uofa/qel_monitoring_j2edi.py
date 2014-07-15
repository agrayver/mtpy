#!/usr/bin/env python

"""
Convert the BIRPP output (j-file) into an EDI file.

Assume that the j-file is name coded not only by station but also by date.
Parse the given directory for a j-file of the given station. Strip its name off the date
information, convert it to an EDI.
Then read in the new EDI, add the date information to the header and save it under a new name,
which contains the date again. Then discard the intermediate EDI file.

"""


import os,sys
import os.path as op

import mtpy.core.edi as MTedi
import mtpy.utils.convert_birrp_output as MTbp
import pdb
import numpy as np
import mtpy.utils.exceptions as MTex


def main():
    print 
    if len(sys.argv) < 4:
        sys.exit('\nNeed at least 4 arguments:\n '
                '<stationname> \n <path to Birrp output files> \n '
                '<survey config file>  <instrument response file> \n'
                '[string to be stripped from the filename]\n\n')
        
    stationname = sys.argv[1].upper()
    datadir = sys.argv[2]
    survey_cfg_fn = sys.argv[3]
    instr_resp_fn = sys.argv[4]
    string2strip = None

    if len(sys.argv) > 4:
        string2strip = sys.argv[4]

    if not op.isdir(datadir):
        print '\tERROR - Data directory does not exist: {0}\n'.format(datadir)
        sys.exit()

    try:
        survey_cfg_fn = op.realpath(op.abspath(op.join(os.curdir,survey_cfg_fn)))
        if not op.isfile(survey_cfg_fn):
            raise
    except:
        print '\tERROR - Config file does not exist: {0}\n'.format(survey_cfg_fn)
        sys.exit()

    try:
        instr_resp_fn = op.realpath(op.abspath(op.join(os.curdir,instr_resp_fn)))
        if not op.isfile(instr_resp_fn):
            raise
    except:
        print '\tERROR - Instrument response file does not exist: {0}\n'.format(instr_resp_fn)
        sys.exit()

        
    convert2edi(stationname,datadir,survey_cfg_fn,instr_resp_fn, string2strip)
    

def convert2edi(station,directory,survey_configfile,instrument_response_file, string2strip=None):

    basedir = op.abspath(os.curdir)
    #name of intermediate coherence file:
    infn_coh = '{0}.coh'.format(station.upper())

    os.chdir(directory)
    print 
    print station,directory, survey_configfile,None,instrument_response_file
    print 
    edifn,cohfn=MTbp.convertbirrpoutput(station,directory,
                                survey_configfile,None,instrument_response_file)
    if edifn is None:
        print 
        try:
            os.remove(infn_coh)
        except:
            pass
        os.chdir(basedir)
        raise MTex.MTpyError_processing('\tERROR - could not write EDI file - check j-file!\n')
        #sys.exit()

    #parse the folder, find the j-file used before (the first one matching the 
    #specs), and determine the date from its name by stripping off the station names
    j_filename_list = [i for i in os.listdir(directory) if op.basename(i).upper().endswith('.j'.upper())]
    j_filename_list = [i for i in j_filename_list if 
                    '{0}'.format(station.upper()) in op.basename(i).upper() ]

    j_file = j_filename_list[0].upper()
    dateinfo = j_file.replace('.J','')
    dateinfo = dateinfo.replace(station.upper(),'')
    
    #TODO : automatise these two steps if possible...!!!
    #...maybe by agreeing on a common format for the date...??
    dateinfo = dateinfo.replace('_RR_B125_','')
    if string2strip is not None:
        dateinfo = dateinfo.replace(string2strip.upper(),'')

    #split the date information
    dateinfo =  dateinfo.split('-')

    try:
        day = int(float(dateinfo[0]))
        month = dateinfo[1].lower()
        month_num = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,
                        'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12,}[month]
        year = 14

    except:
        day = 0
        month_num = 0 
        year = 0

    # re read the edi file:
    e_object = MTedi.Edi(filename=edifn)
    e_object.head['loc'] = 'roma'
    e_object.head['acqby']='UofA'
    e_object.head['acqdate']='2014/{0:02d}/{1:02d}'.format(month_num,day)

    outfn_base = 'roma_{3:02d}{0:02d}{1:02d}_{2}'.format(month_num,day,station.upper(),year)
    outfn = outfn_base+'.edi'
    try:
        outfn_true = e_object.writefile(outfn,allow_overwrite=True, use_info_string=True)
        if outfn_true is None:
            raise
        print 'EDI file written: {0}\n'.format(outfn_true)
    except:
        print '\tERROR - could not write final EDI file {0}\n'.format(outfn)
    
    outfn = outfn_true

    #rename coherence file accordingly:
    outfn_coh = outfn_base+'.coh'

    try:
        os.rename(infn_coh,outfn_coh)
    except:
        print 'Warning - could not find coherence file: {0}'.format(infn_coh)


    
    #rename j file, so that another one can be found and processed, if this code
    # is called within a loop:
    os.rename(j_filename_list[0],j_filename_list[0]+'.done')
    
    #remove intermediate EDI file
    os.remove(edifn)

    os.chdir(basedir)

    return outfn,outfn_coh





if __name__=='__main__':
    main()