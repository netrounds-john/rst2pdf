# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagesetup.ui'
#
# Created: Mon Sep 28 15:29:01 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 353)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.firstTemplate = QtGui.QComboBox(Dialog)
        self.firstTemplate.setObjectName("firstTemplate")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstTemplate)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.size = QtGui.QComboBox(Dialog)
        self.size.setObjectName("size")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.size)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.height = QtGui.QLineEdit(Dialog)
        self.height.setObjectName("height")
        self.horizontalLayout.addWidget(self.height)
        self.height_unit = QtGui.QComboBox(Dialog)
        self.height_unit.setObjectName("height_unit")
        self.horizontalLayout.addWidget(self.height_unit)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.width = QtGui.QLineEdit(Dialog)
        self.width.setObjectName("width")
        self.horizontalLayout_2.addWidget(self.width)
        self.width_unit = QtGui.QComboBox(Dialog)
        self.width_unit.setObjectName("width_unit")
        self.horizontalLayout_2.addWidget(self.width_unit)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.margin_top = QtGui.QLineEdit(Dialog)
        self.margin_top.setObjectName("margin_top")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.margin_top)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.margin_bottom = QtGui.QLineEdit(Dialog)
        self.margin_bottom.setObjectName("margin_bottom")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.margin_bottom)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.margin_left = QtGui.QLineEdit(Dialog)
        self.margin_left.setObjectName("margin_left")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.margin_left)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.margin_right = QtGui.QLineEdit(Dialog)
        self.margin_right.setObjectName("margin_right")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.margin_right)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.spacing_header = QtGui.QLineEdit(Dialog)
        self.spacing_header.setObjectName("spacing_header")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.spacing_header)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.spacing_footer = QtGui.QLineEdit(Dialog)
        self.spacing_footer.setObjectName("spacing_footer")
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.spacing_footer)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_11)
        self.margin_gutter = QtGui.QLineEdit(Dialog)
        self.margin_gutter.setObjectName("margin_gutter")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.margin_gutter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "First Page Template:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Page Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Top Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Bottom Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Left Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Right Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Header Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Footer Margin:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Gutter Margin:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
