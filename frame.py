from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

        self.tabs.addTab(self.tab1, "main")
        self.tabs.addTab(self.tab2, "show formal context")
        self.tabs.addTab(self.tab3, "run FCA")
        self.tabs.addTab(self.tab4, "show concept lattice")
        self.tabs.addTab(self.tab5, "extract association rules")
        self.tabs.addTab(self.tab6, "A.R.M")
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.show()

app = QApplication(sys.argv)
ex = DCA()
sys.exit(app.exec_())