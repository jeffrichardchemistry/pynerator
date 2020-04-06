from pynerator.pynerator_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import QtCore
import sys
import random

class Pynerator(QMainWindow, QWidget):
    def __init__(self):
        super(Pynerator, self).__init__()
        
        self.pyneratorui = Ui_MainWindow()
        self.pyneratorui.setupUi(self)        
        
        self.characters = 'qwertyuiopasdfghjklçzxcvbnm'
        self.uppercase = 'QWERTYUIOPASDFGHJKLÇZXCVBNM'
        self.numbers = '0123456789'
        self.special_characters = '/!@#$%&*()_-=+?:><}{[]'
        Pynerator.Init(self)
        
        self.spinchar_value = 0
        self.spinnumber_value = 0
        self.spinspecialchar_value = 0
        self.spinuppercase_value = 0
    
    def Init(self):
        self.pyneratorui.btn_generate.clicked.connect(self.generate) #connect button in a function
        self.pyneratorui.chkbox_character.stateChanged.connect(self.checkAndreset_char)
        self.pyneratorui.chkbox_number.stateChanged.connect(self.checkAndreset_number)
        self.pyneratorui.chkbox_specialchar.stateChanged.connect(self.checkAndreset_specialchar)
        self.pyneratorui.chkbox_uppercase.stateChanged.connect(self.checkAndreset_upper)

    def checkAndreset_char(self):
        if self.pyneratorui.chkbox_character.checkState() == 0:
            self.pyneratorui.spinBox_character.setValue(0)
        else:
            pass

    def checkAndreset_number(self):
        if self.pyneratorui.chkbox_number.checkState() == 0:
            self.pyneratorui.spinBox_number.setValue(0)
        else:
            pass
    
    def checkAndreset_specialchar(self):
        if self.pyneratorui.chkbox_specialchar.checkState() == 0:
            self.pyneratorui.spinBox_specialchar.setValue(0)
        else:
            pass
    
    def checkAndreset_upper(self):
        if self.pyneratorui.chkbox_uppercase.checkState() == 0:
            self.pyneratorui.spinBox_uppercase.setValue(0)
        else:
            pass

    def generate(self):
        Pynerator.checkGetspin(self)
        password = ''.join(random.choices(self.characters, k=self.spinchar_value)) + \
                   ''.join(random.choices(self.special_characters, k=self.spinspecialchar_value)) + \
                   ''.join(random.choices(self.numbers, k=self.spinnumber_value)) + \
                   ''.join(random.choices(self.uppercase, k=self.spinuppercase_value))
                   
        password = ''.join(random.sample(password, k=len(password)))
        
        self.pyneratorui.txt_password.setText(password)
    
    def checkGetspin(self):
        #check characters and get spin value
        if self.pyneratorui.chkbox_character.checkState() == 2:
            self.spinchar_value = int(self.pyneratorui.spinBox_character.text())
        else:
            self.spinchar_value = 0
            
        #check Numbers and get spin value
        if self.pyneratorui.chkbox_number.checkState() == 2:
            self.spinnumber_value = int(self.pyneratorui.spinBox_number.text())
        else:
            self.spinnumber_value = 0
        
        #check special character and get spin value
        if self.pyneratorui.chkbox_specialchar.checkState() == 2:
            self.spinspecialchar_value = int(self.pyneratorui.spinBox_specialchar.text())
        else:
            self.spinspecialchar_value = 0
        
        #check uppercase and get spin value
        if self.pyneratorui.chkbox_uppercase.checkState() == 2:
            self.spinuppercase_value = int(self.pyneratorui.spinBox_uppercase.text())
        else:
            self.spinuppercase_value = 0 

    
def runGUI():
    app = QApplication(sys.argv)
    gui = Pynerator()
    gui.show()		
    sys.exit(app.exec_())
    
