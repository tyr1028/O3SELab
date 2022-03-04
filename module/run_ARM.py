from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth
from mlxtend.frequent_patterns import association_rules
import pandas as pd

def run_ARM(csv, sup_val, conf_val, ARM_table):
    try:
        #데이터셋 만들기
        dataset = []

        #가져온 support, confidence값 설정
        min_sup = sup_val * 0.01
        min_conf = conf_val * 0.01

        for i in range(len(csv.bools)):
            list_ = []
            for j in range(len(csv.bools[i])):
                if(csv.bools[i][j]):
                    list_.append(csv.properties[j])

            dataset.append(list_)

        te = TransactionEncoder()
        te_result = te.fit(dataset).transform(dataset)
        df = pd.DataFrame(te_result, columns=te.columns_)

        # itemset = fpgrowth(df, min_support=0.01, use_colnames=True)
        itemset = apriori(df, min_support=0.01, use_colnames=True)

        #min_confidence로 Association rule 생성, 표시할 부분들 추가
        rps = association_rules(itemset, metric="confidence", min_threshold = min_conf)
        rps = rps[['antecedents', 'consequents', 'support', 'confidence']]

        #생성한 Association rule에서 min_support 설정하는 부분 추가
        rps = rps[ (rps['support'] >= min_sup)]

        #frozenset str로 바꾸는 부분
        rps["antecedents"] = rps["antecedents"].apply(lambda x: list(x)).astype("unicode")
        rps["consequents"] = rps["consequents"].apply(lambda x: list(x)).astype("unicode")

        #list형식으로 변경
        ARS = rps.values.tolist()

        #Row카운트
        cnt = 0

        #Row갯수 설정
        ARM_table.setRowCount(len(ARS))

        #for문 시작 double부분 str로 설정해야 들어감
        for rule in ARS:
            ARM_table.setItem(cnt, 0, QTableWidgetItem(rule[0]))
            ARM_table.setItem(cnt, 1, QTableWidgetItem(rule[1]))
            ARM_table.setItem(cnt, 2, QTableWidgetItem((str)(rule[2])))
            ARM_table.setItem(cnt, 3, QTableWidgetItem((str)(rule[3])))
            #반복횟수 카운트
            cnt = cnt + 1
    except:
        QMessageBox.warning(ARM_table, 'Failed', 'Error!')