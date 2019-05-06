import sys
from PyQt5.QtWidgets import *
# QMainWindow, QPushButton, QApplication, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt

class Window(QMainWindow):

    enlargeCount = 0
    enlargeButtonsCount = 0
    licznik = 0
    liczba = 0
    numbers = []
    flagNew = 0
    numberorsign = 0 #1 number, 2 sign
    numbers.append(0)
    textL = ""


    # if flag == 1 then addition
    # if flag == 2 then substract
    # if flag == 3 then multiplication
    # if flag == 4 then division
    flag = 0
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(150,150,500,500)
        self.okno = QWidget(self)
        self.setCentralWidget(self.okno)
        self.mainLayout = QVBoxLayout()
        # self.mainLayout.setGeometry(100,100,300,300)
        self.gridLayout = QGridLayout()
        self.okno.setLayout(self.mainLayout)
        self.setWindowTitle("Kalkulator")
        # menu
        #extractAction = QtGui.QActionEvent('&Menu',self)

        self.home()
        self.mainLayout.addLayout(self.gridLayout)
        checkbox = QCheckBox('Zwieksz okno',self)
        checkbox.move(10,30)
        checkbox.stateChanged.connect(self.enlarge)
        self.mainLayout.addWidget(checkbox, alignment=Qt.AlignCenter)
        # print(self.style().objectName())
        self.StyleChoice = QLabel("Windows Vista",self)
        combobox = QComboBox(self)
        combobox.addItem("windowsvista")
        combobox.addItem("windowsxp")
        combobox.addItem("Windows")
        combobox.addItem("Fusion")

        self.mainLayout.addWidget(self.StyleChoice, alignment = Qt.AlignLeft)
        self.mainLayout.addWidget(combobox, alignment = Qt.AlignLeft)
        combobox.activated[str].connect(self.stylechoice)


        self.color = QLabel("Choose color:",self)
        self.mainLayout.addWidget(self.color, alignment=Qt.AlignRight)
        comboboxcolor = QComboBox(self)
        comboboxcolor.addItem("grey")
        comboboxcolor.addItem("red")
        comboboxcolor.addItem("green")
        comboboxcolor.addItem("blue")
        comboboxcolor.addItem("yellow")
        self.mainLayout.addWidget(comboboxcolor, alignment = Qt.AlignRight)
        comboboxcolor.activated[str].connect(self.colorchoice)

        self.show()

        self.initUI()

    def colorchoice(self,text):
        self.btn0.setStyleSheet("background-color:"+text)
        self.btn1.setStyleSheet("background-color:"+text)
        self.btn2.setStyleSheet("background-color:"+text)
        self.btn3.setStyleSheet("background-color:"+text)
        self.btn4.setStyleSheet("background-color:"+text)
        self.btn5.setStyleSheet("background-color:"+text)
        self.btn6.setStyleSheet("background-color:"+text)
        self.btn7.setStyleSheet("background-color:"+text)
        self.btn8.setStyleSheet("background-color:"+text)
        self.btn9.setStyleSheet("background-color:"+text)
        self.btnp.setStyleSheet("background-color:"+text)
        self.btnm.setStyleSheet("background-color:"+text)
        self.btnmn.setStyleSheet("background-color:"+text)
        self.btndz.setStyleSheet("background-color:"+text)
        self.btneq.setStyleSheet("background-color:"+text)
        self.btnC.setStyleSheet("background-color:"+text)

    def stylechoice(self,text):
        self.StyleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def enlarge(self,state):
        if self.enlargeCount == 0:
            self.setGeometry(150,150,800,800)
            self.enlargeCount = 1
        else:
            self.setGeometry(150,150,300,300)
            self.enlargeCount = 0


