import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QTableWidget
from info import Info

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>400</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>400</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>400</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Каталог библиотек</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>20</y>
      <width>101</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Искать</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>80</y>
      <width>461</width>
      <height>261</height>
     </rect>
    </property>
   </widget>
   <widget class="QSplitter" name="splitter">
    <property name="geometry">
     <rect>
      <x>8</x>
      <y>20</y>
      <width>133</width>
      <height>40</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
    <widget class="QComboBox" name="comboBox"/>
    <widget class="QLineEdit" name="lineEdit"/>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menuBar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>500</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Library(QMainWindow):
    def __init__(self):
        super(Library, self).__init__()
        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)

        self.con = sqlite3.connect("library.db")
        self.cur = self.con.cursor()

        self.comboBox.addItems(['автор', 'название'])
        self.pushButton.clicked.connect(self.load_table)

        self.load_table()

    def get_info(self):
        data = list(self.cur.execute("Select * from main").fetchall())
        text_line = self.lineEdit.text()
        value = self.comboBox.currentText()
        if not text_line:
            return []
        if value == 'автор':
            data = list(filter(lambda x: text_line.lower() in x[1][0: len(text_line)].lower(), data))
        else:
            data = list(filter(lambda x: text_line.lower() in x[2][0: len(text_line)].lower(), data))
        return data

    def load_table(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(461)

        data = self.get_info()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(1)

        for i, elem in enumerate(data):
            btn = QPushButton(elem[2], self)
            btn.clicked.connect(self.start_window)
            self.tableWidget.setCellWidget(i, 0, btn)

    def start_window(self):
        sender = self.sender()
        data = list(self.cur.execute(f"Select * from main where название = '{sender.text()}'"))
        self.class_info = Info(data[0], self)
        self.class_info.show()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Library()
    ex.show()
    sys.exit(app.exec())