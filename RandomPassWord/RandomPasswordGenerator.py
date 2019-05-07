import sys
import secrets

from PyQt5.QtWidgets import QWidget,QHBoxLayout,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QLineEdit

class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        #checkbox,input,button,label
        self.checkbox0 = QCheckBox("Lowercase Letter")
        self.checkbox1 = QCheckBox("Uppercase Letter")
        self.checkbox2 = QCheckBox("Number")
        self.checkbox3 = QCheckBox("Symbols")
        self.length = QLineEdit("Length")
        self.button = QPushButton("New Password")
        self.password = QLineEdit("")

        v_box = QVBoxLayout() #Vertical Layout
        v_box.addWidget(self.checkbox0)
        v_box.addWidget(self.checkbox1)
        v_box.addWidget(self.checkbox2)
        v_box.addWidget(self.checkbox3)
        v_box.addWidget(self.length)
        v_box.addWidget(self.button)
        v_box.addWidget(self.password)

        h_box = QHBoxLayout() #Horizontal Layout
        h_box.addLayout(v_box)

        self.setLayout(h_box)

        self.setWindowTitle("Random Password Generator")

        self.button.clicked.connect(lambda : self.generate(self.checkbox0.isChecked(),self.checkbox1.isChecked(),self.checkbox2.isChecked(),self.checkbox3.isChecked(),self.length))

        self.show()

    def generate(self,checkbox0,checkbox1,checkbox2,checkbox3,length):

        lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

        uppercase_letters = [i.upper() for i in lowercase_letters]

        numbers = [0,1,2,3,4,5,6,7,8,9]

        symbols = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*",">","#","{","[","]","}","<"]

        elements = []

        password = ""
        if checkbox0:
            elements.append(lowercase_letters)
        if checkbox1:
            elements.append(uppercase_letters)
        if checkbox2:
            elements.append(numbers)
        if checkbox3:
            elements.append(symbols)
        digitCounter = 0;
        try:
            while(digitCounter < int(self.length.text())):
                randomChoice = str(secrets.choice(secrets.choice(elements)))
                if randomChoice not in password:
                    password+=randomChoice
                    digitCounter+=1
            self.password.setText(password)
        except ValueError:
            self.password.setText("Please enter a length.")
        except IndexError:
            self.password.setText("Please select an option. ")
        except:
            self.password.setText("Error")

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
