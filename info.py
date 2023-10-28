import io
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>620</height>
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
    <width>300</width>
    <height>620</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>300</width>
    <height>620</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Информация о книге</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_image">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>0</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="author_label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>343</y>
      <width>208</width>
      <height>38</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>ArrowCursor</cursorShape>
    </property>
    <property name="text">
     <string>Автор</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="name_label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>265</y>
      <width>208</width>
      <height>39</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="year_label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>420</y>
      <width>208</width>
      <height>39</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>ArrowCursor</cursorShape>
    </property>
    <property name="text">
     <string>Год выпуска</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="genre_label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>497</y>
      <width>208</width>
      <height>39</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>ArrowCursor</cursorShape>
    </property>
    <property name="text">
     <string>Жанр</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QWidget" name="">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>290</y>
      <width>151</width>
      <height>291</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="text_name">
       <property name="font">
        <font>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="text_author">
       <property name="font">
        <font>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="text_year">
       <property name="font">
        <font>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="text_genre">
       <property name="font">
        <font>
         <pointsize>11</pointsize>
        </font>
       </property>
       <property name="text">
        <string/>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menuBar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>300</width>
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


class Info(QMainWindow):
    def __init__(self, data, parent=None):
        super(Info, self).__init__()
        ui_file = io.StringIO(template)
        uic.loadUi(ui_file, self)
        self.label_image.resize(150, 237)
        self.parent = parent
        self.data = data
        self.see_info()

    def see_info(self):
        if self.data[-1] is not None:
            self.label_image.setPixmap(QPixmap(self.data[-1]))
        else:
            self.label_image.setPixmap(QPixmap('standart.png'))
        self.text_name.setText(self.data[2])
        self.text_author.setText(self.data[1])
        self.text_year.setText(str(self.data[3]))
        self.text_genre.setText(self.data[4])
