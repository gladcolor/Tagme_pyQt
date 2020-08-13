# -*- coding: utf-8 -*-


import sys
import os
import glob

from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QColor, QBrush


from TagmeUI import Ui_Form

IMG_SUFFIX = ['*.jpg']
IMG_DIR = r'K:\Research\Tagme\tagme\src\assets\Image'
TAGS = [("E", "Elevated main entry"),\
        ("F", "Solid foundation")]
TAGS_LATTERS = [x[0] for x in TAGS]

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.ImageDir = r''
        #��ӵ�¼��ť�źźͲۡ�ע��display��������С����()
        self.bnImage.clicked.connect(self.display)

        self.bnImageDir.clicked.connect(self.getImageDir)

        self.jpg_file_idx = 0
        self.imageList = []
        
        self.checkboxes = []
        self.cboxes_states = [False] * len(TAGS)

        # pos_Image =self.lb_Image.pos()
        geo_Image = self.lb_Image.geometry()
        Image_bottom = geo_Image.bottom()
        Image_right = geo_Image.right()
        # print("pos_Image: ", pos_Image)
        # print("pos_geometry: ", pos_geometry)

        cb_column_y = Image_bottom - len(TAGS) * 30
        for idx, tag in enumerate(TAGS):
        	        
            cb = QCheckBox(tag[0] + ": " + tag[1],self)
            cb.adjustSize()
            cb.stateChanged.connect(self.clickBox)
            cb.move(Image_right + 20, cb_column_y +  idx * 30)
            self.checkboxes.append(cb)

        self.twImage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.twImage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twImage.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.twImage.itemSelectionChanged.connect(self.selected_changed)

        self.setFocus()

    def getImageList(self, suffixes, image_dir):
        # get images
        image_list = []

        for suffix in suffixes:
            image_list += glob.glob(os.path.join(image_dir, suffix))
        return image_list
        
    def getImageDir(self):
        self.ImageDir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.teImage_folder.setPlainText(self.ImageDir)

        self.setFocus()

        self.imageList = self.getImageList(IMG_SUFFIX, self.ImageDir)
        self.loadImgeList()

        #����˳���ť�źźͲۡ�����close����
        #self.cancel_Button.clicked.connect(self.close)
    def display(self):
        jpg_file = r'K:\Research\Tagme\tagme\src\assets\Image\994_Lv_MH42HjPDzZjE1p2WbDA_-94.839853_29.285741_0_162.74.jpg'
        pix = QPixmap(jpg_file)
        print(pix)
        self.lb_Image.setPixmap(pix)
        self.setFocus()
        
    def clickBox(self, state):

        for idx, cb in enumerate(self.checkboxes):
            self.cboxes_states[idx] = cb.isChecked()
            print("self.cboxes_states: ", self.cboxes_states)

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')

    def loadImgeList(self):
        for idx, img in enumerate(self.imageList):
            row = self.twImage.rowCount()
            self.twImage.insertRow(row)
            basename = os.path.basename(img)
            item = QTableWidgetItem(str(basename))
            # item.setBackground(QBrush(QColor(0, 255, 0)))
            self.twImage.setItem(row, 0, item)

    def selected_changed(self):
        self.jpg_file_idx = self.twImage.selectedItems()[0]
        self.setFocus()
        
    def keyPressEvent(self, e):

        try:
            self.setFocus()

            print(e.text())

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
            if self.jpg_file_idx > (len(self.imageList) - 1):
                  self.jpg_file_idx = len(self.imageList) - 1

            self.drawImages()


        except Exception as e:
            print("Error in keyPressEvent(): ", e)

    def drawImages(self):
        try:
            jpg_file = 	self.imageList[self.jpg_file_idx]
            pix = QPixmap(jpg_file)
            self.lb_Image.setPixmap(pix)
            self.twImage.selectRow(self.jpg_file_idx)

            img_L_idx = max(0, self.jpg_file_idx-1)
            jpg_file = 	self.imageList[img_L_idx]
            pixL = QPixmap(jpg_file)
            self.lb_Image_L.setPixmap(pixL)

            img_R_idx = min(len(self.imageList) - 1, self.jpg_file_idx+1)
            jpg_file = 	self.imageList[img_R_idx]
            pixR = QPixmap(jpg_file)
            self.lb_Image_R.setPixmap(pixR)
        except Exception as e:
            print("Error in drawImages:", e)
    
        
if __name__ == "__main__":
    #�̶��ģ�PyQt5������ҪQApplication����sys.argv�������в����б�ȷ���������˫������
    app = QApplication(sys.argv)
    #��ʼ��
    myWin = MyMainForm()
    #�����ڿؼ���ʾ����Ļ��
    myWin.show()
    #�������У�sys.exit����ȷ�����������˳���
    sys.exit(app.exec_())
