from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def run_FCA(csv, FCA_table):
    try:
        #반복횟수
        cnt = 0

        #lattice 설정
        lattice = csv.lattice

        #FCA개수만큼 row설정
        FCA_table.setRowCount(len(lattice))

        #for문 시작
        for extent, intent in lattice:
            #extent, intent 초기화
            extent_str = ''
            intent_str = ''
            if len(extent) <= 0:
                #아무것도 없으면 비어있는 리스트
                FCA_table.setItem(cnt, 0, QTableWidgetItem('[ ]'))
            else:
                for i in extent:
                    #extent 하나씩 추출해서 뒤에 콤마 붙여주기
                    extent_str = extent_str + i + ','
                #마지막 콤마 삭제
                extent_str = extent_str[:-1]
                #꺾쇠괄호 달아주기
                FCA_table.setItem(cnt, 0, QTableWidgetItem('[' + extent_str + ']'))
            
            #intent부분 같음
            if len(intent) <= 0:
                FCA_table.setItem(cnt, 1, QTableWidgetItem('[ ]'))
            else:
                for i in intent:
                    intent_str = intent_str + i + ','
                intent_str = intent_str[:-1]
                FCA_table.setItem(cnt, 1, QTableWidgetItem('[' + intent_str + ']'))
            #반복횟수 카운트
            cnt = cnt + 1
    except:
        QMessageBox.warning(FCA_table, 'Failed', 'Error!')