# -*- coding: utf-8 -*-


import sys
import os
import glob
import logging
import logging.config
import csv
import yaml
from natsort import natsorted, ns

from datetime import datetime


from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QColor, QBrush



from TagmeUI import Ui_Form

IMG_SUFFIX = ['*.jpg']


def setup_logging(default_path='log_config.yaml', logName='', default_level=logging.DEBUG):
    path = default_path
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            if logName != '':
                config["handlers"]["file"]['filename'] = logName
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


yaml_path = 'log_config.yaml'
setup_logging(yaml_path, logName="info.log")


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.ImageDir = r''
        self.result_file = r''
        #��ӵ�¼��ť�źźͲۡ�ע��display��������С����()
        # self.

        self.bnImageDir.clicked.connect(self.getImageDir)
        self.cbMultiTags.clicked.connect(self.multTag_clicked)
        self.cbAutoScroll.clicked.connect(self.autoScroll_clicked)
        self.bnNext.clicked.connect(self.goNext)
        self.bnLast.clicked.connect(self.goLast)
        self.teImage_folder.textChanged.connect(self.teImage_folder_changed)
        self.teNote.textChanged.connect(self.teNote_changed)
        self.bnSave.clicked.connect(self.handleSave)

        self.jpg_file_idx = 0
        self.TAGS = []
        self.imageList = []
        self.TAG_LATTERS = []
        self.press_count = 0
        self.save_count = 10

        self.read_tag_file()
        
        self.checkboxes = []
        self.cboxes_states = [False] * len(self.TAGS)

        # pos_Image =self.lb_Image.pos()
        geo_Image = self.lb_Image.geometry()
        Image_bottom = geo_Image.bottom()
        Image_right = geo_Image.right()
        # print("pos_Image: ", pos_Image)
        # print("pos_geometry: ", pos_geometry)

        cb_column_y = Image_bottom - len(self.TAGS) * 30
        for idx, tag in enumerate(self.TAGS):
            cb = QCheckBox(tag[0] + ": " + tag[1], self)
            cb.adjustSize()
            cb.stateChanged.connect(self.clickBox)
            cb.move(Image_right + 20, cb_column_y + idx * 30)
            self.checkboxes.append(cb)

        self.twImage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.twImage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.twImage.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twImage.setSelectionMode(QAbstractItemView.SingleSelection)


        self.twImage.itemSelectionChanged.connect(self.selected_changed)

        self.setFocus()

    def teNote_changed(self):
        text = self.teNote.toPlainText()
        item = QTableWidgetItem(text)
        self.twImage.setItem(self.jpg_file_idx, 2, item)

    def teImage_folder_changed(self):
        # time.sleep(0.5)
        if os.path.exists(self.teImage_folder.toPlainText()):
            self.imageList = self.getImageList(IMG_SUFFIX, self.ImageDir)
            self.getResult_file()
            if os.path.exists(self.result_file):
                self.handleOpen()
            else:
                self.loadImgeList()
                self.handleSave()

    def getResult_file(self):
        parent_path = os.path.dirname(self.ImageDir)
        folder_name = os.path.basename(self.ImageDir)
        self.result_file = os.path.join(parent_path, folder_name + "_Tagme_results.csv")

    def autoScroll_clicked(self):
        if self.cbAutoScroll.isChecked():
            # print('Checked')
            self.cbMultiTags.setChecked(False)

    def multTag_clicked(self):
        if self.cbMultiTags.isChecked():
            # print('Checked')
            self.cbAutoScroll.setChecked(False)

    def read_tag_file(self):
        try:
            tag_file = "Tags.txt"
            if os.path.exists(tag_file):
                f = open(tag_file, 'r', encoding='utf8')
                lines = f.readlines()
                for line in lines:
                    fields = line.split(': ')
                    self.TAGS.append(fields)
                self.TAG_LATTERS =  [x[0] for x in self.TAGS]
                f.close()
        except Exception as e:
            print("Error in read_tag_file():", e)
            f.close()

    def writeTags(self):
        old_tags = self.getTagsFromTable()
        logging.info("old_tags：%s", old_tags)
        tags = []
        for i in range(len(self.cboxes_states)):
            if self.checkboxes[i].isChecked():
                tag = self.TAG_LATTERS[i]
                tags.append(tag)
        # if not self.multTag_clicked():
        #     tags = tag
        # else:
        #     tags = ';'.join(tags)
        tags = ';'.join(tags)

        logging.info("tag：%s", tags)
        item = QTableWidgetItem(str(tags))
        self.twImage.setItem(self.jpg_file_idx, 0, item)



    def getImageList(self, suffixes, image_dir):
        # get images
        image_list = []

        for suffix in suffixes:
            image_list += glob.glob(os.path.join(image_dir, suffix))
        image_list = natsorted(image_list)
        return image_list
        
    def getImageDir(self):
        self.ImageDir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.teImage_folder.setPlainText(self.ImageDir)

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

        for idx, cb in enumerate(self.checkboxes):
            # self.cboxes_states[idx] = cb.isChecked()
            if cb.isChecked():
                cb.setStyleSheet("background-color: lightgreen")
            else:
                cb.setStyleSheet("background-color: none")
            # print("self.cboxes_states: ", self.cboxes_states)

        # logging.info("self.cboxes_states: %s", self.cboxes_states)

        self.setFocus()

    def is_key_in_tags(self, key:str, tags:list): # return index
        try:
            key = str(key)
            key = key.upper()
            idx = tags.index(key)
            if idx < 0:
                key = key.lower()
                idx = tags.index(key)
        except Exception as e:
            idx = -1
            return idx
        return idx

    def loadImgeList(self):
        # self.twImage.clear()
        self.twImage.setRowCount(0)
        for idx, img in enumerate(self.imageList):
            row = self.twImage.rowCount()
            self.twImage.insertRow(row)
            basename = os.path.basename(img)
            item = QTableWidgetItem(str(basename))
            # item.setBackground(QBrush(QColor(0, 255, 0)))
            self.twImage.setItem(row, 1, item)
        if self.twImage.rowCount() > 0:
            self.twImage.selectRow(0)
            self.drawImages()
        else:
            self.lb_Image_L.setText("")
            self.lb_Image_R.setText("")
            self.lb_Image.setText("")

        self.jpg_file_idx = 0
        self.twImage.selectRow(self.jpg_file_idx)

    def selected_changed(self):

        # for cb in self.checkboxes:
        #     cb.setChecked(False).
        logging.info("Selected changed. ")

        index = self.twImage.currentIndex().row()
        if index > -1:
            self.jpg_file_idx = index
            self.drawImages()

        # self.getTagsFromTable()

        self.setCheckboxes()
        self.setNote()
        logging.info("Selected change ended. \n")

        self.setFocus()
        
    def keyPressEvent(self, e):

        try:
            previous_row = self.jpg_file_idx

            # if keys change
            key_index = self.is_key_in_tags(e.text(), self.TAG_LATTERS)
            if key_index > -1:
                self.press_count += 1
                state = self.checkboxes[key_index].isChecked()
                if not self.multTag_clicked():
                    for cb in self.checkboxes:
                        cb.setChecked(False)
                    self.checkboxes[key_index].setChecked(True)

                else:
                    self.checkboxes[key_index].setChecked(not state)
                self.writeTags()

                # if AutoScroll
                if self.cbAutoScroll.checkState():
                    self.jpg_file_idx += 1
                # self.drawImages()

            # if got arrow keys
            if (e.key() == QtCore.Qt.Key_Left) or (e.key() == QtCore.Qt.Key_Up):
                # print("<--")
                self.jpg_file_idx -= 1
            if (e.key() == QtCore.Qt.Key_Right) or (e.key() == QtCore.Qt.Key_Down):
                # print("-->")
                self.jpg_file_idx += 1

            if self.jpg_file_idx < 1:
                self.jpg_file_idx = 0
            if self.jpg_file_idx > (len(self.imageList) - 1):
                  self.jpg_file_idx = len(self.imageList) - 1

            # if need to move to another row
            if self.jpg_file_idx != previous_row:
                self.twImage.selectRow(self.jpg_file_idx)
                self.drawImages()


            if self.press_count == self.save_count:
                self.press_count = 0
                self.handleSave()

                now = datetime.now()
                time1 = now.strftime("%H:%M:%S")
                self.lb_info.setText("Saved at " +  time1)

            self.setFocus()

        except Exception as e:
            print("Error in keyPressEvent(): ", e)

    def getTagsFromTable(self):
        index = self.twImage.currentIndex().row()
        tags = ''
        if index is not None:
            row = self.twImage.item(index, 0)
            if row is not None:
                tags = str(row.text())
                # print("tags: ", tags)
            tags = tags.split(';')

        self.setFocus()

        logging.info("tags in getTagsFromTable(): %s", tags)

        return tags

    def setNote(self):
        index = self.twImage.currentIndex().row()
        note_column = 2
        note = ''
        if index is not None:

            item = self.twImage.item(index, note_column)
            if item is not None:
                note = str(item.text())
                # print("item: ", item)
            # tags = tags.split(';')
        self.teNote.setText(note)
        self.setFocus()



    def setCheckboxes(self):
        for cb in self.checkboxes:
            cb.setChecked(False)

        tags = self.getTagsFromTable()
        logging.info("tags in setCheckboxes(): %s", tags)
        for tag in tags:
            idx = self.is_key_in_tags(tag, self.TAG_LATTERS)
            if idx > -1:
                self.checkboxes[idx].setChecked(True)

    def drawImages(self):
        try:
            self.jpg_file_idx = max(0, self.jpg_file_idx)
            self.jpg_file_idx = min(len(self.imageList) - 1, self.jpg_file_idx)
            jpg_file = 	self.imageList[self.jpg_file_idx]
            pix = QPixmap(jpg_file)
            self.lb_Image.setPixmap(pix)
            self.twImage.selectRow(self.jpg_file_idx)

            img_L_idx = max(0, self.jpg_file_idx - 1)
            if self.jpg_file_idx == 0:
                self.lb_Image_L.setText("The first image.")
            else:
                jpg_file = self.imageList[img_L_idx]
                pixL = QPixmap(jpg_file)
                self.lb_Image_L.setPixmap(pixL)

            img_R_idx = min(len(self.imageList) - 1, self.jpg_file_idx + 1)
            if self.jpg_file_idx == (len(self.imageList) - 1):
                self.lb_Image_R.setText("No more image.")
            else:
                jpg_file = 	self.imageList[img_R_idx]
                pixR = QPixmap(jpg_file)
                self.lb_Image_R.setPixmap(pixR)

            self.setFocus()
        except Exception as e:
            print("Error in drawImages:", e)

    def goNext(self):
        if len(self.imageList) == 0:
            return
        self.jpg_file_idx = min(self.jpg_file_idx + 1, len(self.imageList) - 1)
        self.twImage.selectRow(self.jpg_file_idx)
        # print("goNext(): ", self.jpg_file_idx)
        self.drawImages()
        self.setFocus()

    def goLast(self):
        if len(self.imageList) == 0:
            return
        self.jpg_file_idx = max(self.jpg_file_idx - 1, 0)
        self.twImage.selectRow(self.jpg_file_idx)
        # print("goLast(): ", self.jpg_file_idx)
        self.drawImages()
        self.setFocus()
    
    def handleSave(self):
        # path = QtGui.QFileDialog.getSaveFileName(
        #         self, 'Save File', '', 'CSV(*.csv)')
        # options = QFileDialog.Options()
        # # options |= QFileDialog.DontUseNativeDialog
        # path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
        #                                           "CSV Files (*.csv)", options=options)
        # if fileName:
        #     print(fileName)
        headercount = self.twImage.columnCount()
        headertexts = []
        for x in range(0, headercount, 1):
            headertexts.append(self.twImage.horizontalHeaderItem(x).text())


        with open(self.result_file, 'w', newline='', encoding='utf8') as stream:
            writer = csv.writer(stream)
            writer.writerow(headertexts)
            for row in range(self.twImage.rowCount()):
                rowdata = []
                for column in range(self.twImage.columnCount()):
                    item = self.twImage.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)
        print("Results saved in : ", self.result_file)
        self.setFocus()

    def handleOpen(self):
        path = self.result_file

        if os.path.exists(path):
            with open(path, 'r', newline='') as f:
                reader = csv.reader(f, delimiter=',')
                headers = next(reader)
                self.twImage.setRowCount(0)
                # self.twImage.setColumnCount(0)

                for idx, rowdata in enumerate(reader):
                    row = self.twImage.rowCount()
                    self.twImage.insertRow(row)
                    self.twImage.setColumnCount(len(rowdata))
                    for column, data in enumerate(rowdata):
                        item = QTableWidgetItem(str(data))
                        self.twImage.setItem(row, column, item)

            self.jpg_file_idx = 0
            self.twImage.selectRow(self.jpg_file_idx)
if __name__ == "__main__":
    #�̶��ģ�PyQt5������ҪQApplication����sys.argv�������в����б�ȷ���������˫������
    app = QApplication(sys.argv)
    #��ʼ��
    myWin = MyMainForm()
    #�����ڿؼ���ʾ����Ļ��
    myWin.show()
    #�������У�sys.exit����ȷ�����������˳���
    sys.exit(app.exec_())
