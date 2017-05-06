import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Model(QAbstractItemModel):
    def __init__(self, parent=None):
        super(Model,self).__init__(parent)
        self.items = [
            ['たぬき','そば','温'],
            ['きつね', 'うどん', '温'],
            ['月見', 'そば', 'ひや'],
            ['天ぷら', 'うどん', 'ひや']
        ]

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column, None)

    def parent(self, child):
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        if self.items:
            return max([len(item) for item in self.items])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            try:
                return self.items[index.row()][index.column()]
            except:
                return None
        return


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        view = QTableView(self)
        model = Model(self)
        view.setModel(model)
        self.setCentralWidget(view)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()


if __name__ == "__main__":
    main()