#menu
    def initUI(self):
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        enlargeAction = QAction('&Enlarge', self)
        enlargeAction.setShortcut('Ctrl+L')
        enlargeAction.setStatusTip('Enlarge window')
        enlargeAction.triggered.connect(self.enlarge)

        enlargeButtonsAction = QAction('&EnlargeButtons', self)
        enlargeButtonsAction.setShortcut('Ctrl+B')
        enlargeButtonsAction.setStatusTip('Enlarge Buttons')
        enlargeButtonsAction.triggered.connect(self.enlargeButtons)



        # self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(enlargeButtonsAction)
        fileMenu.addAction(enlargeAction)
        fileMenu.addAction(exitAction)

        self.show()

    def enlargeButtons(self):
        if self.enlargeButtonsCount == 0:
            self.btn0.setFixedSize(80,80)
            self.btn1.setFixedSize(80,80)
            self.btn2.setFixedSize(80,80)
            self.btn3.setFixedSize(80,80)
            self.btn4.setFixedSize(80,80)
            self.btn5.setFixedSize(80,80)
            self.btn6.setFixedSize(80,80)
            self.btn7.setFixedSize(80,80)
            self.btn8.setFixedSize(80,80)
            self.btn9.setFixedSize(80,80)
            self.btnp.setFixedSize(80,80)
            self.btnm.setFixedSize(80,80)
            self.btnmn.setFixedSize(80,80)
            self.btndz.setFixedSize(80,80)
            self.btneq.setFixedSize(80,80)
            self.btnC.setFixedSize(80,80)
            self.enlargeButtonsCount = 1
            self.setGeometry(150, 150, 600, 600)
        else:
            self.btn0.setFixedSize(40, 40)
            self.btn1.setFixedSize(40, 40)
            self.btn2.setFixedSize(40, 40)
            self.btn3.setFixedSize(40, 40)
            self.btn4.setFixedSize(40, 40)
            self.btn5.setFixedSize(40, 40)
            self.btn6.setFixedSize(40, 40)
            self.btn7.setFixedSize(40, 40)
            self.btn8.setFixedSize(40, 40)
            self.btn9.setFixedSize(40, 40)
            self.btnp.setFixedSize(40, 40)
            self.btnm.setFixedSize(40, 40)
            self.btnmn.setFixedSize(40, 40)
            self.btndz.setFixedSize(40, 40)
            self.btneq.setFixedSize(40, 40)
            self.btnC.setFixedSize(40, 40)
            self.enlargeButtonsCount = 0
            self.setGeometry(150, 150, 300, 300)
        # self.show()


