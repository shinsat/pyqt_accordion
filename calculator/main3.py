import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.CreateApp()


    def CreateApp(self):

        # Create our grid
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["AC", "C", "CE", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        row = 1
        col = 0

        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            if button == 0:
                grid.addWidget(QPushButton(str(button)), row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(QPushButton(str(button)), row, col, 1, 1)

            col += 1


        self.setLayout(grid)

        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())
