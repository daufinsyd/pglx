#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, subprocess
import pickle
import readline
import linecache # lis les lignes spécifiques de fichier vs pas de global variables dans les class
import time
import getpass
import re
import string
import
path_to_pglx = "/home/Pompiers/Public/Rapports/Pompier-GLX" ### Sert unsiquement pour les fichiers py et images ###
path_to_vars = "/home/Pompiers/Public/.tmp" ### sert pour toutes les vars du rapport et des rapports en gnal ###
path_to_rinter = "/home/Pompiers/Public/Rapports/Interventions" ### sert uniquement pour l'écriture du rapport ###
path_to_rfma = "/home/Pompiers/Public/Rapports/FMA"### sert uniquement pour l'écriture du rapport ###
os.chdir(path_to_vars)
if os.path.isfile(".PathToRInter"):
    path_to_rinter = linecache.getline('.PathToRInter', 1)
if os.path.isfile(".PathToRFma"):
    path_to_rfma = linecache.getline('.PathToRFma', 1)
b = 4
b2 = 2
b3 = 1

class Ui_PompierGLX(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_PompierGLX, self).__init__(parent)
        self.suite()

    def suite(self):
        global PompierGLX, self_ui_inter
        self_ui_inter = self
        PompierGLX = self
        PompierGLX.setObjectName("PompierGLX")
        PompierGLX.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PompierGLX)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 0, 381, 21))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(530, 0, 167, 21))
        self.name.setObjectName("name")
        self.new_rapportInter = QtWidgets.QPushButton(self.frame)
        self.new_rapportInter.setGeometry(QtCore.QRect(30, 70, 241, 31))
        self.new_rapportInter.setObjectName("new_rapportInter")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 241, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 210, 241, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 250, 241, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.button_close = QtWidgets.QPushButton(self.frame)
        self.button_close.setGeometry(QtCore.QRect(690, 510, 97, 31))
        self.button_close.setObjectName("button_close")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 70, 97, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(620, 110, 97, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(610, 210, 151, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 211, 21))
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QLabel(self.frame)
        self.user.setGeometry(QtCore.QRect(290, 40, 67, 21))
        self.user.setObjectName("user")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(500, 250, 261, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(610, 290, 151, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        PompierGLX.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PompierGLX)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        PompierGLX.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PompierGLX)
        self.statusbar.setObjectName("statusbar")
        PompierGLX.setStatusBar(self.statusbar)

        self.retranslateUi(PompierGLX)
        self.button_close.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(PompierGLX)


        self.new_rapportInter.clicked.connect(lambda selfi = self : fonctions_self.new_rapportInter(self))
        self.pushButton_7.clicked.connect(lambda selfi = self :fonctions_self.show_credits(self))
        self.pushButton_8.clicked.connect(lambda selfi = self :fonctions_self.show_license(self))
        self.pushButton_4.clicked.connect(lambda selfi = self :fonctions_self.createInter(self))
        self.pushButton_5.clicked.connect(lambda selfi = self :fonctions_self.create_own(self))
        self.pushButton_9.clicked.connect(lambda selfi = self :fonctions_self.administration(self))

    def retranslateUi(self, PompierGLX):
        file = path_to_vars + '/.centreInter'
        if os.path.isfile(file):
            name_2 = linecache.getline(file, 1)
        else:
            name_2 = "du Centre d'Icendie et de Secours"
        USER = getpass.getuser()
        _translate = QtCore.QCoreApplication.translate
        PompierGLX.setWindowTitle(_translate("PompierGLX", "Pompier-GLX"))
        self.label.setText(_translate("PompierGLX", "Bienvenue dans le Gestionnaire des Sapeurs-Pompiers: "))
        self.name.setText(_translate("PompierGLX", name_2))
        self.new_rapportInter.setText(_translate("PompierGLX", "Rédiger un rapport d\'Intervention"))
        self.pushButton_2.setText(_translate("PompierGLX", "Rédiger un rapport de FMA"))
        self.pushButton_3.setText(_translate("PompierGLX", "Rédiger un rapport de Casernement"))
        self.pushButton_4.setText(_translate("PompierGLX", "Créer une Intervention"))
        self.pushButton_5.setText(_translate("PompierGLX", "Créer une feuille personnalisée"))
        self.button_close.setText(_translate("PompierGLX", "Quitter"))
        self.pushButton_7.setText(_translate("PompierGLX", "Crédits"))
        self.pushButton_8.setText(_translate("PompierGLX", "License"))
        self.pushButton_9.setText(_translate("PompierGLX", "Administration"))
        self.label_2.setText(_translate("PompierGLX", "Vous êtes connecté en tant que:"))
        self.user.setText(_translate("PompierGLX", USER))
        self.pushButton_10.setText(_translate("PompierGLX", "Se connecter sous une autre session"))
        self.pushButton_11.setText(_translate("PompierGLX", "Préférences"))

    def tmp(self):
        print("rien")


