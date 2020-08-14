# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tagme.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1257, 731)
        self.lb_Image = QtWidgets.QLabel(Form)
        self.lb_Image.setGeometry(QtCore.QRect(200, 60, 600, 600))
        self.lb_Image.setScaledContents(True)
        self.lb_Image.setObjectName("lb_Image")
        self.lb_Image_L = QtWidgets.QLabel(Form)
        self.lb_Image_L.setGeometry(QtCore.QRect(20, 60, 120, 120))
        self.lb_Image_L.setScaledContents(True)
        self.lb_Image_L.setObjectName("lb_Image_L")
        self.lb_Image_R = QtWidgets.QLabel(Form)
        self.lb_Image_R.setGeometry(QtCore.QRect(860, 60, 120, 120))
        self.lb_Image_R.setScaledContents(True)
        self.lb_Image_R.setObjectName("lb_Image_R")
        self.bnImageDir = QtWidgets.QPushButton(Form)
        self.bnImageDir.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.bnImageDir.setObjectName("bnImageDir")
        self.teImage_folder = QtWidgets.QTextEdit(Form)
        self.teImage_folder.setGeometry(QtCore.QRect(100, 10, 761, 21))
        self.teImage_folder.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.teImage_folder.setInputMethodHints(QtCore.Qt.ImhNone)
        self.teImage_folder.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.teImage_folder.setReadOnly(True)
        self.teImage_folder.setObjectName("teImage_folder")
        self.twImage = QtWidgets.QTableWidget(Form)
        self.twImage.setGeometry(QtCore.QRect(990, 60, 261, 661))
        self.twImage.setObjectName("twImage")
        self.twImage.setColumnCount(2)
        self.twImage.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twImage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twImage.setHorizontalHeaderItem(1, item)
        self.cbAutoScroll = QtWidgets.QCheckBox(Form)
        self.cbAutoScroll.setGeometry(QtCore.QRect(880, 10, 70, 17))
        self.cbAutoScroll.setObjectName("cbAutoScroll")
        self.cbMultiTags = QtWidgets.QCheckBox(Form)
        self.cbMultiTags.setGeometry(QtCore.QRect(970, 10, 70, 17))
        self.cbMultiTags.setObjectName("cbMultiTags")
        self.bnSave = QtWidgets.QPushButton(Form)
        self.bnSave.setGeometry(QtCore.QRect(1170, 30, 75, 23))
        self.bnSave.setObjectName("bnSave")
        self.teNote = QtWidgets.QTextEdit(Form)
        self.teNote.setGeometry(QtCore.QRect(830, 240, 151, 171))
        self.teNote.setObjectName("teNote")
        self.bnLast = QtWidgets.QPushButton(Form)
        self.bnLast.setGeometry(QtCore.QRect(100, 70, 51, 91))
        self.bnLast.setObjectName("bnLast")
        self.bnNext = QtWidgets.QPushButton(Form)
        self.bnNext.setGeometry(QtCore.QRect(810, 60, 41, 91))
        self.bnNext.setObjectName("bnNext")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_Image.setText(_translate("Form", "Current Image"))
        self.lb_Image_L.setText(_translate("Form", "Previous Image"))
        self.lb_Image_R.setText(_translate("Form", "Next Image"))
        self.bnImageDir.setText(_translate("Form", "Image Folder"))
        item = self.twImage.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Tags"))
        item = self.twImage.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Image"))
        self.cbAutoScroll.setText(_translate("Form", "Auto Scroll"))
        self.cbMultiTags.setText(_translate("Form", "Multi-Tag"))
        self.bnSave.setText(_translate("Form", "Save"))
        self.bnLast.setText(_translate("Form", "<"))
        self.bnNext.setText(_translate("Form", ">"))
