# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_modem_export.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_Export_ModEm(object):
    def setupUi(self, Dialog_Export_ModEm):
        Dialog_Export_ModEm.setObjectName(_fromUtf8("Dialog_Export_ModEm"))
        Dialog_Export_ModEm.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog_Export_ModEm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog_Export_ModEm)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox_error_type = QtGui.QComboBox(self.groupBox)
        self.comboBox_error_type.setObjectName(_fromUtf8("comboBox_error_type"))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.addItem(_fromUtf8(""))
        self.comboBox_error_type.setItemText(7, _fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_error_type, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBox_zxx = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_zxx.sizePolicy().hasHeightForWidth())
        self.checkBox_zxx.setSizePolicy(sizePolicy)
        self.checkBox_zxx.setObjectName(_fromUtf8("checkBox_zxx"))
        self.gridLayout_2.addWidget(self.checkBox_zxx, 0, 0, 1, 1)
        self.checkBox_zxy = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_zxy.sizePolicy().hasHeightForWidth())
        self.checkBox_zxy.setSizePolicy(sizePolicy)
        self.checkBox_zxy.setObjectName(_fromUtf8("checkBox_zxy"))
        self.gridLayout_2.addWidget(self.checkBox_zxy, 1, 0, 1, 1)
        self.comboBox_error_type_zxx = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_error_type_zxx.setObjectName(_fromUtf8("comboBox_error_type_zxx"))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxx.setItemText(7, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_error_type_zxx, 0, 1, 1, 1)
        self.comboBox_error_type_zxy = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_error_type_zxy.setObjectName(_fromUtf8("comboBox_error_type_zxy"))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zxy.setItemText(7, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_error_type_zxy, 1, 1, 1, 1)
        self.comboBox_error_type_zyx = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_error_type_zyx.setObjectName(_fromUtf8("comboBox_error_type_zyx"))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyx.setItemText(7, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_error_type_zyx, 2, 1, 1, 1)
        self.comboBox_error_type_zyy = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_error_type_zyy.setObjectName(_fromUtf8("comboBox_error_type_zyy"))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.addItem(_fromUtf8(""))
        self.comboBox_error_type_zyy.setItemText(7, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_error_type_zyy, 3, 1, 1, 1)
        self.checkBox_zyx = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_zyx.sizePolicy().hasHeightForWidth())
        self.checkBox_zyx.setSizePolicy(sizePolicy)
        self.checkBox_zyx.setObjectName(_fromUtf8("checkBox_zyx"))
        self.gridLayout_2.addWidget(self.checkBox_zyx, 2, 0, 1, 1)
        self.checkBox_zyy = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_zyy.sizePolicy().hasHeightForWidth())
        self.checkBox_zyy.setSizePolicy(sizePolicy)
        self.checkBox_zyy.setObjectName(_fromUtf8("checkBox_zyy"))
        self.gridLayout_2.addWidget(self.checkBox_zyy, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog_Export_ModEm)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox.raise_()
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog_Export_ModEm)
        self.comboBox_error_type.setCurrentIndex(2)
        self.comboBox_error_type_zxx.setCurrentIndex(2)
        self.comboBox_error_type_zxy.setCurrentIndex(2)
        self.comboBox_error_type_zyx.setCurrentIndex(2)
        self.comboBox_error_type_zyy.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Export_ModEm)

    def retranslateUi(self, Dialog_Export_ModEm):
        Dialog_Export_ModEm.setWindowTitle(_translate("Dialog_Export_ModEm", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog_Export_ModEm", "Data", None))
        self.comboBox_error_type.setItemText(0, _translate("Dialog_Export_ModEm", "floor", None))
        self.comboBox_error_type.setItemText(1, _translate("Dialog_Export_ModEm", "value", None))
        self.comboBox_error_type.setItemText(2, _translate("Dialog_Export_ModEm", "egbert", None))
        self.comboBox_error_type.setItemText(3, _translate("Dialog_Export_ModEm", "egbert (floor)", None))
        self.comboBox_error_type.setItemText(4, _translate("Dialog_Export_ModEm", "stddev", None))
        self.comboBox_error_type.setItemText(5, _translate("Dialog_Export_ModEm", "square error", None))
        self.comboBox_error_type.setItemText(6, _translate("Dialog_Export_ModEm", "mean square error", None))
        self.label.setText(_translate("Dialog_Export_ModEm", "Error Type", None))
        self.groupBox_3.setTitle(_translate("Dialog_Export_ModEm", "Component Error Type", None))
        self.checkBox_zxx.setText(_translate("Dialog_Export_ModEm", "zxx", None))
        self.checkBox_zxy.setText(_translate("Dialog_Export_ModEm", "zxy", None))
        self.comboBox_error_type_zxx.setItemText(0, _translate("Dialog_Export_ModEm", "floor", None))
        self.comboBox_error_type_zxx.setItemText(1, _translate("Dialog_Export_ModEm", "value", None))
        self.comboBox_error_type_zxx.setItemText(2, _translate("Dialog_Export_ModEm", "egbert", None))
        self.comboBox_error_type_zxx.setItemText(3, _translate("Dialog_Export_ModEm", "egbert (floor)", None))
        self.comboBox_error_type_zxx.setItemText(4, _translate("Dialog_Export_ModEm", "stddev", None))
        self.comboBox_error_type_zxx.setItemText(5, _translate("Dialog_Export_ModEm", "square error", None))
        self.comboBox_error_type_zxx.setItemText(6, _translate("Dialog_Export_ModEm", "mean square error", None))
        self.comboBox_error_type_zxy.setItemText(0, _translate("Dialog_Export_ModEm", "floor", None))
        self.comboBox_error_type_zxy.setItemText(1, _translate("Dialog_Export_ModEm", "value", None))
        self.comboBox_error_type_zxy.setItemText(2, _translate("Dialog_Export_ModEm", "egbert", None))
        self.comboBox_error_type_zxy.setItemText(3, _translate("Dialog_Export_ModEm", "egbert (floor)", None))
        self.comboBox_error_type_zxy.setItemText(4, _translate("Dialog_Export_ModEm", "stddev", None))
        self.comboBox_error_type_zxy.setItemText(5, _translate("Dialog_Export_ModEm", "square error", None))
        self.comboBox_error_type_zxy.setItemText(6, _translate("Dialog_Export_ModEm", "mean square error", None))
        self.comboBox_error_type_zyx.setItemText(0, _translate("Dialog_Export_ModEm", "floor", None))
        self.comboBox_error_type_zyx.setItemText(1, _translate("Dialog_Export_ModEm", "value", None))
        self.comboBox_error_type_zyx.setItemText(2, _translate("Dialog_Export_ModEm", "egbert", None))
        self.comboBox_error_type_zyx.setItemText(3, _translate("Dialog_Export_ModEm", "egbert (floor)", None))
        self.comboBox_error_type_zyx.setItemText(4, _translate("Dialog_Export_ModEm", "stddev", None))
        self.comboBox_error_type_zyx.setItemText(5, _translate("Dialog_Export_ModEm", "square error", None))
        self.comboBox_error_type_zyx.setItemText(6, _translate("Dialog_Export_ModEm", "mean square error", None))
        self.comboBox_error_type_zyy.setItemText(0, _translate("Dialog_Export_ModEm", "floor", None))
        self.comboBox_error_type_zyy.setItemText(1, _translate("Dialog_Export_ModEm", "value", None))
        self.comboBox_error_type_zyy.setItemText(2, _translate("Dialog_Export_ModEm", "egbert", None))
        self.comboBox_error_type_zyy.setItemText(3, _translate("Dialog_Export_ModEm", "egbert (floor)", None))
        self.comboBox_error_type_zyy.setItemText(4, _translate("Dialog_Export_ModEm", "stddev", None))
        self.comboBox_error_type_zyy.setItemText(5, _translate("Dialog_Export_ModEm", "square error", None))
        self.comboBox_error_type_zyy.setItemText(6, _translate("Dialog_Export_ModEm", "mean square error", None))
        self.checkBox_zyx.setText(_translate("Dialog_Export_ModEm", "zyx", None))
        self.checkBox_zyy.setText(_translate("Dialog_Export_ModEm", "zyy", None))
        self.groupBox_2.setTitle(_translate("Dialog_Export_ModEm", "Mesh", None))

