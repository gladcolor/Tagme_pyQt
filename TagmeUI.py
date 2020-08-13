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
        Form.resize(1091, 736)
        self.bnImage = QtWidgets.QPushButton(Form)
        self.bnImage.setGeometry(QtCore.QRect(400, 680, 75, 23))
        self.bnImage.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bnImage.setObjectName("bnImage")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 690, 75, 23))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lb_Image = QtWidgets.QLabel(Form)
        self.lb_Image.setGeometry(QtCore.QRect(250, 70, 601, 561))
        self.lb_Image.setScaledContents(True)
        self.lb_Image.setObjectName("lb_Image")
        self.lb_Image_L = QtWidgets.QLabel(Form)
        self.lb_Image_L.setGeometry(QtCore.QRect(30, 30, 91, 81))
        self.lb_Image_L.setScaledContents(True)
        self.lb_Image_L.setObjectName("lb_Image_L")
        self.lb_Image_R = QtWidgets.QLabel(Form)
        self.lb_Image_R.setGeometry(QtCore.QRect(900, 30, 151, 131))
        self.lb_Image_R.setScaledContents(True)
        self.lb_Image_R.setObjectName("lb_Image_R")
        self.tb_Images = QtWidgets.QTableView(Form)
        self.tb_Images.setGeometry(QtCore.QRect(20, 180, 141, 501))
        self.tb_Images.setObjectName("tb_Images")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bnImage.setText(_translate("Form", "Image"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.lb_Image.setText(_translate("Form", "Image"))
        self.lb_Image_L.setText(_translate("Form", "TextLabel"))
        self.lb_Image_R.setText(_translate("Form", "TextLabel"))
