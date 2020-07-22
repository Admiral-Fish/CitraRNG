# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from pokemon_display import PokemonDisplay


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 640)
        MainWindow.setMinimumSize(QSize(770, 640))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBoxConnection = QGroupBox(self.centralwidget)
        self.groupBoxConnection.setObjectName(u"groupBoxConnection")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBoxConnection.sizePolicy().hasHeightForWidth())
        self.groupBoxConnection.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.groupBoxConnection)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButtonConnect = QPushButton(self.groupBoxConnection)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonConnect.sizePolicy().hasHeightForWidth())
        self.pushButtonConnect.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButtonConnect, 0, 1, 1, 1)

        self.labelUpdateDelay = QLabel(self.groupBoxConnection)
        self.labelUpdateDelay.setObjectName(u"labelUpdateDelay")

        self.gridLayout_2.addWidget(self.labelUpdateDelay, 1, 0, 1, 1)

        self.labelStatus = QLabel(self.groupBoxConnection)
        self.labelStatus.setObjectName(u"labelStatus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelStatus.sizePolicy().hasHeightForWidth())
        self.labelStatus.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.labelStatus, 1, 2, 1, 1)

        self.comboBoxGameSelection = QComboBox(self.groupBoxConnection)
        self.comboBoxGameSelection.addItem("")
        self.comboBoxGameSelection.addItem("")
        self.comboBoxGameSelection.addItem("")
        self.comboBoxGameSelection.addItem("")
        self.comboBoxGameSelection.setObjectName(u"comboBoxGameSelection")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxGameSelection.sizePolicy().hasHeightForWidth())
        self.comboBoxGameSelection.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.comboBoxGameSelection, 0, 0, 1, 1)

        self.doubleSpinBoxDelay = QDoubleSpinBox(self.groupBoxConnection)
        self.doubleSpinBoxDelay.setObjectName(u"doubleSpinBoxDelay")
        self.doubleSpinBoxDelay.setEnabled(False)
        self.doubleSpinBoxDelay.setMinimum(0.500000000000000)
        self.doubleSpinBoxDelay.setMaximum(2.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBoxDelay, 1, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBoxConnection, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(5)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabGen6 = QWidget()
        self.tabGen6.setObjectName(u"tabGen6")
        self.gridLayout = QGridLayout(self.tabGen6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidgetGen6 = QTabWidget(self.tabGen6)
        self.tabWidgetGen6.setObjectName(u"tabWidgetGen6")
        self.tabMain6 = QWidget()
        self.tabMain6.setObjectName(u"tabMain6")
        self.gridLayout_13 = QGridLayout(self.tabMain6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.comboBoxMainIndex6 = QComboBox(self.tabMain6)
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.addItem("")
        self.comboBoxMainIndex6.setObjectName(u"comboBoxMainIndex6")
        self.comboBoxMainIndex6.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.comboBoxMainIndex6.sizePolicy().hasHeightForWidth())
        self.comboBoxMainIndex6.setSizePolicy(sizePolicy3)

        self.gridLayout_13.addWidget(self.comboBoxMainIndex6, 0, 0, 1, 1)

        self.groupBoxMainRNG6 = QGroupBox(self.tabMain6)
        self.groupBoxMainRNG6.setObjectName(u"groupBoxMainRNG6")
        sizePolicy2.setHeightForWidth(self.groupBoxMainRNG6.sizePolicy().hasHeightForWidth())
        self.groupBoxMainRNG6.setSizePolicy(sizePolicy2)
        self.gridLayout_11 = QGridLayout(self.groupBoxMainRNG6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineEditFrame6 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditFrame6.setObjectName(u"lineEditFrame6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEditFrame6.sizePolicy().hasHeightForWidth())
        self.lineEditFrame6.setSizePolicy(sizePolicy5)
        self.lineEditFrame6.setReadOnly(True)

        self.gridLayout_11.addWidget(self.lineEditFrame6, 3, 2, 1, 2)

        self.labelTiny2 = QLabel(self.groupBoxMainRNG6)
        self.labelTiny2.setObjectName(u"labelTiny2")

        self.gridLayout_11.addWidget(self.labelTiny2, 5, 2, 1, 1)

        self.labelTiny0 = QLabel(self.groupBoxMainRNG6)
        self.labelTiny0.setObjectName(u"labelTiny0")

        self.gridLayout_11.addWidget(self.labelTiny0, 6, 2, 1, 1)

        self.lineEditInitialSeed6 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditInitialSeed6.setObjectName(u"lineEditInitialSeed6")
        sizePolicy5.setHeightForWidth(self.lineEditInitialSeed6.sizePolicy().hasHeightForWidth())
        self.lineEditInitialSeed6.setSizePolicy(sizePolicy5)
        self.lineEditInitialSeed6.setMaxLength(8)
        self.lineEditInitialSeed6.setReadOnly(True)

        self.gridLayout_11.addWidget(self.lineEditInitialSeed6, 1, 2, 1, 2)

        self.labelTiny3 = QLabel(self.groupBoxMainRNG6)
        self.labelTiny3.setObjectName(u"labelTiny3")

        self.gridLayout_11.addWidget(self.labelTiny3, 5, 0, 1, 1)

        self.labelTiny1 = QLabel(self.groupBoxMainRNG6)
        self.labelTiny1.setObjectName(u"labelTiny1")

        self.gridLayout_11.addWidget(self.labelTiny1, 6, 0, 1, 1)

        self.labelMainCurrentSeed6 = QLabel(self.groupBoxMainRNG6)
        self.labelMainCurrentSeed6.setObjectName(u"labelMainCurrentSeed6")

        self.gridLayout_11.addWidget(self.labelMainCurrentSeed6, 2, 0, 1, 2)

        self.lineEditCurrentSeed6 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditCurrentSeed6.setObjectName(u"lineEditCurrentSeed6")
        sizePolicy5.setHeightForWidth(self.lineEditCurrentSeed6.sizePolicy().hasHeightForWidth())
        self.lineEditCurrentSeed6.setSizePolicy(sizePolicy5)
        self.lineEditCurrentSeed6.setMaxLength(16)
        self.lineEditCurrentSeed6.setReadOnly(True)

        self.gridLayout_11.addWidget(self.lineEditCurrentSeed6, 2, 2, 1, 2)

        self.lineEditTiny2 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditTiny2.setObjectName(u"lineEditTiny2")

        self.gridLayout_11.addWidget(self.lineEditTiny2, 5, 3, 1, 1)

        self.lineEditTiny1 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditTiny1.setObjectName(u"lineEditTiny1")

        self.gridLayout_11.addWidget(self.lineEditTiny1, 6, 1, 1, 1)

        self.lineEditTiny3 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditTiny3.setObjectName(u"lineEditTiny3")

        self.gridLayout_11.addWidget(self.lineEditTiny3, 5, 1, 1, 1)

        self.labelMainInitialSeed6 = QLabel(self.groupBoxMainRNG6)
        self.labelMainInitialSeed6.setObjectName(u"labelMainInitialSeed6")

        self.gridLayout_11.addWidget(self.labelMainInitialSeed6, 1, 0, 1, 2)

        self.labelMainFrame6 = QLabel(self.groupBoxMainRNG6)
        self.labelMainFrame6.setObjectName(u"labelMainFrame6")

        self.gridLayout_11.addWidget(self.labelMainFrame6, 3, 0, 1, 1)

        self.lineEditTiny0 = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditTiny0.setObjectName(u"lineEditTiny0")

        self.gridLayout_11.addWidget(self.lineEditTiny0, 6, 3, 1, 1)

        self.pushButtonMainUpdate6 = QPushButton(self.groupBoxMainRNG6)
        self.pushButtonMainUpdate6.setObjectName(u"pushButtonMainUpdate6")
        self.pushButtonMainUpdate6.setEnabled(False)

        self.gridLayout_11.addWidget(self.pushButtonMainUpdate6, 0, 0, 1, 4)

        self.labelSaveVariable = QLabel(self.groupBoxMainRNG6)
        self.labelSaveVariable.setObjectName(u"labelSaveVariable")

        self.gridLayout_11.addWidget(self.labelSaveVariable, 4, 0, 1, 1)

        self.lineEditSaveVariable = QLineEdit(self.groupBoxMainRNG6)
        self.lineEditSaveVariable.setObjectName(u"lineEditSaveVariable")
        self.lineEditSaveVariable.setReadOnly(True)

        self.gridLayout_11.addWidget(self.lineEditSaveVariable, 4, 2, 1, 2)


        self.gridLayout_13.addWidget(self.groupBoxMainRNG6, 0, 1, 2, 1)

        self.mainPokemon6 = PokemonDisplay(self.tabMain6)
        self.mainPokemon6.setObjectName(u"mainPokemon6")
        sizePolicy2.setHeightForWidth(self.mainPokemon6.sizePolicy().hasHeightForWidth())
        self.mainPokemon6.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.mainPokemon6, 1, 0, 1, 1)

        self.tabWidgetGen6.addTab(self.tabMain6, "")
        self.tabEgg6 = QWidget()
        self.tabEgg6.setObjectName(u"tabEgg6")
        self.gridLayout_15 = QGridLayout(self.tabEgg6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.eggParent1_6 = PokemonDisplay(self.tabEgg6)
        self.eggParent1_6.setObjectName(u"eggParent1_6")
        sizePolicy2.setHeightForWidth(self.eggParent1_6.sizePolicy().hasHeightForWidth())
        self.eggParent1_6.setSizePolicy(sizePolicy2)

        self.gridLayout_15.addWidget(self.eggParent1_6, 0, 0, 1, 1)

        self.eggParent2_6 = PokemonDisplay(self.tabEgg6)
        self.eggParent2_6.setObjectName(u"eggParent2_6")
        sizePolicy2.setHeightForWidth(self.eggParent2_6.sizePolicy().hasHeightForWidth())
        self.eggParent2_6.setSizePolicy(sizePolicy2)

        self.gridLayout_15.addWidget(self.eggParent2_6, 0, 1, 1, 1)

        self.groupBoxEggRNG6 = QGroupBox(self.tabEgg6)
        self.groupBoxEggRNG6.setObjectName(u"groupBoxEggRNG6")
        sizePolicy2.setHeightForWidth(self.groupBoxEggRNG6.sizePolicy().hasHeightForWidth())
        self.groupBoxEggRNG6.setSizePolicy(sizePolicy2)
        self.gridLayout_14 = QGridLayout(self.groupBoxEggRNG6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.labelEggReady6 = QLabel(self.groupBoxEggRNG6)
        self.labelEggReady6.setObjectName(u"labelEggReady6")
        sizePolicy5.setHeightForWidth(self.labelEggReady6.sizePolicy().hasHeightForWidth())
        self.labelEggReady6.setSizePolicy(sizePolicy5)

        self.gridLayout_14.addWidget(self.labelEggReady6, 1, 0, 1, 1)

        self.labelEggReadyStatus6 = QLabel(self.groupBoxEggRNG6)
        self.labelEggReadyStatus6.setObjectName(u"labelEggReadyStatus6")

        self.gridLayout_14.addWidget(self.labelEggReadyStatus6, 1, 1, 1, 1)

        self.lineEditEggSeed0_6 = QLineEdit(self.groupBoxEggRNG6)
        self.lineEditEggSeed0_6.setObjectName(u"lineEditEggSeed0_6")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed0_6.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed0_6.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed0_6.setMaxLength(8)
        self.lineEditEggSeed0_6.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditEggSeed0_6, 3, 1, 1, 1)

        self.pushButtonEggUpdate6 = QPushButton(self.groupBoxEggRNG6)
        self.pushButtonEggUpdate6.setObjectName(u"pushButtonEggUpdate6")
        self.pushButtonEggUpdate6.setEnabled(False)

        self.gridLayout_14.addWidget(self.pushButtonEggUpdate6, 0, 0, 1, 2)

        self.labelEggSeed0_6 = QLabel(self.groupBoxEggRNG6)
        self.labelEggSeed0_6.setObjectName(u"labelEggSeed0_6")

        self.gridLayout_14.addWidget(self.labelEggSeed0_6, 3, 0, 1, 1)

        self.labelEggSeed1_6 = QLabel(self.groupBoxEggRNG6)
        self.labelEggSeed1_6.setObjectName(u"labelEggSeed1_6")

        self.gridLayout_14.addWidget(self.labelEggSeed1_6, 2, 0, 1, 1)

        self.lineEditEggSeed1_6 = QLineEdit(self.groupBoxEggRNG6)
        self.lineEditEggSeed1_6.setObjectName(u"lineEditEggSeed1_6")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed1_6.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed1_6.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed1_6.setMaxLength(8)
        self.lineEditEggSeed1_6.setReadOnly(True)

        self.gridLayout_14.addWidget(self.lineEditEggSeed1_6, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.groupBoxEggRNG6, 0, 2, 1, 1)

        self.tabWidgetGen6.addTab(self.tabEgg6, "")

        self.gridLayout.addWidget(self.tabWidgetGen6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabGen6, "")
        self.tabGen7 = QWidget()
        self.tabGen7.setObjectName(u"tabGen7")
        self.tabGen7.setEnabled(False)
        self.gridLayout_12 = QGridLayout(self.tabGen7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidgetGen7 = QTabWidget(self.tabGen7)
        self.tabWidgetGen7.setObjectName(u"tabWidgetGen7")
        self.tabMain7 = QWidget()
        self.tabMain7.setObjectName(u"tabMain7")
        self.gridLayout_7 = QGridLayout(self.tabMain7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.comboBoxMainIndex7 = QComboBox(self.tabMain7)
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.addItem("")
        self.comboBoxMainIndex7.setObjectName(u"comboBoxMainIndex7")
        self.comboBoxMainIndex7.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.comboBoxMainIndex7.sizePolicy().hasHeightForWidth())
        self.comboBoxMainIndex7.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.comboBoxMainIndex7, 0, 0, 1, 1)

        self.groupBoxMainRNG7 = QGroupBox(self.tabMain7)
        self.groupBoxMainRNG7.setObjectName(u"groupBoxMainRNG7")
        sizePolicy2.setHeightForWidth(self.groupBoxMainRNG7.sizePolicy().hasHeightForWidth())
        self.groupBoxMainRNG7.setSizePolicy(sizePolicy2)
        self.gridLayout_3 = QGridLayout(self.groupBoxMainRNG7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelMainInitialSeed7 = QLabel(self.groupBoxMainRNG7)
        self.labelMainInitialSeed7.setObjectName(u"labelMainInitialSeed7")

        self.gridLayout_3.addWidget(self.labelMainInitialSeed7, 1, 0, 1, 1)

        self.lineEditInitialSeed7 = QLineEdit(self.groupBoxMainRNG7)
        self.lineEditInitialSeed7.setObjectName(u"lineEditInitialSeed7")
        sizePolicy5.setHeightForWidth(self.lineEditInitialSeed7.sizePolicy().hasHeightForWidth())
        self.lineEditInitialSeed7.setSizePolicy(sizePolicy5)
        self.lineEditInitialSeed7.setMaxLength(8)
        self.lineEditInitialSeed7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditInitialSeed7, 1, 1, 1, 1)

        self.labelMainCurrentSeed7 = QLabel(self.groupBoxMainRNG7)
        self.labelMainCurrentSeed7.setObjectName(u"labelMainCurrentSeed7")

        self.gridLayout_3.addWidget(self.labelMainCurrentSeed7, 2, 0, 1, 1)

        self.lineEditCurrentSeed7 = QLineEdit(self.groupBoxMainRNG7)
        self.lineEditCurrentSeed7.setObjectName(u"lineEditCurrentSeed7")
        sizePolicy5.setHeightForWidth(self.lineEditCurrentSeed7.sizePolicy().hasHeightForWidth())
        self.lineEditCurrentSeed7.setSizePolicy(sizePolicy5)
        self.lineEditCurrentSeed7.setMaxLength(16)
        self.lineEditCurrentSeed7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditCurrentSeed7, 2, 1, 1, 1)

        self.labelMainFrame7 = QLabel(self.groupBoxMainRNG7)
        self.labelMainFrame7.setObjectName(u"labelMainFrame7")

        self.gridLayout_3.addWidget(self.labelMainFrame7, 3, 0, 1, 1)

        self.lineEditFrame7 = QLineEdit(self.groupBoxMainRNG7)
        self.lineEditFrame7.setObjectName(u"lineEditFrame7")
        sizePolicy5.setHeightForWidth(self.lineEditFrame7.sizePolicy().hasHeightForWidth())
        self.lineEditFrame7.setSizePolicy(sizePolicy5)
        self.lineEditFrame7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditFrame7, 3, 1, 1, 1)

        self.pushButtonMainUpdate7 = QPushButton(self.groupBoxMainRNG7)
        self.pushButtonMainUpdate7.setObjectName(u"pushButtonMainUpdate7")
        self.pushButtonMainUpdate7.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButtonMainUpdate7, 0, 0, 1, 2)


        self.gridLayout_7.addWidget(self.groupBoxMainRNG7, 0, 1, 2, 1)

        self.mainPokemon7 = PokemonDisplay(self.tabMain7)
        self.mainPokemon7.setObjectName(u"mainPokemon7")
        sizePolicy2.setHeightForWidth(self.mainPokemon7.sizePolicy().hasHeightForWidth())
        self.mainPokemon7.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.mainPokemon7, 1, 0, 1, 1)

        self.tabWidgetGen7.addTab(self.tabMain7, "")
        self.tabEgg7 = QWidget()
        self.tabEgg7.setObjectName(u"tabEgg7")
        self.gridLayout_6 = QGridLayout(self.tabEgg7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBoxEggRNG7 = QGroupBox(self.tabEgg7)
        self.groupBoxEggRNG7.setObjectName(u"groupBoxEggRNG7")
        sizePolicy2.setHeightForWidth(self.groupBoxEggRNG7.sizePolicy().hasHeightForWidth())
        self.groupBoxEggRNG7.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.groupBoxEggRNG7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButtonEggUpdate7 = QPushButton(self.groupBoxEggRNG7)
        self.pushButtonEggUpdate7.setObjectName(u"pushButtonEggUpdate7")
        self.pushButtonEggUpdate7.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButtonEggUpdate7, 0, 0, 1, 2)

        self.labelEggReady7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggReady7.setObjectName(u"labelEggReady7")
        sizePolicy5.setHeightForWidth(self.labelEggReady7.sizePolicy().hasHeightForWidth())
        self.labelEggReady7.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.labelEggReady7, 1, 0, 1, 1)

        self.labelEggReadyStatus7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggReadyStatus7.setObjectName(u"labelEggReadyStatus7")

        self.gridLayout_4.addWidget(self.labelEggReadyStatus7, 1, 1, 1, 1)

        self.labelEggSeed3_7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggSeed3_7.setObjectName(u"labelEggSeed3_7")

        self.gridLayout_4.addWidget(self.labelEggSeed3_7, 2, 0, 1, 1)

        self.lineEditEggSeed3_7 = QLineEdit(self.groupBoxEggRNG7)
        self.lineEditEggSeed3_7.setObjectName(u"lineEditEggSeed3_7")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed3_7.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed3_7.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed3_7.setMaxLength(8)
        self.lineEditEggSeed3_7.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditEggSeed3_7, 2, 1, 1, 1)

        self.labelEggSeed2_7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggSeed2_7.setObjectName(u"labelEggSeed2_7")

        self.gridLayout_4.addWidget(self.labelEggSeed2_7, 3, 0, 1, 1)

        self.lineEditEggSeed2_7 = QLineEdit(self.groupBoxEggRNG7)
        self.lineEditEggSeed2_7.setObjectName(u"lineEditEggSeed2_7")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed2_7.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed2_7.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed2_7.setMaxLength(8)
        self.lineEditEggSeed2_7.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditEggSeed2_7, 3, 1, 1, 1)

        self.labelEggSeed1_7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggSeed1_7.setObjectName(u"labelEggSeed1_7")

        self.gridLayout_4.addWidget(self.labelEggSeed1_7, 4, 0, 1, 1)

        self.lineEditEggSeed1_7 = QLineEdit(self.groupBoxEggRNG7)
        self.lineEditEggSeed1_7.setObjectName(u"lineEditEggSeed1_7")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed1_7.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed1_7.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed1_7.setMaxLength(8)
        self.lineEditEggSeed1_7.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditEggSeed1_7, 4, 1, 1, 1)

        self.labelEggSeed0_7 = QLabel(self.groupBoxEggRNG7)
        self.labelEggSeed0_7.setObjectName(u"labelEggSeed0_7")

        self.gridLayout_4.addWidget(self.labelEggSeed0_7, 5, 0, 1, 1)

        self.lineEditEggSeed0_7 = QLineEdit(self.groupBoxEggRNG7)
        self.lineEditEggSeed0_7.setObjectName(u"lineEditEggSeed0_7")
        sizePolicy5.setHeightForWidth(self.lineEditEggSeed0_7.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed0_7.setSizePolicy(sizePolicy5)
        self.lineEditEggSeed0_7.setMaxLength(8)
        self.lineEditEggSeed0_7.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditEggSeed0_7, 5, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBoxEggRNG7, 0, 2, 2, 1)

        self.eggParent1_7 = PokemonDisplay(self.tabEgg7)
        self.eggParent1_7.setObjectName(u"eggParent1_7")
        sizePolicy2.setHeightForWidth(self.eggParent1_7.sizePolicy().hasHeightForWidth())
        self.eggParent1_7.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.eggParent1_7, 0, 0, 2, 1)

        self.eggParent2_7 = PokemonDisplay(self.tabEgg7)
        self.eggParent2_7.setObjectName(u"eggParent2_7")
        sizePolicy2.setHeightForWidth(self.eggParent2_7.sizePolicy().hasHeightForWidth())
        self.eggParent2_7.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.eggParent2_7, 0, 1, 2, 1)

        self.tabWidgetGen7.addTab(self.tabEgg7, "")
        self.tabSOS = QWidget()
        self.tabSOS.setObjectName(u"tabSOS")
        self.gridLayout_8 = QGridLayout(self.tabSOS)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.comboBoxSOSIndex = QComboBox(self.tabSOS)
        self.comboBoxSOSIndex.addItem("")
        self.comboBoxSOSIndex.addItem("")
        self.comboBoxSOSIndex.addItem("")
        self.comboBoxSOSIndex.addItem("")
        self.comboBoxSOSIndex.setObjectName(u"comboBoxSOSIndex")
        self.comboBoxSOSIndex.setEnabled(False)

        self.gridLayout_8.addWidget(self.comboBoxSOSIndex, 0, 0, 1, 1)

        self.groupBoxSOS = QGroupBox(self.tabSOS)
        self.groupBoxSOS.setObjectName(u"groupBoxSOS")
        sizePolicy2.setHeightForWidth(self.groupBoxSOS.sizePolicy().hasHeightForWidth())
        self.groupBoxSOS.setSizePolicy(sizePolicy2)
        self.gridLayout_5 = QGridLayout(self.groupBoxSOS)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButtonSOSUpdate = QPushButton(self.groupBoxSOS)
        self.pushButtonSOSUpdate.setObjectName(u"pushButtonSOSUpdate")
        self.pushButtonSOSUpdate.setEnabled(False)

        self.gridLayout_5.addWidget(self.pushButtonSOSUpdate, 0, 0, 1, 1)

        self.pushButtonSOSReset = QPushButton(self.groupBoxSOS)
        self.pushButtonSOSReset.setObjectName(u"pushButtonSOSReset")
        self.pushButtonSOSReset.setEnabled(False)

        self.gridLayout_5.addWidget(self.pushButtonSOSReset, 0, 1, 1, 1)

        self.labelSOSInitialSeed = QLabel(self.groupBoxSOS)
        self.labelSOSInitialSeed.setObjectName(u"labelSOSInitialSeed")

        self.gridLayout_5.addWidget(self.labelSOSInitialSeed, 1, 0, 1, 1)

        self.lineEditSOSInitialSeed = QLineEdit(self.groupBoxSOS)
        self.lineEditSOSInitialSeed.setObjectName(u"lineEditSOSInitialSeed")
        self.lineEditSOSInitialSeed.setMaxLength(8)
        self.lineEditSOSInitialSeed.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEditSOSInitialSeed, 1, 1, 1, 1)

        self.labelSOSCurrentSeed = QLabel(self.groupBoxSOS)
        self.labelSOSCurrentSeed.setObjectName(u"labelSOSCurrentSeed")

        self.gridLayout_5.addWidget(self.labelSOSCurrentSeed, 2, 0, 1, 1)

        self.lineEditSOSCurrentSeed = QLineEdit(self.groupBoxSOS)
        self.lineEditSOSCurrentSeed.setObjectName(u"lineEditSOSCurrentSeed")
        self.lineEditSOSCurrentSeed.setMaxLength(8)
        self.lineEditSOSCurrentSeed.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEditSOSCurrentSeed, 2, 1, 1, 1)

        self.labelSOSFrame = QLabel(self.groupBoxSOS)
        self.labelSOSFrame.setObjectName(u"labelSOSFrame")

        self.gridLayout_5.addWidget(self.labelSOSFrame, 3, 0, 1, 1)

        self.lineEditSOSFrame = QLineEdit(self.groupBoxSOS)
        self.lineEditSOSFrame.setObjectName(u"lineEditSOSFrame")
        self.lineEditSOSFrame.setMaxLength(8)
        self.lineEditSOSFrame.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEditSOSFrame, 3, 1, 1, 1)

        self.labelSOSChainCount = QLabel(self.groupBoxSOS)
        self.labelSOSChainCount.setObjectName(u"labelSOSChainCount")

        self.gridLayout_5.addWidget(self.labelSOSChainCount, 4, 0, 1, 1)

        self.lineEditSOSChainCount = QLineEdit(self.groupBoxSOS)
        self.lineEditSOSChainCount.setObjectName(u"lineEditSOSChainCount")
        self.lineEditSOSChainCount.setMaxLength(8)
        self.lineEditSOSChainCount.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEditSOSChainCount, 4, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBoxSOS, 0, 1, 2, 1)

        self.sosPokemon = PokemonDisplay(self.tabSOS)
        self.sosPokemon.setObjectName(u"sosPokemon")
        sizePolicy2.setHeightForWidth(self.sosPokemon.sizePolicy().hasHeightForWidth())
        self.sosPokemon.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.sosPokemon, 1, 0, 1, 1)

        self.tabWidgetGen7.addTab(self.tabSOS, "")

        self.gridLayout_12.addWidget(self.tabWidgetGen7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabGen7, "")

        self.gridLayout_10.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CitraRNG 3.1.0", None))
        self.groupBoxConnection.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labelUpdateDelay.setText(QCoreApplication.translate("MainWindow", u"Auto update delay(seconds):", None))
        self.labelStatus.setText(QCoreApplication.translate("MainWindow", u"Status: Not Connected", None))
        self.comboBoxGameSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"XY", None))
        self.comboBoxGameSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"ORAS", None))
        self.comboBoxGameSelection.setItemText(2, QCoreApplication.translate("MainWindow", u"SM", None))
        self.comboBoxGameSelection.setItemText(3, QCoreApplication.translate("MainWindow", u"USUM", None))

        self.comboBoxMainIndex6.setItemText(0, QCoreApplication.translate("MainWindow", u"Party 1", None))
        self.comboBoxMainIndex6.setItemText(1, QCoreApplication.translate("MainWindow", u"Party 2", None))
        self.comboBoxMainIndex6.setItemText(2, QCoreApplication.translate("MainWindow", u"Party 3", None))
        self.comboBoxMainIndex6.setItemText(3, QCoreApplication.translate("MainWindow", u"Party 4", None))
        self.comboBoxMainIndex6.setItemText(4, QCoreApplication.translate("MainWindow", u"Party 5", None))
        self.comboBoxMainIndex6.setItemText(5, QCoreApplication.translate("MainWindow", u"Party 6", None))
        self.comboBoxMainIndex6.setItemText(6, QCoreApplication.translate("MainWindow", u"Wild", None))

        self.groupBoxMainRNG6.setTitle(QCoreApplication.translate("MainWindow", u"Main RNG", None))
        self.labelTiny2.setText(QCoreApplication.translate("MainWindow", u"[2]", None))
        self.labelTiny0.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.labelTiny3.setText(QCoreApplication.translate("MainWindow", u"[3]", None))
        self.labelTiny1.setText(QCoreApplication.translate("MainWindow", u"[1]", None))
        self.labelMainCurrentSeed6.setText(QCoreApplication.translate("MainWindow", u"Current Seed:", None))
        self.labelMainInitialSeed6.setText(QCoreApplication.translate("MainWindow", u"Initial Seed:", None))
        self.labelMainFrame6.setText(QCoreApplication.translate("MainWindow", u"Frame:", None))
        self.pushButtonMainUpdate6.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.labelSaveVariable.setText(QCoreApplication.translate("MainWindow", u"Save Variable:", None))
        self.tabWidgetGen6.setTabText(self.tabWidgetGen6.indexOf(self.tabMain6), QCoreApplication.translate("MainWindow", u"Main", None))
        self.groupBoxEggRNG6.setTitle(QCoreApplication.translate("MainWindow", u"Egg RNG", None))
        self.labelEggReady6.setText(QCoreApplication.translate("MainWindow", u"Egg Ready:", None))
        self.labelEggReadyStatus6.setText(QCoreApplication.translate("MainWindow", u"No egg yet", None))
        self.pushButtonEggUpdate6.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.labelEggSeed0_6.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.labelEggSeed1_6.setText(QCoreApplication.translate("MainWindow", u"[1]", None))
        self.tabWidgetGen6.setTabText(self.tabWidgetGen6.indexOf(self.tabEgg6), QCoreApplication.translate("MainWindow", u"Egg", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGen6), QCoreApplication.translate("MainWindow", u"Gen 6", None))
        self.comboBoxMainIndex7.setItemText(0, QCoreApplication.translate("MainWindow", u"Party 1", None))
        self.comboBoxMainIndex7.setItemText(1, QCoreApplication.translate("MainWindow", u"Party 2", None))
        self.comboBoxMainIndex7.setItemText(2, QCoreApplication.translate("MainWindow", u"Party 3", None))
        self.comboBoxMainIndex7.setItemText(3, QCoreApplication.translate("MainWindow", u"Party 4", None))
        self.comboBoxMainIndex7.setItemText(4, QCoreApplication.translate("MainWindow", u"Party 5", None))
        self.comboBoxMainIndex7.setItemText(5, QCoreApplication.translate("MainWindow", u"Party 6", None))
        self.comboBoxMainIndex7.setItemText(6, QCoreApplication.translate("MainWindow", u"Wild", None))

        self.groupBoxMainRNG7.setTitle(QCoreApplication.translate("MainWindow", u"Main RNG", None))
        self.labelMainInitialSeed7.setText(QCoreApplication.translate("MainWindow", u"Initial Seed:", None))
        self.labelMainCurrentSeed7.setText(QCoreApplication.translate("MainWindow", u"Current Seed:", None))
        self.labelMainFrame7.setText(QCoreApplication.translate("MainWindow", u"Frame:", None))
        self.pushButtonMainUpdate7.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.tabWidgetGen7.setTabText(self.tabWidgetGen7.indexOf(self.tabMain7), QCoreApplication.translate("MainWindow", u"Main", None))
        self.groupBoxEggRNG7.setTitle(QCoreApplication.translate("MainWindow", u"Egg RNG", None))
        self.pushButtonEggUpdate7.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.labelEggReady7.setText(QCoreApplication.translate("MainWindow", u"Egg Ready:", None))
        self.labelEggReadyStatus7.setText(QCoreApplication.translate("MainWindow", u"No egg yet", None))
        self.labelEggSeed3_7.setText(QCoreApplication.translate("MainWindow", u"[3]", None))
        self.labelEggSeed2_7.setText(QCoreApplication.translate("MainWindow", u"[2]", None))
        self.labelEggSeed1_7.setText(QCoreApplication.translate("MainWindow", u"[1]", None))
        self.labelEggSeed0_7.setText(QCoreApplication.translate("MainWindow", u"[0]", None))
        self.tabWidgetGen7.setTabText(self.tabWidgetGen7.indexOf(self.tabEgg7), QCoreApplication.translate("MainWindow", u"Egg", None))
        self.comboBoxSOSIndex.setItemText(0, QCoreApplication.translate("MainWindow", u"SOS 1", None))
        self.comboBoxSOSIndex.setItemText(1, QCoreApplication.translate("MainWindow", u"SOS 2", None))
        self.comboBoxSOSIndex.setItemText(2, QCoreApplication.translate("MainWindow", u"SOS 3", None))
        self.comboBoxSOSIndex.setItemText(3, QCoreApplication.translate("MainWindow", u"SOS 4", None))

        self.groupBoxSOS.setTitle(QCoreApplication.translate("MainWindow", u"SOS RNG", None))
        self.pushButtonSOSUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSOSReset.setToolTip(QCoreApplication.translate("MainWindow", u"This should be used after a battle", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSOSReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.labelSOSInitialSeed.setText(QCoreApplication.translate("MainWindow", u"Initial Seed:", None))
        self.labelSOSCurrentSeed.setText(QCoreApplication.translate("MainWindow", u"Current Seed:", None))
        self.labelSOSFrame.setText(QCoreApplication.translate("MainWindow", u"Frame:", None))
        self.labelSOSChainCount.setText(QCoreApplication.translate("MainWindow", u"Chain Count:", None))
        self.tabWidgetGen7.setTabText(self.tabWidgetGen7.indexOf(self.tabSOS), QCoreApplication.translate("MainWindow", u"SOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGen7), QCoreApplication.translate("MainWindow", u"Gen 7", None))
    # retranslateUi

