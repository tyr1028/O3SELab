# Fact Checker
# O3SE Lab

# [진행상황]


# [계획]
# main
# File을 Load후에 반응이 없어서 제대로 로드되었는지 확인 할 수 없음 -> 완료

# show formal context
# 표의 형태로 구현하기
# 표의 크기를 자연스럽고 보기좋게 할 수 있게 만들기.

# [Concept Explorer]
# 표가 나오고 셀을 클릭할 때 체크상태에 따라 체크, 체크해제 가능

# Object와 Attribute들의 교환 버튼 존재
# Object 늘리기 버튼 줄이기 버튼

# Attribute 늘리기 버튼 줄이기 버튼
# Attribute Name 줄이기 버튼

# Object Count
# Attribute Count

# 실행 취소 버튼

# 다시 저장하기 버튼

# run FCA
#

# show concept lattice

# extract association rules

# a.r.m



from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import concepts

import sys

class DCA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #윈도우창 이름, 아이콘, 창 크기
        self.setWindowTitle('FactChecker')
        self.setWindowIcon((QIcon('icon.png')))
        self.setGeometry(100, 100, 1200, 900)

        #레이아웃 설정
        self.layout = QVBoxLayout(self)

        #탭 생성
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(1200, 900)

        #탭1(main) 버튼, 아이콘 생성
        self.csvbutton = QPushButton('Load csv')
        self.Iconlabel = QLabel()
        self.csvbutton.clicked.connect(self.open_csv)
        self.Iconlabel.setPixmap(QPixmap("Icon.png"))
        self.csvbutton.setMaximumWidth(100)
        
        #로드한 파일 이름 표시
        self.loadname = QLabel()
        self.loadname.setStyleSheet("background-color: #FFFFFF;"
                                    "border-style: solid;"
                                    "border-width: 1px;"
                                    "border-color: #000000")
        self.loadname.setText("")

        #아이콘 중앙배치
        self.iconlayout = QHBoxLayout()
        self.iconlayout.addStretch(1)
        self.iconlayout.addWidget(self.Iconlabel)
        self.iconlayout.addStretch(1)
        
        #버튼과 파일위치 레이아웃 추가
        self.bflayout = QHBoxLayout()
        self.bflayout.addWidget(self.csvbutton)
        self.bflayout.addWidget(self.loadname)

        #버튼, 아이콘 레이아웃 추가
        self.tab1.layout = QVBoxLayout()
        self.tab1.layout.addStretch(0)
        self.tab1.layout.addLayout(self.bflayout)
        self.tab1.layout.addStretch(1)
        self.tab1.layout.addLayout(self.iconlayout)
        self.tab1.layout.addStretch(0)

        #탭에 레이아웃 설정
        self.tab1.setLayout(self.tab1.layout)
    
        #탭2(show formal context)
        self.runbutton_2 = QPushButton('Run') 
        self.runbutton_2.clicked.connect(self.run_Show_formal_context)
        self.savebutton_2 = QPushButton('Save')
        self.savebutton_2.clicked.connect(self.save_csv)

        self.table = QTableWidget(self)

        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.runbutton_2)
        self.buttons.addWidget(self.savebutton_2)

        # 셀 내용 채우기
        self.table.setItem(0, 0, QTableWidgetItem('0'))

        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addLayout(self.buttons)
        self.tab2.layout.addWidget(self.table)
        self.tab2.setLayout(self.tab2.layout)

        #탭3(run fca)

        #탭4(show concept lattice)

        #탭5(extract association rules)

        #탭6(A.R.M)

        #탭 통합
        self.tabs.addTab(self.tab1, "Main")
        self.tabs.addTab(self.tab2, "Show formal context")
        self.tabs.addTab(self.tab3, "Run FCA")
        self.tabs.addTab(self.tab4, "Show concept lattice")
        self.tabs.addTab(self.tab5, "Extract association rules")
        self.tabs.addTab(self.tab6, "A.R.M")
        
        #레이아웃 메인으로 집어넣기
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.show()
    
    def open_csv(self):
        #csv파일 불러오는 버튼 클릭시
        fname = QFileDialog.getOpenFileName(self)
        try:
            self.csv = concepts.load_csv(fname[0])
            QMessageBox.information(self, 'Success', 'Load Success')
            self.loadname.setText(fname[0])
        except:
            QMessageBox.warning(self, 'Failed', 'Load Failed')

    def run_Show_formal_context(self):
        try:
            self.table.setColumnCount(len(self.csv.properties))
            self.table.setRowCount(len(self.csv.objects))
            self.table.setHorizontalHeaderLabels(self.csv.properties)
            self.table.setVerticalHeaderLabels(self.csv.objects)
            for i in range(len(self.csv.objects)):
                for j in range(len(self.csv.properties)):
                    if(self.csv.bools[i][j]):
                        self.table.setItem(i, j, QTableWidgetItem('X'))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem())
        except:
            QMessageBox.warning(self, 'Failed', 'Error!')
    
    def save_csv(self):
        pass

app = QApplication(sys.argv)
ex = DCA()
sys.exit(app.exec_())