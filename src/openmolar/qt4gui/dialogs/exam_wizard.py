#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ############################################################################ #
# #                                                                          # #
# # Copyright (c) 2009-2014 Neil Wallace <neil@openmolar.com>                # #
# #                                                                          # #
# # This file is part of OpenMolar.                                          # #
# #                                                                          # #
# # OpenMolar is free software: you can redistribute it and/or modify        # #
# # it under the terms of the GNU General Public License as published by     # #
# # the Free Software Foundation, either version 3 of the License, or        # #
# # (at your option) any later version.                                      # #
# #                                                                          # #
# # OpenMolar is distributed in the hope that it will be useful,             # #
# # but WITHOUT ANY WARRANTY; without even the implied warranty of           # #
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            # #
# # GNU General Public License for more details.                             # #
# #                                                                          # #
# # You should have received a copy of the GNU General Public License        # #
# # along with OpenMolar.  If not, see <http://www.gnu.org/licenses/>.       # #
# #                                                                          # #
# ############################################################################ #

import logging
from PyQt4 import QtGui, QtCore

from openmolar.settings import localsettings

from openmolar.ptModules.estimates import TXHash
from openmolar.qt4gui.compiled_uis import Ui_exam_wizard
from openmolar.qt4gui.fees import manipulate_plan

LOGGER = logging.getLogger("openmolar")


class ExamWizard(QtGui.QDialog, Ui_exam_wizard.Ui_Dialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.om_gui = parent
        self.pt = self.om_gui.pt

        self.setupUi(self)
        self.dateEdit.setDate(QtCore.QDate().currentDate())
        self.dents_comboBox.addItems(localsettings.activedents)

        performingDent = localsettings.apptix_reverse.get(
            localsettings.clinicianNo, None)
        if performingDent in localsettings.activedents:
            pos = localsettings.activedents.index(performingDent)
            self.dents_comboBox.setCurrentIndex(pos)
        else:
            self.dents_comboBox.setCurrentIndex(-1)

    def getInput(self):
        result = True
        while result:
            result = self.exec_()
            if self.examA_radioButton.isChecked():
                exam = "CE"
            elif self.examB_radioButton.isChecked():
                exam = "ECE"
            else:
                exam = "FCA"
            dent = str(self.dents_comboBox.currentText())
            if dent == "":
                message = _("Please enter the examining Dentist")
                QtGui.QMessageBox.information(self, _("Whoops"), message)
            else:
                break

        if result:
            return (exam, dent, self.dateEdit.date().toPyDate())
        else:
            return()

    def check_dent(self, examdent):
        if examdent == localsettings.ops.get(self.pt.dnt1):
            if (self.pt.dnt2 == 0 or
               self.pt.dnt2 == self.pt.dnt1):  # --no dnt2
                APPLIED = True
            else:
                message = u'''<p>%s %s<br />%s</p>
                <hr /><p><i>%s %s</i></p>''' % (
                    examdent,
                    _("is now both the registered and course dentist"),
                    _("Is this correct?"),
                    _("confirming this will remove reference to"),
                    localsettings.ops.get(self.pt.dnt2))

                if QtGui.QMessageBox.question(self,
                                              "Confirm", message,
                                              QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                              QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
                    self.pt.dnt2 = 0
                    self.om_gui.updateDetails()
                    APPLIED = True
        else:
            message = u'<p>%s %s<br />%s</p>' % (
                examdent,
                _("performed this exam"),
                _("Is this correct?"))

            if examdent != localsettings.ops.get(self.pt.dnt2):
                message += u'<br /><i>%s, %s</i></p>' % (
                    _("confirming this will change the course dentist"),
                    _("but not the registered dentist")
                )
            else:
                message += u'<i>%s %s %s</i>' % (
                    _("consider making"),
                    examdent,
                    _("the registered dentist"))

            if QtGui.QMessageBox.question(self,
                                          _("Confirm"), message,
                                          QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                                          QtGui.QMessageBox.Yes) == QtGui.QMessageBox.Yes:
                self.pt.dnt2 = localsettings.ops_reverse[examdent]
                self.om_gui.updateDetails()
                APPLIED = True

        return APPLIED, examdent

    def perform_exam(self):
        '''
        perform an exam
        '''
        if self.pt.serialno == 0:
            om_gui.advise("no patient selected", 1)
            return
        if self.pt.treatment_course.has_exam:
            self.om_gui.advise(u"<p>%s</p><hr /><p>%s</p>" % (
                               _(
                               'You already have a completed exam on this course of treatment'),
                               _("Unable to perform exam")), 1)
            return

        APPLIED = False
        while not APPLIED:
            result = self.getInput()
            if not result:
                self.om_gui.advise(_("Examination not applied"), 2)
                return False

            examtype, examdent, examd = result

            APPLIED, examdent = self.check_dent(examdent)
            if APPLIED:
                courseno = self.pt.treatment_course.courseno
                self.pt.treatment_course.examt = examtype
                if self.pt.treatment_course.examt == "CE":
                    self.pt.pd5 = examd
                if self.pt.treatment_course.examt == "ECE":
                    self.pt.pd6 = examd
                if self.pt.treatment_course.examt == "FCA":
                    self.pt.pd7 = examd
                self.pt.treatment_course.examd = examd

                self.update_recall_date()

                self.pt.addHiddenNote("exam", "%s" % examtype)

                dentid = localsettings.ops_reverse[examdent]

                hash_ = localsettings.hash_func(
                    "%sexam1%s" %
                    (courseno, examtype))
                tx_hash = TXHash(hash_, True)

                manipulate_plan.add_treatment_to_estimate(
                    self.om_gui, "exam", examtype, dentid, [tx_hash])

                newnotes = unicode(
                    self.om_gui.ui.notesEnter_textEdit.toPlainText().toUtf8())
                if newnotes != "" and newnotes[-1] != "\n":
                    newnotes += "\n"
                newnotes += "%s %s %s\n" % (
                    examtype, _("performed by"), examdent)
                self.om_gui.ui.notesEnter_textEdit.setText(newnotes)

        return APPLIED

    def update_recall_date(self):
        if not self.pt.appt_prefs.recall_active:
            self.om_gui.advise(
                _("WARNING - Not updating recall due to patients recall settings"), 1)
        else:
            date_ = localsettings.formatDate(self.pt.appt_prefs.new_recdent)
            self.om_gui.advise("updating recall date to %s" % date_, 1)
            self.pt.appt_prefs.update_recdent()


if __name__ == "__main__":
    LOGGER.setLevel(logging.DEBUG)

    localsettings.initiate()
    localsettings.loadFeeTables()
    localsettings.station = "reception"

    from openmolar.qt4gui import maingui
    from openmolar.dbtools import patient_class

    app = QtGui.QApplication([])
    mw = maingui.OpenmolarGui()
    mw.getrecord(11956)

    dl = ExamWizard(mw)
    print dl.perform_exam()
