import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class myAccordionItem(QWidget):
    def __init__(self):
        super().__init__()


        pushButton = QPushButton("Hide")
        pushButton.setCheckable(True)
        #pushButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.textArea = QTextBrowser()
        self.textArea.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        pushButton.clicked.connect(lambda checked: self.buttonClicked(checked, self.textArea))

        h = QHBoxLayout()
        h.addWidget(pushButton)
        h.addWidget(self.textArea)

#        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setLayout(h)
        self.show()
#        v.setAlignment(self, Qt.AlignTop)


#        v.addLayout(h)

    def buttonClicked(self, checked, textArea):
        if checked:
            print("checked")
            textArea.hide()
            self.update()
            self.sizeHint()
        else:
            print("notChecked")
            textArea.show()
            self.update()
            self.sizeHint()


class myAccordionSample(QWidget):
    def __init__(self):
        super().__init__()

        v = QVBoxLayout()

        for _ in range(3):
            ui = myAccordionItem()
            v.addWidget(ui)

#        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setLayout(v)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = myAccordionSample()
#    ui = myAccordionItem()

    sys.exit(app.exec_())
