
import pandas as pd
import numpy as np


train1 = pd.read_csv('bare2015.csv')
train2 = pd.read_csv('bare2016.csv')
train3 = pd.read_csv('bare2017.csv')
train4 = pd.read_csv('Beastie2016.csv')
train5 = pd.read_csv('Beastie2017.csv')
train6 = pd.read_csv('Beastie2020.csv')
train7 = pd.read_csv('Gloomyday2013.csv')
train8 = pd.read_csv('Gloomyday2014.csv')
train9 = pd.read_csv('Gloomyday2015.csv')
train10 = pd.read_csv('Gloomyday2017.csv')
train11 = pd.read_csv('Graffiti.csv')
train12 = pd.read_csv('Gwangju2020.csv')
train13 = pd.read_csv('Gwangju2021.csv')
train14 = pd.read_csv('Interview2017.csv')
train15 = pd.read_csv('Interview2018.csv')
train16 = pd.read_csv('Lastgame.csv')
train17 = pd.read_csv('Mist.csv')
train18 = pd.read_csv('Nyinsky.csv')
train19 = pd.read_csv('Shadow.csv')
train20 = pd.read_csv('Sleuth.csv')
train21 = pd.read_csv('Smoke2018.csv')
train22 = pd.read_csv('TheDevil2014.csv')
train23 = pd.read_csv('TheDevil2017.csv')
train24 = pd.read_csv('Trainspotting.csv')
train25 = pd.read_csv('Vanishing2017.csv')
train26 = pd.read_csv('Vanishing2018.csv')
train27 = pd.read_csv('Vanishing2020.csv')
train28 = pd.read_csv('PJH.csv')
train29 = pd.read_csv('Wewillrockyou.csv')

df_train = pd.concat([train1,train2, train3,train4,train5, train6,train7,train8, train9,train10,train11, train12,train13,train14, train15,train16,train17, train18,train19,train20, train21,train22,train23, train24,train25, train26,train27,train28, train29], ignore_index = True)

df_train = df_train.drop([df_train.columns[0]], axis=1)

df_train

df_train.to_csv('train_data.csv', encoding = "utf-8-sig")

test1 = pd.read_csv('bare2020.csv')
test2 = pd.read_csv('Beastieboys2014.csv')
test3 = pd.read_csv('Gloomyday2019.csv')
test4 = pd.read_csv('Smoke2017.csv')
test5 = pd.read_csv('TheDevil2018.csv')
test6 = pd.read_csv('Vanishing.csv')

df_test = pd.concat([test1, test2, test3, test4, test5, test6], ignore_index=True)

df_test = df_test.drop([df_test.columns[0]], axis = 1)

df_test.to_csv('test_data.csv', encoding = "utf-8-sig")

train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