class Ui_rapportInter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_rapportInter, self).__init__(parent)
        self.suite()

    def suite(self):
        global Ui_rapportInter
        Ui_rapportInter = self
        Ui_rapportInter.setObjectName("MainWindow")
        Ui_rapportInter.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_rapportInter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 747, 804))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 0, 2, 1, 1)
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 667, 93))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 634, 257))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_4.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_4.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_4.addWidget(self.comboBox_5, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 5, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_4.addWidget(self.comboBox_6, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 6, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_4.addWidget(self.comboBox_7, 6, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 716, 93))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 683, 184))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_5.addWidget(self.comboBox_8, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_5.addWidget(self.comboBox_9, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_5.addWidget(self.comboBox_10, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_5.addWidget(self.comboBox_11, 3, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 4, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        self.toolBox.addItem(self.page_2, "")
        self.gridLayout_3.addWidget(self.toolBox, 4, 0, 1, 6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 6, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 7, 0, 1, 1)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.gridLayout_3.addWidget(self.dateTimeEdit_3, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 7, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 6, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 10, 2, 1, 1)
        self.toolBox_2 = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 674, 73))
        self.page_3.setObjectName("page_3")

        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        r = 0
        for i in range(0,4): #ATTENTION A changer > utilisateur peut le définir
            self.comboBox_12 = QtWidgets.QComboBox(self.page_3)
            self.comboBox_12.setObjectName("comboBox_12-"+str(r))
            fonctions_self.addItem_comboBox(self, self.comboBox_12, 'l_spv')#ajoute les items
            self.comboBox_12.currentTextChanged.connect(lambda value = self.comboBox_12, name="spv_sll"+"_comboBox_12-"+str(r): fonctions_self.on_combobox_changed(self, value, name)) #connecte immédiatement chaque combobox
            self.gridLayout_8.addWidget(self.comboBox_12, r, 0, 1, 1)#r=row c=colum
            self.comboBox_15 = QtWidgets.QComboBox(self.page_3)
            self.comboBox_15.setObjectName("comboBox_15-"+str(r))
            fonctions_self.addItem_comboBox(self, self.comboBox_15, 'l_spv')#ajoute les items
            self.comboBox_15.currentTextChanged.connect(lambda value = self.comboBox_15, name="spv_sll"+"_comboBox_15-"+str(r): fonctions_self.on_combobox_changed(self, value, name))
            self.gridLayout_8.addWidget(self.comboBox_15, r, 1, 1, 1)
            r = r+1

        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 723, 73))
        self.page_4.setObjectName("page_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        r = 0
        for i in range(0,4):
            self.comboBox_13 = QtWidgets.QComboBox(self.page_4)
            self.comboBox_13.setObjectName("comboBox_13-"+str(r))
            fonctions_self.addItem_comboBox(self, self.comboBox_13, 'l_spv')#ajoute les items
            self.comboBox_13.currentTextChanged.connect(lambda value = self.comboBox_13, name="spv_caserne"+"_comboBox_13-"+str(r): fonctions_self.on_combobox_changed(self, value, name))
            self.gridLayout_9.addWidget(self.comboBox_13, r, 0, 1, 1)#r=row c=colum
            self.comboBox_14 = QtWidgets.QComboBox(self.page_4)
            self.comboBox_14.setObjectName("comboBox_14-"+str(r))
            fonctions_self.addItem_comboBox(self, self.comboBox_14, 'l_spv')#ajoute les items
            self.comboBox_14.currentTextChanged.connect(lambda value = self.comboBox_14, name="spv_caserne"+"_comboBox_14-"+str(r): fonctions_self.on_combobox_changed(self, value, name))
            self.gridLayout_9.addWidget(self.comboBox_14, r, 1, 1, 1)
            r = r+1

        self.toolBox_2.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 661, 135))
        self.page_5.setObjectName("page_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBox_7 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_5.addWidget(self.spinBox_7, 3, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 7, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 4, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_5.addWidget(self.spinBox_3, 0, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_5.addWidget(self.lineEdit_8, 3, 2, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_5.addWidget(self.spinBox_4, 1, 1, 2, 1)
        self.label_22 = QtWidgets.QLabel(self.page_5)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 1, 4, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_5.addWidget(self.spinBox_5, 1, 5, 2, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_5.addWidget(self.lineEdit_7, 1, 7, 2, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 1, 2, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_5.addWidget(self.spinBox_6, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.page_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 3, 4, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.page_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 3, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_5.addWidget(self.spinBox_2, 0, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 3, 7, 1, 1)
        self.toolBox_2.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 710, 129))
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_28 = QtWidgets.QLabel(self.page_6)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 1, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.page_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.page_6)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 0, 4, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_7.addWidget(self.spinBox_10, 0, 5, 1, 1)
        self.spinBox_9 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_7.addWidget(self.spinBox_9, 1, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_7.addWidget(self.lineEdit_11, 1, 3, 1, 1)
        self.spinBox_11 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_7.addWidget(self.spinBox_11, 1, 5, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_7.addWidget(self.lineEdit_12, 1, 7, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_7.addWidget(self.lineEdit_13, 0, 7, 1, 1)
        self.spinBox_12 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_12.setObjectName("spinBox_12")
        self.gridLayout_7.addWidget(self.spinBox_12, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.page_6)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 0, 0, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_7.addWidget(self.spinBox_8, 0, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_7.addWidget(self.lineEdit_10, 0, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.page_6)
        self.label_29.setObjectName("label_29")
        self.gridLayout_7.addWidget(self.label_29, 2, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_7.addWidget(self.lineEdit_14, 2, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.page_6)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 2, 4, 1, 1)
        self.spinBox_13 = QtWidgets.QSpinBox(self.page_6)
        self.spinBox_13.setObjectName("spinBox_13")
        self.gridLayout_7.addWidget(self.spinBox_13, 2, 5, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_7.addWidget(self.lineEdit_15, 2, 7, 1, 1)
        self.toolBox_2.addItem(self.page_6, "")
        self.gridLayout_3.addWidget(self.toolBox_2, 8, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 10, 1, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 11, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 5, 1, 1, 3)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_3.addWidget(self.checkBox_6, 10, 4, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 10, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 10, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 9, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 12, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 12, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Ui_rapportInter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_rapportInter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        Ui_rapportInter.setMenuBar(self.menubar)

        self.retranslateUi(Ui_rapportInter)
        self.toolBox.setCurrentIndex(1)
        self.toolBox_2.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Ui_rapportInter)


        self.spinBox.setMaximum(500000)
        self.spinBox.valueChanged['int'].connect(lambda value = self.spinBox, name="nCodis": fonctions_self.on_spinBox_changed(self, value, name))

        self.spinBox_2.valueChanged['int'].connect(lambda value = self.spinBox_2, name="1erDepart_VSAV": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_3.valueChanged['int'].connect(lambda value = self.spinBox_3, name="1erDepart_FPTSR": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_4.valueChanged['int'].connect(lambda value = self.spinBox_4, name="1erDepart_EPSA": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_5.valueChanged['int'].connect(lambda value = self.spinBox_5, name="1erDepart_VL": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_6.valueChanged['int'].connect(lambda value = self.spinBox_6, name="1erDepart_SMUR": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_7.valueChanged['int'].connect(lambda value = self.spinBox_7, name="1erDepart_heliSMUR": fonctions_self.on_spinBox_changed(self, value, name))

        self.spinBox_8.valueChanged['int'].connect(lambda value = self.spinBox_8, name="renfort_VSAV": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_9.valueChanged['int'].connect(lambda value = self.spinBox_9, name="renfort_EPSA": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_10.valueChanged['int'].connect(lambda value = self.spinBox_10, name="renfort_FPTSR": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_11.valueChanged['int'].connect(lambda value = self.spinBox_11, name="renfort_VL": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_12.valueChanged['int'].connect(lambda value = self.spinBox_12, name="renfort_SMUR": fonctions_self.on_spinBox_changed(self, value, name))
        self.spinBox_13.valueChanged['int'].connect(lambda value = self.spinBox_13, name="renfort_heliSMUR": fonctions_self.on_spinBox_changed(self, value, name))

        self.lineEdit.textChanged.connect(lambda value = self.lineEdit, name="natureInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_2.textChanged.connect(lambda value = self.lineEdit_2, name="localisationInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_3.textChanged.connect(lambda value = self.lineEdit_3, name="demandeurInter": fonctions_self.on_lineEdit_changed(self, value, name))

        self.lineEdit_4.textChanged.connect(lambda value = self.lineEdit_4, name="1erDepart_VSAV_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_5.textChanged.connect(lambda value = self.lineEdit_5, name="1erDepart_EPSA_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_6.textChanged.connect(lambda value = self.lineEdit_6, name="1erDepart_VL_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_7.textChanged.connect(lambda value = self.lineEdit_7, name="1erDepart_FPTSR_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_8.textChanged.connect(lambda value = self.lineEdit_8, name="1erDepart_SMUR_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_9.textChanged.connect(lambda value = self.lineEdit_9, name="1erDepart_heliSMUR_txt": fonctions_self.on_lineEdit_changed(self, value, name))

        self.lineEdit_10.textChanged.connect(lambda value = self.lineEdit_10, name="renfort_VSAV_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_11.textChanged.connect(lambda value = self.lineEdit_11, name="renfort_EPSA_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_12.textChanged.connect(lambda value = self.lineEdit_12, name="renfort_VL_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_13.textChanged.connect(lambda value = self.lineEdit_13, name="renfort_FPTSR_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_14.textChanged.connect(lambda value = self.lineEdit_14, name="renfort_SMUR_txt": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_15.textChanged.connect(lambda value = self.lineEdit_15, name="renfort_heliSMUR_txt": fonctions_self.on_lineEdit_changed(self, value, name))

        self.textEdit.textChanged.connect(lambda value = self.textEdit, name="rapport_txt": fonctions_self.on_textEdit_changed(self, value, name))


        self.dateTimeEdit.dateTimeChanged.connect(lambda value = self.dateTimeEdit, name="date_appel": fonctions_self.on_dateTime_changed(self, value, name))
        self.dateTimeEdit_2.dateTimeChanged.connect(lambda value = self.dateTimeEdit_2, name="date_depart": fonctions_self.on_dateTime_changed(self, value, name))
        self.dateTimeEdit_3.dateTimeChanged.connect(lambda value = self.dateTimeEdit_3, name="date_fin": fonctions_self.on_dateTime_changed(self, value, name))

        self.checkBox.stateChanged.connect(lambda value = self.checkBox, name="remorque": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_2.stateChanged.connect(lambda value = self.checkBox_2, name="gendarmerie": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_3.stateChanged.connect(lambda value = self.checkBox_3, name="edf": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_4.stateChanged.connect(lambda value = self.checkBox_4, name="brigade_verte": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_5.stateChanged.connect(lambda value = self.checkBox_5, name="gdf": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_6.stateChanged.connect(lambda value = self.checkBox_6, name="service_eaux": fonctions_self.on_checkbox_changed(self, value, name))

        #dû à la boucle for, les spv sll et caserne sont connectés et générés directement lors de la création de combobox

        fonctions_self.addItem_comboBox(self, self.comboBox_8, 'l_con_vtu')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_9, 'l_ca_vtu')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_10, 'l_ce_vtu')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_11, 'l_stag_vtu')#ajoute les items

        fonctions_self.addItem_comboBox(self, self.comboBox, 'l_con_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_2, 'l_ca_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_3, 'l_ce1_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_4, 'l_ce2_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_5, 'l_equ_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_6, 'l_equ2_fptl')#ajoute les items
        fonctions_self.addItem_comboBox(self, self.comboBox_7, 'l_stag_fptl')#ajoute les items
        self.comboBox_8.currentTextChanged.connect(lambda value = self.comboBox_12, name="con_vtu": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_9.currentTextChanged.connect(lambda value = self.comboBox_12, name="ca_vtu": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_10.currentTextChanged.connect(lambda value = self.comboBox_12, name="ce_vtu": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_11.currentTextChanged.connect(lambda value = self.comboBox_12, name="stag_vtu": fonctions_self.on_combobox_changed(self, value, name))

        self.comboBox.currentTextChanged.connect(lambda value = self.comboBox_12, name="con_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_2.currentTextChanged.connect(lambda value = self.comboBox_12, name="ca_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_3.currentTextChanged.connect(lambda value = self.comboBox_12, name="ce1_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_4.currentTextChanged.connect(lambda value = self.comboBox_12, name="ce2_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_5.currentTextChanged.connect(lambda value = self.comboBox_12, name="equ_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_6.currentTextChanged.connect(lambda value = self.comboBox_12, name="equ2_fptl": fonctions_self.on_combobox_changed(self, value, name))
        self.comboBox_7.currentTextChanged.connect(lambda value = self.comboBox_12, name="stag_fptl": fonctions_self.on_combobox_changed(self, value, name))

        self.pushButton.clicked.connect(lambda self_new_rapport = self : fonctions.rediger(self_new_rapport))
        self.pushButton_2.clicked.connect(lambda self_win_to_show = self : fonctions_self.close_window(self))

    def retranslateUi(self, Ui_rapportInter):
        _translate = QtCore.QCoreApplication.translate

        os.chdir(path_to_rinter) #n° inter
        if os.path.isfile('.nbInter'):
            nbInter = linecache.getline('.nbInter', 1)
            if nbInter.isdigit():
                nbInter = int(nbInter)
            else:
                nbInter = 0
        else:
            nbInter = 0
        Ui_rapportInter.setWindowTitle(_translate("MainWindow", "PGLX - Rapport d\'intervention N°" + str(nbInter)))
        self.label_2.setText(_translate("MainWindow", "Heur de départ"))
        self.label_5.setText(_translate("MainWindow", "Conducteur"))
        self.label_6.setText(_translate("MainWindow", "CA"))
        self.label_7.setText(_translate("MainWindow", "CE BAT"))
        self.label_8.setText(_translate("MainWindow", "CE BAL"))
        self.label_9.setText(_translate("MainWindow", "EQU BAT"))
        self.label_10.setText(_translate("MainWindow", "EQU BAL"))
        self.label_11.setText(_translate("MainWindow", "Stagiare"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "FPTL"))
        self.label_12.setText(_translate("MainWindow", "Conducteur"))
        self.label_13.setText(_translate("MainWindow", "CA"))
        self.label_14.setText(_translate("MainWindow", "CE / EQU"))
        self.label_15.setText(_translate("MainWindow", "Stagiaire"))
        self.checkBox.setText(_translate("MainWindow", "Remorque ? "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "VTU"))
        self.label_18.setText(_translate("MainWindow", "Demandeur"))
        self.label_17.setText(_translate("MainWindow", "Localisation"))
        self.checkBox_5.setText(_translate("MainWindow", "GDF"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "SPV SLL"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("MainWindow", "SPV Caserne"))
        self.label_19.setText(_translate("MainWindow", "VASV"))
        self.label_20.setText(_translate("MainWindow", "FPTSR / FPT"))
        self.label_21.setText(_translate("MainWindow", "EPSA"))
        self.label_22.setText(_translate("MainWindow", "VL / VLI"))
        self.label_24.setText(_translate("MainWindow", "Heli SMUR"))
        self.label_23.setText(_translate("MainWindow", "SMUR"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), _translate("MainWindow", "Véhicule(s) au premier départ"))
        self.label_28.setText(_translate("MainWindow", "VL / VLI"))
        self.label_26.setText(_translate("MainWindow", "EPSA"))
        self.label_27.setText(_translate("MainWindow", "FPTSR  / FPT"))
        self.label_25.setText(_translate("MainWindow", "VSAV"))
        self.label_29.setText(_translate("MainWindow", "SMUR"))
        self.label_30.setText(_translate("MainWindow", "HéliSMUR"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), _translate("MainWindow", "Renforts"))
        self.label_3.setText(_translate("MainWindow", "Heure de retour"))
        self.label_4.setText(_translate("MainWindow", "N° CODIS"))
        self.checkBox_3.setText(_translate("MainWindow", "ERDF"))
        self.label_16.setText(_translate("MainWindow", "Nature de l\'intervention:"))
        self.label.setText(_translate("MainWindow", "Heure d\'appel"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Rédaction du rapport</p></body></html>"))
        self.checkBox_6.setText(_translate("MainWindow", "Service es Eaux"))
        self.checkBox_4.setText(_translate("MainWindow", "Brigade Verte"))
        self.checkBox_2.setText(_translate("MainWindow", "Gendarmerie"))
        self.pushButton.setText(_translate("MainWindow", "Valider"))
        self.pushButton_2.setText(_translate("MainWindow", "Annuler"))

    def tmp(self):
        print('rmp')


class Ui_create_inter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_create_inter, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        global b, b2
        Ui_create_inter = self
        Ui_create_inter.setObjectName("Ui_create_inter")
        Ui_create_inter.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_create_inter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 747, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 2, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 5, 1, 4)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_5.addWidget(self.dateTimeEdit, 0, 9, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(124, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 11, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_5.addWidget(self.spinBox, 1, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(539, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 3, 1, 9)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 2, 0, 1, 12)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 3, 1, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 4, 1, 1, 4)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 5, 0, 1, 12)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)


        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.spinBox_2.setValue(b)
        self.gridLayout_5.addWidget(self.groupBox, 6, 0, 2, 7)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)

        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_4.addWidget(self.spinBox_3, 1, 2, 1, 1)
        self.spinBox_3.setValue(b2)
        self.gridLayout_5.addWidget(self.groupBox_2, 6, 7, 2, 5)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_5.addWidget(self.line_5, 7, 6, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 8, 0, 1, 12)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 9, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_5.addWidget(self.lineEdit_8, 9, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(492, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 9, 4, 1, 8)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 10, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 10, 1, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(492, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 10, 4, 1, 8)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 11, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_5.addWidget(self.lineEdit_10, 11, 1, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(446, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 11, 5, 1, 7)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 12, 0, 1, 12)
        spacerItem6 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 13, 8, 2, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 13, 11, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_5.addWidget(self.buttonBox, 14, 10, 2, 2)
        spacerItem8 = QtWidgets.QSpacerItem(518, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 15, 0, 1, 10)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 1, 1, 1)

        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_7.addWidget(self.spinBox_4, 1, 2, 1, 1)
        self.spinBox_4.setValue(b3)
        self.gridLayout_5.addWidget(self.groupBox_3, 13, 0, 2, 8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        Ui_create_inter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_create_inter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        Ui_create_inter.setMenuBar(self.menubar)

        for i in range(0, b):
            self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_4.setObjectName("lineEdit_4-" + str(i))
            self.gridLayout.addWidget(self.lineEdit_4, 1+i, 0, 1, 1)
            self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_5.setObjectName("lineEdit_5-" + str(i))
            self.gridLayout.addWidget(self.lineEdit_5, 1+i, 1, 1, 1)
            self.lineEdit_4.textChanged.connect(lambda value = self.lineEdit_4 , name = "fonctionSp-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_5.textChanged.connect(lambda value = self.lineEdit_5 , name = "sp-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        for i in range(0, b2):
            self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
            self.lineEdit_6.setObjectName("lineEdit_6-" + str(i))
            self.gridLayout_4.addWidget(self.lineEdit_6, 1+i, 0, 1, 1)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
            self.lineEdit_7.setObjectName("lineEdit_7-" + str(i))
            self.gridLayout_4.addWidget(self.lineEdit_7, 1+i, 1, 1, 1)
            self.lineEdit_6.textChanged.connect(lambda value = self.lineEdit_6 , name = "engin-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_7.textChanged.connect(lambda value = self.lineEdit_7 , name = "fonctionEngin-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        for i in range(0, b3):
            self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
            self.lineEdit_11.setObjectName("lineEdit_11-"+ str(i))
            self.gridLayout_7.addWidget(self.lineEdit_11, 1+i, 0, 1, 1)
            self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
            self.lineEdit_12.setObjectName("lineEdit_12-"+ str(i))
            self.gridLayout_7.addWidget(self.lineEdit_12, 1+i, 1, 1, 1)
            self.lineEdit_11.textChanged.connect(lambda value = self.lineEdit_11 , name = "enginRenfort-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_12.textChanged.connect(lambda value = self.lineEdit_12 , name = "fonctionEnginRenfort-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        self.retranslateUi(Ui_create_inter)
        QtCore.QMetaObject.connectSlotsByName(Ui_create_inter)

        self.spinBox_2.valueChanged.connect(lambda value = self.spinBox_2 : fonctions_self.on_spinBox_2_changed(self, value))
        self.spinBox_3.valueChanged.connect(lambda value = self.spinBox_3 : fonctions_self.on_spinBox_3_changed(self, value))
        self.spinBox_4.valueChanged.connect(lambda value = self.spinBox_4 : fonctions_self.on_spinBox_4_changed(self, value))

        self.spinBox.setMaximum(800000)
        self.spinBox.valueChanged.connect(lambda value = self.spinBox, name = "nCodis" : fonctions_self.on_spinBox_changed(self, value, name))

        self.lineEdit.textChanged.connect(lambda value = self.lineEdit , name = "centreInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_2.textChanged.connect(lambda value = self.lineEdit_2 , name = "natureInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_3.textChanged.connect(lambda value = self.lineEdit_3 , name = "observation": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_8.textChanged.connect(lambda value = self.lineEdit_8 , name = "demandeurInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_9.textChanged.connect(lambda value = self.lineEdit_9 , name = "telDemandeur": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_10.textChanged.connect(lambda value = self.lineEdit_10 , name = "adresseDemandeur": fonctions_self.on_lineEdit_changed(self, value, name))

        self.dateTimeEdit.dateTimeChanged.connect(lambda value = self.dateTimeEdit , name = "heure_appel": fonctions_self.on_dateTime_changed(self, value, name))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions.create_inter(selfi))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi))

    def retranslateUi(self, Ui_create_inter):
        _translate = QtCore.QCoreApplication.translate
        Ui_create_inter.setWindowTitle(_translate("Ui_create_inter", "Pompier-GLX - Créer une intervention"))
        self.label.setText(_translate("Ui_create_inter", "Centre d\'intervention"))
        self.label_2.setText(_translate("Ui_create_inter", "Intervention N°"))
        self.label_3.setText(_translate("Ui_create_inter", "Nature"))
        self.label_4.setText(_translate("Ui_create_inter", "Observation"))
        self.groupBox.setTitle(_translate("Ui_create_inter", "Personnels"))
        self.label_6.setText(_translate("Ui_create_inter", "Fonction"))
        self.label_7.setText(_translate("Ui_create_inter", "Personnel"))
        self.groupBox_2.setTitle(_translate("Ui_create_inter", "Véhicules"))
        self.label_9.setText(_translate("Ui_create_inter", "Engin"))
        self.label_10.setText(_translate("Ui_create_inter", "Fonction"))
        self.label_11.setText(_translate("Ui_create_inter", "Demandeur"))
        self.label_12.setText(_translate("Ui_create_inter", "Téléphone"))
        self.label_13.setText(_translate("Ui_create_inter", "Adresse"))
        self.groupBox_3.setTitle(_translate("Ui_create_inter", "Renforts"))
        self.label_5.setText(_translate("Ui_create_inter", "Engin"))
        self.label_8.setText(_translate("Ui_create_inter", "Fonction"))


class Ui_create_own(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_create_own, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self


    def suite(self):
        create_own = self
        create_own.setObjectName("create_own")
        create_own.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(create_own)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 760, 507))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        create_own.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(create_own)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuAnnuler = QtWidgets.QMenu(self.menubar)
        self.menuAnnuler.setObjectName("menuAnnuler")
        create_own.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(create_own)
        self.statusbar.setObjectName("statusbar")
        create_own.setStatusBar(self.statusbar)
        self.actionQuitter = QtWidgets.QAction(create_own)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionEnregistrer = QtWidgets.QAction(create_own)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionOuvrir = QtWidgets.QAction(create_own)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.menuAnnuler.addAction(self.actionQuitter)
        self.menuAnnuler.addSeparator()
        self.menuAnnuler.addAction(self.actionEnregistrer)
        self.menuAnnuler.addAction(self.actionOuvrir)
        self.menubar.addAction(self.menuAnnuler.menuAction())

        self.retranslateUi(create_own)
        QtCore.QMetaObject.connectSlotsByName(create_own)

        self.actionQuitter.triggered.connect(lambda selfi = self : fonctions_self.close_window(self))
        self.actionEnregistrer.triggered.connect(lambda selfi = self : fonctions_self.save_to_file(self, ".ownInter"))
        self.actionOuvrir.triggered.connect(lambda selfi = self : fonctions_self.load_to_file(self))
        self.textEdit.textChanged.connect(lambda value = self.textEdit : fonctions_self.on_textEdit_changed(self, value, "ownInter"))

    def retranslateUi(self, create_own):
        _translate = QtCore.QCoreApplication.translate
        create_own.setWindowTitle(_translate("create_own", "PGLX - Créer une feuille personnalisée"))
        self.menuAnnuler.setTitle(_translate("create_own", "Menu"))
        self.actionQuitter.setText(_translate("create_own", "Quitter"))
        self.actionEnregistrer.setText(_translate("create_own", "Enregistrer"))
        self.actionOuvrir.setText(_translate("create_own", "Ouvrir"))

class Ui_Administration(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Administration, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        Administration = self
        Administration.setObjectName("Administration")
        Administration.resize(819, 407)
        self.centralwidget = QtWidgets.QWidget(Administration)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 314))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(302, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 5, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 4, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 1, 7, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 2, 2)
        spacerItem4 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 2, 1, 7)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 0, 2, 2)
        spacerItem5 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 4, 2, 1, 7)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 6, 0, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 6, 2, 1, 7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 8, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(557, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 9, 0, 1, 6)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 9, 6, 2, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Administration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Administration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 27))
        self.menubar.setObjectName("menubar")
        Administration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Administration)
        self.statusbar.setObjectName("statusbar")
        Administration.setStatusBar(self.statusbar)

        self.retranslateUi(Administration)
        QtCore.QMetaObject.connectSlotsByName(Administration)

        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi))
        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.on_administration_ok(selfi))
        self.pushButton.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToRInter"))
        self.pushButton_2.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToRFma"))
        self.pushButton_3.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToVars"))
        self.lineEdit.textChanged.connect(lambda value = self.lineEdit, name = "newCentreInter": fonctions_self.on_lineEdit_changed(self, value, name))

    def retranslateUi(self, Administration):
        _translate = QtCore.QCoreApplication.translate
        Administration.setWindowTitle(_translate("Administration", "PGLX - Administration"))
        self.label.setText(_translate("Administration", "Administration de PGLX"))
        self.label_2.setText(_translate("Administration", "Nom du CIS"))
        self.pushButton.setText(_translate("Administration", "Chemin des interventions"))
        self.pushButton_2.setText(_translate("Administration", "Chemin des FMA ..."))
        self.pushButton_3.setText(_translate("Administration", "Chemin des variables"))

class fonctions_self: #Fonctions faisant appel à self
    def new_rapportInter(self):
        global self_ui_inter
        self_ui_inter = self
        print("Nouveau rapport d'intervention")
        self.centralwidget.setEnabled(False)
        mySW = Ui_rapportInter()
        mySW.show()

    def createInter(self):
        global self_ui_createInter
        self_ui_createInter = self
        print("Nouvelle Intervention")
        self.centralwidget.setEnabled(False)
        mySW = Ui_create_inter()
        mySW.show()

    def create_own(self):
        global self_ui_createOwn
        self_ui_createOwn = self
        print("Nouvelle feuille personnalisée")
        self.centralwidget.setEnabled(False)
        mySW = Ui_create_own()
        mySW.show()

    def administration(self):
        global self_ui_administration
        self_ui_administration = self
        print("Administration")
        self.centralwidget.setEnabled(False)
        mySW = Ui_Administration()
        mySW.show()

    def save_to_file(self, file_to_save): #ATTENTION A PRECISER LE CHEMIN DU FICHER SI IL EST DIFFERENT QUE LE CHEMIN VERS VARS
        os.chdir(path_to_vars)
        cwd = os.getcwd() #current working directory
        print("Dossier actuel", cwd)


        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As",
                path_to_rinter,
                )

        #for i in range(0, nbLigne)

        subprocess.call(["cp", file_to_save, fileName]) #ATTENTION le dernier dossier garde le nom du dossier précédent
            #path_to_session = new_path_to_session

    def load_to_file(self):#ATTENTION A PRECISER LE CHEMIN DU FICHER SI IL EST DIFFERENT QUE LE CHEMIN VERS VARS

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open",  path_to_rinter, '')

        if fileName:
            file = open(fileName[0], 'r') #prend la 1er valeur de fileName (cf getOpenFileName)
            contenue = file.read()
            self.textEdit.setText(contenue)
            self.textEdit.setReadOnly(True)

    def open_dir(self, file_to_save):
        os.chdir(path_to_vars)
        fileName = QtWidgets.QFileDialog.getExistingDirectory(directory="/home")
        print("Chemin: ", fileName)
        file = open(file_to_save, 'w')
        file.write(str(fileName))
        file.close()
        return fileName

    def on_administration_ok(self):
        global path_to_rinter, path_to_vars, path_to_rfma, centreInter, a

        os.chdir(path_to_vars)
        if os.path.isfile(".newCentreInter"):
            centreInter_2 = linecache.getline(".newCentreInter", 1)
            centreInter = centreInter_2
            print('Nouveau centre:', centreInter)
            file = open(".centreInter", 'w')
            file.write(str(centreInter))
            file.close()

        if os.path.isfile(".newPathToVars"):
            path_to_vars_2 = linecache.getline(".newPathToVars", 1)
            if os.path.exists(path_to_vars_2 + "/"):
                path_to_vars = path_to_vars_2
                print(path_to_vars)
            else:
                path_to_vars = path_to_vars_2
                print("!A n'est pas un chemin, chemin forcé!")
        if os.path.isfile(".newPathToRInter"):
            path_to_rinter_2 = linecache.getline(".newPathToRInter", 1)
            if os.path.exists(path_to_rinter_2):
                path_to_rinter = path_to_rinter_2
                file = open(".PathToRInter", 'w')
                file.write(path_to_rinter)
                file.close()
                print(path_to_rinter)
            else:
                path_to_rinter = path_to_rinter_2
                file = open(".PathToRInter", 'w')
                file.write(path_to_rinter)
                file.close()
                print("!A n'est pas un chemin, chemin forcé!")
        if os.path.isfile(".newPathToRFma"):
            path_to_rfma_2 = linecache.getline(".newPathToRFma", 1)
            if os.path.exists(path_to_rfma_2):
                path_to_rfma = path_to_rfma_2
                file = open(".PathToRFma", 'w')
                file.write(path_to_rfma)
                file.close()
                print(path_to_rfma)
            else:
                path_to_rfma = path_to_rfma_2
                file = open(".PathToRFma", 'w')
                file.write(path_to_rfma)
                file.close()
                print("!A n'est pas un chemin, chemin forcé!")


        fonctions_self.close_window(self)

        print(path_to_rfma)
        print(path_to_vars)
        print(path_to_rinter)


        conn = cups.Connection()
        # Get a list of all printers
        printers = conn.getPrinters()
        for printer in printers:
          # Print name of printers to stdout
             #(screen)
            print(printer, printers[printer]["device-uri"])
        # get first printer from printer list
        printer_name = printers.keys()[0]
        conn.printFile(printer_name, filename,
           "Python_Status_print", {})


    def on_spinBox_changed(self, value, name):
        os.chdir(path_to_vars)
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(value))
        file.close()

    def on_lineEdit_changed(self, value, name):
        os.chdir(path_to_vars)
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(value))
        file.close()

    def on_textEdit_changed(self, value, name):
        os.chdir(path_to_vars)
        value = value.toPlainText()
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(value))
        file.close()

    def on_dateTime_changed(self, value, name):
        os.chdir(path_to_vars)

        temp = QtWidgets.QDateTimeEdit() #permet d'appeler la fonction textFromDateTime pour le QDateTime value
        date_time = temp.textFromDateTime(value)

        print(name, "a pris pour valeur:", date_time)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(date_time))
        file.close()

    def on_checkbox_changed(self, value, name):
        os.chdir(path_to_vars)
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(value))
        file.close()

    def on_combobox_changed(self, value, name):
        os.chdir(path_to_vars)
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(value)
        file.close()

    def addItem_comboBox(self, combobox, file_items): #Ajoute à combobox les items présents dans le fichier file_items (lui même présent dans path_to_pglx)
        os.chdir(path_to_pglx)#les listes con_fptl .... sont logées dans path_to_pglx protégé en écriture
        if os.path.isfile('.' + file_items):
            liste = open('.' + file_items,'r')
            print("Travail sur", self, combobox, 'pour', '.' + file_items)
            i=1
            ligne = liste.readline()
            while ligne != "":
                ligne = liste.readline()
                i+=1
            liste.close()
            l = 1
            n = 1
            for n in range(1, i+1):
                l = l + 1
                item = linecache.getline('.' + file_items, n)
                combobox.addItem(str(item))
                print('ajouté:', item)
        else:
            print('!E404: pas de fichier')

    def on_spinBox_2_changed(self, value):
        print("Nombre de personnels:", value)
        global b, Ui_create_inter
        b = value
        #self.spinBox_2.setValue(5)
        win = Ui_create_inter()
        Ui_create_inter.suite(self)
        #self.spinBox_2.setValue(5)

    def on_spinBox_3_changed(self, value):
        print("Nombre de personnels:", value)
        global b2, Ui_create_inter
        b2 = value
        win = Ui_create_inter()
        Ui_create_inter.suite(self)

    def on_spinBox_4_changed(self, value):
        print("Nombre de personnels:", value)
        global b3, Ui_create_inter
        b3 = value
        win = Ui_create_inter()
        Ui_create_inter.suite(self)

    def close_window(self):
        self.close()
        global self_ui_inter
        self_ui_inter.centralwidget.setEnabled(True)

    def show_credits(self):
        self.Credits = Credits()
        self.Credits.show()

    def show_license(self):
        self.License = License()
        self.License.show()

class fonctions: #fonctions ne faisant pas appel à self

    def create_inter(self):
        global b, b2, b3, heure_appel, centreInter, nCodis, natureInter, observation, demandeurInter, telDemandeur, adresseDemandeur, personnel, engins
        print("Création de l'intervention en cours ...")
        print("Récupération des variables dans les fichiers")
        os.chdir(path_to_vars)
        heure_appel = fonctions.get_line_alpha(path_to_vars, ".heure_appel", 1)
        centreInter = fonctions.get_line_alpha(path_to_vars, ".centreInter", 1)
        nCodis = fonctions.get_line(path_to_vars, ".nCodis", 1)
        natureInter = fonctions.get_line_alpha(path_to_vars, ".natureInter", 1)
        observation = fonctions.get_line_alpha(path_to_vars, ".observation", 1)
        demandeurInter = fonctions.get_line_alpha(path_to_vars, ".demandeurInter", 1)
        telDemandeur = fonctions.get_line_alpha(path_to_vars, ".telDemandeur", 1)
        adresseDemandeur = fonctions.get_line_alpha(path_to_vars, ".adresseDemandeur", 1)

        personnel = []
        for i in range(0, b):
            fonctions_sp = str(fonctions.get_line_alpha(path_to_vars, ".fonctionSp-" + str(i), 1))
            sp = str(fonctions.get_line_alpha(path_to_vars, ".sp-" + str(i), 1))
            personnel.append([fonctions_sp, sp])
        print("Personnels:", personnel)

        engins = []
        for i in range(0, b2):
            fonction_engin = str(fonctions.get_line_alpha(path_to_vars, ".engin-" + str(i), 1))
            engin = str(fonctions.get_line_alpha(path_to_vars, ".fonctionEngin-" + str(i), 1))
            engins.append([fonction_engin, engin])
        print("Engins:", engins)

        renforts = []
        for i in range(0, b3):
            fonction_engin_renfort = str(fonctions.get_line_alpha(path_to_vars, ".enginRenfort-" + str(i), 1))
            engin_renfort = str(fonctions.get_line_alpha(path_to_vars, ".fonctionEnginRenfort-" + str(i), 1))
            renforts.append([fonction_engin_renfort, engin_renfort])
        print("Engins:", renforts)

        starLine = fonctions.create_line(80, "*")
        dashLine = fonctions.create_line(80, '-')
        fonctions.write_function(path_to_vars, "000000", heure_appel, '\n', starLine, '\n', heure_appel, '      ', centreInter, '\n', "N° Intervention: ", nCodis, '\n', "NATURE: ",  natureInter, '\n', "OBSERVATIONS: ", observation, '\n', dashLine, '\n', "DEMANDEUR: ", demandeurInter, '\n', "TELEPHONE: ", telDemandeur, '\n', "ADRESSE: ", adresseDemandeur, '\n', dashLine, '\n', "Personnels / Équipes", '\n', personnel, '\n \n', dashLine, '\n', "Engins", '\n', engins, '\n', dashLine, '\n \n', "Renforts: \n", renforts, '\n \n', starLine)

        print("ALERTE: Nouvelle intervention en cours !")
        self.hide()
        self_ui_inter.centralwidget.setEnabled(True)

    def write_function(path, name, *args, **keywords):
        os.chdir(path)
        print("Ecriture de", name)
        file = open(name, 'w')
        for i in args:
            print("Ecrit", i)
            file.write(str(i))
        file.close()

    def create_line(length, symbol):
        line = ""
        for i in range(0, length):
            line += str(symbol)
        print(line)
        return line

    def get_line_alpha(path, fichier, line):
        os.chdir(path)
        if os.path.isfile(fichier):
            linecache.clearcache()
            value = linecache.getline(fichier, line)
            print("Valeur pour", fichier, value)
            return value
        else:
            print("!A pas de fichier correcte")
            return "!A"

    def get_line(path, fichier, line):
        os.chdir(path)
        if os.path.isfile(fichier):
            value = linecache.getline(fichier, line)
            if value.isdigit():
                print("Valeur pour ", fichier, ":", value)
                return value
            else:
                print("Valeur pour ", fichier, ": 0")
                return 0
        else:
            print("Valeur pour ", fichier, ": 0")
            return 0

    def rediger(self_new_rapport):
        global self_ui_inter
        fma = False #{DEL}
        print("Rédaction en cours ...")
        print("Récupération des variables dans les fichiers")

        os.chdir(path_to_rinter) #n° inter
        if fma == False:
            file_nombre = '.nbInter'
        else:
            file_nombre = '.nbFma'
        if os.path.isfile(file_nombre):
            nombre = linecache.getline(file_nombre, 1)
            if nombre.isdigit():
                nombre = int(nombre) + 1
            else:
                nombre = 0
        else:
            nombre = 0

        os.chdir(path_to_vars)

        heure_appel = linecache.getline('.date_appel', 1)
        heure_depart = linecache.getline('.date_depart', 1)
        heure_fin = linecache.getline('.date_fin', 1)

        ncodis = linecache.getline('.nCodis', 1)
        con_fptl = linecache.getline('.con_fptl', 1)
        if str(con_fptl) != "":
            fptl = True
        else:
            fptl = False
        ca_fptl = linecache.getline('.ca_fptl', 1)
        ce_fptl = linecache.getline('.ce_fptl', 1)
        ce2_fptl = linecache.getline('.ce2_fptl', 1)
        equ_fptl = linecache.getline('.equ_fptl', 1)
        equ2_fptl = linecache.getline('.equ2_fptl', 1)
        stag_fptl = linecache.getline('.stag_fptl', 1)

        con_vtu = linecache.getline('.con_vtu', 1)
        if str(con_vtu) != "":
            vtu = True
        else:
            vtu = False
        ca_vtu = linecache.getline('.ca_vtu', 1)
        ce_vtu = linecache.getline('.ce_vtu', 1)
        stag_vtu = linecache.getline('.stag_vtu', 1)
        remorque = linecache.getline('.remorque', 1)
        if str(remorque) == 0:
            remorque = False
        else:
            remorque = True
        nature_inter = linecache.getline('.natureInter', 1)
        loc_inter = linecache.getline('.localisationInter', 1)
        demandeur_inter = linecache.getline('.demandeurInter', 1)

        spv_sll = []
        spv_caserne = []
        r = 4
        for i in range(0, r):
            a = linecache.getline('.spv_sll_comboBox_12-' + str(i), 1)
            if a != "":
                spv_sll.append(a)
            a = linecache.getline('.spv_sll_comboBox_15-' + str(i), 1)
            if a != "":
                spv_sll.append(a)
            a = linecache.getline('.spv_caserne_comboBox_13-' + str(i), 1)
            if a != "":
                spv_caserne.append(a)
            a = linecache.getline('.spv_caserne_comboBox_14-' + str(i), 1)
            if a != "":
                spv_caserne.append(a)

        print("SPV SLL", spv_sll)
        if spv_sll == []:
            spv_sll = False

        print("SPV CAS:", spv_caserne)
        if spv_caserne == []:
            spv_caserne = False

        if os.path.isfile('.1erDepart_VSAV'):
            vsav_1erDepart = linecache.getline('.1erDepart_VSAV', 1)
        else:
            vsav_1erDepart = '0'
        if os.path.isfile('.1erDepart_FPTSR'):
            fptsr_1erDepart = linecache.getline('.1erDepart_FPTSR', 1)
        else:
            fptsr_1erDepart = '0'
        if os.path.isfile('.1erDepart_EPSA'):
            epsa_1erDepart = linecache.getline('.1erDepart_EPSA', 1)
        else:
            epsa_1erDepart = '0'
        if os.path.isfile('.1erDepart_VL'):
            vl_1erDepart = linecache.getline('.1erDepart_VL', 1)
        else:
            vl_1erDepart = '0'
        if os.path.isfile('.1erDepart_SMUR'):
            smur_1erDepart = linecache.getline('.1erDepart_SMUR', 1)
        else:
            smur_1erDepart = '0'
        if os.path.isfile('.1erDepart_heliSMUR'):
            helismur_1erDepart = linecache.getline('.1erDepart_heliSMUR', 1)
        else:
            helismur_1erDepart = '0'

        vsav_1erDepart_txt = linecache.getline('.1erDepart_VSAV_txt', 1)
        fptsr_1erDepart_txt = linecache.getline('.1erDepart_FPTSR_txt', 1)
        epsa_1erDepart_txt = linecache.getline('.1erDepart_EPSA_txt', 1)
        vl_1erDepart_txt = linecache.getline('.1erDepart_VL_txt', 1)
        smur_1erDepart_txt = linecache.getline('.1erDepart_SMUR_txt', 1)
        helismur_1erDepart_txt = linecache.getline('.1erDepart_heliSMUR_txt', 1)

        if os.path.isfile('.renfort_VSAV'):
            vsav_renfort = linecache.getline('.renfort_VSAV', 1)
        else:
            vsav_renfort = '0'
        if os.path.isfile('.renfort_FPTSR'):
            fptsr_renfort = linecache.getline('.renfort_FPTSR', 1)
        else:
            fptsr_renfort = '0'
        if os.path.isfile('.renfort_EPSA'):
            epsa_renfort = linecache.getline('.renfort_EPSA', 1)
        else:
            epsa_renfort = '0'
        if os.path.isfile('.renfort_VL'):
            vl_renfort = linecache.getline('.renfort_VL', 1)
        else:
            vl_renfort = '0'
        if os.path.isfile('.renfort_SMUR'):
            smur_renfort = linecache.getline('.renfort_SMUR', 1)
        else:
            smur_renfort = '0'
        if os.path.isfile('.renfort_heliSMUR'):
            helismur_renfort= linecache.getline('.renfort_heliSMUR', 1)
        else:
            helismur_renfort = '0'

        vsav_renfort_txt = linecache.getline('.renfort_VSAV_txt', 1)
        fptsr_renfort_txt = linecache.getline('.renfort_FPTSR_txt', 1)
        epsa_renfort_txt = linecache.getline('.renfort_EPSA_txt', 1)
        vl_renfort_txt = linecache.getline('.renfort_VL_txt', 1)
        smur_renfort_txt = linecache.getline('.renfort_SMUR_txt', 1)
        helismur_renfort_txt = linecache.getline('.renfort_heliSMUR_txt', 1)

        if os.path.isfile('.gendarmerie'):
            gendarmerie = linecache.getline('.gendarmerie', 1)
        else:
            gendarmerie = '0'
        if os.path.isfile('.edf'):
            edf = linecache.getline('.edf', 1)
        else:
            edf = '0'
        if os.path.isfile('.gdf'):
            gdf = linecache.getline('.gdf', 1)
        else:
            gdf = '0'
        if os.path.isfile('.bridage_verte'):
            brigade_verte = linecache.getline('.bridage_verte', 1)
        else:
            brigade_verte = '0'
        if os.path.isfile('.service_eaux'):
            service_eaux = linecache.getline('.service_eaux', 1)
        else:
            service_eaux = '0'

        rapport = linecache.getline('.rapport_txt', 1)

        print("Ecriture du rapport en cours ...")


        if fma == False:
            type_rapport = "Intervention"
        else:
            type_rapport = "FMA"

        ligne1 = type_rapport + ': ' + 'N° '  + str(nombre) + '  |  N° CODIS: ' + str(ncodis) + "\n"
        ligne2 = 'Date d\'appel: ' + str(heure_appel) + "  " + 'Date de départ: ' + str(heure_depart) + "  " + 'Date de retour: ' + str(heure_fin) + "\n"
        ligne3 = "Véhicules: "
        if fptl == True:
            ligne3 += '  FPTL'
        if vtu == True:
            ligne3 += '  VTU'
        if remorque == True:
            ligne3 += '  Remorque emportée'
        ligne3 += "\n"
        ligne4 = 'Nature: ' + str(nature_inter) + "\n"
        ligne5 = 'Localisation: ' + str(loc_inter) + "\n"
        ligne6 = 'Demandeur: ' + str(demandeur_inter) + "\n"
        ligne7 = '\n Sapeur-Pompiers & Fonctions \n'

        if fptl == True:
            ligne8 = "CA FPTL: " + str(ca_fptl) + '\n'
            ligne9 = "Conducteur FPTL: " + str(con_fptl) + '\n'
            ligne10 = "CE BAT FPTL: " + str(ce_fptl) + '\n'
            ligne11 = "EQU BAT FPRL: " + str(equ_fptl) + '\n'
            ligne12 = "CE BAL FPTL: " + str(ce2_fptl) + '\n'
            ligne13 = "EQU BAT FPTL: " + str(equ2_fptl) + '\n'
            ligne13_2 = "Stagiaire FPTL" + str(stag_fptl) + '\n'
        if vtu == True:
            ligne14 = "\n CA VTU: " + str(ca_vtu) + '\n'
            ligne15 = "Conducteur VTU: " + str(con_vtu) + '\n'
            ligne16 = "EQU VTU: " + str(ce_vtu) + '\n'
            ligne16_2 = "Stagiaire VTU" + str(stag_vtu) + '\n'

        linecache.clearcache()
        nb_ligne_rapport = fonctions.nombre_de_ligne('.rapport_txt')
        ligne_text = ""
        for i in range (0, nb_ligne_rapport):
            ligne_text += linecache.getline('.rapport_txt', i)
            print('Rapport:', ligne_text)


        if fma == False:
            if spv_sll == False:
                ligne17 = "Pas de SPV SLL" + '\n'
            else:
                ligne17 = "SPV SLL:" + '\n'
                ligne18 = spv_sll
            print("SPV SLL:", ligne17)


        else:
            ligne17 = "Formateurs:" + '\n'
            l = linecache.getline('.formateurs', 1)

            ligne18 = l
            if ligne18 == "":
                ligne18 = "Aucun"
            else:
                ligne18 = ""
            print(ligne18, "ligne18")


            l = linecache.getline('.formateurs', 2)
            ligne19 = l

            l = linecache.getline('.formateurs', 2)
            ligne20 = l


        if spv_caserne != False:
            if fma == True:
                ligne21 = '\n' + "Autres participants" + '\n'
            else:
                ligne21 = '\n' + "\n SPV à la Caserne" + '\n'
                ligne22 = spv_caserne
            print("SPV CAS:", ligne21)
        else:
            if fma == True:
                ligne21 = '\n'+ "Pas d'autres participants" + '\n'
            else:
                ligne21 = '\n' + "Pas de SPV à la Caserne" + '\n'


        os.chdir(path_to_vars)  # mène vers le répertoire des variables
        with open('0rapport', 'w') as fichier:
            fichier.write(ligne1)
            fichier.write(ligne2)
            fichier.write(ligne3)
            fichier.write("\n")
            fichier.write(ligne4)
            fichier.write(ligne5)
            fichier.write(ligne6)
            fichier.write("\n")
            fichier.write(ligne7)
            if fptl == True:
                fichier.write(ligne8)
                fichier.write(ligne9)
                fichier.write(ligne10)
                fichier.write(ligne11)
                fichier.write(ligne12)
                fichier.write(ligne13)
            if vtu == True:
                fichier.write(ligne14)
                fichier.write(ligne15)
                fichier.write(ligne16)

            fichier.write('\n')

            fichier.write(ligne17)

            if spv_sll != False:
                fichier.write(str(ligne18))

            fichier.write(ligne21)
            if spv_caserne != False:
                fichier.write(str(ligne22))

            fichier.write("\n \n Véhicules au 1e départ \n")
            if (vsav_1erDepart[0] != '0') and (vsav_1erDepart != ""):
                fichier.write("VSAV:" + vsav_1erDepart + '  ' + vsav_1erDepart_txt + '\n')
            if (fptsr_1erDepart[0] != '0') and (fptsr_1erDepart != ""):
                fichier.write("FPTSR/FPT:" + fptsr_1erDepart + '  ' + fptsr_1erDepart_txt + '\n')
            if (epsa_1erDepart[0] != '0') and (epsa_1erDepart != ""):
                fichier.write("EPSA/EPA:" + epsa_1erDepart + '  ' + epsa_1erDepart_txt + '\n')
            if (vl_1erDepart[0] != '0') and (vl_1erDepart != ""):
                fichier.write("VL/VLI:" + vl_1erDepart + '  ' + vl_1erDepart_txt + '\n')
            if (smur_1erDepart[0]  != '0') and (smur_1erDepart != ""):
                fichier.write("SMUR:" + smur_1erDepart + '  ' + smur_1erDepart_txt + '\n')
            if (helismur_1erDepart[0] != '0') and (helismur_1erDepart != ""):
                fichier.write("HéliSMUR:" + helismur_1erDepart + '  ' + helismur_1erDepart_txt + '\n')


            fichier.write("\n Véhicules en renfort \n")
            if (vsav_renfort[0] != '0') and (vsav_renfort != ""):
                fichier.write("VSAV:" + vsav_renfort + '  ' + vsav_renfort_txt )#+ '\n')
            if (fptsr_renfort[0] != '0') and (fptsr_renfort != ""):
                fichier.write("FPTSR/FPT:" + fptsr_renfort + '  ' + fptsr_renfort_txt )#+ '\n')
            if (epsa_renfort[0] != '0') and (epsa_renfort != ""):
                fichier.write("EPSA/EPA:" + epsa_renfort + '  ' + epsa_renfort_txt )#+ '\n')
            if (vl_renfort[0] != '0') and (vl_renfort != ""):
                fichier.write("VL/VLI:" + vl_renfort + '  ' + vl_renfort_txt )#+ '\n')
            if (smur_renfort[0]  != '0') and (smur_renfort != ""):
                fichier.write("SMUR:" + smur_renfort + '  ' + smur_renfort_txt )#+ '\n')
            if (helismur_renfort[0] != '0') and (helismur_renfort != ""):
                fichier.write("HéliSMUR:" + helismur_renfort + '  ' + helismur_renfort_txt )#+ '\n')

            fichier.write("\n \n")

            if gendarmerie != '0':
                fichier.write("Gendarmerie SLL | ")
            if gdf != '0':
                fichier.write("GRDF SLL | ")
            if service_eaux != '0':
                fichier.write("Service des eaux SLL | ")
            if edf != '0':
                fichier.write("ERDF SLL | ")
            if brigade_verte != '0':
                fichier.write("Brigade Verte SLL | ")

            fichier.write('\n')
            fichier.write('\n' + 'Rapport de l\'intervention:' + '\n')
            fichier.write(ligne_text)

            print("Rapport rédigé avec succès !")

            self_ui_inter.centralwidget.setEnabled(True)
            Ui_rapportInter.close()


            name = "Rapport-" + str(nombre)
            nombre_2 = nombre

            if os.path.isfile(path_to_rinter + '/' + name):
                while os.path.isfile(path_to_rinter + '/' + name):
                    nombre_2 += 1
                    name = "Rapport-" + str(nombre_2)

            if fma == False:
                new_name = path_to_rinter + '/' + name
            else:
                path_to_rfma = path_to_rinter #{DEL}
                new_name = path_to_rfma + '/' + name

            subprocess.call(["mv", "0rapport", new_name])
            file_tmp = path_to_vars + '/' + ".1erDepart_VSAV"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_FPTSR"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_EPSA"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_VL"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_SMUR"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_heliSMUR"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".1erDepart_VSAV_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_FPTSR_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_EPSA_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_VL_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_SMUR_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".1erDepart_heliSMUR_txt"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".renfort_VSAV"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_FPTSR"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_EPSA"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_VL"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_SMUR"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_heliSMUR"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".renfort_VSAV_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_FPTSR_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_EPSA_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_VL_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_SMUR_txt"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".renfort_heliSMUR_txt"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".bridage_verte"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".gendarmerie"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".gdf"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".edf"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".service_eaux"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".con_vtu"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".ca_vtu"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".ce_vtu"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".stag_vtu"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".con_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".ca_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".ce_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".ce2_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".equ_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".equ_fptl"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".stag_fptl"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".remorque"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".rapport_txt"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".date_appel"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".date_depart"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".date_fin"
            fonctions.delete_file(file_tmp)

            for i in range(0, 12):
                file_tmp = path_to_vars + '/' + ".spv_caserne_comboBox_13-" + str(i)
                fonctions.delete_file(file_tmp)
                file_tmp = path_to_vars + '/' + ".spv_caserne_comboBox_14-" + str(i)
                fonctions.delete_file(file_tmp)
                file_tmp = path_to_vars + '/' + ".spv_sll_comboBox_12-" + str(i)
                fonctions.delete_file(file_tmp)
                file_tmp = path_to_vars + '/' + ".spv_sll_comboBox_15-" + str(i)
                fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".nCodis"
            fonctions.delete_file(file_tmp)

            file_tmp = path_to_vars + '/' + ".localisationInter"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".natureInter"
            fonctions.delete_file(file_tmp)
            file_tmp = path_to_vars + '/' + ".demandeurInter"
            fonctions.delete_file(file_tmp)

            file = open(file_nombre, 'w')
            file.write(str(nombre))
            file.close()

    def delete_file(file_to_delete):
        subprocess.call(["rm", file_to_delete])

    def nombre_de_ligne(fichier): # fonction pour connaitre le nombre de ligne pour le fichier "fichier"
        global nb_ligne
        if os.path.isfile(fichier):
            liste = open(fichier,'r')
            nb_ligne=0
            ligne = "test_de_continuation"
            while ligne != "":
                ligne = liste.readline()
                nb_ligne+=1
                print("nbligne::", nb_ligne, "   ", ligne)
            liste.close()
            nb_ligne = nb_ligne-1
            print('NB LIGNE a la fin de la fonction', nb_ligne)
        else:
            nb_ligne = 0
            print("PAS DE FICHIER !A")
        return nb_ligne


class Credits(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Credits, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Pompier-GLX - Crédits')
        self.show()

        os.chdir(path_to_pglx)
        file = open('.credits', 'r')
        contenue = file.read()
        self.textEdit.setText(contenue)
        self.textEdit.setReadOnly(True)

class License(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(License, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Pompier-GLX - Licence')
        self.show()

        os.chdir(path_to_pglx)
        file = open('COPYRIGHT', 'r')
        contenue = file.read()
        self.textEdit.setText(contenue)
        self.textEdit.setReadOnly(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mySW = Ui_PompierGLX()
    mySW.show()
    sys.exit(app.exec_())

"""
    <Pompier-GLX>
    Copyright (C) <2013>  <Sydney Rodolphe Torcuato Gems>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
