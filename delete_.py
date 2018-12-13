
# coding: utf-8

import pandas as pd

bigdf=pd.read_csv('Big.csv')
smalldf=pd.read_csv('Small.csv')

for item in bigdf.columns:
    if item not in smalldf.columns:
        bigdf.drop(str(item), axis=1, inplace=True)
