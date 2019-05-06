import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import sqrt

NUM = 0.0
NEW_NUMBER = 0.0
SUM_IT = 0.0
RESULT = 0.0
SYMBOL = ""

OPERATION = False


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'This is a cool calculator'
        self.left = 300
        self.top = 300
        self.width = 270
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(260, 420)

        self.line = QLineEdit(self)
        self.line.move(10, 10)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(40)
        self.line.setFont(font)
        self.line.resize(240, 70)
        self.line.setStyleSheet("border: none; background: #323232;")

        # numbers
        zero = QPushButton("0", self)
        zero.move(5, 350)
        zero.resize(130, 70)
        zero.clicked.connect(self.show_numbers)
        zero.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")
        one = QPushButton("1", self)
        one.move(5, 290)
        one.resize(70, 70)
        one.clicked.connect(self.show_numbers)
        one.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        two = QPushButton("2", self)
        two.move(65, 290)
        two.resize(70, 70)
        two.clicked.connect(self.show_numbers)
        two.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        three = QPushButton("3", self)
        three.move(125, 290)
        three.resize(70, 70)
        three.clicked.connect(self.show_numbers)
        three.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        four = QPushButton("4", self)
        four.move(5, 230)
        four.resize(70, 70)
        four.clicked.connect(self.show_numbers)
        four.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        five = QPushButton("5", self)
        five.move(65, 230)
        five.resize(70, 70)
        five.clicked.connect(self.show_numbers)
        five.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        six = QPushButton("6", self)
        six.move(125, 230)
        six.resize(70, 70)
        six.clicked.connect(self.show_numbers)
        six.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        seven = QPushButton("7", self)
        seven.move(5, 170)
        seven.resize(70, 70)
        seven.clicked.connect(self.show_numbers)
        seven.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        eight = QPushButton("8", self)
        eight.move(65, 170)
        eight.resize(70, 70)
        eight.clicked.connect(self.show_numbers)
        eight.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        nine = QPushButton("9", self)
        nine.move(125, 170)
        nine.resize(70, 70)
        nine.clicked.connect(self.show_numbers)
        nine.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        # SYMBOLS
        plus = QPushButton("+", self)
        plus.move(185, 290)
        plus.resize(70, 70)
        plus.clicked.connect(self.symbol)
        plus.setStyleSheet(
            "QPushButton { background-color: #FF9500; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #BE6A0A; }")

        minus = QPushButton("-", self)
        minus.move(185, 230)
        minus.resize(70, 70)
        minus.clicked.connect(self.symbol)
        minus.setStyleSheet(
            "QPushButton { background-color: #FF9500; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #BE6A0A; }")

        multiply = QPushButton("x", self)
        multiply.move(185, 170)
        multiply.resize(70, 70)
        multiply.clicked.connect(self.symbol)
        multiply.setStyleSheet(
            "QPushButton { background-color: #FF9500; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #BE6A0A; }")

        divide = QPushButton("÷", self)
        divide.move(185, 110)
        divide.resize(70, 70)
        divide.clicked.connect(self.symbol)
        divide.setStyleSheet(
            "QPushButton { background-color: #FF9500; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #BE6A0A; }")

        point = QPushButton(".", self)
        point.move(125, 350)
        point.resize(70, 70)
        point.clicked.connect(self.point)
        point.setStyleSheet(
            "QPushButton { background-color: #505050; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #D4D4D2; }")

        equals = QPushButton("=", self)
        equals.move(185, 350)
        equals.resize(70, 70)
        equals.clicked.connect(self.symbol)
        equals.setStyleSheet(
            "QPushButton { background-color: #FF9500; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #BE6A0A; }")

        ce = QPushButton("CE", self)
        ce.move(5, 110)
        ce.resize(70, 70)
        ce.clicked.connect(self.ce)
        ce.setStyleSheet(
            "QPushButton { background-color: #1C1C1C; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #505050; }")

        root = QPushButton("√", self)
        root.move(125, 110)
        root.resize(70, 70)
        root.clicked.connect(self.root)
        root.setStyleSheet(
            "QPushButton { background-color: #1C1C1C; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #505050; }")

        c = QPushButton("C", self)
        c.move(65, 110)
        c.resize(70, 70)
        c.clicked.connect(self.c)
        c.setStyleSheet(
            "QPushButton { background-color: #1C1C1C; font-size: 20px; border-style: solid; border-width: 1px; margin-left: 7px; margin-top: 4px; margin-right: 6; margin-bottom: 8px } QPushButton:pressed { background-color: #505050; }")

        self.show()

    def point(self):
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")

    def ce(self):
        self.line.backspace()

    def c(self):
        global NUM
        global NEW_NUMBER
        global RESULT
        global SYMBOL

        self.line.clear()
        NUM = 0.0
        NEW_NUMBER = 0.0
        RESULT = 0.0
        SYMBOL = ""

    def root(self):
        try:
            NUM = float(self.line.text())
        except ValueError:
            return
        NUM = sqrt(NUM)
        self.line.setText(str(NUM))

    def show_numbers(self):
        global NUM
        global NEW_NUMBER
        global OPERATION

        sender = self.sender()
        NEW_NUMBER = int(sender.text())
        set_num = str(NEW_NUMBER)

        if OPERATION == False:
            self.line.setText(self.line.text() + set_num)
        else:
            self.line.setText(set_num)
            OPERATION = False

    def symbol(self):
        global SUM_IT
        global NUM
        global OPERATION
        global SYMBOL

        SUM_IT += 1

        if SUM_IT > 1:
            self.equal()

        NUM = self.line.text()
        sender = self.sender()
        SYMBOL = sender.text()

        OPERATION = True

    def equal(self):
        global NUM
        global NEW_NUMBER
        global RESULT
        global SYMBOL
        global OPERATION
        global SUM_IT

        SUM_IT = 0

        NEW_NUMBER = self.line.text()
        if SYMBOL == "+":
            RESULT = float(NUM) + float(NEW_NUMBER)
        elif SYMBOL == "-":
            RESULT = float(NUM) - float(NEW_NUMBER)
        elif SYMBOL == "x":
            RESULT = float(NUM) * float(NEW_NUMBER)
        elif SYMBOL == "÷":
            RESULT = float(NUM) / float(NEW_NUMBER)

        self.line.setText(str(RESULT))
        OPERATION = True


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(APP.exec_())
