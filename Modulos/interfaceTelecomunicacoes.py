# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceTelecomunicacoes.ui'
#
# Created: Tue May 27 15:40:06 2014
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1010, 660)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineSearch = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSearch.sizePolicy().hasHeightForWidth())
        self.lineSearch.setSizePolicy(sizePolicy)
        self.lineSearch.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineSearch.setObjectName("lineSearch")
        self.gridLayout_3.addWidget(self.lineSearch, 0, 0, 1, 1)
        self.buttonPesquisar = QtGui.QPushButton(self.centralwidget)
        self.buttonPesquisar.setMaximumSize(QtCore.QSize(180, 27))
        self.buttonPesquisar.setObjectName("buttonPesquisar")
        self.gridLayout_3.addWidget(self.buttonPesquisar, 0, 1, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 2, 5, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(420, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 5, 1, 1)
        self.listPossibles = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listPossibles.sizePolicy().hasHeightForWidth())
        self.listPossibles.setSizePolicy(sizePolicy)
        self.listPossibles.setMaximumSize(QtCore.QSize(415, 25))
        self.listPossibles.setObjectName("listPossibles")
        self.gridLayout_3.addWidget(self.listPossibles, 1, 0, 1, 2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabAbordagem = QtGui.QWidget()
        self.tabAbordagem.setObjectName("tabAbordagem")
        self.gridLayout_2 = QtGui.QGridLayout(self.tabAbordagem)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textAbordagem = QtGui.QTextBrowser(self.tabAbordagem)
        self.textAbordagem.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textAbordagem.setFrameShadow(QtGui.QFrame.Plain)
        self.textAbordagem.setOpenExternalLinks(True)
        self.textAbordagem.setObjectName("textAbordagem")
        self.gridLayout_2.addWidget(self.textAbordagem, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabAbordagem, "")
        self.tabVideoAula = QtGui.QWidget()
        self.tabVideoAula.setObjectName("tabVideoAula")
        self.gridLayout_5 = QtGui.QGridLayout(self.tabVideoAula)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.tabVideoAula)
        self.videoPlayer.setObjectName("videoPlayer")
        self.verticalLayout_4.addWidget(self.videoPlayer)
        self.seekSlider = phonon.Phonon.SeekSlider(self.tabVideoAula)
        self.seekSlider.setObjectName("seekSlider")
        self.verticalLayout_4.addWidget(self.seekSlider)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.tabVideoAula)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.tabVideoAula)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_4.addWidget(self.volumeSlider)
        self.buttonReproduzir = QtGui.QPushButton(self.tabVideoAula)
        self.buttonReproduzir.setObjectName("buttonReproduzir")
        self.horizontalLayout_4.addWidget(self.buttonReproduzir)
        self.buttonPausar = QtGui.QPushButton(self.tabVideoAula)
        self.buttonPausar.setObjectName("buttonPausar")
        self.horizontalLayout_4.addWidget(self.buttonPausar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_5.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabVideoAula, "")
        self.tabSimulacao = QtGui.QWidget()
        self.tabSimulacao.setObjectName("tabSimulacao")
        self.gridLayout_4 = QtGui.QGridLayout(self.tabSimulacao)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textExplicacao = QtGui.QTextBrowser(self.tabSimulacao)
        self.textExplicacao.setObjectName("textExplicacao")
        self.verticalLayout.addWidget(self.textExplicacao)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonSimular = QtGui.QPushButton(self.tabSimulacao)
        self.buttonSimular.setObjectName("buttonSimular")
        self.horizontalLayout_2.addWidget(self.buttonSimular)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabSimulacao, "")
        self.tabExercicios = QtGui.QWidget()
        self.tabExercicios.setObjectName("tabExercicios")
        self.gridLayout_7 = QtGui.QGridLayout(self.tabExercicios)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textExercicio = QtGui.QTextBrowser(self.tabExercicios)
        self.textExercicio.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textExercicio.setFrameShadow(QtGui.QFrame.Plain)
        self.textExercicio.setOpenExternalLinks(True)
        self.textExercicio.setObjectName("textExercicio")
        self.gridLayout_7.addWidget(self.textExercicio, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabExercicios, "")
        self.tabReferencias = QtGui.QWidget()
        self.tabReferencias.setObjectName("tabReferencias")
        self.gridLayout_6 = QtGui.QGridLayout(self.tabReferencias)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.textReferencias = QtGui.QTextBrowser(self.tabReferencias)
        self.textReferencias.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textReferencias.setFrameShadow(QtGui.QFrame.Plain)
        self.textReferencias.setOpenExternalLinks(True)
        self.textReferencias.setObjectName("textReferencias")
        self.gridLayout_6.addWidget(self.textReferencias, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabReferencias, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setObjectName("formLayout")
        self.radioNavegador = QtGui.QRadioButton(self.tab)
        self.radioNavegador.setObjectName("radioNavegador")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.radioNavegador)
        self.radioAudacity = QtGui.QRadioButton(self.tab)
        self.radioAudacity.setObjectName("radioAudacity")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.radioAudacity)
        self.radioGedit = QtGui.QRadioButton(self.tab)
        self.radioGedit.setObjectName("radioGedit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.radioGedit)
        self.radioGnu = QtGui.QRadioButton(self.tab)
        self.radioGnu.setObjectName("radioGnu")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioGnu)
        self.buttonAbrir = QtGui.QPushButton(self.tab)
        self.buttonAbrir.setObjectName("buttonAbrir")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.buttonAbrir)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 3, 4, 3)
        self.checkEdicao = QtGui.QCheckBox(self.centralwidget)
        self.checkEdicao.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkEdicao.setTristate(False)
        self.checkEdicao.setObjectName("checkEdicao")
        self.gridLayout_3.addWidget(self.checkEdicao, 3, 0, 1, 2)
        self.widgetEditarArvore = QtGui.QFrame(self.centralwidget)
        self.widgetEditarArvore.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetEditarArvore.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetEditarArvore.setObjectName("widgetEditarArvore")
        self.gridLayout = QtGui.QGridLayout(self.widgetEditarArvore)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelEditarArvore = QtGui.QLabel(self.widgetEditarArvore)
        self.labelEditarArvore.setMinimumSize(QtCore.QSize(170, 0))
        self.labelEditarArvore.setMaximumSize(QtCore.QSize(175, 16777215))
        self.labelEditarArvore.setObjectName("labelEditarArvore")
        self.horizontalLayout_3.addWidget(self.labelEditarArvore)
        self.lineAdicionar = QtGui.QLineEdit(self.widgetEditarArvore)
        self.lineAdicionar.setEnabled(True)
        self.lineAdicionar.setMinimumSize(QtCore.QSize(190, 0))
        self.lineAdicionar.setMaximumSize(QtCore.QSize(370, 16777215))
        self.lineAdicionar.setObjectName("lineAdicionar")
        self.horizontalLayout_3.addWidget(self.lineAdicionar)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAdicionar = QtGui.QPushButton(self.widgetEditarArvore)
        self.buttonAdicionar.setEnabled(True)
        self.buttonAdicionar.setMinimumSize(QtCore.QSize(110, 0))
        self.buttonAdicionar.setObjectName("buttonAdicionar")
        self.horizontalLayout.addWidget(self.buttonAdicionar)
        self.buttonDeletar = QtGui.QPushButton(self.widgetEditarArvore)
        self.buttonDeletar.setEnabled(True)
        self.buttonDeletar.setMinimumSize(QtCore.QSize(110, 0))
        self.buttonDeletar.setObjectName("buttonDeletar")
        self.horizontalLayout.addWidget(self.buttonDeletar)
        self.buttonSalvar = QtGui.QPushButton(self.widgetEditarArvore)
        self.buttonSalvar.setEnabled(True)
        self.buttonSalvar.setMinimumSize(QtCore.QSize(110, 0))
        self.buttonSalvar.setMaximumSize(QtCore.QSize(145, 27))
        self.buttonSalvar.setObjectName("buttonSalvar")
        self.horizontalLayout.addWidget(self.buttonSalvar)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widgetEditarArvore, 4, 0, 1, 2)
        self.treeAssuntos = QtGui.QTreeWidget(self.centralwidget)
        self.treeAssuntos.setMaximumSize(QtCore.QSize(415, 16777215))
        self.treeAssuntos.setAnimated(True)
        self.treeAssuntos.setObjectName("treeAssuntos")
        self.treeAssuntos.headerItem().setText(0, "1")
        self.gridLayout_3.addWidget(self.treeAssuntos, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 23))
        self.menubar.setObjectName("menubar")
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionSobre_Qt = QtGui.QAction(MainWindow)
        self.actionSobre_Qt.setObjectName("actionSobre_Qt")
        self.menuSobre.addAction(self.actionSobre)
        self.menuSobre.addAction(self.actionSobre_Qt)
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SATEC - Sistema de Aprendizagem de Telecomunicações", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPesquisar.setText(QtGui.QApplication.translate("MainWindow", "&Pesquisar assunto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Relógio:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textAbordagem.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Seja bem vindo ao Sistema de Aprendizagem.<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"> Por favor utilize o manual para verificar como se utiliza o programa.<br /><br />Bom estudo !<br /><br /></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbordagem), QtGui.QApplication.translate("MainWindow", "Aborgadem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Volume:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonReproduzir.setText(QtGui.QApplication.translate("MainWindow", "Reproduzir", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonPausar.setText(QtGui.QApplication.translate("MainWindow", "Pausar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVideoAula), QtGui.QApplication.translate("MainWindow", "Vídeo-Aula", None, QtGui.QApplication.UnicodeUTF8))
        self.textExplicacao.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Texto sobre explicação da simulação atual.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"><br /></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSimular.setText(QtGui.QApplication.translate("MainWindow", "&Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSimulacao), QtGui.QApplication.translate("MainWindow", "Simulação", None, QtGui.QApplication.UnicodeUTF8))
        self.textExercicio.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Texto sobre os exercícios do assunto atual.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"><br /></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExercicios), QtGui.QApplication.translate("MainWindow", "Exercícios", None, QtGui.QApplication.UnicodeUTF8))
        self.textReferencias.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\">Texto sobre as referências do assunto atual.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:9pt;\"><br /></span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReferencias), QtGui.QApplication.translate("MainWindow", "Referências", None, QtGui.QApplication.UnicodeUTF8))
        self.radioNavegador.setText(QtGui.QApplication.translate("MainWindow", "Navegador", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAudacity.setText(QtGui.QApplication.translate("MainWindow", "Audacity", None, QtGui.QApplication.UnicodeUTF8))
        self.radioGedit.setText(QtGui.QApplication.translate("MainWindow", "Gedit", None, QtGui.QApplication.UnicodeUTF8))
        self.radioGnu.setText(QtGui.QApplication.translate("MainWindow", "GNU Radio", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAbrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Programas Externos", None, QtGui.QApplication.UnicodeUTF8))
        self.checkEdicao.setText(QtGui.QApplication.translate("MainWindow", "Modo de edição - Árvore de assuntos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEditarArvore.setText(QtGui.QApplication.translate("MainWindow", "Assunto a ser adicionado:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAdicionar.setText(QtGui.QApplication.translate("MainWindow", "&Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeletar.setText(QtGui.QApplication.translate("MainWindow", "&Deletar ", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSalvar.setText(QtGui.QApplication.translate("MainWindow", "&Salvar Árvore", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSobre.setTitle(QtGui.QApplication.translate("MainWindow", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre.setText(QtGui.QApplication.translate("MainWindow", "Sobre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre_Qt.setText(QtGui.QApplication.translate("MainWindow", "Sobre Qt", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import phonon
