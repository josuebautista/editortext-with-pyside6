# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon = QIcon()
        icon.addFile(u":/prefijoNuevo/images/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon1 = QIcon()
        icon1.addFile(u":/prefijoNuevo/images/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon2 = QIcon()
        icon2.addFile(u":/prefijoNuevo/images/cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon2)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon3 = QIcon()
        icon3.addFile(u":/prefijoNuevo/images/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon3)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon4 = QIcon()
        icon4.addFile(u":/prefijoNuevo/images/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon5 = QIcon()
        icon5.addFile(u":/prefijoNuevo/images/redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon6 = QIcon()
        iconThemeName = u"accessories-character-map"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u":/prefijoNuevo/images/about.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionAbout.setIcon(icon6)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon7 = QIcon()
        icon7.addFile(u":/prefijoNuevo/images/about2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAboutQt.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFIle.addAction(self.actionQuit)
        self.menuFIle.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"AboutQt", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

