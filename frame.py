# Fact Checker
# O3SE Lab

# [진행상황]


# [계획]
# main
# File을 Load후에 반응이 없어서 제대로 로드되었는지 확인 할 수 없음 -> 완료

# show formal context
# 표의 형태로 구현하기
# 표의 크기를 자연스럽고 보기좋게 할 수 있게 만들기. ->완료

# [Concept Explorer]
# 표가 나오고 셀을 클릭할 때 체크상태에 따라 체크, 체크해제 가능

# Object와 Attribute들의 교환 버튼 존재
# Object 늘리기 버튼 줄이기 버튼

# Attribute 늘리기 버튼 줄이기 버튼
# Attribute Name 줄이기 버튼

# Object Count ->완료
# Attribute Count ->완료

# 실행 취소 버튼

# 다시 저장하기 버튼

# run FCA ->완료
#

# show concept lattice ->진행중

# extract association rules

# a.r.m



from fileinput import filename
from msilib.schema import Directory
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import pandas as pd

from tkinter import *
import tkinter.filedialog

import concepts
import sys

from pdf2image import convert_from_path

from PIL import Image

from module.save_csv import save_csv
from module.run_show_formal_context import run_Show_formal_context
from module.run_FCA import run_FCA

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

class DCA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #윈도우창 이름, 아이콘, 창 크기
        self.setWindowTitle('FactChecker')
        self.setWindowIcon((QIcon('source/icon.png')))
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
        self.Iconlabel.setPixmap(QPixmap("source/icon.png"))
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
        self.runbutton_2.clicked.connect(lambda:run_Show_formal_context(self.table, self.csv, self.objects, self.properties))
        self.savebutton_2 = QPushButton('Save')
        self.savebutton_2.clicked.connect(lambda:save_csv(self.table))

        self.objects = QLabel('objects: ')
        self.properties = QLabel('properties: ')

        self.table = QTableWidget(self)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch) # 추후 수정

        self.buttons_2 = QHBoxLayout()
        self.buttons_2.addWidget(self.runbutton_2)
        self.buttons_2.addWidget(self.savebutton_2)

        self.information = QVBoxLayout()
        self.information.addStretch(0)
        self.information.addWidget(self.objects)
        self.information.addStretch(0)
        self.information.addWidget(self.properties)
        self.information.addStretch(1)

        self.table_and_information = QHBoxLayout()
        self.table_and_information.addLayout(self.information)
        self.table_and_information.addWidget(self.table)


        # 셀 내용 채우기
        self.table.setItem(0, 0, QTableWidgetItem('0'))

        self.tab2.layout = QVBoxLayout()
        self.tab2.layout.addLayout(self.buttons_2)
        self.tab2.layout.addLayout(self.table_and_information)
        self.tab2.setLayout(self.tab2.layout)

        #탭3(run fca)
        #run 버튼
        self.runbutton_3 = QPushButton('Run') 
        self.runbutton_3.clicked.connect(lambda:run_FCA(self.csv, self.FCA_table))

        #extent intent만 필요함, 마지막줄은 화면에 자동으로 크기 맞춰주는 코드
        self.FCA_table = QTableWidget(self)
        self.FCA_table.setColumnCount(2)
        self.FCA_table.setHorizontalHeaderLabels(['Extent','Intent'])
        self.FCA_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #레이아웃 추가
        self.tab3.layout = QVBoxLayout()
        self.tab3.layout.addWidget(self.runbutton_3)
        self.tab3.layout.addWidget(self.FCA_table)

        self.tab3.setLayout(self.tab3.layout)

        #탭4(show concept lattice)
        self.runbutton_4 = QPushButton('Run and Save') 
        self.runbutton_4.clicked.connect(self.concept_lattice)
        self.savebutton_4 = QPushButton('Show')
        self.savebutton_4.clicked.connect(self.show_lattice)

        self.image_scroll = QScrollArea()
        self.image_scroll.setAlignment(Qt.AlignCenter)
        self.image_scroll.resize(800, 600)
        self.lattice_img = QLabel()
        self.lattice_img.setScaledContents(True)

        self.image_slider = QSlider(Qt.Horizontal, self)
        self.image_slider.setTickPosition(2)
        self.image_slider.setTickInterval(1)
        self.image_slider.setRange(5, 20)
        self.image_slider.setValue(10)
        self.image_slider.setSingleStep(1)
        self.image_slider.valueChanged.connect(self.image_size)

        self.zoom_value = str(self.image_slider.value()*0.1)
        self.zoom_rate = QLabel("Zoom: " + self.zoom_value[0:3])

        self.buttons_4 = QHBoxLayout()
        self.buttons_4.addWidget(self.runbutton_4)
        self.buttons_4.addWidget(self.savebutton_4)

        self.tab4.layout = QVBoxLayout()
        self.tab4.layout.addLayout(self.buttons_4)
        self.tab4.layout.addWidget(self.image_slider)
        self.tab4.layout.addWidget(self.zoom_rate)
        self.tab4.layout.addWidget(self.image_scroll)

        self.tab4.setLayout(self.tab4.layout)

        #탭5(extract association rules)
        self.min_support = QLabel("minimum support :")
        self.min_conf = QLabel("minimum confidence :")

        #입력받는 부분
        self.support_val = QLineEdit()
        self.support_val.setPlaceholderText("Enter support(0 ~ 1) value")
        self.conf_val = QLineEdit()
        self.conf_val.setPlaceholderText("Enter confidence(0 ~ 1) value")

        self.runbutton_5 = QPushButton('Run')
        self.savebutton_5 = QPushButton('Save')

        self.association_rule_table = QTableWidget(self)
        self.association_rule_table.setHorizontalHeaderLabels(['antecedents', 'consequence', 'support', 'confidence'])
        self.association_rule_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.conf_sup_layout = QHBoxLayout()
        self.conf_sup_layout.addWidget(self.min_support)
        self.conf_sup_layout.addWidget(self.support_val)
        self.conf_sup_layout.addWidget(self.min_conf)
        self.conf_sup_layout.addWidget(self.conf_val)

        self.buttons_5 = QHBoxLayout()
        self.buttons_5.addWidget(self.runbutton_5)
        self.buttons_5.addWidget(self.savebutton_5)

        self.tab5.layout = QVBoxLayout()
        self.tab5.layout.addLayout(self.conf_sup_layout)
        self.tab5.layout.addLayout(self.buttons_5)
        self.tab5.layout.addWidget(self.association_rule_table)

        self.tab5.setLayout(self.tab5.layout)

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
        #csv파일 불러오는 버튼 클릭시 파일탐색기 열기
        fname = QFileDialog.getOpenFileName(self)
        try:
            self.csv = concepts.load_csv(fname[0])
            QMessageBox.information(self, 'Success', 'Load Success')
            self.loadname.setText(fname[0])
        except:
            QMessageBox.warning(self, 'Failed', 'Load Failed')

    def concept_lattice(self):
        try:
            self.ltc = self.csv.lattice
            self.viz = self.ltc.graphviz(render=True)
            print(self.ltc)
        except:
            QMessageBox.warning(self, 'Failed', 'Error!')
    
    #pip install pdf2image
    def show_lattice(self):
        try:
            self.pages = convert_from_path('Lattice.gv.pdf')

            self.pages[0].save('lattice.png', 'PNG')

            filename = 'lattice.png'

            self.img_lattice = Image.open(filename)

            self.lattice_img.setPixmap(QPixmap(filename))

            #내꺼 테스트할때 쓰는 코드
            # self.img_lattice = Image.open('page0.jpg')

            # self.lattice_img.setPixmap(QPixmap('page0.jpg'))
            self.image_scroll.setWidget(self.lattice_img)
 
        except:
            QMessageBox.warning(self, 'Failed', 'Error!')
    
    def image_size(self):
        self.lattice_size = self.img_lattice.size
        self.lattice_img.resize(int(self.lattice_size[0]*(self.image_slider.value()*0.1)),int(self.lattice_size[1]*(self.image_slider.value()*0.1)))

        self.zoom_value = str(self.image_slider.value()*0.1)
        self.zoom_rate.setText("Zoom: " + self.zoom_value[0:3])

app = QApplication(sys.argv)
ex = DCA()
sys.exit(app.exec_())