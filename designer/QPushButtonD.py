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

        self.v = QVBoxLayout()

        for _ in range(0, 20):
            h = QHBoxLayout()
            btn = QPushButton("BTN")
            label = QLabel("HOHOHOHO")

            h.addWidget(btn)
            h.addWidget(label)
            h.addStretch()

            self.v.addLayout(h)
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

        vLayout = QVBoxLayout()
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)
#        self.setLayout(self.v)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = myTestWidget()
    sys.exit(app.exec_())


