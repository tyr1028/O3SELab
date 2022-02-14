from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def run_Show_formal_context(table, csv, objects, properties):
    try:
        #불러온 csv파일로 테이블 크기 설정
        table.setColumnCount(len(csv.properties))
        table.setRowCount(len(csv.objects))

        #테이블 헤더 설정
        table.setHorizontalHeaderLabels(csv.properties)
        table.setVerticalHeaderLabels(csv.objects)

        #테이블 아이템 설정
        for i in range(len(csv.objects)):
            for j in range(len(csv.properties)):
                if(csv.bools[i][j]):
                    table.setItem(i, j, QTableWidgetItem('X'))
                else:
                    table.setItem(i, j, QTableWidgetItem())
        
        #object, properties 수
        objects.setText('objects: ' + str(len(csv.objects)))
        properties.setText('properties: ' + str(len(csv.properties)))
    except:
        QMessageBox.warning(table, 'Failed', 'Error!')