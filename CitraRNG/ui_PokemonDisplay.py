# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PokemonDisplay.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_PokemonDisplay(object):
    def setupUi(self, PokemonDisplay):
        if not PokemonDisplay.objectName():
            PokemonDisplay.setObjectName(u"PokemonDisplay")
        PokemonDisplay.resize(195, 434)
        self.gridLayout = QGridLayout(PokemonDisplay)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxPokemon = QGroupBox(PokemonDisplay)
        self.groupBoxPokemon.setObjectName(u"groupBoxPokemon")
        self.gridLayout_2 = QGridLayout(self.groupBoxPokemon)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayoutCharacteristics = QGridLayout()
        self.gridLayoutCharacteristics.setObjectName(u"gridLayoutCharacteristics")
        self.labelSpecies = QLabel(self.groupBoxPokemon)
        self.labelSpecies.setObjectName(u"labelSpecies")

        self.gridLayoutCharacteristics.addWidget(self.labelSpecies, 0, 0, 1, 1)

        self.labelSpeciesValue = QLabel(self.groupBoxPokemon)
        self.labelSpeciesValue.setObjectName(u"labelSpeciesValue")

        self.gridLayoutCharacteristics.addWidget(self.labelSpeciesValue, 0, 1, 1, 1)

        self.labelGender = QLabel(self.groupBoxPokemon)
        self.labelGender.setObjectName(u"labelGender")

        self.gridLayoutCharacteristics.addWidget(self.labelGender, 1, 0, 1, 1)

        self.labelGenderValue = QLabel(self.groupBoxPokemon)
        self.labelGenderValue.setObjectName(u"labelGenderValue")

        self.gridLayoutCharacteristics.addWidget(self.labelGenderValue, 1, 1, 1, 1)

        self.labelNature = QLabel(self.groupBoxPokemon)
        self.labelNature.setObjectName(u"labelNature")

        self.gridLayoutCharacteristics.addWidget(self.labelNature, 2, 0, 1, 1)

        self.labelNatureValue = QLabel(self.groupBoxPokemon)
        self.labelNatureValue.setObjectName(u"labelNatureValue")

        self.gridLayoutCharacteristics.addWidget(self.labelNatureValue, 2, 1, 1, 1)

        self.labelAbility = QLabel(self.groupBoxPokemon)
        self.labelAbility.setObjectName(u"labelAbility")

        self.gridLayoutCharacteristics.addWidget(self.labelAbility, 3, 0, 1, 1)

        self.labelAbilityValue = QLabel(self.groupBoxPokemon)
        self.labelAbilityValue.setObjectName(u"labelAbilityValue")

        self.gridLayoutCharacteristics.addWidget(self.labelAbilityValue, 3, 1, 1, 1)

        self.labelItem = QLabel(self.groupBoxPokemon)
        self.labelItem.setObjectName(u"labelItem")

        self.gridLayoutCharacteristics.addWidget(self.labelItem, 4, 0, 1, 1)

        self.labelItemValue = QLabel(self.groupBoxPokemon)
        self.labelItemValue.setObjectName(u"labelItemValue")

        self.gridLayoutCharacteristics.addWidget(self.labelItemValue, 4, 1, 1, 1)

        self.labelSV = QLabel(self.groupBoxPokemon)
        self.labelSV.setObjectName(u"labelSV")

        self.gridLayoutCharacteristics.addWidget(self.labelSV, 5, 0, 1, 1)

        self.labelSVValue = QLabel(self.groupBoxPokemon)
        self.labelSVValue.setObjectName(u"labelSVValue")

        self.gridLayoutCharacteristics.addWidget(self.labelSVValue, 5, 1, 1, 1)

        self.labelHiddenPower = QLabel(self.groupBoxPokemon)
        self.labelHiddenPower.setObjectName(u"labelHiddenPower")

        self.gridLayoutCharacteristics.addWidget(self.labelHiddenPower, 6, 0, 1, 1)

        self.labelHiddenPowerValue = QLabel(self.groupBoxPokemon)
        self.labelHiddenPowerValue.setObjectName(u"labelHiddenPowerValue")

        self.gridLayoutCharacteristics.addWidget(self.labelHiddenPowerValue, 6, 1, 1, 1)

        self.labelFriendship = QLabel(self.groupBoxPokemon)
        self.labelFriendship.setObjectName(u"labelFriendship")

        self.gridLayoutCharacteristics.addWidget(self.labelFriendship, 7, 0, 1, 1)

        self.labelFriendshipValue = QLabel(self.groupBoxPokemon)
        self.labelFriendshipValue.setObjectName(u"labelFriendshipValue")

        self.gridLayoutCharacteristics.addWidget(self.labelFriendshipValue, 7, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayoutCharacteristics, 1, 0, 1, 1)

        self.pushButtonUpdate = QPushButton(self.groupBoxPokemon)
        self.pushButtonUpdate.setObjectName(u"pushButtonUpdate")
        self.pushButtonUpdate.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButtonUpdate, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.gridLayoutMoves = QGridLayout()
        self.gridLayoutMoves.setObjectName(u"gridLayoutMoves")
        self.labelMove1 = QLabel(self.groupBoxPokemon)
        self.labelMove1.setObjectName(u"labelMove1")

        self.gridLayoutMoves.addWidget(self.labelMove1, 0, 0, 1, 1)

        self.labelMove1Name = QLabel(self.groupBoxPokemon)
        self.labelMove1Name.setObjectName(u"labelMove1Name")

        self.gridLayoutMoves.addWidget(self.labelMove1Name, 0, 1, 1, 1)

        self.labelMove1PP = QLabel(self.groupBoxPokemon)
        self.labelMove1PP.setObjectName(u"labelMove1PP")

        self.gridLayoutMoves.addWidget(self.labelMove1PP, 0, 2, 1, 1)

        self.labelMove2 = QLabel(self.groupBoxPokemon)
        self.labelMove2.setObjectName(u"labelMove2")

        self.gridLayoutMoves.addWidget(self.labelMove2, 1, 0, 1, 1)

        self.labelMove2Name = QLabel(self.groupBoxPokemon)
        self.labelMove2Name.setObjectName(u"labelMove2Name")

        self.gridLayoutMoves.addWidget(self.labelMove2Name, 1, 1, 1, 1)

        self.labelMove2PP = QLabel(self.groupBoxPokemon)
        self.labelMove2PP.setObjectName(u"labelMove2PP")

        self.gridLayoutMoves.addWidget(self.labelMove2PP, 1, 2, 1, 1)

        self.labelMove3 = QLabel(self.groupBoxPokemon)
        self.labelMove3.setObjectName(u"labelMove3")

        self.gridLayoutMoves.addWidget(self.labelMove3, 2, 0, 1, 1)

        self.labelMove3Name = QLabel(self.groupBoxPokemon)
        self.labelMove3Name.setObjectName(u"labelMove3Name")

        self.gridLayoutMoves.addWidget(self.labelMove3Name, 2, 1, 1, 1)

        self.labelMove3PP = QLabel(self.groupBoxPokemon)
        self.labelMove3PP.setObjectName(u"labelMove3PP")

        self.gridLayoutMoves.addWidget(self.labelMove3PP, 2, 2, 1, 1)

        self.labelMove4 = QLabel(self.groupBoxPokemon)
        self.labelMove4.setObjectName(u"labelMove4")

        self.gridLayoutMoves.addWidget(self.labelMove4, 3, 0, 1, 1)

        self.labelMove4Name = QLabel(self.groupBoxPokemon)
        self.labelMove4Name.setObjectName(u"labelMove4Name")

        self.gridLayoutMoves.addWidget(self.labelMove4Name, 3, 1, 1, 1)

        self.labelMove4PP = QLabel(self.groupBoxPokemon)
        self.labelMove4PP.setObjectName(u"labelMove4PP")

        self.gridLayoutMoves.addWidget(self.labelMove4PP, 3, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayoutMoves, 5, 0, 1, 1)

        self.gridLayoutStats = QGridLayout()
        self.gridLayoutStats.setObjectName(u"gridLayoutStats")
        self.labelAtk = QLabel(self.groupBoxPokemon)
        self.labelAtk.setObjectName(u"labelAtk")

        self.gridLayoutStats.addWidget(self.labelAtk, 1, 0, 1, 1)

        self.labelDefEV = QLabel(self.groupBoxPokemon)
        self.labelDefEV.setObjectName(u"labelDefEV")

        self.gridLayoutStats.addWidget(self.labelDefEV, 2, 2, 1, 1)

        self.labelSpAIV = QLabel(self.groupBoxPokemon)
        self.labelSpAIV.setObjectName(u"labelSpAIV")

        self.gridLayoutStats.addWidget(self.labelSpAIV, 3, 1, 1, 1)

        self.labelSpA = QLabel(self.groupBoxPokemon)
        self.labelSpA.setObjectName(u"labelSpA")

        self.gridLayoutStats.addWidget(self.labelSpA, 3, 0, 1, 1)

        self.labelDefIV = QLabel(self.groupBoxPokemon)
        self.labelDefIV.setObjectName(u"labelDefIV")

        self.gridLayoutStats.addWidget(self.labelDefIV, 2, 1, 1, 1)

        self.labelHP = QLabel(self.groupBoxPokemon)
        self.labelHP.setObjectName(u"labelHP")

        self.gridLayoutStats.addWidget(self.labelHP, 0, 0, 1, 1)

        self.labelSpAEV = QLabel(self.groupBoxPokemon)
        self.labelSpAEV.setObjectName(u"labelSpAEV")

        self.gridLayoutStats.addWidget(self.labelSpAEV, 3, 2, 1, 1)

        self.labelSpD = QLabel(self.groupBoxPokemon)
        self.labelSpD.setObjectName(u"labelSpD")

        self.gridLayoutStats.addWidget(self.labelSpD, 4, 0, 1, 1)

        self.labelHPIV = QLabel(self.groupBoxPokemon)
        self.labelHPIV.setObjectName(u"labelHPIV")

        self.gridLayoutStats.addWidget(self.labelHPIV, 0, 1, 1, 1)

        self.labelHPEV = QLabel(self.groupBoxPokemon)
        self.labelHPEV.setObjectName(u"labelHPEV")

        self.gridLayoutStats.addWidget(self.labelHPEV, 0, 2, 1, 1)

        self.labelAtkEV = QLabel(self.groupBoxPokemon)
        self.labelAtkEV.setObjectName(u"labelAtkEV")

        self.gridLayoutStats.addWidget(self.labelAtkEV, 1, 2, 1, 1)

        self.labelDef = QLabel(self.groupBoxPokemon)
        self.labelDef.setObjectName(u"labelDef")

        self.gridLayoutStats.addWidget(self.labelDef, 2, 0, 1, 1)

        self.labelAtkIV = QLabel(self.groupBoxPokemon)
        self.labelAtkIV.setObjectName(u"labelAtkIV")

        self.gridLayoutStats.addWidget(self.labelAtkIV, 1, 1, 1, 1)

        self.labelSpDIV = QLabel(self.groupBoxPokemon)
        self.labelSpDIV.setObjectName(u"labelSpDIV")

        self.gridLayoutStats.addWidget(self.labelSpDIV, 4, 1, 1, 1)

        self.labelSpeEV = QLabel(self.groupBoxPokemon)
        self.labelSpeEV.setObjectName(u"labelSpeEV")

        self.gridLayoutStats.addWidget(self.labelSpeEV, 5, 2, 1, 1)

        self.labelSpeIV = QLabel(self.groupBoxPokemon)
        self.labelSpeIV.setObjectName(u"labelSpeIV")

        self.gridLayoutStats.addWidget(self.labelSpeIV, 5, 1, 1, 1)

        self.labelSpDEV = QLabel(self.groupBoxPokemon)
        self.labelSpDEV.setObjectName(u"labelSpDEV")

        self.gridLayoutStats.addWidget(self.labelSpDEV, 4, 2, 1, 1)

        self.labelSpe = QLabel(self.groupBoxPokemon)
        self.labelSpe.setObjectName(u"labelSpe")

        self.gridLayoutStats.addWidget(self.labelSpe, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayoutStats, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxPokemon, 0, 0, 1, 1)


        self.retranslateUi(PokemonDisplay)

        QMetaObject.connectSlotsByName(PokemonDisplay)
    # setupUi

    def retranslateUi(self, PokemonDisplay):
        PokemonDisplay.setWindowTitle(QCoreApplication.translate("PokemonDisplay", u"Pokemon", None))
        self.groupBoxPokemon.setTitle(QCoreApplication.translate("PokemonDisplay", u"Pokemon", None))
        self.labelSpecies.setText(QCoreApplication.translate("PokemonDisplay", u"Species:", None))
        self.labelSpeciesValue.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelGender.setText(QCoreApplication.translate("PokemonDisplay", u"Gender:", None))
        self.labelGenderValue.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelNature.setText(QCoreApplication.translate("PokemonDisplay", u"Nature:", None))
        self.labelNatureValue.setText(QCoreApplication.translate("PokemonDisplay", u"Hardy", None))
        self.labelAbility.setText(QCoreApplication.translate("PokemonDisplay", u"Ability:", None))
        self.labelAbilityValue.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelItem.setText(QCoreApplication.translate("PokemonDisplay", u"Item:", None))
        self.labelItemValue.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelSV.setText(QCoreApplication.translate("PokemonDisplay", u"PSV/TSV:", None))
        self.labelSVValue.setText(QCoreApplication.translate("PokemonDisplay", u"0000/0000", None))
        self.labelHiddenPower.setText(QCoreApplication.translate("PokemonDisplay", u"Hidden Power:", None))
        self.labelHiddenPowerValue.setText(QCoreApplication.translate("PokemonDisplay", u"Fighting", None))
        self.labelFriendship.setText(QCoreApplication.translate("PokemonDisplay", u"Friendship:", None))
        self.labelFriendshipValue.setText(QCoreApplication.translate("PokemonDisplay", u"0", None))
        self.pushButtonUpdate.setText(QCoreApplication.translate("PokemonDisplay", u"Update", None))
        self.labelMove1.setText(QCoreApplication.translate("PokemonDisplay", u"Move 1:", None))
        self.labelMove1Name.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelMove1PP.setText(QCoreApplication.translate("PokemonDisplay", u"PP: 0", None))
        self.labelMove2.setText(QCoreApplication.translate("PokemonDisplay", u"Move 2:", None))
        self.labelMove2Name.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelMove2PP.setText(QCoreApplication.translate("PokemonDisplay", u"PP: 0", None))
        self.labelMove3.setText(QCoreApplication.translate("PokemonDisplay", u"Move 3:", None))
        self.labelMove3Name.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelMove3PP.setText(QCoreApplication.translate("PokemonDisplay", u"PP: 0", None))
        self.labelMove4.setText(QCoreApplication.translate("PokemonDisplay", u"Move 4:", None))
        self.labelMove4Name.setText(QCoreApplication.translate("PokemonDisplay", u"None", None))
        self.labelMove4PP.setText(QCoreApplication.translate("PokemonDisplay", u"PP: 0", None))
        self.labelAtk.setText(QCoreApplication.translate("PokemonDisplay", u"Atk: 0", None))
        self.labelDefEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelSpAIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelSpA.setText(QCoreApplication.translate("PokemonDisplay", u"SpA: 0", None))
        self.labelDefIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelHP.setText(QCoreApplication.translate("PokemonDisplay", u"HP: 0/0", None))
        self.labelSpAEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelSpD.setText(QCoreApplication.translate("PokemonDisplay", u"SpD: 0", None))
        self.labelHPIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelHPEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelAtkEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelDef.setText(QCoreApplication.translate("PokemonDisplay", u"Def: 0", None))
        self.labelAtkIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelSpDIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelSpeEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelSpeIV.setText(QCoreApplication.translate("PokemonDisplay", u"IV: 0", None))
        self.labelSpDEV.setText(QCoreApplication.translate("PokemonDisplay", u"EV: 0", None))
        self.labelSpe.setText(QCoreApplication.translate("PokemonDisplay", u"Spe: 0", None))
    # retranslateUi

