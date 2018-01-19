
import pandas as pd

train = pd.read_csv("data/train.csv", index_col = 'id')
test = pd.read_csv("data/test.csv", index_col = 'id')
print(train.head(3))
print(test.head(3))