from pynerator_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
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
        self.pyneratorui.btn_generate.clicked.connect(self.generate) #connect buton to a function
        self.pyneratorui.spinBox_character.setMaximum(len(self.characters)) #max value to spinbox
        self.pyneratorui.spinBox_uppercase.setMaximum(len(self.uppercase)) #max value to spinbox
        self.pyneratorui.spinBox_number.setMaximum(len(self.numbers)) #max value to spinbox
        self.pyneratorui.spinBox_specialchar.setMaximum(len(self.special_characters)) #max value to spinbox
    
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

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Pynerator()
    gui.show()   
    
    sys.exit(app.exec_())
    