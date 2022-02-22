import concepts
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
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
te_result = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_result, columns=te.columns_)

itemset = apriori(df, use_colnames=True)
print(itemset)
rps = association_rules(itemset, metric="confidence", min_threshold=0.0)
rps = rps[['antecedents', 'consequents', 'support', 'confidence']]


print(rps)

val_list = rps.values.tolist()
print(val_list)


rps = association_rules(itemset, metric="support", min_threshold=0.0)
rps = rps[['antecedents', 'consequents', 'support', 'confidence']]


print(rps)

val_list = rps.values.tolist()
print(val_list)