from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from tkinter import *
import tkinter.filedialog

import pandas as pd

def save_csv(table):
    try:
        csv_save = [[0 for col in range(table.columnCount()+1)] for row in range(table.rowCount()+1)]
        
        #object names to list        
        for x in range(table.columnCount()):
            csv_save[0][x] = (table.horizontalHeaderItem(x).text())

        #property names to list
        for y in range(table.rowCount()):
            csv_save[y+1][0] = (table.verticalHeaderItem(y).text())

        #bool to list
        for x in range(table.rowCount()):
            for y in range(table.columnCount()):
                csv_save[x+1][y+1] = (table.item(x,y).text())

        #기존 csv파일과 동일한 형식 유지
        csv_save[0].insert(0, 'name')
        csv_save[0].pop()
        
        try:
            #파일 탐색기 오픈 후 경로지정
            root = Tk().withdraw()
            title = 'Save project as'
            ftypes = [('csv file', '.csv'), ('Allfiles', '*')]
            filename = tkinter.filedialog.asksaveasfilename(filetypes=ftypes, title=title, initialfile='filename.csv')

            if '.csv' in filename or filename == '':
                pass
            else:
                filename = filename + '.csv'

            #파일 저장 코드
            # print(filename)
            dataframe = pd.DataFrame(csv_save)
            dataframe.to_csv(filename, header=False, index=False)
        except:
            pass

    except:
        QMessageBox.warning(table, 'Failed', 'Error!')