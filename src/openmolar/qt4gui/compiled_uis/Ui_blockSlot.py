#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar1/src/openmolar/qt-designer/blockSlot.ui'
#
# Created: Wed Nov  6 23:05:24 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(345, 361)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 2, 1)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(
            20,
            34,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.blockStart_frame = QtGui.QFrame(self.tab)
        self.blockStart_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.blockStart_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.blockStart_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.blockStart_frame.setObjectName(_fromUtf8("blockStart_frame"))
        self.gridLayout.addWidget(self.blockStart_frame, 1, 1, 1, 1)
        self.blockEnd_frame = QtGui.QFrame(self.tab)
        self.blockEnd_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.blockEnd_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.blockEnd_frame.setObjectName(_fromUtf8("blockEnd_frame"))
        self.gridLayout.addWidget(self.blockEnd_frame, 2, 1, 1, 1)
        self.length_label = QtGui.QLabel(self.tab)
        self.length_label.setAlignment(QtCore.Qt.AlignCenter)
        self.length_label.setObjectName(_fromUtf8("length_label"))
        self.gridLayout.addWidget(self.length_label, 1, 2, 2, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 4)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 3)
        self.pt_label = QtGui.QLabel(self.tab_2)
        self.pt_label.setMinimumSize(QtCore.QSize(0, 50))
        self.pt_label.setTextFormat(QtCore.Qt.AutoText)
        self.pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pt_label.setObjectName(_fromUtf8("pt_label"))
        self.gridLayout_2.addWidget(self.pt_label, 3, 0, 1, 3)
        self.changePt_pushButton = QtGui.QPushButton(self.tab_2)
        self.changePt_pushButton.setObjectName(
            _fromUtf8("changePt_pushButton"))
        self.gridLayout_2.addWidget(self.changePt_pushButton, 3, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 3)
        self.reason_comboBox = QtGui.QComboBox(self.tab_2)
        self.reason_comboBox.setObjectName(_fromUtf8("reason_comboBox"))
        self.gridLayout_2.addWidget(self.reason_comboBox, 4, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(
            20,
            99,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 5, 2, 1, 1)
        self.length_spinBox = QtGui.QSpinBox(self.tab_2)
        self.length_spinBox.setMinimum(-600)
        self.length_spinBox.setMaximum(600)
        self.length_spinBox.setSingleStep(5)
        self.length_spinBox.setObjectName(_fromUtf8("length_spinBox"))
        self.gridLayout_2.addWidget(self.length_spinBox, 2, 3, 1, 1)
        self.startTime_frame = QtGui.QFrame(self.tab_2)
        self.startTime_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.startTime_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.startTime_frame.setObjectName(_fromUtf8("startTime_frame"))
        self.gridLayout_2.addWidget(self.startTime_frame, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("accepted()")),
            Dialog.accept)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL(_fromUtf8("rejected()")),
            Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Options"))
        self.label.setText(
            _("Would you like to Block (or partially Block) this Slot?"))
        self.label_3.setText(_("Block Start"))
        self.label_4.setText(_("Bock End"))
        self.label_2.setText(_("Text to apply"))
        self.comboBox.setItemText(0, _("//Blocked//"))
        self.comboBox.setItemText(1, _("Emergency"))
        self.comboBox.setItemText(2, _("Reserved Clinical Time"))
        self.comboBox.setItemText(3, _("Out of Office"))
        self.comboBox.setItemText(4, _("Lunch"))
        self.comboBox.setItemText(5, _("Catch up time"))
        self.comboBox.setItemText(6, _("Phone Call"))
        self.length_label.setText(_("minutes"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            _("Insert a Block"))
        self.label_7.setText(_("Insert A Patient into this slot?"))
        self.label_5.setText(_("Start Time"))
        self.label_6.setText(_("Length"))
        self.pt_label.setText(_("Chosen Patient is<br />"))
        self.changePt_pushButton.setText(_("Change"))
        self.label_9.setText(_("Reason for appointment is"))
        self.length_spinBox.setSuffix(_(" minutes"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            _("Insert a Known Patient"))


if __name__ == "__main__":
    import gettext
    gettext.install("openmolar")
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
