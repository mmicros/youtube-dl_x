# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloader.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1022, 662)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self._urls = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"URL");
        self._urls.setHeaderItem(__qtreewidgetitem)
        self._urls.setObjectName(u"_urls")
        self._urls.setFrameShadow(QFrame.Plain)
        self._urls.setMidLineWidth(1)
        self._urls.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self._urls.setAlternatingRowColors(True)
        self._urls.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._urls.setWordWrap(True)
        self._urls.setColumnCount(2)
        self._urls.header().setVisible(True)

        self.gridLayout.addWidget(self._urls, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self._btnChooseFile = QPushButton(self.widget)
        self._btnChooseFile.setObjectName(u"_btnChooseFile")

        self.gridLayout_2.addWidget(self._btnChooseFile, 0, 0, 1, 1)

        self._btnDownload = QPushButton(self.widget)
        self._btnDownload.setObjectName(u"_btnDownload")

        self.gridLayout_2.addWidget(self._btnDownload, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 4, 1)

        self._prBar = QProgressBar(self.centralwidget)
        self._prBar.setObjectName(u"_prBar")
        self._prBar.setValue(0)

        self.gridLayout.addWidget(self._prBar, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self._lbProg = QLabel(self.centralwidget)
        self._lbProg.setObjectName(u"_lbProg")

        self.horizontalLayout.addWidget(self._lbProg)

        self._lbUpdate = QLabel(self.centralwidget)
        self._lbUpdate.setObjectName(u"_lbUpdate")

        self.horizontalLayout.addWidget(self._lbUpdate)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        main.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Youtube-dl Audio Downloader", None))
        ___qtreewidgetitem = self._urls.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("main", u"Title/Artist", None));
        self._btnChooseFile.setText(QCoreApplication.translate("main", u"Import Bookmark File", None))
        self._btnDownload.setText(QCoreApplication.translate("main", u"Download", None))
        self._lbProg.setText(QCoreApplication.translate("main", u"Progress: ", None))
        self._lbUpdate.setText("")
    # retranslateUi

