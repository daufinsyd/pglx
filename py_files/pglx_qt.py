#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5 import *
import os, sys, subprocess, random
import pickle
import readline
import linecache # lis les lignes spécifiques de fichier vs pas de global variables dans les class
import time
import getpass
import datetime
#from fonctions import *

path_to_pglx = "/home/Pompiers/Public/Rapports/Pompier-GLX" ### Sert unsiquement pour les fichiers py et images ###
path_to_vars = "/home/Pompiers/Public/.tmp" ### sert pour toutes les vars du rapport et des rapports en gnal ###
path_to_rinter = "/home/Pompiers/Public/Rapports/Interventions/2014" ### sert uniquement pour l'écriture du rapport ###
path_to_rfma = "/home/Pompiers/Public/Rapports/FMA/2014"### sert uniquement pour l'écriture du rapport ###
path_to_rcasernement = "/home/Pompiers/Public/Rapports/Casernements/2014"### sert uniquement pour l'écriture du rapport ###
path_to_session = "/home/Pompiers/Public/.tmp/session" ### sert à stocker à travers le temps des variables
path_to_stats_personnal = "/home/Pompiers/Public/Rapports/Statistiques/Personnels"

if os.path.exists(path_to_pglx) == False:
    subprocess.call(["mkdir", "-p", path_to_pglx])
    if os.path.exists(path_to_pglx) == False:
        print("Impossible de créer un chemin")

if os.path.exists(path_to_vars) == False:
    subprocess.call(["mkdir", "-p", path_to_vars])
    if os.path.exists(path_to_vars) == False:
        print("Impossible de créer un chemin")

if os.path.exists(path_to_rinter) == False:
    subprocess.call(["mkdir", "-p", path_to_rinter])
    if os.path.exists(path_to_rinter) == False:
        print("Impossible de créer un chemin")

if os.path.exists(path_to_rfma) == False:
    subprocess.call(["mkdir", "-p", path_to_rfma])
    if os.path.exists(path_to_rfma) == False:
        print("Impossible de créer un chemin")

if os.path.exists(path_to_rcasernement) == False:
    subprocess.call(["mkdir", "-p", path_to_rcasernement])
    if os.path.exists(path_to_rcasernement) == False:
        print("Impossible de créer un chemin")

if os.path.exists(path_to_session) == False:
    subprocess.call(["mkdir", "-p", path_to_session])
    if os.path.exists(path_to_session) == False:
        print("Impossible de créer un chemin")

os.chdir(path_to_vars)
if os.path.isfile(".PathToRInter"):
    path_ = linecache.getline('.PathToRInter', 1)
    if os.path.exists(path_):
        path_to_rinter = path_
    else:
        print("Tentative de création du répertoire")
        subprocess.call(["mkdir", "-p", path_])
        if os.path.isfile(path_):
            path_to_rinter = path_
            print("nouveau chemin: ", path_to_rinter)
        else:
            print("Impossible de créer le chemin, utilisation du chemin par défaut")

if os.path.isfile(".PathToRFma"):
    path_to_rfma_ = linecache.getline('.PathToRFma', 1)
    if os.path.exists(path_to_rfma_):
        path_to_rfma = path_to_rfma_
    else:
        print("Tentative de création du répertoire")
        subprocess.call(["mkdir", "-p", path_to_rfma_])
        if os.path.isfile(path_to_rfma_):
            path_to_rfma = path_to_rfma_
            print("nouveau chemin: ", path_to_rfma)
        else:
            print("Impossible de créer le chemin, utilisation du chemin par défaut")

if os.path.isfile(".PathToSession"):
    path_to_session_ = linecache.getline('.PathToSession', 1)
    if os.path.exists(path_to_session_):
        path_to_session = path_to_session_
    else:
        print("Tentative de création du répertoire")
        subprocess.call(["mkdir", "-p", path_to_session_])
        if os.path.isfile(path_to_session_):
            path_to_session = path_to_session_
            print("nouveau chemin: ", path_to_rfma)
        else:
            print("Impossible de créer le chemin, utilisation du chemin par défaut")



b = 4
b2 = 2
b3 = 1
b_casernement = 8

b_fma_formateur = 3
b_fma_spv = 18
b_fma_vehicules = 2
b_fma_lieux = 1
NCODISMAX = 500000 #nombre maximum pour le numero CODIS

nbSPVSLL = 4 #nb SPV SLL dans boucle for
nbSPVCas = 5 #nb SPV Cas dans boucle for

NFPTL = 2#A REMETTRE à 1
NVTU = 2#A REMETTRE VALEUR PAR DEFAUT
NVL = 2#A REMETTRE VALEUR PAR DEFAUT
NEPSA=0
NFPTSR=0
NVSAV=0

#tailles des fenêtres
xPglxSize = 730
yPglxSize = 400
xRapportInterSize = 800
yRapportInterSize = 600
xCreateInterSize = 800
yCreateInterSize = 600
xCreateOwnSize = 800
yCreateOwnSize = 600
xAdministrationSize = 819
yAdministrationSize = 407
xCasernementSize = 833
yCasernementSize = 679
xFmaSize = 856
yFmaSize = 467
xListIntersSize = 727
yListIntersSize = 472
xListInterPersonnalSize = 727
yListInterPersonnalSize = 472
xDialogAddUserSize = 272
yDialogAddUserSize = 226
xDialogRemoveUserSize = 272
yDialogRemoveUserSize = 226


DEBUG = 3



DELETE_INTER_RITGHS = 100
userRights = 999

#nbSPVSLL = fonctions.get_line_int(path_to_session, "nbSPVSLL", 1, 5)
print("nbSPVCLL", nbSPVSLL)

#nbSPVCas = fonctions.get_line_int(path_to_session, "nbSPVCas", 1, 6)
print("nbSPVCas", nbSPVCas)

class Ui_PompierGLX(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_PompierGLX, self).__init__(parent)
        fonctions.update_vars()
        self.suite()

    def suite(self):
        global PompierGLX, self_ui_inter, Ui_PompierGLX
        self_ui_inter = self
        PompierGLX = self
        PompierGLX.setObjectName("PompierGLX")
        PompierGLX.resize(xPglxSize, yPglxSize)
        self.centralwidget = QtWidgets.QWidget(PompierGLX)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 7, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 7, 6, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 3, 6, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton_listeInters = QtWidgets.QPushButton(self.frame)
        self.pushButton_listeInters.setObjectName("pushButton_listeInters")
        self.gridLayout_2.addWidget(self.pushButton_listeInters, 10, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 155, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.button_close = QtWidgets.QPushButton(self.frame)
        self.button_close.setObjectName("button_close")
        self.gridLayout_2.addWidget(self.button_close, 12, 7, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 8, 4, 1, 4)
        self.line2 = QtWidgets.QFrame(self.frame)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.gridLayout_2.addWidget(self.line2, 9, 0, 1, 1)
        self.new_rapportInter = QtWidgets.QPushButton(self.frame)
        self.new_rapportInter.setObjectName("new_rapportInter")
        self.gridLayout_2.addWidget(self.new_rapportInter, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 4, 6, 1, 2)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 9, 6, 2, 2)
        spacerItem2 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 5, 1, 1, 3)
        self.user = QtWidgets.QLabel(self.frame)
        self.user.setObjectName("user")
        self.gridLayout_2.addWidget(self.user, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 5, 6, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 8, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 3, 2, 2)

        self.line_personnal = QtWidgets.QFrame(self.frame)
        self.line_personnal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_personnal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_personnal.setObjectName("line_personnal")
        self.gridLayout_2.addWidget(self.line_personnal, 11, 0, 1, 1)

        self.pushButton_personnalInter = QtWidgets.QPushButton(self.frame)
        self.pushButton_personnalInter.setObjectName("pushButton_personnalInter")
        self.gridLayout_2.addWidget(self.pushButton_personnalInter, 12, 0, 1, 1)

        self.line1 = QtWidgets.QFrame(self.frame)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.gridLayout_2.addWidget(self.line1, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 11, 7, 3, 1)
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setMinimumSize(QtCore.QSize(150, 20))
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        PompierGLX.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PompierGLX)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        PompierGLX.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PompierGLX)
        self.statusbar.setObjectName("statusbar")
        PompierGLX.setStatusBar(self.statusbar)

        self.retranslateUi(PompierGLX)

        QtCore.QMetaObject.connectSlotsByName(PompierGLX)


        #CONNEXIONS
        self.new_rapportInter.clicked.connect(lambda selfi = self : fonctions_self.new_rapportInter(self))
        self.pushButton_personnalInter.clicked.connect(lambda selfi = self:fonctions_self.personnalInters(self))
        self.pushButton_7.clicked.connect(lambda selfi = self :fonctions_self.show_credits(self))
        self.pushButton_8.clicked.connect(lambda selfi = self :fonctions_self.show_license(self))
        self.pushButton_4.clicked.connect(lambda selfi = self :fonctions_self.createInter(self))
        self.pushButton_5.clicked.connect(lambda selfi = self :fonctions_self.create_own(self))
        self.pushButton_9.clicked.connect(lambda selfi = self :fonctions_self.administration(self))
        self.pushButton_3.clicked.connect(lambda selfi = self :fonctions_self.casernement(self))
        self.pushButton_2.clicked.connect(lambda selfi = self :fonctions_self.fma(self))
        self.pushButton_listeInters.clicked.connect(lambda selfi = self :fonctions_self.listInters(self))
        self.button_close.clicked.connect(self.close)

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xPglxSize, yPglxSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xPglxSize = size.width()
        yPglxSize = size.height()

    def retranslateUi(self, PompierGLX):
        file = path_to_pglx + '/.centreInter'
        if os.path.isfile(file):
            name_2 = linecache.getline(file, 1)
        else:
            name_2 = "du Centre d'Icendie et de Secours"
        USER = getpass.getuser()

        _translate = QtCore.QCoreApplication.translate
        PompierGLX.setWindowTitle(_translate("PompierGLX", "Pompier-GLX"))
        self.pushButton_4.setText(_translate("PompierGLX", "Créer une Intervention"))
        self.pushButton_9.setText(_translate("PompierGLX", "Administration"))
        self.pushButton_7.setText(_translate("PompierGLX", "Crédits"))
        self.label_2.setText(_translate("PompierGLX", "Vous êtes connecté en tant que"))
        self.label.setText(_translate("PompierGLX", "Bienvenue dans le Gestionnaire des Sapeurs-Pompiers du "))
        self.pushButton_listeInters.setText(_translate("PompierGLX", "Liste des Inters"))
        self.pushButton_3.setText(_translate("PompierGLX", "Rédiger un rapport de Casernement"))
        self.button_close.setText(_translate("PompierGLX", "Quitter"))
        self.pushButton_10.setText(_translate("PompierGLX", "Se connecter sous une autre session"))
        self.new_rapportInter.setText(_translate("PompierGLX", "Rédiger un rapport d\'Intervention"))
        self.pushButton_8.setText(_translate("PompierGLX", "License"))
        self.pushButton_11.setText(_translate("PompierGLX", "Préférences"))
        self.user.setText(_translate("PompierGLX", USER))
        self.pushButton_2.setText(_translate("PompierGLX", "Rédiger un rapport de FMA"))
        self.pushButton_5.setText(_translate("PompierGLX", "Créer une feuille personnalisée"))
        self.name.setText(_translate("PompierGLX", name_2))
        self.pushButton_personnalInter.setText(_translate("PompierGLX", "Mes Interventions"))


    def tmp(self):
        print("rien")


