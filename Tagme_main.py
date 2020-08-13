# -*- coding: utf-8 -*-


import sys
import os
import glob

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget


from TagmeUI import Ui_Form

IMG_SUFFIX = ['*.jpg']
IMG_DIR = r'K:\Research\Tagme\tagme\src\assets\Image'
TAGS = [("E", "Elevated main entry"),\
        ("F", "Solid foundation")]


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #��ӵ�¼��ť�źźͲۡ�ע��display��������С����()
        self.bnImage.clicked.connect(self.display)
        
        # get images 
        self.image_list = []
        for suffix in IMG_SUFFIX:
        	  self.image_list += glob.glob(os.path.join(IMG_DIR, suffix))
        
        self.jpg_file_idx = 0
        
        self.checkboxes = []

        # pos_Image =self.lb_Image.pos()
        geo_Image = self.lb_Image.geometry()
        Image_bottom = geo_Image.bottom()
        Image_right = geo_Image.right()
        # print("pos_Image: ", pos_Image)
        # print("pos_geometry: ", pos_geometry)
        
        for idx, tag in enumerate(TAGS):
        	        
	      	  cb = QCheckBox(tag[0] + ": " + tag[1],self)
	      	  cb.stateChanged.connect(self.clickBox)
	      	  cb.move(Image_right + 20, Image_bottom - idx * 30)
	      	  self.checkboxes.append(cb)
        
        self.setFocus()
        
        
        
        #����˳���ť�źźͲۡ�����close����
        #self.cancel_Button.clicked.connect(self.close)
    def display(self):
        jpg_file = r'K:\Research\Tagme\tagme\src\assets\Image\994_Lv_MH42HjPDzZjE1p2WbDA_-94.839853_29.285741_0_162.74.jpg'
        pix = QPixmap(jpg_file)
        print(pix)
        self.lb_Image.setPixmap(pix)
        self.setFocus()
        
    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')
        
    def keyPressEvent(self, e):
        self.setFocus()
        print(e.key())
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_Left:
            print("<--")
            self.jpg_file_idx -= 1         
        if e.key() == QtCore.Qt.Key_Right:
            print("-->")
            self.jpg_file_idx += 1
        
        if self.jpg_file_idx < 1:
            self.jpg_file_idx = 0
        if self.jpg_file_idx > (len(self.image_list) - 1):
        	  self.jpg_file_idx = len(self.image_list) - 1    
        
        jpg_file = 	self.image_list[self.jpg_file_idx]  
        pix = QPixmap(jpg_file)         
        self.lb_Image.setPixmap(pix)
        
        img_L_idx = max(0, self.jpg_file_idx-1)
        jpg_file = 	self.image_list[img_L_idx]  
        pixL = QPixmap(jpg_file)         
        self.lb_Image_L.setPixmap(pixL)
        
        img_R_idx = min(len(self.image_list), self.jpg_file_idx+1)
        jpg_file = 	self.image_list[img_R_idx]  
        pixR = QPixmap(jpg_file)         
        self.lb_Image_R.setPixmap(pixR)

    
        
if __name__ == "__main__":
    #�̶��ģ�PyQt5������ҪQApplication����sys.argv�������в����б�ȷ���������˫������
    app = QApplication(sys.argv)
    #��ʼ��
    myWin = MyMainForm()
    #�����ڿؼ���ʾ����Ļ��
    myWin.show()
    #�������У�sys.exit����ȷ�����������˳���
    sys.exit(app.exec_())
