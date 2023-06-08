import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


def encode_onehot(val, labels):
    return pd.Series([1 if label == val else 0 for label in labels])


labels = data['whoAmI'].unique()

onehot_data = data['whoAmI'].apply(lambda x: encode_onehot(x, labels))

onehot_data.columns = labels

onehot_data.head()