# buttons
    def home(self):

        self.resultlabel = QLabel("0",self)
        self.resultlabel.setFont(QtGui.QFont('SansSerif', 15))
        self.resultlabel.resize(self.resultlabel.minimumSizeHint())
        # self.resultlabel.setText("wynik")
        self.mainLayout.addWidget(self.resultlabel)

        self.btn0 = QPushButton('0',self)
        self.btn0.clicked.connect(self.on_click0)
        self.btn0.resize(self.btn0.minimumSizeHint())
        # btn0.move(100, 50)
        self.gridLayout.addWidget(self.btn0,1,0)

        self.btn1 = QPushButton('1',self)
        self.btn1.clicked.connect(self.on_click1)
        self.btn1.resize(self.btn1.minimumSizeHint())
        self.gridLayout.addWidget(self.btn1,1,1)
        # btn1.move(100,100)

        self.btn2 = QPushButton('2',self)
        self.btn2.clicked.connect(self.on_click2)
        self.btn2.resize(self.btn2.minimumSizeHint())
        self.gridLayout.addWidget(self.btn2,1,2)
        # btn2.move(100,150)

        self.btn3 = QPushButton('3',self)
        self.btn3.clicked.connect(self.on_click3)
        self.btn3.resize(self.btn3.minimumSizeHint())
        self.gridLayout.addWidget(self.btn3,2,0)
        # btn3.move(100,200)

        self.btn4 = QPushButton('4',self)
        self.btn4.clicked.connect(self.on_click4)
        self.btn4.resize(self.btn4.minimumSizeHint())
        self.gridLayout.addWidget(self.btn4,2,1)
        # btn4.move(100, 250)

        self.btn5 = QPushButton('5',self)
        self.btn5.clicked.connect(self.on_click5)
        self.btn5.resize(self.btn5.minimumSizeHint())
        self.gridLayout.addWidget(self.btn5,2,2)
        # btn5.move(100, 300)

        self.btn6 = QPushButton('6',self)
        self.btn6.clicked.connect(self.on_click6)
        self.btn6.resize(self.btn6.minimumSizeHint())
        self.gridLayout.addWidget(self.btn6,3,0)
        # btn6.move(100, 350)

        self.btn7 = QPushButton('7',self)
        self.btn7.clicked.connect(self.on_click7)
        self.btn7.resize(self.btn7.minimumSizeHint())
        self.gridLayout.addWidget(self.btn7,3,1)
        # btn7.move(100, 400)

        self.btn8 = QPushButton('8',self)
        self.btn8.clicked.connect(self.on_click8)
        self.btn8.resize(self.btn8.minimumSizeHint())
        self.gridLayout.addWidget(self.btn8,3,2)
        # btn8.move(100, 450)

        self.btn9 = QPushButton('9',self)
        self.btn9.clicked.connect(self.on_click9)
        self.btn9.resize(self.btn9.minimumSizeHint())
        self.gridLayout.addWidget(self.btn9,4,0)
        # btn9.move(100, 500)

        self.btnp = QPushButton('+',self)
        self.btnp.clicked.connect(self.on_clickp)
        self.btnp.resize(self.btnp.minimumSizeHint())
        self.gridLayout.addWidget(self.btnp,1,3)
        # btnp.move(200, 500)

        self.btnm = QPushButton('-',self)
        self.btnm.clicked.connect(self.on_clickm)
        self.btnm.resize(self.btnm.minimumSizeHint())
        self.gridLayout.addWidget(self.btnm,2,3)
        # btnm.move(200, 450)

        self.btnmn = QPushButton('*',self)
        self.btnmn.clicked.connect(self.on_clickmn)
        self.btnmn.resize(self.btnmn.minimumSizeHint())
        self.gridLayout.addWidget(self.btnmn,3,3)
        # btnmn.move(200, 400)

        self.btndz = QPushButton('/',self)
        self.btndz.clicked.connect(self.on_clickdz)
        self.btndz.resize(self.btndz.minimumSizeHint())
        self.gridLayout.addWidget(self.btndz,4,3)
        # btndz.move(200, 350)

        self.btneq = QPushButton('=',self)
        self.btneq.clicked.connect(self.on_clickeq)
        self.btneq.resize(self.btneq.minimumSizeHint())
        self.gridLayout.addWidget(self.btneq,4,2)

        self.btnC = QPushButton('C', self)
        self.btnC.clicked.connect(self.on_clickC)
        self.btnC.resize(self.btnC.minimumSizeHint())
        self.gridLayout.addWidget(self.btnC, 4, 1)

        # btneq.move(200, 300)
        self.btn0.setFixedSize(40, 40)
        self.btn1.setFixedSize(40, 40)
        self.btn2.setFixedSize(40, 40)
        self.btn3.setFixedSize(40, 40)
        self.btn4.setFixedSize(40, 40)
        self.btn5.setFixedSize(40, 40)
        self.btn6.setFixedSize(40, 40)
        self.btn7.setFixedSize(40, 40)
        self.btn8.setFixedSize(40, 40)
        self.btn9.setFixedSize(40, 40)
        self.btnp.setFixedSize(40, 40)
        self.btnm.setFixedSize(40, 40)
        self.btnmn.setFixedSize(40, 40)
        self.btndz.setFixedSize(40, 40)
        self.btneq.setFixedSize(40, 40)
        self.btnC.setFixedSize(40, 40)



    def on_click0(self):
        self.liczba = self.liczba*10 + 0
        print(self.liczba)

        self.textL = self.textL+"0"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click1(self):
        self.liczba = self.liczba * 10 + 1
        print(self.liczba)
        self.textL = self.textL+"1"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click2(self):
        self.liczba = self.liczba * 10 + 2
        print(self.liczba)
        self.textL = self.textL+"2"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1

    def on_click3(self):

        self.liczba = self.liczba * 10 + 3
        print(self.liczba)
        self.textL = self.textL+"3"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click4(self):
        self.liczba = self.liczba * 10 + 4
        print(self.liczba)
        self.textL = self.textL+"4"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        # self.licznik = self.licznik + 1

    def on_click5(self):
        self.liczba = self.liczba * 10 + 5
        print(self.liczba)
        self.textL = self.textL+"5"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click6(self):
        self.liczba = self.liczba * 10 + 6
        print(self.liczba)
        self.textL = self.textL+"6"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click7(self):
        self.liczba = self.liczba * 10 + 7
        print(self.liczba)
        self.textL = self.textL+"7"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click8(self):
        self.liczba = self.liczba * 10 + 8
        print(self.liczba)
        self.textL = self.textL+"8"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_click9(self):
        self.liczba = self.liczba * 10 + 9
        print(self.liczba)
        self.textL = self.textL+"9"
        if self.licznik == 0:
            self.textL = (str)(self.liczba)
        self.resultlabel.setText(self.textL)
        self.numberorsign = 1
        # self.licznik = self.licznik + 1

    def on_clickm(self):
        self.flagNew = self.flag
        self.flag = 2
        result = 0
        # first = self.numbers[-2]
        if self.liczba!=0:
            if self.licznik == 0:
                self.numbers.append(self.liczba)
        if self.numberorsign == 1:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                # print(self.numbers[-1],' - ',self.liczba,' = ',result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                if self.liczba!=0:
                    result = self.numbers[-1] / self.liczba
                    self.numbers.append(result)
                else:
                    self.resultlabel.setText("Nie dziel przez zero")
                    self.liczba = 0
                    return

        self.numberorsign = 2

        # self.numbers.append(self.liczba)
        self.liczba = 0


        print('wynik',self.numbers[-1])
        self.textL = self.textL+"-"
        self.resultlabel.setText(self.textL)
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickp(self):
        self.flagNew = self.flag
        self.flag = 1
        result = 0
        # first = self.numbers[-2]
        if self.liczba!=0:
            if self.licznik == 0:
                self.numbers.append(self.liczba)

        if self.numberorsign == 1:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                if self.liczba!=0:
                    result = self.numbers[-1] / self.liczba
                    self.numbers.append(result)
                else:
                    self.resultlabel.setText("Nie dziel przez zero")
                    self.liczba = 0
                    return

        self.numberorsign = 2
        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik', self.numbers[-1])
        self.textL = self.textL+"+"
        self.resultlabel.setText(self.textL)
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickmn(self):
        self.flagNew = self.flag
        self.flag = 3
        result = 0
        # first = self.numbers[-2]
        if self.liczba!=0:

            if self.licznik == 0:
                self.numbers.append(self.liczba)

        if self.numberorsign == 1:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                # print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                if self.liczba!=0:
                    result = self.numbers[-1] / self.liczba
                    self.numbers.append(result)
                else:
                    self.resultlabel.setText("Nie dziel przez zero")
                    self.liczba = 0
                    return

        self.numberorsign = 2
        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik', self.numbers[-1])
        # print(self.liczba)
        self.textL = self.textL+"*"
        self.resultlabel.setText(self.textL)
        self.licznik = self.licznik + 1

    def on_clickdz(self):
        self.flagNew = self.flag
        self.flag = 4
        result = 0
        # first = self.numbers[-2]
        if self.liczba!=0:
            if self.licznik == 0:
                self.numbers.append(self.liczba)
        if self.numberorsign == 1:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                if self.liczba!=0:
                    result = self.numbers[-1] / self.liczba
                    self.numbers.append(result)
                else:
                    self.resultlabel.setText("Nie dziel przez zero")
                    self.liczba = 0
                    return

        self.numberorsign = 2
        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik = ', self.numbers[-1])
        # print(self.liczba)
        self.textL = self.textL+"/"
        self.resultlabel.setText(self.textL)
        self.licznik = self.licznik + 1

    def on_clickeq(self):
        self.flagNew = self.flag
        self.flag = 0
        result = 0
        if self.numberorsign == 1:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                if self.liczba != 0:
                    result = self.numbers[-1] / self.liczba
                    self.numbers.append(result)
                else:
                    self.resultlabel.setText("Nie dziel przez zero")
                    self.liczba = 0
                    self.numbers = []
                    self.numbers.append(0)
                    self.licznik = 0
                    self.textL = ""
                    return
        print('wynik = ', self.numbers[-1])
        self.textL = self.textL+"="
        self.resultlabel.setText(self.textL+(str)(self.numbers[-1]))
        self.liczba = 0
        self.numbers = []
        self.numbers.append(0)
        self.licznik = 0
        self.textL = ""

    def on_clickC(self):
        self.liczba = 0
        self.numbers = []
        self.numbers.append(0)
        self.licznik = 0
        self.textL = ""
        self.textL = self.textL+"0"
        self.resultlabel.setText(self.textL)


    def close(self):
        choice = QMessageBox.question(self,'Extract',"Are you sure you want to quit?",QMessageBox.Yes|QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            sys.exit()
        else:
            pass

    def rozmiar_wiek(self):
        self.btn0.resize(100, 100)
        self.btn1.resize(100,100)

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_0:
            self.on_click0()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_1:
            self.on_click1()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_2:
            self.on_click2()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_3:
            self.on_click3()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_4:
            self.on_click4()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_5:
            self.on_click5()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_6:
            self.on_click6()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_7:
            self.on_click7()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_8:
            self.on_click8()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_9:
            self.on_click9()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Plus:
            self.on_clickp()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Minus:
            self.on_clickm()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Slash:
            self.on_clickdz()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Asterisk:
            self.on_clickmn()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_Equal:
            self.on_clickeq()
        if type(event) == QtGui.QKeyEvent and event.key() == QtCore.Qt.Key_C:
            self.on_clickC()

def run():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()
