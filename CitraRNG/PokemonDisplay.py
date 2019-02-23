from PySide2.QtWidgets import QWidget
from ui_PokemonDisplay import Ui_PokemonDisplay
from Pokemon import Pokemon
from Util import colorIV, colorPSV

class PokemonDisplay(QWidget, Ui_PokemonDisplay):
    def __init__(self, parent = None):
        super(PokemonDisplay, self).__init__(parent)
        self.setupUi(self)

    def updateInformation(self, pkm):
        self.labelSpeciesValue.setText(pkm.species())
        self.labelGenderValue.setText(pkm.gender())
        self.labelNatureValue.setText(pkm.nature())
        self.labelAbilityValue.setText(pkm.ability())
        self.labelItemValue.setText(pkm.heldItem())
        self.labelSVValue.setText("PSV/TSV: " + colorPSV(pkm.PSV(), pkm.TSV()) + str(pkm.TSV()))
        self.labelHiddenPowerValue.setText(pkm.hiddenPower())
        self.labelFriendshipValue.setText(str(pkm.currentFriendship()))
        
        self.labelHP.setText("HP: " + pkm.HPCurrent() + "/" + pkm.HP())
        self.labelAtk.setText("Atk: " + pkm.Atk())
        self.labelDef.setText("Def: " + pkm.Def())
        self.labelSpA.setText("SpA: " + pkm.SpA())
        self.labelSpD.setText("SpD: " + pkm.SpD())
        self.labelSpe.setText("Spe: " + pkm.Spe())
        self.labelHPIV.setText("IV: " + colorIV(pkm.IVHP()))
        self.labelAtkIV.setText("IV: " + colorIV(pkm.IVAtk()))
        self.labelDefIV.setText("IV: " + colorIV(pkm.IVDef()))
        self.labelSpAIV.setText("IV: " + colorIV(pkm.IVSpA()))
        self.labelSpDIV.setText("IV: " + colorIV(pkm.IVSpD()))
        self.labelSpeIV.setText("IV: " + colorIV(pkm.IVSpe()))
        self.labelHPEV.setText("EV: " + str(pkm.EVHP()))
        self.labelAtkEV.setText("EV: " + str(pkm.EVAtk()))
        self.labelDefEV.setText("EV: " + str(pkm.EVDef()))
        self.labelSpAEV.setText("EV: " + str(pkm.EVSpA()))
        self.labelSpDEV.setText("EV: " + str(pkm.EVSpD()))
        self.labelSpeEV.setText("EV: " + str(pkm.EVSpe()))
    
        self.labelMove1Name.setText(pkm.move1())
        self.labelMove2Name.setText(pkm.move2())
        self.labelMove3Name.setText(pkm.move3())
        self.labelMove4Name.setText(pkm.move4())
        self.labelMove1PP.setText("PP: " + str(pkm.move1PP()))
        self.labelMove2PP.setText("PP: " + str(pkm.move2PP()))
        self.labelMove3PP.setText("PP: " + str(pkm.move3PP()))
        self.labelMove4PP.setText("PP: " + str(pkm.move4PP()))

    def setTitle(self, name):
        self.groupBoxPokemon.setTitle(name)