'''Вот мой вариант исполнения вида one hot без использования встроенной функции'''
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

new_col = list(set(data['whoAmI']))

for i in new_col:
    new_list = []
    for el in range(len(data['whoAmI'])):
        if i == data['whoAmI'][el]:
            new_list.append(1)
        else:
            new_list.append(0)
    data[i] = new_list

data.head()
