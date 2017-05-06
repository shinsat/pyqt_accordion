from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi, loadUiType
from PyQt5.QtCore import *

import sys

class myTestWidget(QWidget):
    def __init__(self):
        super().__init__()
#        self.btn = loadUi('QPushButton.ui')
#        self.label = loadUi('QLabel.ui')
        widget = QWidget()

        vbox = QVBoxLayout()
        upper = QFrame()
        upper.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter = QSplitter(Qt.Vertical)

        self.v = QVBoxLayout()

        for _ in range(0, 15):
            h = QHBoxLayout()
            btn = QPushButton("BTN")
            label = QLabel("HOHOHOHO")

            h.addWidget(btn)
            h.addWidget(label)
            h.addStretch()

#            self.v.addLayout(h)
            vbox.addLayout(h)

        vbox2 = QVBoxLayout()
        bottomBtn = QPushButton("Next")
        bottomBtn.clicked.connect(self.refreshMe)
        vbox2.addWidget(bottomBtn)

        upper.setLayout(vbox)
        bottom.setLayout(vbox2)

        splitter.addWidget(upper)
        splitter.addWidget(bottom)

        self.v.addWidget(splitter)


#        self.v.addWidget(bottomBtn)

        widget.setLayout(self.v)


        #Scroll Area creation
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
    #    scroll.setWidget(self.v)
        scroll.setWidget(widget)

#        scroll.setWidget()
#        self.v.addWidget(scroll)

        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(scroll)
        self.setLayout(self.vLayout)
#        self.setLayout(self.v)
        self.show()

    def refreshMe(self):
        print("kk")

        self.vLayout.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = myTestWidget()
    sys.exit(app.exec_())


