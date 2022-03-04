import concepts
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules, fpgrowth
import pandas as pd


csv = concepts.load_csv('TestData.csv')

dataset = []

for i in range(len(csv.bools)):
    list_ = []
    for j in range(len(csv.bools[i])):
        if(csv.bools[i][j]):
            list_.append(csv.properties[j])

    dataset.append(list_)

print(dataset)

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

print(frequent_itemsets)

te = TransactionEncoder()
te_result = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_result, columns=te.columns_)

itemset = apriori(df, use_colnames=True)
print(itemset)

rps = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.0)
rps = rps[['antecedents', 'consequents', 'support', 'confidence']]


print(rps)

rps = rps[ (rps['support'] >= 0.0)]

# val_list = rps.values.tolist()
# print(val_list)


# rps = association_rules(itemset, metric="support", min_threshold=0.0)
# rps = rps[['antecedents', 'consequents', 'support', 'confidence']]

rps["antecedents"] = rps["antecedents"].apply(lambda x: list(x)).astype("unicode")
rps["consequents"] = rps["consequents"].apply(lambda x: list(x)).astype("unicode")


print(rps)