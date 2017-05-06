from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
# window.setWindowTitle('QPushButton')
# window.setGeometry(50,50,600,400)

button = QPushButton('Close', window)

window.show()
app.exec_()