class Ui_rapportInter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_rapportInter, self).__init__(parent)
        self.suite()

    def suite(self):
        global Ui_rapportInter, NCODISMAX, nbSPVSLL, nbSPVCas, NFPTL, NVTU, NVL
        Ui_rapportInter = self
        Ui_rapportInter.setObjectName("MainWindow")
        Ui_rapportInter.resize(xRapportInterSize, yRapportInterSize)
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
        #typeInter
        self.comboBox_typeInter = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_typeInter.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_typeInter.setObjectName("comboBox_typeInter")
        self.gridLayout_3.addWidget(self.comboBox_typeInter, 1, 4, 1, 1)

        fonctions_self.addItem_comboBox(self, self.comboBox_typeInter, 'typesInter')#ajoute le type d'inter

        self.label_typeInter = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_typeInter.setObjectName("label_typeInter")
        self.gridLayout_3.addWidget(self.label_typeInter, 0, 4, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_3.addWidget(self.dateTimeEdit, 0, 2, 1, 1)
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)#Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")

        #FPTL
        for i in range(1, NFPTL+1):
            self.FPTL = QtWidgets.QWidget()
            self.FPTL.setGeometry(QtCore.QRect(0, 0, 667, 93))
            self.FPTL.setObjectName("FPTL" + '-' + str(i))
            self.gridLayout_4 = QtWidgets.QGridLayout(self.FPTL)
            self.gridLayout_4.setObjectName("gridLayout_4" + '-' + str(i))
            self.label_5 = QtWidgets.QLabel(self.FPTL)
            self.label_5.setObjectName("label_5" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
            self.comboBox = QtWidgets.QComboBox(self.FPTL)
            self.comboBox.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox.setObjectName("comboBox" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox, 0, 1, 2, 1)
            self.label_6 = QtWidgets.QLabel(self.FPTL)
            self.label_6.setObjectName("label_6" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
            self.comboBox_2 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_2.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_2.setObjectName("comboBox_2" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_2, 2, 1, 2, 1)
            self.label_7 = QtWidgets.QLabel(self.FPTL)
            self.label_7.setObjectName("label_7" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
            self.comboBox_3 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_3.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_3.setObjectName("comboBox_3" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_3, 4, 1, 2, 1)
            self.label_8 = QtWidgets.QLabel(self.FPTL)
            self.label_8.setObjectName("label_8" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
            self.comboBox_4 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_4.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_4.setObjectName("comboBox_4" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_4, 6, 1, 2, 1)
            self.label_9 = QtWidgets.QLabel(self.FPTL)
            self.label_9.setObjectName("label_9" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)
            self.comboBox_5 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_5.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_5.setObjectName("comboBox_5" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_5, 8, 1, 2, 1)
            self.label_10 = QtWidgets.QLabel(self.FPTL)
            self.label_10.setObjectName("label_10" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_10, 5, 0, 1, 1)
            self.comboBox_6 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_6.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_6.setObjectName("comboBox_6" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_6, 10, 1, 2, 1)
            self.label_11 = QtWidgets.QLabel(self.FPTL)
            self.label_11.setObjectName("label_11" + '-' + str(i))
            self.gridLayout_4.addWidget(self.label_11, 6, 0, 1, 1)
            self.comboBox_7 = QtWidgets.QComboBox(self.FPTL)
            self.comboBox_7.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_7.setObjectName("comboBox_7" + '-' + str(i))
            self.gridLayout_4.addWidget(self.comboBox_7, 12, 1, 1, 1)
            #self.scrollArea_2.setWidget(self.FPTL)
            #self.verticalLayout.addWidget(self.scrollArea_2)
            self.toolBox.addItem(self.FPTL, "")

            #MODIFICATIONS
            fonctions_self.addItem_comboBox(self, self.comboBox, 'l_con_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_2, 'l_ca_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_3, 'l_ce_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_4, 'l_ce2_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_5, 'l_equ_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_6, 'l_equ2_fptl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_7, 'l_stag_fptl')#ajoute les items

            #CONNEXIONS
            self.comboBox.currentTextChanged.connect(lambda value = self.comboBox, name="con_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_2.currentTextChanged.connect(lambda value = self.comboBox_2, name="ca_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_3.currentTextChanged.connect(lambda value = self.comboBox_3, name="ce1_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_4.currentTextChanged.connect(lambda value = self.comboBox_4, name="ce2_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_5.currentTextChanged.connect(lambda value = self.comboBox_5, name="equ_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_6.currentTextChanged.connect(lambda value = self.comboBox_6, name="equ2_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_7.currentTextChanged.connect(lambda value = self.comboBox_7, name="stag_fptl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))

            #_translate
            _translate = QtCore.QCoreApplication.translate
            self.label_5.setText(_translate("MainWindow", "Conducteur"))
            self.label_6.setText(_translate("MainWindow", "CA"))
            self.label_7.setText(_translate("MainWindow", "CE BAT"))
            self.label_8.setText(_translate("MainWindow", "CE BAL"))
            self.label_9.setText(_translate("MainWindow", "EQU BAT"))
            self.label_10.setText(_translate("MainWindow", "EQU BAL"))
            self.label_11.setText(_translate("MainWindow", "Stagiare"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.FPTL), _translate("MainWindow", "FPTL" + '-' + str(i)))

        #VTU
        for i in range(1, NVTU+1):
            self.VTU = QtWidgets.QWidget()
            self.VTU.setGeometry(QtCore.QRect(0, 0, 716, 93))
            self.VTU.setObjectName("VTU" + '-' + str(i))
            self.gridLayout_5 = QtWidgets.QGridLayout(self.VTU)
            self.gridLayout_5.setObjectName("gridLayout_5" + '-' + str(i))
            self.label_12 = QtWidgets.QLabel(self.VTU)
            self.label_12.setObjectName("label_12" + '-' + str(i))
            self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
            self.comboBox_8 = QtWidgets.QComboBox(self.VTU)
            self.comboBox_8.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_8.setObjectName("comboBox_8" + '-' + str(i))
            self.gridLayout_5.addWidget(self.comboBox_8, 0, 1, 1, 1)
            self.label_13 = QtWidgets.QLabel(self.VTU)
            self.label_13.setObjectName("label_13" + '-' + str(i))
            self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
            self.comboBox_9 = QtWidgets.QComboBox(self.VTU)
            self.comboBox_9.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_9.setObjectName("comboBox_9" + '-' + str(i))
            self.gridLayout_5.addWidget(self.comboBox_9, 1, 1, 1, 1)
            self.label_14 = QtWidgets.QLabel(self.VTU)
            self.label_14.setObjectName("label_14" + '-' + str(i))
            self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)
            self.comboBox_10 = QtWidgets.QComboBox(self.VTU)
            self.comboBox_10.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_10.setObjectName("comboBox_10" + '-' + str(i))
            self.gridLayout_5.addWidget(self.comboBox_10, 2, 1, 1, 1)
            self.label_15 = QtWidgets.QLabel(self.VTU)
            self.label_15.setObjectName("label_15" + '-' + str(i))
            self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)
            self.comboBox_11 = QtWidgets.QComboBox(self.VTU)
            self.comboBox_11.setMinimumSize(QtCore.QSize(0, 32))
            self.comboBox_11.setObjectName("comboBox_11" + '-' + str(i))
            self.gridLayout_5.addWidget(self.comboBox_11, 3, 1, 1, 1)
            self.checkBox = QtWidgets.QCheckBox(self.VTU)
            self.checkBox.setObjectName("checkBox" + '-' + str(i))
            self.gridLayout_5.addWidget(self.checkBox, 4, 0, 1, 1)
            #self.scrollArea_3.setWidget(self.VTU)
            #self.verticalLayout_2.addWidget(self.scrollArea_3)
            self.toolBox.addItem(self.VTU, "")

            #MODIFICATIONS
            fonctions_self.addItem_comboBox(self, self.comboBox_8, 'l_con_vtu')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_9, 'l_ca_vtu')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_10, 'l_ce_vtu')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_11, 'l_stag_vtu')#ajoute les items

            #CONNEXIONS
            self.checkBox.stateChanged.connect(lambda value = self.checkBox, name="remorque" + '-' + str(i): fonctions_self.on_checkbox_changed(self, value, name))
            self.comboBox_8.currentTextChanged.connect(lambda value = self.comboBox_8, name="con_vtu" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_9.currentTextChanged.connect(lambda value = self.comboBox_9, name="ca_vtu" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_10.currentTextChanged.connect(lambda value = self.comboBox_10, name="ce_vtu" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_11.currentTextChanged.connect(lambda value = self.comboBox_11, name="stag_vtu" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))

            #_translate
            _translate = QtCore.QCoreApplication.translate
            self.label_12.setText(_translate("MainWindow", "Conducteur"))
            self.label_13.setText(_translate("MainWindow", "CA"))
            self.label_14.setText(_translate("MainWindow", "CE / EQU"))
            self.label_15.setText(_translate("MainWindow", "Stagiaire"))
            self.checkBox.setText(_translate("MainWindow", "Remorque ? "))
            self.toolBox.setItemText(self.toolBox.indexOf(self.VTU), _translate("MainWindow", "VTU" + '-' + str(i)))




        #VL
        for i in range(1, NVL+1):
            self.VL = QtWidgets.QWidget()
            self.VL.setGeometry(QtCore.QRect(0, 0, 730, 192))#AJOUTE
            self.VL.setObjectName("VL" + '-' + str(i))
            self.gridLayout_10 = QtWidgets.QGridLayout(self.VL)
            self.gridLayout_10.setObjectName("gridLayout_10" + '-' + str(i))
            self.label_32 = QtWidgets.QLabel(self.VL)
            self.label_32.setObjectName("label_32" + '-' + str(i))

            self.gridLayout_10.addWidget(self.label_32, 2, 0, 1, 1)
            self.comboBox_17 = QtWidgets.QComboBox(self.VL)
            self.comboBox_17.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBox_17.setObjectName("comboBox_17" + '-' + str(i))
            self.gridLayout_10.addWidget(self.comboBox_17, 2, 1, 1, 1)
            self.label_34 = QtWidgets.QLabel(self.VL)
            self.label_34.setObjectName("label_34" + '-' + str(i))
            self.gridLayout_10.addWidget(self.label_34, 4, 0, 1, 1)
            self.comboBox_18 = QtWidgets.QComboBox(self.VL)
            self.comboBox_18.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBox_18.setObjectName("comboBox_18" + '-' + str(i))
            self.gridLayout_10.addWidget(self.comboBox_18, 3, 1, 1, 1)
            self.label_35 = QtWidgets.QLabel(self.VL)
            self.label_35.setObjectName("label_35" + '-' + str(i))
            self.gridLayout_10.addWidget(self.label_35, 6, 0, 1, 1)
            self.label_33 = QtWidgets.QLabel(self.VL)
            self.label_33.setObjectName("label_33" + '-' + str(i))
            self.gridLayout_10.addWidget(self.label_33, 3, 0, 1, 1)
            self.label_36 = QtWidgets.QLabel(self.VL)
            self.label_36.setObjectName("label_36" + '-' + str(i))
            self.gridLayout_10.addWidget(self.label_36, 5, 0, 1, 1)
            self.comboBox_19 = QtWidgets.QComboBox(self.VL)
            self.comboBox_19.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBox_19.setObjectName("comboBox_19" + '-' + str(i))
            self.gridLayout_10.addWidget(self.comboBox_19, 4, 1, 1, 1)
            self.comboBox_20 = QtWidgets.QComboBox(self.VL)
            self.comboBox_20.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBox_20.setObjectName("comboBox_20" + '-' + str(i))
            self.gridLayout_10.addWidget(self.comboBox_20, 5, 1, 1, 1)
            self.comboBox_21 = QtWidgets.QComboBox(self.VL)
            self.comboBox_21.setMinimumSize(QtCore.QSize(0, 30))
            self.comboBox_21.setObjectName("comboBox_21" + '-' + str(i))
            self.gridLayout_10.addWidget(self.comboBox_21, 6, 1, 1, 1)
            self.toolBox.addItem(self.VL, "")

            #MODIFICATIONS
            fonctions_self.addItem_comboBox(self, self.comboBox_17, 'l_con_vl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_18, 'l_ca_vl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_19, 'l_ce_vl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_20, 'l_equ_vl')#ajoute les items
            fonctions_self.addItem_comboBox(self, self.comboBox_21, 'l_stag_vl')#ajoute les items

            #CONNEXIONS
            self.comboBox_17.currentTextChanged.connect(lambda value = self.comboBox_17, name="con_vl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_18.currentTextChanged.connect(lambda value = self.comboBox_18, name="ca_vl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_19.currentTextChanged.connect(lambda value = self.comboBox_19, name="ce_vl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_20.currentTextChanged.connect(lambda value = self.comboBox_20, name="equ_vl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox_21.currentTextChanged.connect(lambda value = self.comboBox_21, name="stag_vl" + '-' + str(i): fonctions_self.on_combobox_changed(self, value, name))


            #retranslateUi
            _translate = QtCore.QCoreApplication.translate
            self.label_32.setText(_translate("MainWindow", "Conducteur VL"))
            self.label_34.setText(_translate("MainWindow", "CE VL"))
            self.label_35.setText(_translate("MainWindow", "Stagiaire"))
            self.label_33.setText(_translate("MainWindow", "CA VL"))
            self.label_36.setText(_translate("MainWindow", "EQU VL"))
            self.toolBox.setItemText(self.toolBox.indexOf(self.VL), _translate("MainWindow", "VL-" + str(i)))

        self.gridLayout_3.addWidget(self.toolBox, 10, 0, 1, 6)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 3, 1, 1)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.gridLayout_3.addWidget(self.dateTimeEdit_3, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 3, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 3, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_3.addWidget(self.checkBox_5, 16, 2, 1, 1)
        self.toolBox_2 = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        self.toolBox_2.setObjectName("toolBox_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)#Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 674, 73))
        self.page_3.setObjectName("page_3")

        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        r = 0
        for i in range(0,nbSPVSLL): #NB SPV SLL défaut=4
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
        for i in range(0,nbSPVCas):#nb SPV caserne: déf=5
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
        self.gridLayout_3.addWidget(self.toolBox_2, 14, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 16, 1, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_3.addWidget(self.dateTimeEdit_2, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 17, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 2, 4, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_3.addWidget(self.checkBox_6, 16, 4, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 16, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 16, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 15, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 18, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 18, 3, 1, 1)
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

        #MODIFICATIONS
        self.spinBox.setMaximum(NCODISMAX)
        actual_date = datetime.datetime.now()
        self.dateTimeEdit.setDateTime(actual_date)
        self.dateTimeEdit_2.setDateTime(actual_date)
        self.dateTimeEdit_3.setDateTime(actual_date)



        #CONNEXIONS
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

        #self.checkBox.stateChanged.connect(lambda value = self.checkBox, name="remorque": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_2.stateChanged.connect(lambda value = self.checkBox_2, name="gendarmerie": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_3.stateChanged.connect(lambda value = self.checkBox_3, name="edf": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_4.stateChanged.connect(lambda value = self.checkBox_4, name="brigade_verte": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_5.stateChanged.connect(lambda value = self.checkBox_5, name="gdf": fonctions_self.on_checkbox_changed(self, value, name))
        self.checkBox_6.stateChanged.connect(lambda value = self.checkBox_6, name="service_eaux": fonctions_self.on_checkbox_changed(self, value, name))

        #dû à la boucle for, les spv sll et caserne sont connectés et générés directement lors de la création de combobox

        self.comboBox_typeInter.currentTextChanged.connect(lambda value = self.comboBox_typeInter, name="typeInter": fonctions_self.on_combobox_changed(self, value, name))

        self.pushButton.clicked.connect(lambda self_new_rapport = self : fonctions.rediger(self_new_rapport))
        self.pushButton_2.clicked.connect(lambda self_win_to_show = self : fonctions_self.close_window(self, ""))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xRapportInterSize, yRapportInterSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xRapportInterSize = size.width()
        yRapportInterSize = size.height()

    def retranslateUi(self, Ui_rapportInter):
        global path_to_rinter, path_to_vars, path_to_rfma, path_to_pglx
        _translate = QtCore.QCoreApplication.translate

        print(path_to_pglx + '/' + '.nbInter')
        os.chdir(path_to_pglx) #n° inter #{ATTENTION} a changer si path_to_pglx mène vers un répertoir sans les bonnes permissions ?
        if os.path.isfile('.nbInter'):
            print("AAAAAAAAAAAAAAAAAA")
            nbInter = linecache.getline('.nbInter', 1)
            if nbInter.isdigit():
                nbInter = int(nbInter)
            else:
                nbInter = 0
                fonctions.write_function(path_to_pglx, '.nbInter', 0)#{ATTENTION} a changer si path_to_pglx mène vers un répertoir sans les bonnes permissions ?
        else:
            nbInter = 0
            fonctions.write_function(path_to_pglx, '.nbInter', 0)#{ATTENTION} a changer si path_to_pglx mène vers un répertoir sans les bonnes permissions ?
        print("Numéro Intervention:", nbInter)

        Ui_rapportInter.setWindowTitle(_translate("MainWindow", "PGLX - Rapport d\'intervention N°" + str(nbInter)))
        self.label_typeInter.setText(_translate("MainWindow", "Type d\'intervention"))
        self.label_2.setText(_translate("MainWindow", "Heur de départ"))
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
        Ui_create_inter.resize(xCreateInterSize, yCreateInterSize)
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

            if fonctions.file_exists(path_to_vars, ".fonctionSp-" + str(i)):
                self.lineEdit_4.setText(linecache.getline(".fonctionSp-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".sp-" + str(i)):
                self.lineEdit_5.setText(linecache.getline(".sp-" + str(i), 1))

            self.lineEdit_4.textChanged.connect(lambda value = self.lineEdit_4 , name = "fonctionSp-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_5.textChanged.connect(lambda value = self.lineEdit_5 , name = "sp-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        for i in range(0, b2):
            self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
            self.lineEdit_6.setObjectName("lineEdit_6-" + str(i))
            self.gridLayout_4.addWidget(self.lineEdit_6, 1+i, 0, 1, 1)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
            self.lineEdit_7.setObjectName("lineEdit_7-" + str(i))
            self.gridLayout_4.addWidget(self.lineEdit_7, 1+i, 1, 1, 1)

            if fonctions.file_exists(path_to_vars, ".engin-" + str(i)):
                self.lineEdit_6.setText(linecache.getline(".engin-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".fonctionEngin-" + str(i)):
                self.lineEdit_7.setText(linecache.getline(".fonctionEngin-" + str(i), 1))

            self.lineEdit_6.textChanged.connect(lambda value = self.lineEdit_6 , name = "engin-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_7.textChanged.connect(lambda value = self.lineEdit_7 , name = "fonctionEngin-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        for i in range(0, b3):
            self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
            self.lineEdit_11.setObjectName("lineEdit_11-"+ str(i))
            self.gridLayout_7.addWidget(self.lineEdit_11, 1+i, 0, 1, 1)
            self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
            self.lineEdit_12.setObjectName("lineEdit_12-"+ str(i))
            self.gridLayout_7.addWidget(self.lineEdit_12, 1+i, 1, 1, 1)

            if fonctions.file_exists(path_to_vars, ".enginRenfort-" + str(i)):
                self.lineEdit_11.setText(linecache.getline(".enginRenfort-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".fonctionEnginRenfort-" + str(i)):
                self.lineEdit_12.setText(linecache.getline(".fonctionEnginRenfort-" + str(i), 1))

            self.lineEdit_11.textChanged.connect(lambda value = self.lineEdit_11 , name = "enginRenfort-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_12.textChanged.connect(lambda value = self.lineEdit_12 , name = "fonctionEnginRenfort-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        self.retranslateUi(Ui_create_inter)
        QtCore.QMetaObject.connectSlotsByName(Ui_create_inter)

        #MODIFICATIONS;
        self.dateTimeEdit.setDateTime(datetime.datetime.now())

        #rempli si possible le formulaire (pour la mise à jour)
        if fonctions.file_is_int(path_to_vars, ".nCodis", 1):
                self.spinBox.setValue(int(linecache.getline(".nCodis", 1)))
        if fonctions.file_exists(path_to_vars, ".centreInter"):
                self.lineEdit.setText(linecache.getline(".centreInter", 1))
        if fonctions.file_exists(path_to_vars, ".natureInter"):
                self.lineEdit_2.setText(linecache.getline(".natureInter", 1))
        if fonctions.file_exists(path_to_vars, ".observation"):
                self.lineEdit_3.setText(linecache.getline(".observation", 1))
        if fonctions.file_exists(path_to_vars, ".demandeurInter"):
                self.lineEdit_8.setText(linecache.getline(".demandeurInter", 1))
        if fonctions.file_exists(path_to_vars, ".telDemandeur"):
                self.lineEdit_9.setText(linecache.getline(".telDemandeur", 1))
        if fonctions.file_exists(path_to_vars, ".adresseDemandeur"):
                self.lineEdit_10.setText(linecache.getline(".adresseDemandeur", 1))

        #CONNEXIONS

        self.spinBox_2.valueChanged.connect(lambda value = self.spinBox_2 : fonctions_self.on_spinBox_2_changed(self, value))
        self.spinBox_3.valueChanged.connect(lambda value = self.spinBox_3 : fonctions_self.on_spinBox_3_changed(self, value))
        self.spinBox_4.valueChanged.connect(lambda value = self.spinBox_4 : fonctions_self.on_spinBox_4_changed(self, value))

        self.spinBox.setMaximum(NCODISMAX)
        self.spinBox.valueChanged.connect(lambda value = self.spinBox, name = "nCodis" : fonctions_self.on_spinBox_changed(self, value, name))

        self.lineEdit.textChanged.connect(lambda value = self.lineEdit , name = "centreInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_2.textChanged.connect(lambda value = self.lineEdit_2 , name = "natureInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_3.textChanged.connect(lambda value = self.lineEdit_3 , name = "observation": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_8.textChanged.connect(lambda value = self.lineEdit_8 , name = "demandeurInter": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_9.textChanged.connect(lambda value = self.lineEdit_9 , name = "telDemandeur": fonctions_self.on_lineEdit_changed(self, value, name))
        self.lineEdit_10.textChanged.connect(lambda value = self.lineEdit_10 , name = "adresseDemandeur": fonctions_self.on_lineEdit_changed(self, value, name))

        self.dateTimeEdit.dateTimeChanged.connect(lambda value = self.dateTimeEdit , name = "heure_appel": fonctions_self.on_dateTime_changed(self, value, name))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions.create_inter(selfi))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xCreateInterSize, yCreateInterSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xCreateInterSize = size.width()
        yCreateInterSize = size.height()

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
        create_own.resize(xCreateOwnSize, yCreateOwnSize)
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

        self.actionQuitter.triggered.connect(lambda selfi = self : fonctions_self.close_window(self, ""))
        self.actionEnregistrer.triggered.connect(lambda selfi = self : fonctions_self.save_to_file(self, ".ownInter"))
        self.actionOuvrir.triggered.connect(lambda selfi = self : fonctions_self.load_to_file(self))
        self.textEdit.textChanged.connect(lambda value = self.textEdit : fonctions_self.on_textEdit_changed(self, value, "ownInter"))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xCreateOwnSize, yCreateOwnSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xCreateOwnSize = size.width()
        yCreateOwnSize = size.height()

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
        global nbSPVSLL, nbSPVSLL
        Administration = self
        Administration.setObjectName("Administration")
        Administration.resize(xAdministrationSize, yAdministrationSize)
        self.centralwidget = QtWidgets.QWidget(Administration)
        self.centralwidget.setObjectName("centralwidget")

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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 555))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 7, 0, 2, 2)
        self.listWidget_BlackList = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_BlackList.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_BlackList.setObjectName("listWidget_BlackList")
        self.gridLayout_3.addWidget(self.listWidget_BlackList, 3, 9, 10, 1)
        spacerItem1 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 8, 3, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 4, 1, 3)
        self.nbSPVCas = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nbSPVCas.setObjectName("nbSPVCas")
        self.gridLayout_3.addWidget(self.nbSPVCas, 11, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 3, 1, 6)
        self.listWidget_WhiteUser = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_WhiteUser.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_WhiteUser.setObjectName("listWidget_WhiteUser")
        self.gridLayout_3.addWidget(self.listWidget_WhiteUser, 3, 5, 10, 3)
        spacerItem3 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 8, 2, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(302, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 7, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 5, 2, 1, 3)
        self.spinBox_nbSPVCas = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbSPVCas.setObjectName("spinBox_nbSPVCas")
        self.gridLayout_3.addWidget(self.spinBox_nbSPVCas, 11, 3, 1, 1)
        self.spinBox_nbSPVSLL = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbSPVSLL.setObjectName("spinBox_nbSPVSLL")
        self.gridLayout_3.addWidget(self.spinBox_nbSPVSLL, 10, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(141, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 10, 4, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 20, 8, 1, 2)
        self.pushButton_session = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_session.setObjectName("pushButton_session")
        self.gridLayout_3.addWidget(self.pushButton_session, 9, 0, 1, 2)
        self.label_nbFPTL = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbFPTL.setObjectName("label_nbFPTL")
        self.gridLayout_3.addWidget(self.label_nbFPTL, 15, 0, 1, 1)
        self.spinBox_nbFPTL = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbFPTL.setObjectName("spinBox_nbFPTL")
        self.gridLayout_3.addWidget(self.spinBox_nbFPTL, 15, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 2, 2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem7, 19, 9, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 11, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 6, 0, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(557, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 20, 0, 1, 8)
        spacerItem10 = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 0, 0, 1, 3)
        self.pushButton_ListAdd = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_ListAdd.setText("")
        icon = QtGui.QIcon.fromTheme("add")
        self.pushButton_ListAdd.setIcon(icon)
        self.pushButton_ListAdd.setObjectName("pushButton_ListAdd")
        self.gridLayout_3.addWidget(self.pushButton_ListAdd, 6, 8, 2, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 19, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(198, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 9, 2, 1, 3)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(565, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem13, 6, 2, 1, 3)
        self.label_nbSPVSLL = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbSPVSLL.setObjectName("label_nbSPVSLL")
        self.gridLayout_3.addWidget(self.label_nbSPVSLL, 10, 0, 1, 2)
        self.label_BlackList = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_BlackList.setObjectName("label_BlackList")
        self.gridLayout_3.addWidget(self.label_BlackList, 2, 9, 1, 1)
        self.spinBox_nbVL = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbVL.setObjectName("spinBox_nbVL")
        self.gridLayout_3.addWidget(self.spinBox_nbVL, 16, 1, 1, 1)
        self.pushButton_ListRemove = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_ListRemove.setText("")
        icon = QtGui.QIcon.fromTheme("remove")
        self.pushButton_ListRemove.setIcon(icon)
        self.pushButton_ListRemove.setObjectName("pushButton_ListRemove")
        self.gridLayout_3.addWidget(self.pushButton_ListRemove, 9, 8, 2, 1)
        self.label_nbVTU = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbVTU.setObjectName("label_nbVTU")
        self.gridLayout_3.addWidget(self.label_nbVTU, 17, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem14, 19, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_nbVL = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbVL.setObjectName("label_nbVL")
        self.gridLayout_3.addWidget(self.label_nbVL, 16, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem15, 12, 2, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 12, 0, 1, 2)
        self.spinBox_nbVTU = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbVTU.setObjectName("spinBox_nbVTU")
        self.gridLayout_3.addWidget(self.spinBox_nbVTU, 17, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 14, 0, 1, 10)
        self.label_nbEPSA = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbEPSA.setObjectName("label_nbEPSA")
        self.gridLayout_3.addWidget(self.label_nbEPSA, 15, 4, 1, 1)
        self.label_nbFPTSR = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbFPTSR.setObjectName("label_nbFPTSR")
        self.gridLayout_3.addWidget(self.label_nbFPTSR, 16, 4, 1, 1)
        self.label_nbVSAV = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nbVSAV.setObjectName("label_nbVSAV")
        self.gridLayout_3.addWidget(self.label_nbVSAV, 17, 4, 1, 1)
        self.spinBox_nbEPSA = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbEPSA.setObjectName("spinBox_nbEPSA")
        self.gridLayout_3.addWidget(self.spinBox_nbEPSA, 15, 5, 1, 1)
        self.spinBox_nbFPTSR = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbFPTSR.setObjectName("spinBox_nbFPTSR")
        self.gridLayout_3.addWidget(self.spinBox_nbFPTSR, 16, 5, 1, 1)
        self.spinBox_nbVSAV = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_nbVSAV.setObjectName("spinBox_nbVSAV")
        self.gridLayout_3.addWidget(self.spinBox_nbVSAV, 17, 5, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Administration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Administration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 22))
        self.menubar.setObjectName("menubar")
        Administration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Administration)
        self.statusbar.setObjectName("statusbar")
        Administration.setStatusBar(self.statusbar)

        self.retranslateUi(Administration)
        QtCore.QMetaObject.connectSlotsByName(Administration)

        #MODIFICATIONS
        self.spinBox_nbSPVCas.setValue(nbSPVCas)
        self.spinBox_nbSPVSLL.setValue(nbSPVSLL)
        self.spinBox_nbFPTL.setValue(NFPTL)
        self.spinBox_nbVL.setValue(NVL)
        self.spinBox_nbEPSA.setValue(NEPSA)
        self.spinBox_nbFPTSR.setValue(NFPTSR)
        self.spinBox_nbVSAV.setValue(NVSAV)
        self.spinBox_nbVTU.setValue(NVTU)

        blackListedUser = fonctions.get_line_alpha(path_to_session, "blackList", 1, "")
        blackListedUser = blackListedUser.split()
        for i in blackListedUser:
            self.listWidget_BlackList.addItem(i)
        whiteListedUser = fonctions.get_line_alpha(path_to_session, "whiteList", 1, "")
        whiteListedUser = whiteListedUser.split()
        for i in whiteListedUser:
            self.listWidget_WhiteUser.addItem(i)
        #CONNEXION

        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))#fichiers supprimés ?
        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.on_administration_ok(selfi))

        self.listWidget_WhiteUser.setCurrentRow(0)
        self.listWidget_WhiteUser.currentRowChanged.connect(lambda selfi = self, user = self.listWidget_WhiteUser.currentRow() : fonctions.on_userList_changed(0, user, selfi))

        self.pushButton.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToRInter"))
        self.pushButton_2.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToRFma"))
        self.pushButton_3.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToVars"))
        self.pushButton_session.clicked.connect(lambda selfi = self : fonctions_self.open_dir(selfi, ".newPathToSession"))
        self.lineEdit.textChanged.connect(lambda value = self.lineEdit, name = "newCentreInter": fonctions.on_lineEdit_changed(path_to_session, value, name))
        self.pushButton_ListAdd.clicked.connect(lambda selfi = self : fonctions_self.DialogAddUser(self))
        #En attente: self.pushButton_ListRemove.clicked.connect(lambda selfi = self, whitelist = self.listWidget_WhiteUser.currentItem(), blacklist = self.listWidget_BlackList.currentItem() : fonctions_self.on_removeListItem_clicked(selfi, whitelist, blacklist))
        self.pushButton_ListRemove.clicked.connect(lambda selfi = self : fonctions_self.DialogRemoveUser(self))

        self.spinBox_nbSPVCas.valueChanged.connect(lambda value=self.spinBox_nbSPVCas, name = "nbSPVCas": fonctions.on_nbSpinbox_changed(nbSPVCas, value, name))
        self.spinBox_nbSPVSLL.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "nbSPVSLL": fonctions.on_nbSpinbox_changed(nbSPVSLL, value, name))
        self.spinBox_nbFPTL.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NFPTL": fonctions.on_nbSpinbox_changed(NFPTL, value, name))
        self.spinBox_nbVL.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NVL": fonctions.on_nbSpinbox_changed(NVL, value, name))
        self.spinBox_nbEPSA.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NEPSA": fonctions.on_nbSpinbox_changed(NEPSA, value, name))
        self.spinBox_nbFPTSR.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NFPTSR": fonctions.on_nbSpinbox_changed(NFPTSR, value, name))
        self.spinBox_nbVSAV.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NVSAV": fonctions.on_nbSpinbox_changed(NVSAV, value, name))
        self.spinBox_nbVTU.valueChanged.connect(lambda value=self.spinBox_nbSPVSLL, name = "NVTU": fonctions.on_nbSpinbox_changed(NVTU, value, name))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xAdministrationSize, yAdministrationSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xAdministrationSize = size.width()
        yAdministrationSize = size.height()

    def retranslateUi(self, Administration):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Administration", "Administration de PGLX"))
        self.label_2.setText(_translate("Administration", "Nom du CIS"))
        self.label_BlackList.setText(_translate("Administration", "Liste Noire"))
        self.pushButton.setText(_translate("Administration", "Chemin des interventions"))
        self.pushButton_2.setText(_translate("Administration", "Chemin des FMA ..."))
        self.pushButton_3.setText(_translate("Administration", "Chemin des variables"))
        self.pushButton_session.setText(_translate("Administration", "Chemin session"))
        self.label_nbSPVSLL.setText(_translate("Administration", "Nombre de Pompier(s) SLL"))
        self.nbSPVCas.setText(_translate("Administration", "Nombre de Pompiers(s) Caserne"))
        self.label_nbSPVSLL.setText(_translate("Administration", "Nombre de Pompier(s) SLL"))
        self.label_BlackList.setText(_translate("Administration", "Liste Noire"))
        self.label_nbFPTL.setText(_translate("Administration", "Nombre de FPTL"))
        self.label_nbVTU.setText(_translate("Administration", "Nombre de VTU"))
        self.label_nbVL.setText(_translate("Administration", "Nombre de VL"))
        self.label_2.setText(_translate("Administration", "Nom du CIS"))
        self.pushButton_4.setText(_translate("Administration", "Changer le mot de passe"))
        self.label_nbEPSA.setText(_translate("Administration", "Nombre d\'EPSA"))
        self.label_nbFPTSR.setText(_translate("Administration", "Nombre de FPTSR"))
        self.label_nbVSAV.setText(_translate("Administration", "Nombre de VSAV"))

class Ui_Casernement(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_Casernement, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        global b_casernement
        Casernement = self
        Casernement.setObjectName("Casernement")
        Casernement.resize(xCasernementSize, yCasernementSize)
        self.centralwidget = QtWidgets.QWidget(Casernement)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_central = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_central.setObjectName("gridLayout_central")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_frame = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_frame.setObjectName("gridLayout_frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 793, 573))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_scroll = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_scroll.setObjectName("gridLayout_scroll")
        spacerItem = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_scroll.addItem(spacerItem, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_scroll.addWidget(self.label, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_scroll.addItem(spacerItem1, 0, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_scroll.addWidget(self.label_2, 1, 0, 1, 1)
        self.datetime_debut = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.datetime_debut.setObjectName("datetime_debut")
        self.gridLayout_scroll.addWidget(self.datetime_debut, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_scroll.addWidget(self.label_3, 2, 0, 1, 1)
        self.datetime_fin = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents)
        self.datetime_fin.setObjectName("datetime_fin")
        self.gridLayout_scroll.addWidget(self.datetime_fin, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_scroll.addWidget(self.line, 3, 0, 1, 5)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_scroll.addWidget(self.label_4, 4, 0, 1, 1)
        self.lieux_txt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lieux_txt.setObjectName("lieux_txt")
        self.gridLayout_scroll.addWidget(self.lieux_txt, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_scroll.addWidget(self.label_5, 5, 0, 1, 1)
        self.responsable_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.responsable_1.setObjectName("responsable_1")
        self.gridLayout_scroll.addWidget(self.responsable_1, 5, 1, 1, 2)
        self.responsable_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.responsable_2.setObjectName("responsable_2")
        self.gridLayout_scroll.addWidget(self.responsable_2, 5, 3, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_scroll.addWidget(self.line_2, 6, 0, 1, 5)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_groupBox = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_groupBox.setObjectName("gridLayout_groupBox")

        self.spinBox_nb_perso = QtWidgets.QSpinBox(self.groupBox)#SpinBox pour le nombre de personnel et d'activité
        self.spinBox_nb_perso.setObjectName("spinBox_nb_perso")
        self.gridLayout_groupBox.addWidget(self.spinBox_nb_perso, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_groupBox.addWidget(self.label_6, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_groupBox.addItem(spacerItem2, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_groupBox.addWidget(self.label_7, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_groupBox.addItem(spacerItem3, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_groupBox.addWidget(self.label_8, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_groupBox.addItem(spacerItem4, 0, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_groupBox.addWidget(self.label_9, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_groupBox.addItem(spacerItem5, 0, 7, 1, 1)

        for i in range(0, b_casernement):
            self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_4.setObjectName("lineEdit_4-" + str(i))
            self.gridLayout_groupBox.addWidget(self.lineEdit_4, 1+i, 0, 1, 2)
            self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_5.setObjectName("lineEdit_5-" + str(i))
            self.gridLayout_groupBox.addWidget(self.lineEdit_5, 1+i, 2, 1, 2)

            if fonctions.file_exists(path_to_vars, ".activite-" + str(i)):
                self.lineEdit_4.setText(linecache.getline(path_to_vars + '/'  + ".activite-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".personnel-" + str(i)):
                self.lineEdit_5.setText(linecache.getline(path_to_vars + '/'  + ".personnel-" + str(i), 1))

            self.lineEdit_4.textChanged.connect(lambda value = self.lineEdit_4 , name = "activite-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_5.textChanged.connect(lambda value = self.lineEdit_5 , name = "personnel-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

            self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_6.setObjectName("lineEdit_6-" + str(i))
            self.gridLayout_groupBox.addWidget(self.lineEdit_6, 1+i, 4, 1, 2)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
            self.lineEdit_7.setObjectName("lineEdit_7-" + str(i))
            self.gridLayout_groupBox.addWidget(self.lineEdit_7, 1+i, 6, 1, 2)

            if fonctions.file_exists(path_to_vars, ".activite_2-" + str(i)):
                self.lineEdit_6.setText(linecache.getline(path_to_vars + '/'  + ".activite_2-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".personnel_2-" + str(i)):
                self.lineEdit_7.setText(linecache.getline(path_to_vars + '/'  + ".personnel_2-" + str(i), 1))

            self.lineEdit_6.textChanged.connect(lambda value = self.lineEdit_6 , name = "activite_2-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_7.textChanged.connect(lambda value = self.lineEdit_7 , name = "personnel_2-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        self.gridLayout_scroll.addWidget(self.groupBox, 7, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_scroll.addWidget(self.line_3, 8, 0, 1, 5)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout_scroll.addWidget(self.label_10, 9, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_scroll.addWidget(self.textEdit, 10, 0, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(590, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_scroll.addItem(spacerItem6, 11, 0, 1, 4)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_scroll.addWidget(self.buttonBox, 11, 4, 1, 1)
        self.equipe_txt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.equipe_txt.setObjectName("equipe_txt")
        self.gridLayout_scroll.addWidget(self.equipe_txt, 4, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_frame.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_central.addWidget(self.frame, 0, 0, 1, 1)
        Casernement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Casernement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 27))
        self.menubar.setObjectName("menubar")
        Casernement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Casernement)
        self.statusbar.setObjectName("statusbar")
        Casernement.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Casernement)
        self.toolBar.setObjectName("toolBar")
        Casernement.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(Casernement)
        QtCore.QMetaObject.connectSlotsByName(Casernement)

        #MODIFICATIONS
        self.spinBox_nb_perso.setValue(b_casernement)
        actualDate = datetime.datetime.now()
        self.datetime_debut.setDateTime(actualDate)
        self.datetime_fin.setDateTime(actualDate)

        if fonctions.file_exists(path_to_vars, ".lieu"):
                self.lieux_txt.setText(linecache.getline(path_to_vars + '/'  + ".lieu", 1))
        if fonctions.file_exists(path_to_vars, ".equipe"):
                self.equipe_txt.setText(linecache.getline(path_to_vars + '/'  + ".equipe", 1))
        if fonctions.file_exists(path_to_vars, ".responsable_1"):
                self.responsable_1.setText(linecache.getline(path_to_vars + '/'  + ".responsable_1", 1))
        if fonctions.file_exists(path_to_vars, ".responsable_2"):
                self.responsable_2.setText(linecache.getline(path_to_vars + '/'  + ".responsable_2", 1))

        #CONNEXIONS
        self.spinBox_nb_perso.valueChanged.connect(lambda value = self.spinBox_nb_perso : fonctions_self.on_spinBox_nb_peronnel_changed(self, value))

        self.datetime_fin.dateTimeChanged.connect(lambda value = self.datetime_fin, name = "dateFin": fonctions_self.on_dateTime_changed(self, value, name))
        self.datetime_debut.dateTimeChanged.connect(lambda value = self.datetime_debut, name = "dateDebut": fonctions_self.on_dateTime_changed(self, value, name))

        self.lieux_txt.textChanged.connect(lambda value = self.lieux_txt, name = "lieu": fonctions_self.on_lineEdit_changed(self, value, name))
        self.equipe_txt.textChanged.connect(lambda value = self.equipe_txt, name = "equipe": fonctions_self.on_lineEdit_changed(self, value, name))
        self.responsable_1.textChanged.connect(lambda value = self.responsable_1, name = "responsable_1": fonctions_self.on_lineEdit_changed(self, value, name))
        self.responsable_2.textChanged.connect(lambda value = self.responsable_2, name = "responsable_2": fonctions_self.on_lineEdit_changed(self, value, name))

        self.textEdit.textChanged.connect(lambda value = self.textEdit, name = "rapport_casernement": fonctions_self.on_textEdit_changed(self, value, name))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions.casernement(selfi))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xCasernementSize, yCasernementSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xCasernementSize = size.width()
        yCasernementSize = size.height()

    def retranslateUi(self, Casernement):
        _translate = QtCore.QCoreApplication.translate
        Casernement.setWindowTitle(_translate("Casernement", "PGLX - Feuille de Casernement"))
        self.label.setText(_translate("Casernement", "Feuille de Casernement"))
        self.label_2.setText(_translate("Casernement", "Heure de début"))
        self.label_3.setText(_translate("Casernement", "Heure de fin"))
        self.label_4.setText(_translate("Casernement", "Lieu et équipe"))
        self.lieux_txt.setText(_translate("Casernement", "Lieu du casernement"))
        self.label_5.setText(_translate("Casernement", "Responsables"))
        self.groupBox.setTitle(_translate("Casernement", "Personnel"))
        self.label_6.setText(_translate("Casernement", "Activité"))
        self.label_7.setText(_translate("Casernement", "Personnel"))
        self.label_8.setText(_translate("Casernement", "Activité"))
        self.label_9.setText(_translate("Casernement", "Personnel"))
        self.label_10.setText(_translate("Casernement", "Rapport"))
        self.equipe_txt.setText(_translate("Casernement", "équipe"))
        self.toolBar.setWindowTitle(_translate("Casernement", "toolBar"))

class Ui_FMA(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_FMA, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        global xFmaSize, yFmaSize
        FMA = self
        FMA.setObjectName("FMA")
        FMA.resize(xFmaSize, yFmaSize)
        print('x', xFmaSize)
        self.centralwidgetA = QtWidgets.QWidget(FMA)
        self.centralwidgetA.setObjectName("centralwidgetA")
        self.gridLayout_princiaple = QtWidgets.QGridLayout(self.centralwidgetA)
        self.gridLayout_princiaple.setObjectName("gridLayout_princiaple")
        self.frameA = QtWidgets.QFrame(self.centralwidgetA)
        self.frameA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameA.setObjectName("frameA")
        self.gridLayout_frame = QtWidgets.QGridLayout(self.frameA)
        self.gridLayout_frame.setObjectName("gridLayout_frame")
        self.scrollAreaA = QtWidgets.QScrollArea(self.frameA)
        self.scrollAreaA.setWidgetResizable(True)
        self.scrollAreaA.setObjectName("scrollAreaA")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 816, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_scroll = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_scroll.setObjectName("gridLayout_scroll")
        self.groupBox_info = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_info.setObjectName("groupBox_info")
        self.gridLayout_groupBox = QtWidgets.QGridLayout(self.groupBox_info)
        self.gridLayout_groupBox.setObjectName("gridLayout_groupBox")
        self.label = QtWidgets.QLabel(self.groupBox_info)
        self.label.setObjectName("label")
        self.gridLayout_groupBox.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_info)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_groupBox.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.groupBox_info)
        self.label_2.setObjectName("label_2")
        self.gridLayout_groupBox.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.groupBox_info)
        self.label_4.setObjectName("label_4")
        self.gridLayout_groupBox.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_info)
        self.label_3.setObjectName("label_3")
        self.gridLayout_groupBox.addWidget(self.label_3, 2, 0, 1, 1)

        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.groupBox_info)
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.gridLayout_groupBox.addWidget(self.dateTimeEdit_start, 1, 1, 1, 1)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.groupBox_info)
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.gridLayout_groupBox.addWidget(self.dateTimeEdit_end, 2, 1, 1, 1)

        self.gridLayout_scroll.addWidget(self.groupBox_info, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_scroll.addWidget(self.line, 1, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.Formateurs = QtWidgets.QWidget()
        self.Formateurs.setObjectName("Formateurs")
        self.gridLayout_tab_formateur = QtWidgets.QGridLayout(self.Formateurs)
        self.gridLayout_tab_formateur.setObjectName("gridLayout_tab_formateur")
        self.label_8 = QtWidgets.QLabel(self.Formateurs)
        self.label_8.setObjectName("label_8")
        self.gridLayout_tab_formateur.addWidget(self.label_8, 0, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.Formateurs)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_tab_formateur.addWidget(self.spinBox, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_tab_formateur.addItem(spacerItem, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Formateurs)
        self.label_5.setObjectName("label_5")
        self.gridLayout_tab_formateur.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_formateur.addItem(spacerItem1, 1, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.Formateurs)
        self.label_6.setObjectName("label_6")
        self.gridLayout_tab_formateur.addWidget(self.label_6, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_formateur.addItem(spacerItem2, 1, 4, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.Formateurs)
        self.label_7.setObjectName("label_7")
        self.gridLayout_tab_formateur.addWidget(self.label_7, 1, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(147, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_formateur.addItem(spacerItem3, 1, 7, 1, 1)

        for i in range(0, b_fma_formateur):
            self.lineEdit_2 = QtWidgets.QLineEdit(self.Formateurs)
            self.lineEdit_2.setObjectName("lineEdit_2-" + str(i))
            self.gridLayout_tab_formateur.addWidget(self.lineEdit_2, 2+i, 0, 1, 3)
            self.lineEdit_3 = QtWidgets.QLineEdit(self.Formateurs)
            self.lineEdit_3.setObjectName("lineEdit_3-" + str(i))
            self.gridLayout_tab_formateur.addWidget(self.lineEdit_3, 2+i, 3, 1, 2)
            self.lineEdit_4 = QtWidgets.QLineEdit(self.Formateurs)
            self.lineEdit_4.setObjectName("lineEdit_4-" + str(i))
            self.gridLayout_tab_formateur.addWidget(self.lineEdit_4, 2+i, 5, 1, 3)

            if fonctions.file_exists(path_to_vars, ".formateurNom-" + str(i)):
                self.lineEdit_2.setText(linecache.getline(path_to_vars + '/'  + ".formateurNom-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".formateurFormation-" + str(i)):
                self.lineEdit_3.setText(linecache.getline(path_to_vars + '/'  + ".formateurFormation-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".formateurCentre-" + str(i)):
                self.lineEdit_4.setText(linecache.getline(path_to_vars + '/'  + ".formateurCentre-" + str(i), 1))


            self.lineEdit_2.textChanged.connect(lambda value = self.lineEdit_2 , name = "formateurNom-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_3.textChanged.connect(lambda value = self.lineEdit_3 , name = "formateurFormation-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_4.textChanged.connect(lambda value = self.lineEdit_4 , name = "formateurCentre-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))


        self.tabWidget.addTab(self.Formateurs, "")
        self.tab_spv = QtWidgets.QWidget()
        self.tab_spv.setObjectName("tab_spv")
        self.gridLayout_tab_spv = QtWidgets.QGridLayout(self.tab_spv)
        self.gridLayout_tab_spv.setObjectName("gridLayout_tab_spv")
        self.label_9 = QtWidgets.QLabel(self.tab_spv)
        self.label_9.setObjectName("label_9")
        self.gridLayout_tab_spv.addWidget(self.label_9, 0, 0, 1, 2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_spv)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_tab_spv.addWidget(self.spinBox_2, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_tab_spv.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_spv)
        self.label_10.setObjectName("label_10")
        self.gridLayout_tab_spv.addWidget(self.label_10, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(248, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_spv.addItem(spacerItem5, 1, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.tab_spv)
        self.label_11.setObjectName("label_11")
        self.gridLayout_tab_spv.addWidget(self.label_11, 1, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_spv.addItem(spacerItem6, 1, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_spv)
        self.label_12.setObjectName("label_12")
        self.gridLayout_tab_spv.addWidget(self.label_12, 1, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_spv.addItem(spacerItem7, 1, 6, 1, 1)

        for i in range(0, b_fma_spv):
            self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_spv)
            self.lineEdit_5.setObjectName("lineEdit_5-" + str(i))
            self.gridLayout_tab_spv.addWidget(self.lineEdit_5, 2+i, 0, 1, 3)
            self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_spv)
            self.lineEdit_6.setObjectName("lineEdit_6-" + str(i))
            self.gridLayout_tab_spv.addWidget(self.lineEdit_6, 2+i, 3, 1, 2)
            self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_spv)
            self.lineEdit_7.setObjectName("lineEdit_7-" + str(i))
            self.gridLayout_tab_spv.addWidget(self.lineEdit_7, 2+i, 5, 1, 2)

            if fonctions.file_exists(path_to_vars, ".spvNom-" + str(i)):
                self.lineEdit_5.setText(linecache.getline(path_to_vars + '/'  + ".spvNom-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".spvFormation-" + str(i)):
                self.lineEdit_6.setText(linecache.getline(path_to_vars + '/'  + ".spvFormation-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".spvCentre-" + str(i)):
                self.lineEdit_7.setText(linecache.getline(path_to_vars + '/'  + ".spvCentre-" + str(i), 1))

            self.lineEdit_5.textChanged.connect(lambda value = self.lineEdit_5 , name = "spvNom-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_6.textChanged.connect(lambda value = self.lineEdit_6 , name = "spvFormation-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_7.textChanged.connect(lambda value = self.lineEdit_7 , name = "spvCentre-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))


        self.tabWidget.addTab(self.tab_spv, "")
        self.tab_materiel = QtWidgets.QWidget()
        self.tab_materiel.setObjectName("tab_materiel")
        self.gridLayout_tab_materiel = QtWidgets.QGridLayout(self.tab_materiel)
        self.gridLayout_tab_materiel.setObjectName("gridLayout_tab_materiel")
        self.label_13 = QtWidgets.QLabel(self.tab_materiel)
        self.label_13.setObjectName("label_13")
        self.gridLayout_tab_materiel.addWidget(self.label_13, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_materiel)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_tab_materiel.addWidget(self.spinBox_3, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_tab_materiel.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(137, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_materiel.addItem(spacerItem9, 1, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.tab_materiel)
        self.label_14.setObjectName("label_14")
        self.gridLayout_tab_materiel.addWidget(self.label_14, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(567, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_materiel.addItem(spacerItem10, 1, 3, 1, 2)

        for i in range(0, b_fma_vehicules):
            self.comboBox = QtWidgets.QComboBox(self.tab_materiel)
            self.comboBox.setObjectName("comboBox-" + str(i))
            self.gridLayout_tab_materiel.addWidget(self.comboBox, 2+i, 0, 1, 2)
            fonctions_self.addItem_comboBox(self, self.comboBox, 'l_vehicle_fma')#ajoute les items

            self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_materiel)
            self.lineEdit_8.setObjectName("lineEdit_8-" + str(i))
            self.gridLayout_tab_materiel.addWidget(self.lineEdit_8, 2+i, 2, 1, 2)
            self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_materiel)
            self.lineEdit_9.setObjectName("lineEdit_9-" + str(i))
            self.gridLayout_tab_materiel.addWidget(self.lineEdit_9, 2+i, 4, 1, 1)

            if fonctions.file_exists(path_to_vars, ".vehiculeCentre-" + str(i)):
                self.lineEdit_8.setText(linecache.getline(path_to_vars + '/'  + ".vehiculeCentre-" + str(i), 1))
            if fonctions.file_exists(path_to_vars, ".vehiculeAutre-" + str(i)):
                self.lineEdit_9.setText(linecache.getline(path_to_vars + '/'  + ".vehiculeAutre-" + str(i), 1))

            if fonctions.file_is_int(path_to_vars, ".vehiculeID-" + str(i), 1):
                chemin = path_to_vars + '/'  + ".vehiculeID-" + str(i)
                self.comboBox.setCurrentIndex(int(linecache.getline(chemin, 1)))

            self.comboBox.currentTextChanged.connect(lambda value = self.comboBox, name="vehicule-" + str(i): fonctions_self.on_combobox_changed(self, value, name))
            self.comboBox.currentIndexChanged.connect(lambda value = self.comboBox.currentIndex(), name="vehiculeID-" + str(i): fonctions_self.on_combobox_changed(self, str(value), name))#enregistre l'index pour avoir l'index lors du rafraîchissement de la page
            self.lineEdit_8.textChanged.connect(lambda value = self.lineEdit_8 , name = "vehiculeCentre-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))
            self.lineEdit_9.textChanged.connect(lambda value = self.lineEdit_9 , name = "vehiculeAutre-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))


        self.tabWidget.addTab(self.tab_materiel, "")
        self.tab_autres = QtWidgets.QWidget()
        self.tab_autres.setObjectName("tab_autres")
        self.gridLayout_tab_autre = QtWidgets.QGridLayout(self.tab_autres)
        self.gridLayout_tab_autre.setObjectName("gridLayout_tab_autre")
        self.label_15 = QtWidgets.QLabel(self.tab_autres)
        self.label_15.setObjectName("label_15")
        self.gridLayout_tab_autre.addWidget(self.label_15, 0, 0, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.tab_autres)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_tab_autre.addWidget(self.spinBox_4, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(629, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_tab_autre.addItem(spacerItem11, 0, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 64, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_tab_autre.addItem(spacerItem12, 0, 3, 1, 1)

        for i in range(0, b_fma_lieux):

            self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_autres)
            self.lineEdit_10.setObjectName("lineEdit_10-" + str(i))
            self.gridLayout_tab_autre.addWidget(self.lineEdit_10, 1+i, 0, 1, 5)

            if fonctions.file_exists(path_to_vars, ".lieu-" + str(i)):
                self.lineEdit_10.setText(linecache.getline(path_to_vars + '/'  + ".lieu-" + str(i), 1))

            self.lineEdit_10.textChanged.connect(lambda value = self.lineEdit_10 , name = "lieu-" + str(i): fonctions_self.on_lineEdit_changed(self, value, name))

        self.tabWidget.addTab(self.tab_autres, "")
        self.tab_rapport = QtWidgets.QWidget()
        self.tab_rapport.setObjectName("tab_rapport")
        self.gridLayout_tab_rapport = QtWidgets.QGridLayout(self.tab_rapport)
        self.gridLayout_tab_rapport.setObjectName("gridLayout_tab_rapport")
        self.textEdit = QtWidgets.QTextEdit(self.tab_rapport)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_tab_rapport.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_rapport, "")
        self.gridLayout_scroll.addWidget(self.tabWidget, 2, 0, 1, 2)
        spacerItem13 = QtWidgets.QSpacerItem(559, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_scroll.addItem(spacerItem13, 3, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_scroll.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.scrollAreaA.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_frame.addWidget(self.scrollAreaA, 0, 0, 1, 1)
        self.gridLayout_princiaple.addWidget(self.frameA, 0, 0, 1, 1)
        FMA.setCentralWidget(self.centralwidgetA)
        self.menubar = QtWidgets.QMenuBar(FMA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 856, 27))
        self.menubar.setObjectName("menubar")
        FMA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FMA)
        self.statusbar.setObjectName("statusbar")
        FMA.setStatusBar(self.statusbar)

        self.retranslateUi(FMA)
        #self.tabWidget.setCurrentIndex(1) redéfini plus tard
        QtCore.QMetaObject.connectSlotsByName(FMA)

        #MODIFICATIONS
        self.dateTimeEdit_start.dateTimeChanged.connect(lambda value = self.dateTimeEdit_start , name = "dateDebut": fonctions_self.on_dateTime_changed(self, value, name))
        self.dateTimeEdit_start.dateTimeChanged.connect(lambda value = self.dateTimeEdit_start.dateTime , name = "QDateDebut": fonctions_self.on_dateTime_changed(self, value, name))# réutiliser lors de l'actualisation de la page
        self.dateTimeEdit_start.setDateTime(datetime.datetime.now())

        self.dateTimeEdit_end.dateTimeChanged.connect(lambda value = self.dateTimeEdit_end , name = "dateFin": fonctions_self.on_dateTime_changed(self, value, name))
        self.dateTimeEdit_end.setDateTime(datetime.datetime.now())

        self.dateTimeEdit_start.dateTimeFromText("17/03/2014 10:36")

        self.spinBox.setValue(b_fma_formateur)
        self.spinBox_2.setValue(b_fma_spv)
        self.spinBox_3.setValue(b_fma_vehicules)
        self.spinBox_4.setValue(b_fma_lieux)

        if os.path.isfile(path_to_vars + '/.rapport_fma'): #remet les valeurs du ficher rapport dans textEdit
            nb_ligne = fonctions.nombre_de_ligne(".rapport_fma")
            var = ""
            for i in range(0, nb_ligne+1):
                var += linecache.getline(".rapport_fma", i)
            self.textEdit.setText(var)

        if os.path.isfile(path_to_vars + '/.theme_fma'):
            var = linecache.getline(path_to_vars + '/.theme_fma', 1)
            self.lineEdit.setText(var)

        if fonctions.file_is_int(path_to_vars, '.tabID', 1):
            file = path_to_vars + '/.tabID'
            index = int(linecache.getline(file, 1))
            if (index >= 0 or index <= 4):
                self.tabWidget.setCurrentIndex(index)
                print("Index", index)
            else:
                print("Index hors rang")
        else:
            print("Index par défaut")

        #if os.path.isfile(path_to_vars + '/.QDateDebut'):
        #    var = linecache.getline(path_to_vars + '/.QDateDebut', 1)
        #    self.dateTimeEdit_start.setDateTime(var)

        if os.path.isfile(path_to_vars + '/.theme_fma'):
            var = linecache.getline(path_to_vars + '/.theme_fma', 1)
            self.lineEdit.setText(var)

        #CONNEXION

        self.tabWidget.currentChanged['int'].connect(fonctions_self.save_tab)#lorsque la page est changée

        self.lineEdit.textChanged.connect(lambda value = self.lineEdit, name = "theme_fma": fonctions_self.on_lineEdit_changed(self, value, name))

        self.textEdit.textChanged.connect(lambda value = self.textEdit, name = "rapport_fma": fonctions_self.on_textEdit_changed(self, value, name))

        self.spinBox.valueChanged.connect(lambda value=self.spinBox : fonctions_self.on_spinBox_fma_formateurs_changed(self, value))
        self.spinBox_2.valueChanged.connect(lambda value=self.spinBox_2 : fonctions_self.on_spinBox_fma_spv_changed(self, value))
        self.spinBox_3.valueChanged.connect(lambda value=self.spinBox_3 : fonctions_self.on_spinBox_fma_vehicules_changed(self, value))
        self.spinBox_4.valueChanged.connect(lambda value=self.spinBox_4 : fonctions_self.on_spinBox_fma_lieux_changed(self, value))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions.fma(selfi))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, path_to_vars, '.date', '.dateDebut', '.dateFin', '.theme_fma'))
        self.buttonBox.rejected.connect(fonctions.fma_delete_files)#supprime les fichiers

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xFmaSize, yFmaSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xFmaSize = size.width()
        yFmaSize = size.height()

    def retranslateUi(self, FMA):
        _translate = QtCore.QCoreApplication.translate
        FMA.setWindowTitle(_translate("FMA", "PGLX - FMA"))
        self.groupBox_info.setTitle(_translate("FMA", "FMA"))
        self.label.setText(_translate("FMA", "Formation"))
        self.label_2.setText(_translate("FMA", "Date de début"))
        #self.label_4.setText(_translate("FMA", "Date"))#N'est plus utuilisé
        self.label_3.setText(_translate("FMA", "Date de fin"))
        self.label_8.setText(_translate("FMA", "Nombre"))
        self.label_5.setText(_translate("FMA", "Nom"))
        self.label_6.setText(_translate("FMA", "Formation"))
        self.label_7.setText(_translate("FMA", "Centre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Formateurs), _translate("FMA", "Formateurs"))
        self.label_9.setText(_translate("FMA", "Nombre"))
        self.label_10.setText(_translate("FMA", "Nom"))
        self.label_11.setText(_translate("FMA", "Formation"))
        self.label_12.setText(_translate("FMA", "Centre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spv), _translate("FMA", "SPV"))
        self.label_13.setText(_translate("FMA", "Nombre"))
        self.label_14.setText(_translate("FMA", "Centre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_materiel), _translate("FMA", "Véhicule & Matériel"))
        self.label_15.setText(_translate("FMA", "Lieu(x)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_autres), _translate("FMA", "Autres"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rapport), _translate("FMA", "Rapport"))

class Ui_ListInters(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_ListInters, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        ListInters = self
        ListInters.setObjectName("ListInters")
        ListInters.resize(xListIntersSize, yListIntersSize)
        self.centralwidget = QtWidgets.QWidget(ListInters)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 4, 3, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        self.treeWidget.headerItem().setFont(1, font)
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 4)
        self.pushButton_delete = QtWidgets.QPushButton(self.frame)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_2.addWidget(self.pushButton_delete, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ListInters.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListInters)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 22))
        self.menubar.setObjectName("menubar")
        ListInters.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListInters)
        self.statusbar.setObjectName("statusbar")
        ListInters.setStatusBar(self.statusbar)



        #MODIFICATIONS
        fichier = path_to_rinter + '/.dataInters.pglxdi'
        nbInters = fonctions.nombre_de_ligne(fichier)
        print('Nombre Inters', nbInters)

        fichier = '.dataInters.pglxdi'
        if fonctions.file_exists(path_to_rinter, fichier):
            os.chdir(path_to_rinter)
            entete = linecache.getline(fichier, 3).rstrip('\n').split(";;")
            print("Entete du fichier", entete)

            nbInteridx = entete.index("nbInter")
            nameidx = entete.index("name")
            dateidx = entete.index("date")
            callTimeidx = entete.index("callTime")
            departureTimeidx = entete.index("departureTime")
            endTimeidx = entete.index("endTime")
            useridx = entete.index("user")
            aloneidx = entete.index("alone")
            nature = entete.index("nature")
            vehicle = entete.index("vehicles")
            try:
                typeInter = entete.index("typeInter")
            except:
                pass

            for ligne in range(4, nbInters+1):#le fichier commence avec deux lignes de description + une ligne d'entête
                donnees = linecache.getline(fichier, ligne).rstrip('\n').split(";;")
                if DEBUG >= 1:
                    print("donnees", donnees)
                if donnees[0] != "":
                    item_i = QtWidgets.QTreeWidgetItem()
                    item_i.setText(0, donnees[nbInteridx])#N° inter
                    item_i.setText(1, donnees[dateidx])#date
                    try:
                        item_i.setText(2, donnees[typeInter])#Nature
                    except:
                        item_i.setText(2, '-')#Nature
                    item_i.setText(3, donnees[departureTimeidx])#heure départ
                    item_i.setText(4, donnees[endTimeidx])#heure retour
                    item_i.setText(5, donnees[vehicle])#Moyens
                    item_i.setText(6, donnees[useridx])#rédacteur
                    item_i.setText(7, donnees[aloneidx])#seul ou non ?
                    item_i.setText(8, donnees[nature])#Nature
                    self.treeWidget.addTopLevelItem(item_i)

        self.retranslateUi(ListInters)
        QtCore.QMetaObject.connectSlotsByName(ListInters)


        #CONNEXIONS
        self.pushButton.clicked.connect(lambda selfi = self : fonctions.on_listInterOpen_clicked(selfi))
        self.treeWidget.currentItemChanged.connect(lambda lineID = self.treeWidget.currentItem() : fonctions.on_treeListItemInters_clicked(lineID))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))
        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))#CAR PAS DE CHANGEMNTS

        userRights = 0
        DELETE_INTER_RITGHS = 1
        if userRights >= DELETE_INTER_RITGHS:
            self.pushButton_delete.clicked.connect(lambda selfi = self, : fonctions_self.on_listInterDelete_clicked(self))
        else:
            print("[WW] Cette action recquière une élévation des privilèges")
            self.pushButton_delete.clicked.connect(lambda selfi = self, : fonctions_self.DialogPerms(self))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xListIntersSize, yListInterSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xListIntersSize = size.width()
        yListInterSize = size.height()

    def retranslateUi(self, ListInters):
        _translate = QtCore.QCoreApplication.translate
        ListInters.setWindowTitle(_translate("ListInters", "PGLX - Liste des Interventions"))
        self.pushButton.setText(_translate("ListInters", "Ouvrir"))
        self.treeWidget.headerItem().setText(0, _translate("ListInters", "Intervention"))
        self.treeWidget.headerItem().setText(1, _translate("ListInters", "Date"))
        self.treeWidget.headerItem().setText(2, _translate("ListInters", "Type Inter"))
        self.treeWidget.headerItem().setText(3, _translate("ListInters", "Départ"))
        self.treeWidget.headerItem().setText(4, _translate("ListInters", "Retour"))
        self.treeWidget.headerItem().setText(5, _translate("ListInters", "Moyens"))
        self.treeWidget.headerItem().setText(6, _translate("ListInters", "Rédacteur"))
        self.treeWidget.headerItem().setText(7, _translate("ListInters", "Seul ?"))
        self.treeWidget.headerItem().setText(8, _translate("ListInters", "Nature ?"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        #self.treeWidget.topLevelItem(0).setText(0, _translate("ListInters", "Nouvel élément"))
        #self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("ListInters", "Nouvel élément"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_delete.setText(_translate("ListInters", "Supprimer"))
        self.pushButton_3.setText(_translate("ListInters", "Imprimer"))

class Ui_ListIntersPersonnal(QtWidgets.QMainWindow):#pas de fichier .ui crée, copié depuis Ui_ListInters
    '''
    Cette classe ne devrait être que temporaire et remplacée par des graphiques!
    '''
    def __init__(self, parent=None):
        super(Ui_ListIntersPersonnal, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        ListIntersPersonnal = self
        ListIntersPersonnal.setObjectName("ListIntersPersonnal")
        ListIntersPersonnal.resize(xListInterPersonnalSize, yListInterPersonnalSize)
        self.centralwidget = QtWidgets.QWidget(ListIntersPersonnal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 4, 3, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        self.treeWidget.headerItem().setFont(1, font)
        #item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        #item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 4)
        self.pushButton_delete = QtWidgets.QPushButton(self.frame)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_2.addWidget(self.pushButton_delete, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ListIntersPersonnal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListIntersPersonnal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 22))
        self.menubar.setObjectName("menubar")
        ListIntersPersonnal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListIntersPersonnal)
        self.statusbar.setObjectName("statusbar")
        ListIntersPersonnal.setStatusBar(self.statusbar)



        #MODIFICATIONS
        USER = getpass.getuser()
        USER = fonctions.getRealUserName(USER)
        if DEBUG >= 3:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa', USER)
        fichier = path_to_stats_personnal + '/.' + USER.upper()
        nbInters = fonctions.nombre_de_ligne(fichier) - 3 #car 3 lignes de ommentaire
        print('Nombre Inters', nbInters, "Fichier:", fichier)

        fichier = '.' + USER.upper()
        if fonctions.file_exists(path_to_stats_personnal, fichier):
            os.chdir(path_to_stats_personnal)
            entete = linecache.getline(fichier, 3).rstrip('\n').split(";;")
            print("Entete du fichier", entete)

            nbInteridx = entete.index("nbInter")
            dateidx = entete.index("date")
            dureeidx = entete.index("duree")
            typeInteridx = entete.index('typeInter')
            vehicle = entete.index("vehicule")
            fonction = entete.index('fonction')
            ncodis = entete.index('ncodis')
            try:
                typeInter = entete.index("typeInter")
            except:
                pass

            for ligne in range(4, nbInters+1):#le fichier commence avec deux lignes de description + une ligne d'entête
                donnees = linecache.getline(fichier, ligne).rstrip('\n').split(";;")

                item_i = QtWidgets.QTreeWidgetItem()
                item_i.setText(0, donnees[nbInteridx])#N° inter
                item_i.setText(1, donnees[dateidx])#date
                try:
                    item_i.setText(2, donnees[typeInter])#Nature
                except:
                    item_i.setText(2, '-')#Nature
                item_i.setText(3, donnees[dureeidx])#heure départ
                item_i.setText(4, donnees[vehicle])#heure retour
                item_i.setText(5, donnees[fonction])#Moyens
                item_i.setText(6, donnees[ncodis])#rédacteur
                self.treeWidget.addTopLevelItem(item_i)

        self.retranslateUi(ListIntersPersonnal)
        QtCore.QMetaObject.connectSlotsByName(ListIntersPersonnal)


        #CONNEXIONS
        self.pushButton.clicked.connect(lambda selfi = self : fonctions.on_listInterOpen_clicked(selfi))
        self.treeWidget.currentItemChanged.connect(lambda lineID = self.treeWidget.currentItem() : fonctions.on_listInterPersonnalOpen_clicked(lineID))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))
        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.close_window(selfi, ""))#CAR PAS DE CHANGEMNTS

        userRights = 0
        DELETE_INTER_RITGHS = 1
        if userRights >= DELETE_INTER_RITGHS:
            self.pushButton_delete.clicked.connect(lambda selfi = self, : fonctions_self.on_listInterDelete_clicked(self))
        else:
            print("Cette action recquière une élévation des privilèges")
            self.pushButton_delete.clicked.connect(lambda selfi = self, : fonctions_self.DialogPerms(self))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xListInterPersonnalSize, yListInterPersonnalSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xListInterPersonnalSize = size.width()
        yListInterPersonnalSize = size.height()

    def retranslateUi(self, ListIntersPersonnal):
        _translate = QtCore.QCoreApplication.translate
        ListIntersPersonnal.setWindowTitle(_translate("ListIntersPersonnal", "PGLX - Mes Interventions"))
        self.pushButton.setText(_translate("ListIntersPersonnal", "Ouvrir"))
        self.treeWidget.headerItem().setText(0, _translate("ListIntersPersonnal", "N° Intervention"))
        self.treeWidget.headerItem().setText(1, _translate("ListIntersPersonnal", "Date"))
        self.treeWidget.headerItem().setText(2, _translate("ListIntersPersonnal", "Type Inter"))
        self.treeWidget.headerItem().setText(3, _translate("ListIntersPersonnal", "Durée"))
        self.treeWidget.headerItem().setText(4, _translate("ListIntersPersonnal", "Engin"))
        self.treeWidget.headerItem().setText(5, _translate("ListIntersPersonnal", "Fonction"))
        self.treeWidget.headerItem().setText(6, _translate("ListIntersPersonnal", "N° CODIS"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        #self.treeWidget.topLevelItem(0).setText(0, _translate("ListInters", "Nouvel élément"))
        #self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("ListInters", "Nouvel élément"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_delete.setText(_translate("ListIntersPersonnal", "Supprimer"))
        self.pushButton_3.setText(_translate("ListIntersPersonnal", "Imprimer"))

class PersonnalInters_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PersonnalInters_MainWindow, self).__init__()

        self.widget = Ui_PersonnalInters(self)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Test")
        self.resize(400,  400)

        self.show()

        print('a')


class Ui_PersonnalInters(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_PersonnalInters, self).__init__(parent)
        #self.suite()
        global selfi
        selfi = self

        imageSize = QtCore.QSize(200, 200)
        self.image = QtGui.QImage()
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)

    def suite(self):
        PersonnalInters = self
        PersonnalInters.setObjectName("PersonnalInters")
        PersonnalInters.resize(829, 606)
        self.centralwidget = QtWidgets.QWidget(PersonnalInters)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(200, 200))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        self.label_sessionPerso = QtWidgets.QLabel(self.frame)
        self.label_sessionPerso.setObjectName("label_sessionPerso")
        self.gridLayout_2.addWidget(self.label_sessionPerso, 0, 0, 1, 1)
        self.label_user = QtWidgets.QLabel(self.frame)
        self.label_user.setObjectName("label_user")
        self.gridLayout_2.addWidget(self.label_user, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 200))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setMinimumSize(QtCore.QSize(200, 200))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        PersonnalInters.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PersonnalInters)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 24))
        self.menubar.setObjectName("menubar")
        PersonnalInters.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PersonnalInters)
        self.statusbar.setObjectName("statusbar")
        PersonnalInters.setStatusBar(self.statusbar)

        self.retranslateUi(PersonnalInters)
        QtCore.QMetaObject.connectSlotsByName(PersonnalInters)

        #modifications:
        self.gridLayout_2.setviewport(widget)

    def paintEvent(self, event):

        qp = QtGui.QPainter()
        qp.begin(self.widget)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')

        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 600)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 600)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 600)

    def retranslateUi(self, PersonnalInters):
        _translate = QtCore.QCoreApplication.translate
        PersonnalInters.setWindowTitle(_translate("PersonnalInters", "PersonnalInters"))
        self.label_sessionPerso.setText(_translate("PersonnalInters", "Session personnelle:"))
        self.label_user.setText(_translate("PersonnalInters", "user"))
        self.pushButton.setText(_translate("PersonnalInters", "PushButton"))




class Ui_DialogAddUser(QDialog):
    def __init__(self, parent=None):
        super(Ui_DialogAddUser, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        DialogAddUser = self
        DialogAddUser.setObjectName("DialogAddUser")
        DialogAddUser.resize(xDialogAddUserSize, yDialogAddUserSize)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogAddUser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dialogAddUser = QtWidgets.QWidget(DialogAddUser)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        self.dialogAddUser.setFont(font)
        self.dialogAddUser.setObjectName("dialogAddUser")
        self.gridLayout = QtWidgets.QGridLayout(self.dialogAddUser)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_userName = QtWidgets.QLabel(self.dialogAddUser)
        self.label_userName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_userName.setObjectName("label_userName")
        self.gridLayout.addWidget(self.label_userName, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 2)
        self.lineEdit_userName = QtWidgets.QLineEdit(self.dialogAddUser)
        self.lineEdit_userName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.gridLayout.addWidget(self.lineEdit_userName, 1, 0, 1, 4)
        self.groupBox_list = QtWidgets.QGroupBox(self.dialogAddUser)
        self.groupBox_list.setTitle("")
        self.groupBox_list.setObjectName("groupBox_list")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_list)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_whiteList = QtWidgets.QRadioButton(self.groupBox_list)
        self.radioButton_whiteList.setObjectName("radioButton_whiteList")
        self.gridLayout_3.addWidget(self.radioButton_whiteList, 0, 0, 1, 1)
        self.radioButton_blackList = QtWidgets.QRadioButton(self.groupBox_list)
        self.radioButton_blackList.setObjectName("radioButton_blackList")
        self.gridLayout_3.addWidget(self.radioButton_blackList, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_list, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.dialogAddUser)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 3)
        self.gridLayout_2.addWidget(self.dialogAddUser, 0, 0, 1, 1)

        self.retranslateUi(DialogAddUser)
        QtCore.QMetaObject.connectSlotsByName(DialogAddUser)

        #MODIFICATIONS
        self.radioButton_blackList.setChecked(True)
        user_whiteList = fonctions.get_line_alpha(path_to_session, "whiteList", 1, "")
        user_blackList = fonctions.get_line_alpha(path_to_session, "blackList", 1, "")

        #CONNEXIONS
        self.radioButton_blackList.clicked.connect(lambda list = 1 : fonctions.on_radioButton_clicked(path_to_vars, "list", 1))
        self.radioButton_whiteList.clicked.connect(lambda list = 0 : fonctions.on_radioButton_clicked(path_to_vars, "list", 0))

        self.lineEdit_userName.textChanged.connect(lambda value = self.lineEdit_userName : fonctions.on_lineEdit_changed(path_to_vars, value, 'listUser'))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.on_adminList_ok(selfi, ".listUser", ".list"))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_adminsWindows(selfi, path_to_vars))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xDialogAddUserSize, yDialogAddUserSize, DEBUG
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xDialogAddUserSize = size.width()
        yDialogAddUserSize = size.height()

    def retranslateUi(self, DialogAddUser):
        _translate = QtCore.QCoreApplication.translate
        DialogAddUser.setWindowTitle(_translate("DialogAddUser", "PGLX - Liste"))
        self.label_userName.setText(_translate("DialogAddUser", "Nom de l\'utilisateur"))
        self.radioButton_whiteList.setText(_translate("DialogAddUser", "Liste Blanche"))
        self.radioButton_blackList.setText(_translate("DialogAddUser", "Liste Noire"))


class Ui_DialogRemoveUser(QDialog):
    def __init__(self, parent=None):
        super(Ui_DialogRemoveUser, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        DialogRemoveUser = self
        DialogRemoveUser.setObjectName("DialogRemoveUser")
        DialogRemoveUser.resize(xDialogRemoveUserSize, yDialogRemoveUserSize)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogRemoveUser)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dialogRemoveUser = QtWidgets.QWidget(DialogRemoveUser)
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        self.dialogRemoveUser.setFont(font)
        self.dialogRemoveUser.setObjectName("dialogRemoveUser")
        self.gridLayout = QtWidgets.QGridLayout(self.dialogRemoveUser)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_userName = QtWidgets.QLabel(self.dialogRemoveUser)
        self.label_userName.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_userName.setObjectName("label_userName")
        self.gridLayout.addWidget(self.label_userName, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 2)
        self.lineEdit_userName = QtWidgets.QLineEdit(self.dialogRemoveUser)
        self.lineEdit_userName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.gridLayout.addWidget(self.lineEdit_userName, 1, 0, 1, 4)
        self.groupBox_list = QtWidgets.QGroupBox(self.dialogRemoveUser)
        self.groupBox_list.setTitle("")
        self.groupBox_list.setObjectName("groupBox_list")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_list)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_whiteList = QtWidgets.QRadioButton(self.groupBox_list)
        self.radioButton_whiteList.setObjectName("radioButton_whiteList")
        self.gridLayout_3.addWidget(self.radioButton_whiteList, 0, 0, 1, 1)
        self.radioButton_blackList = QtWidgets.QRadioButton(self.groupBox_list)
        self.radioButton_blackList.setObjectName("radioButton_blackList")
        self.gridLayout_3.addWidget(self.radioButton_blackList, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_list, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 89, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.dialogRemoveUser)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 3)
        self.gridLayout_2.addWidget(self.dialogRemoveUser, 0, 0, 1, 1)

        self.retranslateUi(DialogRemoveUser)
        QtCore.QMetaObject.connectSlotsByName(DialogRemoveUser)

        #MODIFICATIONS
        self.radioButton_blackList.setChecked(True)
        user_whiteList = fonctions.get_line_alpha(path_to_session, "whiteList", 1, "")
        user_blackList = fonctions.get_line_alpha(path_to_session, "blackList", 1, "")

        #CONNEXIONS
        self.radioButton_blackList.clicked.connect(lambda list = 1 : fonctions.on_radioButton_clicked(path_to_vars, "list", 1))
        self.radioButton_whiteList.clicked.connect(lambda list = 0 : fonctions.on_radioButton_clicked(path_to_vars, "list", 0))

        self.lineEdit_userName.textChanged.connect(lambda value = self.lineEdit_userName : fonctions.on_lineEdit_changed(path_to_vars, value, 'listUser'))

        self.buttonBox.accepted.connect(lambda selfi = self : fonctions_self.on_adminListRemove_ok(selfi, ".listUser", ".list"))
        self.buttonBox.rejected.connect(lambda selfi = self : fonctions_self.close_adminsWindows(selfi, path_to_vars))

    def resizeEvent(self, resizeEvent):#garde les dimensions en mémoire (pour la session actuelle)
        global xDialogRemoveUserSize, yDialogRemoveUserSize
        size=self.size()
        if DEBUG >= 1:
            print("h", size.height(), 'w', size.width())
        xDialogRemoveUserSize = size.width()
        yDialogRemoveUserSize = size.height()

    def retranslateUi(self, DialogRemoveUser):
        _translate = QtCore.QCoreApplication.translate
        DialogRemoveUser.setWindowTitle(_translate("DialogRemoveUser", "PGLX - Liste"))
        self.label_userName.setText(_translate("DialogRemoveUser", "Nom de l\'utilisateur"))
        self.radioButton_whiteList.setText(_translate("DialogRemoveUser", "Liste Blanche"))
        self.radioButton_blackList.setText(_translate("DialogRemoveUser", "Liste Noire"))


class Ui_PassWord(QDialog):
    def __init__(self, parent=None):
        super(Ui_PassWord, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        PassWord = self
        PassWord.setObjectName("PassWord")
        PassWord.resize(418, 124)
        PassWord.setMinimumSize(QtCore.QSize(418, 124))
        self.gridLayout = QtWidgets.QGridLayout(PassWord)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(PassWord)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(PassWord)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 32))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PassWord)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 2)

        self.retranslateUi(PassWord)
        self.buttonBox.accepted.connect(PassWord.accept)
        self.buttonBox.rejected.connect(PassWord.reject)
        QtCore.QMetaObject.connectSlotsByName(PassWord)

    def retranslateUi(self, PassWord):
        _translate = QtCore.QCoreApplication.translate
        PassWord.setWindowTitle(_translate("PassWord", "PGLX - Authentification"))
        self.label.setText(_translate("PassWord", "Cette action requiers une élévation des privilèges"))

class Ui_PermsError(QDialog):
    def __init__(self, parent=None):
        super(Ui_PermsError, self).__init__(parent)
        self.suite()
        global selfi
        selfi = self

    def suite(self):
        PermsError = self
        PermsError.setObjectName("PermsError")
        PermsError.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PermsError)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(PermsError)
        self.textEdit.setMinimumSize(QtCore.QSize(350, 110))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(PermsError)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.buttonBox.accepted.connect(PermsError.accept)
        self.buttonBox.rejected.connect(PermsError.reject)

        self.retranslateUi(PermsError)
        QtCore.QMetaObject.connectSlotsByName(PermsError)

        #CONNEXIONS



    def retranslateUi(self, PermsError):
        _translate = QtCore.QCoreApplication.translate
        PermsError.setWindowTitle(_translate("PermsError", "PGLX - Zone interdite"))
        self.textEdit.setHtml(_translate("PermsError", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vous n\'avez pas les dertoits suffisants pour effectuer cette commande.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Si vous n\'utilisez pas la bonne session, veuillez vous enregistrer avec la bonne</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">via le menu principal de PGLX.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Un rapport a été envoyé au(x) responsable(s) du centre.</p></body></html>"))

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

    def casernement(self):
        global self_ui_casernement
        self_ui_casernement = self
        print("Casernement")
        self.centralwidget.setEnabled(False)
        mySW = Ui_Casernement()
        mySW.show()

    def fma(self):
        global self_ui_fma
        self_ui_fma = self
        print("FMA")
        self.centralwidget.setEnabled(False)
        mySW = Ui_FMA()
        mySW.show()

    def personnalInters(self):
        global self_ui_personnalInter
        self_ui_personnalInter = self
        print("Mes Inters")
        self.centralwidget.setEnabled(False)
        mySW = Ui_ListIntersPersonnal()
        mySW.show()

    def listInters(self):
        global self_ui_listInters
        self_ui_listInters = self
        print("Liste des Interventions")
        self.centralwidget.setEnabled(False)
        mySW = Ui_ListInters()
        mySW.show()

    def DialogAddUser(self):
        global self_ui_dialogAddUser
        self_ui_dialogAddUser = self
        print("DialogAddUser")
        self.centralwidget.setEnabled(False)
        mySW = Ui_DialogAddUser()
        mySW.show()

    def DialogRemoveUser(self):
        global self_ui_dialogRemoveUser
        self_ui_dialogRemoveUser = self
        print("DialogRemoveUser")
        self.centralwidget.setEnabled(False)
        mySW = Ui_DialogRemoveUser()
        mySW.show()

    def DialogPerms(self):
        global self_ui_dialogPerms
        self_ui_dialogPerms = self
        print("DialogPerms")
        mySW = Ui_PermsError()
        mySW.show()


    def save_tab(self):
        global i, self_de_la_fenetre
        print("Widget", QtWidgets)
        i = self
        i = str(i)
        print("Page:", i)
        fonctions.write_function(path_to_vars, ".tabID", i)

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
        global path_to_rinter, path_to_vars, path_to_rfma, centreInter, a, Ui_PompierGLX

        os.chdir(path_to_session)
        if os.path.isfile(".newCentreInter"):
            centreInter_2 = linecache.getline(".newCentreInter", 1)
            centreInter = centreInter_2
            print('Nouveau centre:', centreInter)
            path = path_to_pglx + '/' + '.centreInter'
            file = open(path, 'w')
            file.write(str(centreInter))
            file.close()

        os.chdir(path_to_vars)
        if os.path.isfile(".newPathToVars"):
            path_to_vars_2 = linecache.getline(".newPathToVars", 1)
            if os.path.exists(path_to_vars_2 + "/"):
                path_to_vars = path_to_vars_2
                print(path_to_vars)
            else:
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
                print("!A n'est pas un chemin, chemin forcé!")


        fonctions_self.close_window(self, "")
        fonctions.update_vars()

        print(path_to_rfma)
        print(path_to_vars)
        print(path_to_rinter)


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

    def on_date_changed(self, value, name):
        os.chdir(path_to_vars)

        temp = QtWidgets.QDateEdit() #permet d'appeler la fonction textFromDate pour le QDate value
        print("BBB", value)

        date_time=""
        print(name, "a pris pour valeur:", date_time)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(date_time))
        file.close()

    def on_time_changed(self, value, name):
        os.chdir(path_to_vars)

        temp = QtWidgets.QTimeEdit() #permet d'appeler la fonction textFromDate pour le QDate value
        date_time = temp.text(value)

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

    def on_removeListItem_clicked(self, whitelist, blacklist):
        print(whitelist)
        print(blacklist)

    def on_adminList_ok(self, user, list):
        global self_ui_dialogAddUser
        print("user to add", user, 'liste', list, 'self', self)
        os.chdir(path_to_session)
        user = fonctions.get_line_alpha(path_to_vars, user, 1, "!A")
        list = fonctions.get_line_int(path_to_vars, list, 1, 1)
        if list == 1:
            file = "blackList"
        else:
            file = "whiteList"

        users = fonctions.get_line_alpha(path_to_session, file, 1, "!A")
        users = users.split()
        user = user[0:len(user)-1]#sinon toujours diférents (i et user)
        print("AAAAAAAAAAAAAAAAAAaaa", users)
        for i in users:
            print("BB i et user", str(i), str(user))
            if i == user:#user:
                print("Identique", i)
                users.remove(i)
            else:
                print('DIFF')
        users.append(user)
        users = " ".join(users)
        fichier = open(file, 'w')
        fichier.write(users)
        fichier.close()

        self.close()
        Ui_Administration.suite(self_ui_dialogAddUser)

    def on_adminListRemove_ok(self, user, list):
        global self_ui_dialogRemoveUser
        print("user to remove", user, 'liste', list, 'self', self)
        os.chdir(path_to_session)
        user = fonctions.get_line_alpha(path_to_vars, user, 1, "!A")
        list = fonctions.get_line_int(path_to_vars, list, 1, 1)
        if list == 1:
            file = "blackList"
        else:
            file = "whiteList"

        users = fonctions.get_line_alpha(path_to_session, file, 1, "!A")
        users = users.split()
        user = user[0:len(user)-1]
        for i in users:
            print("BB i et user", str(i), str(user))
            if i == user:#user:
                print("Identique", i)
                users.remove(i)
            else:
                print('DIFF')
        users = " ".join(users)
        fichier = open(file, 'w')
        fichier.write(users)
        fichier.close()

        self.close()
        Ui_Administration.suite(self_ui_dialogRemoveUser)

    def on_listInterDelete_clicked(self):
        global listInterNum
        os.chdir(path_to_rinter)
        listInterNum = int(listInterNum)
        nbInters = fonctions.nombre_de_ligne('.dataInters')
        file = open('newData', 'w') #nouveau fichier temporaire crée
        for i in range(1, nbInters+1):
            if i != listInterNum:
                file.write(str(fonctions.get_line_alpha(path_to_rinter, '.dataInters', i, "")))#si l'inter est la celle que l'on veut supprimer elle n'est pas réécrite, autrement si
        file.close()

        subprocess.call(["rm", ".dataInters"])
        subprocess.call(["mv", "newData", ".dataInters"])

        Ui_ListInters.suite(self)

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

    def on_spinBox_nb_peronnel_changed(self, value):#pour le casernement
        print("Nombre de personnels et d'activité:", value)
        global b_casernement, Ui_Casernement
        b_casernement = value
        win = Ui_Casernement()
        Ui_Casernement.suite(self)
        print("Rechargement de la page Casernement ...")


    def on_spinBox_fma_formateurs_changed(self, value):#pour les foramteurs (FMA)
        print("Nombre de formateurs:", value)
        global b_fma_formateur, Ui_FMA
        b_fma_formateur = value
        win = Ui_FMA()
        Ui_FMA.suite(self)

    def on_spinBox_fma_spv_changed(self, value):#pour les spv (FMA)
        print("Nombre de personnels en formation:", value)
        global b_fma_spv, Ui_FMA
        b_fma_spv = value
        win = Ui_FMA()
        Ui_FMA.suite(self)

    def on_spinBox_fma_vehicules_changed(self, value):#pour les véhicules (FMA)
        print("Nombre de véhicules pour la FMA:", value)
        global b_fma_vehicules, Ui_FMA
        b_fma_vehicules = value
        win = Ui_FMA()
        Ui_FMA.suite(self)

    def on_spinBox_fma_lieux_changed(self, value):#pour les lieux (FMA)
        print("Nombre de lieux pour la FMA:", value)
        global b_fma_lieux, Ui_FMA
        b_fma_lieux = value
        win = Ui_FMA()
        Ui_FMA.suite(self)


    def close_window(self, *args):#supprime les *args DONNER LE CHEMIN | ATTENTION ne pas utiliser '/' pour les nom la focntion del appelle os.chdir(path)
        self.close()
        path = args[0] #le chemin est (et doit) être donnée en premier
        if os.path.exists(path):
            for i in args:
                fonctions.delete_all_file(path, str(i))
                print(i)
        global self_ui_inter
        self_ui_inter.centralwidget.setEnabled(True)

    def close_adminsWindows(self, *args):# réactive les args widgets
        self.close()
        self_ui_dialogAddUser.centralwidget.setEnabled(True)
        self_ui_inter.centralwidget.setEnabled(True)


    def show_credits(self):
        self.Credits = Credits()
        self.Credits.show()

    def show_license(self):
        self.License = License()
        self.License.show()

class fonctions:
    def update_vars():  # met à jour les divers variables (ex: chemins, nom caserne ...)
        global NCODISMAX, path_to_session, path_to_pglx, path_to_vars, path_to_rinter, path_to_rfma, path_to_rcasernement, path_to_stats_personnal, b, b2, b3, b_casernement, b_fma_formateur, b_fma_spv, b_fma_vehicules, b_fma_lieux, nbSPVCas, nbSPVSLL, self_ui_inter, NVTU, NVL, NFPTL, NFPTSR, NVSAV, NEPSA
        print("var update ...")
        path_to_session = "/home/Pompiers/Public/.tmp/session"  ### sert à stocker à travers le temps des variables
        path_to_pglx = "/home/Pompiers/Public/Rapports/Pompier-GLX"  ### Sert unsiquement pour les fichiers py et images ###
        path_to_vars = "/home/Pompiers/Public/.tmp"  ### sert pour toutes les vars du rapport et des rapports en gnal ###
        path_to_rinter = "/home/Pompiers/Public/Rapports/Interventions/2014"  ### sert uniquement pour l'écriture du rapport ###
        path_to_rfma = "/home/Pompiers/Public/Rapports/FMA/2014"  ### sert uniquement pour l'écriture du rapport ###
        path_to_rcasernement = "/home/Pompiers/Public/Rapports/Casernements/2014"  ### sert uniquement pour l'écriture du rapport ###
        path_to_stats_personnal = "/home/Pompiers/Public/Rapports/Statistiques/Personnels"

        os.chdir(path_to_session)

        NCODISMAX = fonctions.get_line_int(path_to_session, "NCODISMAX", 1, 500000)

        os.chdir(path_to_vars)
        if os.path.isfile(".PathToRInter"):
            path_ = linecache.getline('.PathToRInter', 1)
            if os.path.exists(path_):
                path_to_rinter = path_
            else:
                print("Tentative de création du répertoire")
                subprocess.call(["mkdir", "-p", path_])
                if os.path.isfile(path_):
                    path_to_rinter = path_
                    print("nouveau chemi: ", path_to_rinter)
                else:
                    print("Impossible de créer le chemin, utilisation du chemin par défaut")

        if os.path.isfile(".PathToRFma"):
            path_to_rfma_ = linecache.getline('.PathToRFma', 1)
            if os.path.exists(path_to_rfma_):
                path_to_rfma = path_to_rfma_
        b = 4
        b2 = 2
        b3 = 1
        b_casernement = 8

        b_fma_formateur = 3
        b_fma_spv = 18
        b_fma_vehicules = 2
        b_fma_lieux = 1

        nbSPVSLL = fonctions.get_line_int(path_to_session, "nbSPVSLL", 1, 4)
        print("nbSPVCLL", nbSPVSLL)

        nbSPVCas = fonctions.get_line_int(path_to_session, "nbSPVCas", 1, 5)
        print("nbSPVCas", nbSPVCas)

        NFPTL = fonctions.get_line_int(path_to_session, "NFPTL", 1, 1)
        NVTU = fonctions.get_line_int(path_to_session, "NVTU", 1, 1)
        NVL = fonctions.get_line_int(path_to_session, "NVL", 1, 1)
        NEPSA=fonctions.get_line_int(path_to_session, "NEPSA", 1, 0)
        NFPTSR=fonctions.get_line_int(path_to_session, "NFPTSR", 1, 0)
        NVSAV=fonctions.get_line_int(path_to_session, "NVSAV", 1, 0)

    def messageBox(icon, title, text, detailedtext):
        #icons| NoIcon:0 | Question:4 | Information:1 | Warning:2 | Critical:3
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setDetailedText(detailedtext)
        msgBox.addButton(QtWidgets.QPushButton('Continuer'), 1)
        msgBox.addButton(QtWidgets.QPushButton('Annuler'), 0)
        status = msgBox.exec_()

    def on_nbSpinbox_changed(var, value, name):  #change la valeur d'une variable
        var = value
        fonctions.update_vars()
        os.chdir(path_to_session)
        fichier = open(name, 'w')
        fichier.write(str(value))
        fichier.close()
        print(name, "a pris pour valeur", var)



    def on_lineEdit_changed(path, value, name):
        os.chdir(path)
        print(name, "a pris pour valeur:", value)
        file_to_w = '.' + name
        file = open(file_to_w, 'w')
        file.write(str(value))
        file.close()

    def on_radioButton_clicked(path, name, value):
        print(name, value)
        os.chdir(path)
        file = open("." + name, 'w')
        file.write(str(value))
        file.close()

    def on_userList_changed(list, user, self):
        self.listWidget_WhiteUser.setCurrentRow(0)
        print("selected user", str(user), "opur", list)
        a = []
        a.append(user)
        print('ee', a)
        file = open('AAA', 'w')
        file.write(str(user))
        file.close()

    def on_treeListItemInters_clicked(lineID):
        global listInterNum
        listInterNum = lineID.text(0) #renvoi la valeur en texte de la colonne 0 de la ligne lineID de treeWidget
        listInterNum = int(listInterNum) + 3 #le fichier comprend 2 lignes de description + 1 ligne d'entete (l'intervention 1 sera sur la ligne 1+3=4)

    def on_listInterOpen_clicked(self):
        global listInterNum
        print("visionnage de l'intervention N°", listInterNum)
        os.chdir(path_to_rinter)

        fileToOpen = fonctions.get_line_alpha(path_to_rinter, '.dataInters.pglxdi', int(listInterNum), "!A")#cherche la ligne listInterNum

        if fileToOpen == "!A":
            print("PAS DE FICHIER ARRET")
        else:#prendre le nom du fichier à ouvrir depuis la ligne et l'ouvrir
            fileToOpen = fileToOpen.split(';;')
            fileToOpen = fileToOpen[1] #nom du fichier
            subprocess.call(["xdg-open", fileToOpen])

    def on_listInterPersonnalOpen_clicked(lineID):
        print("visionnage de l'intervention N°")
        #recherche de l'id de l'inter (ncodis)
        os.chdir(path_to_stats_personnal)

        #recherche de la ligne séletionnée lineID
        lineID = int(lineID.text(0)) #car 3 lignes de description


        USER = getpass.getuser()
        USER = fonctions.getRealUserName(USER)
        USER = USER.upper()
        file = '.' + str(USER)
        fileToOpen = fonctions.get_line_alpha(path_to_stats_personnal, file, 3, "!A")#cherche la ligne listInterNum

        if fileToOpen == "!A":
            print("PAS DE FICHIER ARRET")
        else:
            print("Dans le fichier", file, 'lineID', lineID)
            #chercher la colonne ayant ncodis
            entete = linecache.getline(file, 3)
            entete = entete.rstrip('\n').split(';;')
            nbInter = entete.index('nbInter')

            #rechercher de la ligne contenant le même numéro d'inter (lineID)
            lineno = 4
            entete = linecache.getline(file, lineno)
            entete = entete.rstrip('\n').split(';;')
            print('CCCCC', nbInter,'lineID', lineID, entete)
            id = entete[nbInter]

            verif = 1000

            while int(id) != int(lineID) and verif != 0:
                lineno += 1
                verif -= 1
                entete = linecache.getline(file, lineno)
                entete = entete.rstrip('\n').split(';;')
                print('CCCCC', nbInter, 'lineID', lineID, entete)
                try:
                    id = entete[nbInter]
                    print('XXX', id)
                except:
                    print('[EE] error in entete[nbInter-1]')

            if verif == 0:
                print('[WW] arrêt de la boucle car le compteur de vérification est devenu faux')
            print('ligne à chercher:', id)

            #Recherche de ncodis dans la ligne id
            entete = linecache.getline(file, 3)
            entete = entete.rstrip('\n').split(';;')
            codis = entete.index('ncodis')
            print('codis', codis)
            entete = linecache.getline(file, lineno)
            entete = entete.rstrip('\n').split(';;')
            ncodis = entete[codis]
            print('ncodis (id):', ncodis)
            id = ncodis

        #recherche du nom du rapport grâce à l'id (ncodis) trouvé


        os.chdir(path_to_rinter)
        file = '.dataInters.pglxdi'
        fileToOpen = fonctions.get_line_alpha(path_to_rinter, file, 3, "!A")#cherche la ligne listInterNum

        if fileToOpen == "!A":
            print("PAS DE FICHIER ARRET")
        else:
            entete = fileToOpen.rstrip('\n').split(";;")
            ncodis = entete.index("ncodis")
            line = 4
            donnees = linecache.getline(file, line)
            donnees = donnees.rstrip('\n').split(";;")
            print('recherche de id =', id)
            verif = 2000#nombre de lignes à vérifier avant d'arrête la boucle
            try:
                d = donnees[ncodis]
            except:
                print('[WW] la ligne d\'intervention a été rédigée avec une version antérieur >> pas le même nombre de colonne \n'
                      'la ligne ne sera pas prise en compte et peut empêcher le programme d\'effectuer l\'action demandée')
                d = -1#rend la ligne actuelle fausse

            loopPrevent = 0
            loop = 6
            while int(d) != int(id) and verif != 0 and loopPrevent < loop:#si 6 lignes de suites ne sont vides arrêt de la boucle
                verif -= 1
                line += 1
                donnees = linecache.getline(file, line)
                donnees = donnees.rstrip('\n').split(";;")
                try:
                    print('ncodis:', donnees[ncodis], 'verif', verif)
                    d = donnees[ncodis]
                    loopPrevent = 0
                except:
                    print('[WW] la ligne d\'intervention a été rédigée avec une version antérieur >> pas le même nombre de colonne \n'
                      'la ligne ne sera pas prise en compte et peut empêcher le programme d\'effectuer l\'action demandée')
                    d = -1
                    if donnees[0] == '':#si 6 lignes de suites ne sont vides arrêt de la boucle
                        loopPrevent += 1
                    else:
                        loopPrevent = 0


            if loopPrevent >= loop:
                print('[WW] Arrêt de la boucle car le nombre maximal de ligne vide a été atteinte (' + str(loop) + ')')
                fonctions.messageBox(2,'Erreur', 'Arrêt de la boucle car le nombre maximal de ligne vide a été atteinte (' + str(loop) + ')', 'le nombre de tour peut être défini dans les options \n le fichier ne sera pas ouvert')
            elif verif == 0:
                print('[WW] la boucle s\'est arrêté car ncodis n\'a pas été trouvé dans les \a lignes définies par verif')
                fonctions.messageBox(2,'Erreur', 'la boucle s\'est arrêté car ncodis n\'a pas été trouvé dans les \a lignes définies par verif', 'le nombre de vérification peut être défini dans les options \n le fichier ne sera pas ouvert')

            else:
                line = linecache.getline(file, line)
                line = line.rstrip('\n').split(';;')
                name = entete.index('name')
                name = line[name]
                print("Nom du rapport", name)

                subprocess.call(["xdg-open", name])


    def file_is_int(path_to_file, file, line):  #regarde si un fichier existe et si son contenu à la ligne line est un entier: renvoi 1 si true et 0 si false
        var = 0
        if fonctions.file_exists(path_to_file, file):
            linecache.clearcache()  #permet d'actualiser le fichier file
            var = linecache.getline(path_to_file + '/' + file, line)
            print(var)
            length = len(var)
            i=0
            if length >0 :
                while(var[i].isdigit()):
                    i = i+1
                if i == length-1:
                    var = 1
                else:
                    var = 0
            else:
                if var.isdigit():
                    var = 1
                else:
                    var = 0

        if DEBUG >= 3:
            print("Int ?", file, var)
        return var

    def file_exists(path_to_file, file):  #regarde si un fichier existe et si son contenu (1ère ligne) est un entier
        if DEBUG >= 3:
            print("File ?", file, os.path.isfile(path_to_file + '/' + file))
        return os.path.isfile(path_to_file + '/' + file)


    def create_inter(self):
        global b, b2, b3, heure_appel, centreInter, nCodis, natureInter, observation, demandeurInter, telDemandeur, adresseDemandeur, personnel, engins
        print("Création de l'intervention en cours ...")
        print("Récupération des variables dans les fichiers")
        os.chdir(path_to_vars)
        heure_appel = fonctions.get_line_alpha(path_to_vars, ".heure_appel", 1, "")
        centreInter = fonctions.get_line_alpha(path_to_vars, ".centreInter", 1, "")
        nCodis = fonctions.get_line(path_to_vars, ".nCodis", 1, "!Non renseigné")
        natureInter = fonctions.get_line_alpha(path_to_vars, ".natureInter", 1, "")
        observation = fonctions.get_line_alpha(path_to_vars, ".observation", 1, "")
        demandeurInter = fonctions.get_line_alpha(path_to_vars, ".demandeurInter", 1, "")
        telDemandeur = fonctions.get_line_alpha(path_to_vars, ".telDemandeur", 1, "")
        adresseDemandeur = fonctions.get_line_alpha(path_to_vars, ".adresseDemandeur", 1, "")

        personnel = []
        for i in range(0, b):
            fonctions_sp = str(fonctions.get_line_alpha(path_to_vars, ".fonctionSp-" + str(i), 1, ""))
            sp = str(fonctions.get_line_alpha(path_to_vars, ".sp-" + str(i), 1, ""))
            personnel.append([fonctions_sp, sp])
        print("Personnels:", personnel)

        engins = []
        for i in range(0, b2):
            fonction_engin = str(fonctions.get_line_alpha(path_to_vars, ".engin-" + str(i), 1, ""))
            engin = str(fonctions.get_line_alpha(path_to_vars, ".fonctionEngin-" + str(i), 1, ""))
            engins.append([fonction_engin, engin])
        print("Engins:", engins)

        renforts = []
        for i in range(0, b3):
            fonction_engin_renfort = str(fonctions.get_line_alpha(path_to_vars, ".enginRenfort-" + str(i), 1, ""))
            engin_renfort = str(fonctions.get_line_alpha(path_to_vars, ".fonctionEnginRenfort-" + str(i), 1, ""))
            renforts.append([fonction_engin_renfort, engin_renfort])
        print("Engins:", renforts)

        starLine = fonctions.create_line(80, "*")
        dashLine = fonctions.create_line(80, '-')
        fonctions.write_function(path_to_vars, "000000", heure_appel, '\n', starLine, '\n', heure_appel, '      ',
                                 centreInter, '\n', "N° Intervention: ", nCodis, '\n', "NATURE: ", natureInter, '\n',
                                 "OBSERVATIONS: ", observation, '\n', dashLine, '\n', "DEMANDEUR: ", demandeurInter, '\n',
                                 "TELEPHONE: ", telDemandeur, '\n', "ADRESSE: ", adresseDemandeur, '\n', dashLine, '\n',
                                 "Personnels / Équipes", '\n', personnel, '\n \n', dashLine, '\n', "Engins", '\n', engins,
                                 '\n', dashLine, '\n \n', "Renforts: \n", renforts, '\n \n', starLine)

        fonctions.delete_file(path_to_vars + '/' + ".heure_appel")
        fonctions.delete_file(path_to_vars + '/' + ".centreInter")
        fonctions.delete_file(path_to_vars + '/' + ".nCodis")
        fonctions.delete_file(path_to_vars + '/' + ".natureInter")
        fonctions.delete_file(path_to_vars + '/' + ".observation")
        fonctions.delete_file(path_to_vars + '/' + ".demandeurInter")
        fonctions.delete_file(path_to_vars + '/' + ".telDemandeur")
        fonctions.delete_file(path_to_vars + '/' + ".adresseDemandeur")
        for i in range(0, b):
            fonctions.delete_file(path_to_vars + '/' + ".fonctionSp-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".sp-" + str(i))
        for i in range(0, b2):
            fonctions.delete_file(path_to_vars + '/' + ".engin-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".fonctionEngin-" + str(i))
        for i in range(0, b3):
            fonctions.delete_file(path_to_vars + '/' + ".enginRenfort-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".fonctionEnginRenfort-" + str(i))

        print("ALERTE: Nouvelle intervention en cours !")
        self.hide()
        self_ui_inter.centralwidget.setEnabled(True)


    def casernement(self):
        global path_to_rcasernement
        print("Création du rapport de casernement en cours ...")
        print("Récupération des variables dans les fichiers")
        dateDebut = fonctions.get_line_alpha(path_to_vars, ".dateDebut", 1, "!Intemporel")
        dateFin = fonctions.get_line_alpha(path_to_vars, ".dateFin", 1, '!Intemporel')
        lieu = fonctions.get_line_alpha(path_to_vars, ".lieu", 1, '!Pas de lieu indiqué')
        equipe = fonctions.get_line_alpha(path_to_vars, ".equipe", 1, "")
        responsable_1 = fonctions.get_line_alpha(path_to_vars, ".responsable_1", 1, "!Irresponsable")
        responsable_2 = fonctions.get_line_alpha(path_to_vars, ".responsable_2", 1, "")

        personnel = []
        for i in range(0, b_casernement):
            activite = str(fonctions.get_line_alpha(path_to_vars, ".activite-" + str(i), 1, ""))
            spv = str(fonctions.get_line_alpha(path_to_vars, ".personnel-" + str(i), 1, ""))
            if spv != "!A":
                if activite == "!A":
                    personnel.append([" AUCUNE ", spv])
                else:
                    personnel.append([activite, spv])
            activite = str(fonctions.get_line_alpha(path_to_vars, ".activite_2-" + str(i), 1, ""))
            spv = str(fonctions.get_line_alpha(path_to_vars, ".personnel_2-" + str(i), 1, ""))
            if spv != "!A" or spv != "!A":
                if activite == "!A":
                    personnel.append([" AUCUNE ", spv])
                else:
                    personnel.append([activite, spv])

        print("Personnels:", personnel)

        nb_ligne = fonctions.nombre_de_ligne(".rapport_casernement")
        rapport = ""
        for i in range(0, nb_ligne + 1):
            rapport += linecache.getline(".rapport_casernement", i)
        print("Rapport", rapport)

        starLine = fonctions.create_line(80, "*")
        dashLine = fonctions.create_line(80, '-')

        name = "Rapport-Casernement-" + str(datetime.datetime.now())
        fonctions.write_function(path_to_rcasernement, name, "RAPPORT CASERNEMENT", '\n', starLine, '\n',
                                 "Date de Début: " + str(dateDebut), '\n', "Date de Fin: " + str(dateFin), '\n',
                                 dashLine + '\n', "Lieu" + str(lieu), '\n', "Équipe de garde" + str(equipe), '\n',
                                 "RESPONSABLES: ", '\n', str(responsable_1), '\n', str(responsable_2), '\n', dashLine, '\n',
                                 "PERSONNELS:", '\n', str(personnel), '\n', dashLine, '\n', "Rapport:", '\n', str(rapport))

        fonctions.delete_file(path_to_vars + '/' + ".dateDebut")
        fonctions.delete_file(path_to_vars + '/' + ".dateFin")
        fonctions.delete_file(path_to_vars + '/' + ".lieu")
        fonctions.delete_file(path_to_vars + '/' + ".equipe")
        fonctions.delete_file(path_to_vars + '/' + ".responsable_1")
        fonctions.delete_file(path_to_vars + '/' + ".responsable_2")
        for i in range(0, b_casernement):
            fonctions.delete_file(path_to_vars + '/' + ".activite-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".personnel-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".activite_2-" + str(i))
            fonctions.delete_file(path_to_vars + '/' + ".personnel_2-" + str(i))
        fonctions.delete_file(path_to_vars + '/' + ".rapport_casernement" + str(i))

        self.hide()
        self_ui_inter.centralwidget.setEnabled(True)


    def fma(self):
        global path_to_rfma
        print("Création du rapport de FMA en cours ...")
        print("Récupération des variables dans les fichiers")
        themeFma = fonctions.get_line_alpha(path_to_vars, ".theme_fma", 1, 'Pas de thème particulier')
        dateDebut = fonctions.get_line_alpha(path_to_vars, ".dateDebut", 1, "Intemporel")
        dateFin = fonctions.get_line_alpha(path_to_vars, ".dateFin", 1, "!Intemporel")
        theme = fonctions.get_line_alpha(path_to_vars, ".theme", 1, "!Pas de thème indiqué")

        fonctions_self.close_window(self, "")

        formateurs = []
        for i in range(0, b_fma_formateur):
            formateur = str(fonctions.get_line_alpha(path_to_vars, ".formateurNom-" + str(i), 1, ""))
            formation = str(fonctions.get_line_alpha(path_to_vars, ".formateurFormation-" + str(i), 1, ""))
            centre = str(fonctions.get_line_alpha(path_to_vars, ".formateurCentre-" + str(i), 1, ""))
            if formateur != "!A":  #si le personnel est renseigné
                if centre == "!A":  #si pas de centre renseigneé, mettre aucun
                    formateurs.append(str(formateur) + ' ' + str(formation) + " AUCUN ")
                else:
                    formateurs.append(str(formateur) + ' ' + str(formation) + ' ' + str(centre))

        print("Formateurs:", formateurs)

        personnel = []
        for i in range(0, b_fma_spv):
            spv = str(fonctions.get_line_alpha(path_to_vars, ".spvNom-" + str(i), 1, ""))
            formation = str(fonctions.get_line_alpha(path_to_vars, ".spvFormation-" + str(i), 1, ""))
            centre = str(fonctions.get_line_alpha(path_to_vars, ".spvCentre-" + str(i), 1, ""))
            if spv != "!A":  #si le personnel est renseigné
                if centre == "!A":  #si pas de centre renseigneé, mettre aucun
                    personnel.append(str(spv).rstrip('\n') + ' ' + str(formation).rstrip('\n') + " AUCUN ")
                else:
                    personnel.append(str(spv).rstrip('\n') + ' ' + str(formation).rstrip('\n') + ' ' + str(centre).rstrip('\n'))

        print("Personnels formés:", personnel)

        vehicules = []  #et matériel #ATTENTION COMBOBOX
        for i in range(0, b_fma_vehicules):
            vehicule = str(fonctions.get_line_alpha(path_to_vars, ".vehicule-" + str(i), 1, ""))
            centre = str(fonctions.get_line_alpha(path_to_vars, ".vehiculeCentre-" + str(i), 1, ""))
            autre = str(fonctions.get_line_alpha(path_to_vars, ".vehiculeAutre-" + str(i), 1, ""))
            if vehicule != "!A":  #si le personnel est renseigné
                if centre == "!A":  #si pas de centre renseigné, mettre aucun
                    if autre == "!A":
                        vehicules.append(str(vehicule).rstrip('\n') + " AUCUN " + "RAS")
                    else:
                        vehicules.append(str(vehicule).rstrip('\n') + " AUCUN " + str(autre).rstrip('\n'))
                else:
                    vehicules.append(str(vehicule).rstrip('\n') + ' ' + str(centre).rstrip('\n') + ' ' + str(autre).rstrip('\n'))

        print("Véhicules:", vehicules)

        lieux = []
        for i in range(0, b_fma_lieux):
            lieu = str(fonctions.get_line_alpha(path_to_vars, ".lieu-" + str(i), 1, "!Pas de lieu indiqué"))
            lieu = lieu.rstrip('\n')
            lieux.append(lieu)

        print("Lieu(x) de formation:", lieux)

        nb_ligne = fonctions.nombre_de_ligne(".rapport_fma")
        rapport = ""
        for i in range(0, nb_ligne + 1):
            rapport += linecache.getline(".rapport_fma", i)
        print("Rapport", rapport)

        starLine = fonctions.create_line(80, "*")
        dashLine = fonctions.create_line(80, '-')

        name = "Rapport-FMA-" + str(datetime.datetime.now())

        personnel = '\n'.join(personnel)
        formateurs = '\n'.join(formateurs)
        vehicules = "\n".join(vehicules)
        lieux = "\n".join(lieux)


        vehicules = vehicules.strip('[]')

        if DEBUG >= 3:
            print("AAAAAA", vehicules, '\n', "CCCCCC", vehicules)  # {DEL}
        fonctions.write_function(path_to_rfma, name, "RAPPORT FMA", '\n', starLine, '\n', "Formation: ", themeFma, '\n',
                                 "Date de début: ", dateDebut, " Date de fin:", dateFin, '\n', dashLine, '\n',
                                 "FORMATTEURS:", '\n', formateurs, '\n', dashLine, '\n', "SPV Formés:", '\n', personnel,
                                 '\n', dashLine, '\n', "Véhicules:", '\n', vehicules, '\n', dashLine, '\n', "Lieu(x):",
                                 '\n', lieux, '\n', starLine, '\n', "RAPPORT:", '\n', rapport)

        fonctions.fma_delete_files()  #supprime les fichiers, est utilisé car lors de la fermeture de FMA en cancel il faut également effacer les même fichiers.

        os.chdir(path_to_rfma)

        user = getpass.getuser()

        lieu = ""
        for i in lieux:
            if i != '\n':
                lieu += str(i)
            elif i == '\n':
                lieu += " : "

        data = "0" + ";;" + str(name).rstrip('\n') + ';;' + str(dateDebut).rstrip('\n') + ';;' + str(dateFin).rstrip('\n') + ';;' +  str(user).rstrip('\n') + ';;' + str(themeFma).rstrip('\n') + ';;' + str(lieu).rstrip('\n')
        if fonctions.file_exists(path_to_rfma, '.dataFma.pglxdf'):
            file = open(".dataFma.pglxdf", 'a')
            file.write('\n')
            file.write(data)
            file.close()
        else:
            file = open(".dataFma.pglxdf", 'w')
            file.write("#PGLX DATA FMA" + '\n' + "#version;;0.5" + '\n' + "nbFma;;name;;dateDebut;;dateFin;;user;;themeFma;;lieux".rstrip('\n') + '\n')
            file.write(data)
            file.close()

    def fma_delete_files():
        os.chdir(path_to_vars)
        fonctions.delete_all_file(path_to_vars, '.theme_fma', '.heureDebut', '.heureFin', '.theme', '.rapport_fma')
        for i in range(0, b_fma_formateur):
            fonctions.delete_all_file(path_to_vars, '.formateurNom-' + str(i), ".formateurFormation-" + str(i),
                                      ".formateurCentre-" + str(i), '.lieu-' + str(i))
        for i in range(0, b_fma_spv):
            fonctions.delete_all_file(path_to_vars, '.spvNom-' + str(i), ".spvFormation-" + str(i), ".spvCentre-" + str(i))
        for i in range(0, b_fma_vehicules):
            fonctions.delete_all_file(path_to_vars, '.vehicule-' + str(i), ".vehiculeCentre-" + str(i),
                                      ".vehiculeAutre-" + str(i))


    def getRealUserName(user):

        line = fonctions.read_file(path_to_pglx, '.dicoNames', "}", "!A")
        if line != '!A':
            line = line.rstrip('\n').split('}')#crée une liste des lignes
            line = "".join(line)#regroupe toutes les lignes sur une seule
            line = line.split(';;')#sépare les éléments de la ligne unique

            if DEBUG >= 3:
                print("getRealUserName", line)
            userName = line.index(user)
            userName = line[userName]
            realName = line.index(user)#le vrai nom est positionné juste avant le nom système
            realName = line[realName-1]
            print('user', user, 'username:', userName, 'realname', realName)
        else:
            realName = "pglx"
            print("[WW] pas de fichier .dicoNames trouvé")
        return realName

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
        if DEBUG >= 1:
            print("create_line", line)
        return line


    def get_line_alpha(path, fichier, line, exceptSring):
        os.chdir(path)
        if os.path.isfile(fichier):
            linecache.clearcache()
            value = linecache.getline(fichier, line)
            if DEBUG >= 2:
                print("Valeur pour", fichier, value)
            return value
        else:
            if DEBUG >= 2:
                print("!A pas de fichier correcte pour", fichier)
            return exceptSring


    def get_line(path, fichier, line):  #retourne la valeur de la ligne
        os.chdir(path)
        if os.path.isfile(fichier):
            value = linecache.getline(fichier, line)
            if value.isdigit():
                if DEBUG >= 2:
                    print("Valeur pour ", fichier, ":", value)
                return value
            else:
                if DEBUG >= 2:
                    print("Valeur pour ", fichier, ": 0")
                return 0
        else:
            if DEBUG >= 2:
                print("Valeur pour ", fichier, ": 0")
            return 0

    def get_line_int(path, fichier, line, exceptNumber): #renvoi la valeur de la ligne et exceptNumber si la ligne n'est pas conforme ou n'existe pas
        os.chdir(path)
        if fonctions.file_is_int(path, fichier, line) == 1:
            linecache.clearcache()
            return int(linecache.getline(fichier, line))
        else:
            return exceptNumber

    def read_file(path, file, replaceStrip, exceptString):#renvoi toutes les lignes d'un fichier, séparées par replaceStrip, si pas de ligne ou pas de fichier renvoi except string
        if DEBUG >= 2:
            print('lecture du fichier', path, file)
        if fonctions.file_exists(path, file):
            nbLignes = fonctions.nombreLigne(path, file)
            fileText = ""
            if DEBUG >= 3:
                print('Nb Lignes =', nbLignes)
            for i in range(1, nbLignes+1):
                line = fonctions.get_line_alpha(path, file, i, "")
                try:
                    line = line.split("\n")
                    line = replaceStrip.join(line)
                    fileText += line
                except:
                    print('Erreur fatale!')
            if DEBUG >= 1:
                print("Fichier text:", file, "=", fileText)
        else:
            fileText = exceptString
        return fileText

    def rediger(self_new_rapport):
        #ATTENTION LES RAPPORTS DE CASERNEMENT sont traités dans fonctions.casernement
            # LES RAPPORTS DE FMA sont traités dans fonctions.fma
        global self_ui_inter, Ui_rapportInter, NFPTL, NVTU, NVL

        print("Rédaction en cours ...")
        print("Récupération des variables dans les fichiers")

        os.chdir(path_to_rinter)  #n° inter



        file = '.dataInters.pglxdi'
        nombre = fonctions.nombreDeLigne(path_to_rinter, '.dataInters.pglxdi') + -2 #car il y a 3 lignes de description dans le fichier
        print('Intervention N°:', nombre)

        filesToDelete=[]

        os.chdir(path_to_vars)

        heure_appel = linecache.getline('.date_appel', 1)
        heure_depart = linecache.getline('.date_depart', 1)
        heure_fin = linecache.getline('.date_fin', 1)
        ncodis = linecache.getline('.nCodis', 1)
        typeInter = fonctions.get_line_alpha(path_to_vars, '.typeInter', 1, "Aucun Type")
        typeInter = typeInter.rstrip('\n')

        filesToDelete.append('.date_appel')
        filesToDelete.append('.date_depart')
        filesToDelete.append('.date_fin')
        filesToDelete.append('.nCodis')
        filesToDelete.append('.typeInter')

        fptl = []
        equipage_fptl = []# contient les équipages de tous les fptl
        for i in range(1, NFPTL+1):
            con_fptl = linecache.getline('.con_fptl' + '-' + str(i), 1)
            if str(con_fptl) != "":
                fptl.append(1)#ajoute à la liste des fptl sorties le fptl N° i
            else:
                fptl.append(0)

            ca_fptl = linecache.getline('.ca_fptl' + '-' + str(i), 1)
            ce_fptl = linecache.getline('.ce_fptl' + '-' + str(i), 1)
            ce2_fptl = linecache.getline('.ce2_fptl' + '-' + str(i), 1)
            equ_fptl = linecache.getline('.equ_fptl' + '-' + str(i), 1)
            equ2_fptl = linecache.getline('.equ2_fptl' + '-' + str(i), 1)
            stag_fptl = linecache.getline('.stag_fptl' + '-' + str(i), 1)

            filesToDelete.append('.ca_fptl' + '-' + str(i))
            filesToDelete.append('.ce_fptl' + '-' + str(i))
            filesToDelete.append('.ce2_fptl' + '-' + str(i))
            filesToDelete.append('.equ_fptl' + '-' + str(i))
            filesToDelete.append('.equ2_fptl' + '-' + str(i))
            filesToDelete.append('.stag_fptl' + '-' + str(i))
            filesToDelete.append('.con_fptl' + '-' + str(i))

            #si la fonction a un personnel, il est ajouté à la liste
            if ca_fptl != "":
                equipage_fptl.append("CA FPTL-" + str(i) + ": " + str(ca_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ca_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "CA")
            if con_fptl != "":
                equipage_fptl.append("Conducteur FPTL-" + str(i) + ": " + str(con_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(con_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "Conducteur")
            if ce_fptl != "":
                equipage_fptl.append("CE BAT FPTL-" + str(i) + ": " + str(ce_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ce_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "CE")
            if ce2_fptl != "":
                equipage_fptl.append("CE BAL FPTL-" + str(i) + ": " + str(ce2_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ce2_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "CE")
            if equ_fptl != "":
                equipage_fptl.append("EQU BAT FPRL-" + str(i) + ": " + str(equ_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(equ_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "EQU")
            if equ2_fptl != "":
                equipage_fptl.append("EQU BAT FPTL-" + str(i) + ": " + str(equ2_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(equ2_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "EQU")
            if stag_fptl != "":
                equipage_fptl.append("Stagiaire FPTL-" + str(i) + ": " + str(stag_fptl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(stag_fptl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "FPTL", typeInter, "Stagiaire")

            equipage_fptl.append('\n')#permet lors de l'écriture d'ajouter un retour à la ligne lors du passage d'un autre véhicule de même catégorie


        vtu = []
        remorque = []
        equipage_vtu=[]
        for i in range(1, NVTU+1):
            con_vtu = linecache.getline('.con_vtu' + '-' + str(i), 1)
            if str(con_vtu) != "":
                vtu.append(1)#ajoute à la liste des vtu sorties le vtu N° i
            else:
                vtu.append(0)

            ca_vtu = linecache.getline('.ca_vtu' + '-' + str(i), 1)
            ce_vtu = linecache.getline('.ce_vtu' + '-' + str(i), 1)
            stag_vtu = linecache.getline('.stag_vtu' + '-' + str(i), 1)
            remorque_ = linecache.getline('.remorque' + '-' + str(i), 1)

            filesToDelete.append('.ca_vtu' + '-' + str(i))
            filesToDelete.append('.ce_vtu' + '-' + str(i))
            filesToDelete.append('.stag_vtu' + '-' + str(i))
            filesToDelete.append('.remorque' + '-' + str(i))
            filesToDelete.append('.con_vtu' + '-' + str(i))

            if os.path.isfile(path_to_vars + "/.remorque" + '-' + str(i)) and str(remorque_)[0] == "2":
                remorque.append(1)
            else:
                remorque.append(0)
            if DEBUG >= 3:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", remorque)#//TODO: remove

            if ca_vtu != "":
                equipage_vtu.append("CA VTU-" + str(i) + ": " + str(ca_vtu).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ca_vtu).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VTU", typeInter, "CA")
            if con_vtu != "":
                equipage_vtu.append("Conducteur VTU-" + str(i) + ": " + str(con_vtu).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(con_vtu).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VTU", typeInter, "Conducteur")
            if ce_vtu != "":
                equipage_vtu.append("EQU VTU-" + str(i) + ": " + str(ce_vtu).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ce_vtu).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VTU", typeInter, "CE")
            if stag_vtu != "":
                equipage_vtu.append("Stagiaire VTU-" + str(i) + ": " + str(stag_vtu).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(stag_vtu).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VTU", typeInter, "Stagiaire")

            equipage_vtu.append('\n')#permet lors de l'écriture d'ajouter un retour à la ligne lors du passage d'un autre véhicule de même catégorie


        vl=[]
        equipage_vl=[]
        for i in range(1, NVL+1):
            con_vl = linecache.getline('.con_vl' + '-' + str(i), 1)

            if str(con_vl) != "":
                vl.append(1)#ajoute à la liste des vl sorties la vl N° i
            else:
                vl.append(0)

            ca_vl = fonctions.get_line_alpha(path_to_vars, '.ca_vl' + '-' + str(i), 1, "")
            ce_vl = fonctions.get_line_alpha(path_to_vars, '.ce_vl' + '-' + str(i), 1, "")
            equ_vl = fonctions.get_line_alpha(path_to_vars, '.equ_vl' + '-' + str(i), 1, "")
            stag_vl = fonctions.get_line_alpha(path_to_vars, '.stag_vl' + '-' + str(i), 1, "")

            filesToDelete.append('.ca_vl' + '-' + str(i))
            filesToDelete.append('.ce_vl' + '-' + str(i))
            filesToDelete.append('.equ_vl' + '-' + str(i))
            filesToDelete.append('.stag_vl' + '-' + str(i))
            filesToDelete.append('.con_vl' + '-' + str(i))

            if ca_vl != "":
                equipage_vl.append("CA VL-" + str(i) + ": " + str(ca_vl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ca_vl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VL", typeInter, "CA")#crée la ficher personnelle du CA //TODO: ADD typeInter
            if con_vl != "":
                equipage_vl.append("Conducteur VL-" + str(i) + ": " + str(con_vl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(con_vl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VL", typeInter, "Conducteur")#Conducteur
            if ce_vl != "":
                equipage_vl.append("CE VL-" + str(i) + ": " + str(ce_vl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(ce_vl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VL", typeInter, "CE")#CE
            if equ_vl != "":
                equipage_vl.append("EQU VL-" + str(i) + ": " + str(equ_vl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(equ_vl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VL", typeInter, "EQU")#EQU
            if stag_vl != "":
                equipage_vl.append("Stagiaire VL-" + str(i) + ": " + str(stag_vl).rstrip('\n') + ";;")
                fonctions.createOwnStats(str(stag_vl).rstrip('\n'), nombre, heure_depart, heure_fin, ncodis, "VL", typeInter, "Stagiaire")#Stagiaire

            equipage_vl.append('\n')#permet lors de l'écriture d'ajouter un retour à la ligne lors du passage d'un autre véhicule de même catégorie


        nature_inter = linecache.getline('.natureInter', 1)
        loc_inter = linecache.getline('.localisationInter', 1)
        demandeur_inter = linecache.getline('.demandeurInter', 1)

        filesToDelete.append('.natureInter')
        filesToDelete.append('.localisationInter')
        filesToDelete.append('.demandeurInter')


        spv_sll = []
        spv_caserne = []
        r = nbSPVCas#//TODO: attention r=nbSpvCas est défini par utilisateur >> r=nbSpvCas et non 4
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

            filesToDelete.append('.spv_sll_comboBox_12' + '-' + str(i))
            filesToDelete.append('.spv_sll_comboBox_15' + '-' + str(i))
            filesToDelete.append('.spv_caserne_comboBox_13' + '-' + str(i))
            filesToDelete.append('.spv_caserne_comboBox_14' + '-' + str(i))

        whitespace = "        "#marge du document

        spv_sll = whitespace.join(spv_sll)
        print("SPV SLL", spv_sll)
        if spv_sll == []:
            spv_sll = False

        spv_caserne = whitespace.join(spv_caserne)
        print("SPV CAS:", spv_caserne)
        if spv_caserne == []:
            spv_caserne = False

        equipage_fptl = " ".join(equipage_fptl)
        print("Equipages FPLT", equipage_fptl)
        if equipage_fptl == []:
            equipage_fptl = False

        equipage_vtu = " ".join(equipage_vtu)
        print("Equipages VTU", equipage_vtu)
        if equipage_vtu == []:
            equipage_vtu = False

        equipage_vl = " ".join(equipage_vl)
        print("Equipages VL", equipage_vl)
        if equipage_vl == []:
            equipage_vl = False

        ifalone = 1
        if os.path.isfile('.1erDepart_VSAV'):
            vsav_1erDepart = linecache.getline('.1erDepart_VSAV', 1)
            ifalone = 0
        else:
            vsav_1erDepart = '0'
        if os.path.isfile('.1erDepart_FPTSR'):
            fptsr_1erDepart = linecache.getline('.1erDepart_FPTSR', 1)
            ifalone = 0
        else:
            fptsr_1erDepart = '0'
        if os.path.isfile('.1erDepart_EPSA'):
            epsa_1erDepart = linecache.getline('.1erDepart_EPSA', 1)
            ifalone = 0
        else:
            epsa_1erDepart = '0'
        if os.path.isfile('.1erDepart_VL'):
            vl_1erDepart = linecache.getline('.1erDepart_VL', 1)
            ifalone = 0
        else:
            vl_1erDepart = '0'
        if os.path.isfile('.1erDepart_SMUR'):
            smur_1erDepart = linecache.getline('.1erDepart_SMUR', 1)
            ifalone = 0
        else:
            smur_1erDepart = '0'
        if os.path.isfile('.1erDepart_heliSMUR'):
            helismur_1erDepart = linecache.getline('.1erDepart_heliSMUR', 1)
            ifalone = 0
        else:
            helismur_1erDepart = '0'

        filesToDelete.append('.1erDepart_VSAV')
        filesToDelete.append('.1erDepart_FPTSR')
        filesToDelete.append('.1erDepart_EPSA')
        filesToDelete.append('.1erDepart_VL')
        filesToDelete.append('.1erDepart_SMUR')
        filesToDelete.append('.1erDepart_heliSMUR')

        vsav_1erDepart_txt = linecache.getline('.1erDepart_VSAV_txt', 1)
        fptsr_1erDepart_txt = linecache.getline('.1erDepart_FPTSR_txt', 1)
        epsa_1erDepart_txt = linecache.getline('.1erDepart_EPSA_txt', 1)
        vl_1erDepart_txt = linecache.getline('.1erDepart_VL_txt', 1)
        smur_1erDepart_txt = linecache.getline('.1erDepart_SMUR_txt', 1)
        helismur_1erDepart_txt = linecache.getline('.1erDepart_heliSMUR_txt', 1)

        filesToDelete.append('.1erDepart_VSAV_txt')
        filesToDelete.append('.1erDepart_FPTSR_txt')
        filesToDelete.append('.1erDepart_EPSA_txt')
        filesToDelete.append('.1erDepart_VL_txt')
        filesToDelete.append('.1erDepart_SMUR_txt')
        filesToDelete.append('.1erDepart_heliSMUR_txt')

        if os.path.isfile('.renfort_VSAV'):
            vsav_renfort = linecache.getline('.renfort_VSAV', 1)
            ifalone = 0
            filesToDelete.append('.renfort_VSAV')
        else:
            vsav_renfort = '0'
        if os.path.isfile('.renfort_FPTSR'):
            fptsr_renfort = linecache.getline('.renfort_FPTSR', 1)
            ifalone = 0
            filesToDelete.append('.renfort_FPTSR')
        else:
            fptsr_renfort = '0'
        if os.path.isfile('.renfort_EPSA'):
            epsa_renfort = linecache.getline('.renfort_EPSA', 1)
            ifalone = 0
            filesToDelete.append('.renfort_EPSA')
        else:
            epsa_renfort = '0'
        if os.path.isfile('.renfort_VL'):
            vl_renfort = linecache.getline('.renfort_VL', 1)
            filesToDelete.append('.renfort_VL')
            ifalone = 0
        else:
            vl_renfort = '0'
        if os.path.isfile('.renfort_SMUR'):
            smur_renfort = linecache.getline('.renfort_SMUR', 1)
            filesToDelete.append('.renfort_SMUR')
            ifalone = 0
        else:
            smur_renfort = '0'
        if os.path.isfile('.renfort_heliSMUR'):
            helismur_renfort = linecache.getline('.renfort_heliSMUR', 1)
            filesToDelete.append('.renfort_heliSMUR')
            ifalone = 0
        else:
            helismur_renfort = '0'

        vsav_renfort_txt = linecache.getline('.renfort_VSAV_txt', 1)
        fptsr_renfort_txt = linecache.getline('.renfort_FPTSR_txt', 1)
        epsa_renfort_txt = linecache.getline('.renfort_EPSA_txt', 1)
        vl_renfort_txt = linecache.getline('.renfort_VL_txt', 1)
        smur_renfort_txt = linecache.getline('.renfort_SMUR_txt', 1)
        helismur_renfort_txt = linecache.getline('.renfort_heliSMUR_txt', 1)

        filesToDelete.append('.renfort_VSAV_txt')
        filesToDelete.append('.renfort_FPTSR_txt')
        filesToDelete.append('.renfort_EPSA_txt')
        filesToDelete.append('.renfort_VL_txt')
        filesToDelete.append('.renfort_SMUR_txt')
        filesToDelete.append('.renfort_heliSMUR_txt')

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

        filesToDelete.append('.gendarmerie')
        filesToDelete.append('.edf')
        filesToDelete.append('.gdf')
        filesToDelete.append('.bridage_verte')
        filesToDelete.append('.service_eaux')

        rapport = linecache.getline('.rapport_txt', 1)

        filesToDelete.append('.rapport_txt')

        print("Ecriture du rapport en cours ...")

        type_rapport = "Intervention"


        ligne1 = type_rapport + ': ' + 'N° ' + str(nombre) + '  |  N° CODIS: ' + str(ncodis) + "\n"
        ligne2 = 'Date d\'appel: ' + str(heure_appel).rstrip('\n') + '\n' + '        Date de départ: ' + str(heure_depart).rstrip('\n') + '\n' + '        Date de retour: ' + str(heure_fin).rstrip('\n') + '\n' + '\n'#espaces mis ici pour la marge car on écrit la ligne qui  comporte des retour à la ligne
        ligne3_bis = "Véhicules: "
        ligne3 = ""#ligne3 sert à écrire les véhicules dans .dataInters.pglxdi et ne veut donc pas 'Véhicules'

        j=0
        for i in fptl:
            j += 1
            if i != 0:
                ligne3 += ' FPTL-' + str(j)
        j=0
        for i in vtu:
            j += 1
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa", 'i', i, 'vtu', vtu, 'r', r)
            if i != 0:
                ligne3 += ' VTU-' + str(j)
            if remorque[i-1] == 1:#i-1 car la boucle for i commence à i=1
                ligne3 += ' & remorque'
        j=0
        for i in vl:
            j += 1
            if i != 0:
                ligne3 += ' VL-' + str(j)


        ligne3 += "\n"
        ligne4 = 'Nature: ' + str(nature_inter).rstrip('\n') + "\n"
        ligne5 = 'Localisation: ' + str(loc_inter).rstrip('\n') + "\n"
        ligne6 = 'Demandeur: ' + str(demandeur_inter).rstrip('\n') + "\n"
        ligne7 = '>>Sapeur-Pompiers & Fonctions'


        linecache.clearcache()
        nb_ligne_rapport = fonctions.nombre_de_ligne('.rapport_txt')
        ligne_text = ""
        for i in range(0, nb_ligne_rapport + 1):
            ligne_text += linecache.getline('.rapport_txt', i)
            print('Rapport:', ligne_text)

        if spv_sll == False:
            ligne17 = ">>Pas de SPV SLL" + '\n'
        else:
            ligne17 = ">>SPV SLL:" + '\n'
            ligne18 = spv_sll
        print("SPV SLL:", ligne17)

        if spv_caserne != False:
            ligne21 = ">>SPV à la Caserne" + '\n'
            ligne22 = spv_caserne
            print(">>SPV CAS:", ligne21)
        else:
            ligne21 = "Pas de SPV à la Caserne" + '\n'

        #whitespace est défini plus haut car utilisé dans spv_cas et spv_sll


        os.chdir(path_to_vars)  # mène vers le répertoire des variables
        with open('0rapport', 'w') as fichier:
            fichier.write(whitespace)
            fichier.write(ligne1)
            fichier.write(whitespace)
            fichier.write(ligne2)
            fichier.write(whitespace)
            fichier.write(ligne3_bis)
            fichier.write(whitespace)
            fichier.write(ligne3)
            fichier.write("\n")
            fichier.write(whitespace)
            fichier.write(ligne4)
            fichier.write(whitespace)
            fichier.write(typeInter)
            fichier.write('\n')
            fichier.write(whitespace)
            fichier.write(ligne5)
            fichier.write(whitespace)
            fichier.write(ligne6)
            fichier.write("\n" + "\n")
            fichier.write(whitespace)
            fichier.write(ligne7)


            fichier.write('\n')
            equipage_vl = equipage_vl.split(";;")
            for i in equipage_vl:
                fichier.write(whitespace)
                fichier.write(i)
                fichier.write('\n')

            fichier.write('\n')
            equipage_vtu = equipage_vtu.split(";;")
            for i in equipage_vtu:
                fichier.write(whitespace)
                fichier.write(i)
                fichier.write('\n')

            fichier.write('\n')
            equipage_fptl = equipage_fptl.split(";;")
            for i in equipage_fptl:
                fichier.write(whitespace)
                fichier.write(i)
                fichier.write('\n')

            fichier.write('\n')

            fichier.write(whitespace)
            fichier.write(ligne17)

            if spv_sll != False:
                fichier.write(whitespace)
                fichier.write(str(ligne18))

            fichier.write('\n \n')
            fichier.write(whitespace)
            fichier.write(ligne21)
            if spv_caserne != False:
                fichier.write(whitespace)
                fichier.write(str(ligne22))

            fichier.write('\n \n')
            fichier.write(whitespace)
            fichier.write(">>Véhicules au 1e départ\n")

            data1erDepart = "" #pour rédiger le fichier data
            data1erDepartTxt = ""

            if (vsav_1erDepart[0] != '0') and (vsav_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("VSAV:" + vsav_1erDepart.rstrip('\n') + '  ' + vsav_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += vsav_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += vsav_1erDepart_txt.rstrip('\n') + ";;"
            if (fptsr_1erDepart[0] != '0') and (fptsr_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("FPTSR/FPT:" + fptsr_1erDepart.rstrip('\n') + '  ' + fptsr_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += fptsr_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += fptsr_1erDepart_txt.rstrip('\n') + ";;"
            if (epsa_1erDepart[0] != '0') and (epsa_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("EPSA/EPA:" + epsa_1erDepart.rstrip('\n') + '  ' + epsa_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += epsa_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += epsa_1erDepart_txt.rstrip('\n') + ";;"
            if (vl_1erDepart[0] != '0') and (vl_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("VL/VLI:" + vl_1erDepart.rstrip('\n') + '  ' + vl_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += vl_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += vl_1erDepart_txt.rstrip('\n') + ";;"
            if (smur_1erDepart[0] != '0') and (smur_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("SMUR:" + smur_1erDepart.rstrip('\n') + '  ' + smur_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += smur_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += smur_1erDepart_txt.rstrip('\n') + ";;"
            if (helismur_1erDepart[0] != '0') and (helismur_1erDepart != ""):
                fichier.write(whitespace)
                fichier.write("HéliSMUR:" + helismur_1erDepart.rstrip('\n') + '  ' + helismur_1erDepart_txt.rstrip('\n') + '\n')
                data1erDepart += helismur_1erDepart.rstrip('\n') + ";;"
                data1erDepartTxt += helismur_1erDepart_txt.rstrip('\n') + ";;"

            fichier.write('\n')
            fichier.write(whitespace)
            fichier.write(">>Véhicules en renfort\n")

            dataRenforts = ""
            dataRenfortsTxt = ""

            if (vsav_renfort[0] != '0') and (vsav_renfort != ""):
                fichier.write(whitespace)
                fichier.write("VSAV:" + vsav_renfort.rstrip('\n') + '  ' + vsav_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += vsav_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += vsav_renfort_txt.rstrip('\n') + ";;"
            if (fptsr_renfort[0] != '0') and (fptsr_renfort != ""):
                fichier.write(whitespace)
                fichier.write("FPTSR/FPT:" + fptsr_renfort.rstrip('\n') + '  ' + fptsr_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += fptsr_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += fptsr_renfort_txt.rstrip('\n') + ";;"
            if (epsa_renfort[0] != '0') and (epsa_renfort != ""):
                fichier.write(whitespace)
                fichier.write("EPSA/EPA:" + epsa_renfort.rstrip('\n') + '  ' + epsa_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += epsa_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += epsa_renfort_txt.rstrip('\n') + ";;"
            if (vl_renfort[0] != '0') and (vl_renfort != ""):
                fichier.write(whitespace)
                fichier.write("VL/VLI:" + vl_renfort.rstrip('\n') + '  ' + vl_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += vl_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += vl_renfort_txt.rstrip('\n') + ";;"
            if (smur_renfort[0] != '0') and (smur_renfort != ""):
                fichier.write(whitespace)
                fichier.write("SMUR:" + smur_renfort.rstrip('\n') + '  ' + smur_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += smur_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += smur_renfort_txt.rstrip('\n') + ";;"
            if (helismur_renfort[0] != '0') and (helismur_renfort != ""):
                fichier.write(whitespace)
                fichier.write("HéliSMUR:" + helismur_renfort.rstrip('\n') + '  ' + helismur_renfort_txt.rstrip('\n') + '\n')
                dataRenforts += helismur_renfort.rstrip('\n') + ";;"
                dataRenfortsTxt += helismur_renfort_txt.rstrip('\n') + ";;"

            fichier.write("\n \n")

            if gendarmerie != '0':
                fichier.write(whitespace)
                fichier.write("Gendarmerie SLL | ")
            if gdf != '0':
                fichier.write(whitespace)
                fichier.write("GRDF SLL | ")
            if service_eaux != '0':
                fichier.write(whitespace)
                fichier.write("Service des eaux SLL | ")
            if edf != '0':
                fichier.write(whitespace)
                fichier.write("ERDF SLL | ")
            if brigade_verte != '0':
                fichier.write(whitespace)
                fichier.write("Brigade Verte SLL | ")

            fichier.write('\n' + '\n')
            fichier.write(whitespace)
            fichier.write('>>Rapport de l\'intervention:' + '\n')
            fichier.write(whitespace)
            fichier.write(ligne_text)

            print("Rapport rédigé avec succès !")

            self_ui_inter.centralwidget.setEnabled(True)
            Ui_rapportInter.close()


            name = "Rapport-" + str(datetime.datetime.now())



            new_name = path_to_rinter + '/' + name

            subprocess.call(["mv", "0rapport", new_name])

            os.chdir(path_to_rinter)

            user = getpass.getuser()
            data = str(nombre).rstrip('\n') + ';;' + str(name).rstrip('\n') + ';;' + str(datetime.datetime.now()).rstrip('\n')\
                   + ';;' + str(heure_appel.rstrip('\n')) + ';;' + str(heure_depart.rstrip('\n')) + ';;' + \
                   str(heure_fin.rstrip('\n')) + ';;' + str(user).rstrip('\n') + ';;' + str(ifalone).rstrip('\n') + ";;" + \
                   nature_inter.rstrip('\n') + ";;" + ligne3.rstrip('\n') + ';;' + typeInter + ';;' + str(ncodis)
            if fonctions.file_exists(path_to_rinter, '.dataInters.pglxdi'):
                file = open(".dataInters.pglxdi", 'a')
                file.write('\n')
                file.write(data)
                file.close()
            else:
                file = open(".dataInters.pglxdi", 'a')
                file.write("#PGLX DATA I" + '\n' + "#version;;0.5" + '\n' + "nbInter;;name;;date;;callTime;;departureTime;;endTime;;user;;alone;;nature;;vehicles;;typeInter;;ncodis".rstrip('\n') + '\n')
                file.write(data)
                file.close()

            subprocess.call(["xdg-open", name])

            filesToDelete = ' '.join(filesToDelete)
            filesToDelete = filesToDelete.split()
            for i in filesToDelete:
                fileToDelete = path_to_vars + '/' + str(i)
                fonctions.delete_file(fileToDelete)

            #REDIGE UNE FICHIER DATA POUR CHAQUE INTERVENTION
            ligne1 = "inter;;ncodis}{" + str(nombre).rstrip('\n') + ";;" + str(ncodis).rstrip('\n')
            ligne2 = "dAppel;;dDepart;;dRetour}{" + heure_appel.rstrip('\n') + ";;" + heure_depart.rstrip('\n') + ";;" + heure_fin.rstrip('\n')
            ligne3 = "vehicules}{" + ";;".join((str(ligne3).rstrip('\n')).split())
            ligne4 = "nature}{" + str(nature_inter).rstrip('\n')
            ligne5 = "localisation}{" + str(loc_inter).rstrip('\n')
            ligne6 = "demandeur}{" + str(demandeur_inter).rstrip('\n')
            ligne7 = "typeInter}{" + str(typeInter)

            equipage_fptl = ((str(";;".join(equipage_fptl)).rstrip('\n')))
            equipage_vtu = ((str(";;".join(equipage_vtu)).rstrip('\n')))
            equipage_vl = ((str(";;".join(equipage_vl)).rstrip('\n')))

            ligne8 = "spv&fonctions}{" + equipage_fptl + "}{" + equipage_vtu + "}{" + equipage_vl
            if spv_sll != False:
                ligne9 = "spvSll}{" + ";;".join((str(spv_sll).rstrip('\n')).split())
            else:
                ligne9 = "spvSll}{"
            if spv_caserne != False:
                ligne10 = "spvCas}{" + ";;".join((str(spv_caserne).rstrip('\n')).split())
            else:
                ligne10 = "spvCas}{"
            ligne11 = "premDepart}{" + data1erDepart
            ligne112 = "premDepartTxt}{" + data1erDepartTxt
            ligne12 = "renfort}{" + dataRenforts
            ligne122 = "renfortTxt}{" + dataRenfortsTxt
            ligne13 = "gendarmerie;;GRDF;;ERDF;;brigadeVerte;;serviceDesEaux}{" + gendarmerie.rstrip('\n') + ';;' + gdf.rstrip('\n') + ";;" + edf.rstrip('\n') + ";;" + brigade_verte.rstrip('\n') + ';;' + service_eaux.rstrip('\n')
            ligne_text = ligne_text.split('\n')
            ligne_text = ";".join(ligne_text)#remplace les '\n' par ';'
            ligne14 = "rapport}{" + ligne_text.rstrip('\n')

            name = '.' + name + '.pglxdid' #pglxDataInterDetailed >> ;; sépare les éléments et }{ les groupes d'éléments des valeurs
            file = open(name, 'w')
            file.write("# PGLX DATA INTER" + '\n')
            file.write("#version;;0.5" + '\n')
            file.write(ligne1 + '\n')
            file.write(ligne2 + '\n')
            file.write(ligne3 + '\n')
            file.write(ligne4 + '\n')
            file.write(ligne5 + '\n')
            file.write(ligne6 + '\n')
            file.write(ligne7 + '\n')
            file.write(ligne8 + '\n')
            file.write(ligne9 + '\n')
            file.write(ligne10 + '\n')
            file.write(ligne11 + '\n')
            file.write(ligne112 + '\n')
            file.write(ligne12 + '\n')
            file.write(ligne122 + '\n')
            file.write(ligne13 + '\n')
            file.write(ligne14 + '\n')
            file.close()

            global PompierGLX
            PompierGLX.close()
            mySW = Ui_PompierGLX()
            mySW.show()

    def createOwnStats(name, nInter, date_depart, date_fin, ncodis, vehicule, typeInter, fonction):
        global path_to_stats_personnal, path_to_vars
        tmp1 = date_depart.split()
        tmp1 = tmp1[1].split(':')
        tmp1 = int(tmp1[0]) * 3600 + int(tmp1[1]) * 60

        tmp2 = date_fin.split()
        tmp2 = tmp2[1].split(':')
        tmp2 = int(tmp2[0]) * 3600 + int(tmp2[1]) * 60

        tmp3 = date_depart.split()
        tmp3 = tmp3[1].split('/')
        tmp4 = date_fin.split()
        tmp4 = tmp4[1].split('/')

        if tmp3[0] != tmp4[0]:#si les jours sont différents
            tmp1 -= 24 * 3600#soustraire 24 heures à temps de début | devient ainsi négatif et s'additionne à temp de fin

        duree = tmp2 - tmp1

        name = name.rstrip('\n')
        name = name.upper()

        os.chdir(path_to_stats_personnal)
        try:
            if os.path.isfile('.' + str(name)):
                fichier = open('.' + str(name), 'a')
            else:
                fichier = open('.' + str(name), 'w')
                fichier.write("#PGLX DATA : personnal stats for: " + str(name) + '\n')
                fichier.write('version;;0.5' + '\n')
                fichier.write("nbInter;;name;;date;;duree;;typeInter;;vehicule;;fonction;;ncodis" + '\n')

            fichier.write(str(nInter) + ';;' + str(name) + ';;' + str(date_depart).rstrip('\n') + ';;' +
                          str(duree).rstrip('\n') + ';;' + str(typeInter).rstrip('\n') + ';;' + str(vehicule).rstrip('\n') +
                          ';;' + str(fonction).rstrip('\n') + ';;' + str(ncodis).rstrip('\n') + '\n')
            fichier.close()
        except:
            print('error')

        os.chdir(path_to_vars)

    def delete_file(file_to_delete):
        subprocess.call(["rm", file_to_delete])


    def delete_all_file(path, *args):
        os.chdir(path)
        for i in args:
            subprocess.call(["rm", i])


    def nombre_de_ligne(fichier):  # fonction pour connaitre le nombre de ligne pour le fichier "fichier"
        global nb_ligne
        if os.path.isfile(fichier):
            liste = open(fichier, 'r')
            nb_ligne = 0
            ligne = "test_de_continuation"
            while ligne != "":
                ligne = liste.readline()
                nb_ligne += 1
                print("nbligne::", nb_ligne, "   ", ligne)
            liste.close()
            nb_ligne = nb_ligne - 1
            print('NB LIGNE a la fin de la fonction', nb_ligne)
        else:
            nb_ligne = 0
            print("PAS DE FICHIER !A")
        return nb_ligne

    def nombreDeLigne(path, fichier):
        #global nb_ligne
        os.chdir(path)
        if os.path.isfile(fichier):
            liste = open(fichier, 'r')
            nb_ligne = 0
            ligne = "test_de_continuation"
            while ligne != "":
                ligne = liste.readline()
                nb_ligne += 1
                print("nbligne::", nb_ligne, "   ", ligne)
            liste.close()
            nb_ligne = nb_ligne - 1
            print('NB LIGNE a la fin de la fonction', nb_ligne)
        else:
            nb_ligne = 0
            print("PAS DE FICHIER !A")
        return nb_ligne

    def nombreLigne(path, fichier):
        if fonctions.file_exists(path, fichier):
            os.chdir(path)
            liste = open(fichier, 'r')
            nb_ligne = 0
            j=0
            ligne = liste.readline()
            while j != 10:#si 10 lignes sont égales à ""
                nb_ligne += 1
                if ligne == "":
                    j += 1
                else:
                    j = 0
                ligne = liste.readline()
                print("nbligne::", nb_ligne, "   ", ligne)
            nb_ligne -= j
            print("Nombre de lignes:", nb_ligne)
        else:
            print(path, fichier, "n'est pas un fichier !")
            nb_ligne = 0

        return nb_ligne

    def copyto(sourcePath, destPath):#copie sourcePath vers destPath
        subprocess.call(["cp", "-R", sourcePath, destPath])

    def sendemail(fromaddr_, toaddr_, msgfrom, msgto, msgsubject, body_, server_, serverlogin):
        print("envoi de l'email encours ...")

        fromaddr = (fromaddr_)
        toaddr = (toaddr_)
        msg = MIMEMultipart()
        msg['From'] = msgfrom
        msg['To'] =  msgto
        msg['Subject'] = (msgsubject)

        body = (body_)
        msg.attach(MIMEText(body, ('plain')))

        import smptlib
        server = smptlib.SMPT(server_)
        server.login(serverlogin)
        text = msg.as_string()
        sender.sendmail(fromaddr, toaddr, text)

        print("email envoyé")

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
    fonctions.update_vars()
    mySW = Ui_PompierGLX()
    mySW.show()
    sys.exit(app.exec_())

"""
    Pompier-GLX 3.2.10 Beta
    Copyright (C) 2013-2014  Sydney Rodolphe Torcuato Gems

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
