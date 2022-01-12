from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import concepts

import sys

class DCA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FactChecker')
        self.setWindowIcon((QIcon('icon.png')))
        self.setGeometry(100, 100, 1200, 900)

        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(1200, 900)

        self.csvbutton = QPushButton('Load csv')
        self.Iconlabel = QLabel()
        self.csvbutton.clicked.connect(self.open_csv)
        self.Iconlabel.setPixmap(QPixmap("Icon.png"))
        self.csvbutton.setMaximumWidth(100)

        self.csvbutton.move(20, 20)
        self.Iconlabel.move(600,450)

        self.iconlayout = QHBoxLayout()
        self.iconlayout.addStretch(1)
        self.iconlayout.addWidget(self.Iconlabel)
        self.iconlayout.addStretch(1)

        self.tab1.layout = QVBoxLayout()
        self.tab1.layout.addWidget(self.csvbutton)
        self.tab1.layout.addLayout(self.iconlayout)

        self.tab1.setLayout(self.tab1.layout)

        self.tabs.addTab(self.tab1, "main")
        self.tabs.addTab(self.tab2, "show formal context")
        self.tabs.addTab(self.tab3, "run FCA")
        self.tabs.addTab(self.tab4, "show concept lattice")
        self.tabs.addTab(self.tab5, "extract association rules")
        self.tabs.addTab(self.tab6, "A.R.M")
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.show()
    
    def open_csv(self):
        fname = QFileDialog.getOpenFileName(self)
        self.csv = concepts.load_csv(fname[0])

app = QApplication(sys.argv)
ex = DCA()
sys.exit(app.exec_())