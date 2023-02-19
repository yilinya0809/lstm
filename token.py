
import sys
!{sys.executable} -m pip install --upgrade pip

import sys
!{sys.executable} -m pip install konlpy

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import jpype

okt = Okt()

train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

print('훈련용 리뷰 개수 :',len(train_data))
print('테스트용 리뷰 개수 :',len(test_data))

train_data['Reviews'].nunique()

test_data['Reviews'].nunique()

train_data.drop_duplicates(subset=['Reviews'], inplace=True)
test_data.drop_duplicates(subset=['Reviews'], inplace=True)

print('훈련용 샘플의 수 :',len(train_data))
print('테스트용 샘플의 수 :',len(test_data))

train_data['Score'].value_counts().plot(kind = 'bar')

print(train_data.groupby('Score').size().reset_index(name = 'count'))

print(train_data.isnull().values.any())

## Train 데이터 전처리
## 한글과 공백을 제외하고 모두 제거
train_data['Reviews'] = train_data['Reviews'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

## 빈 샘플을 null로 변경, 개수 확인
train_data['Reviews'] = train_data['Reviews'].str.replace('^ +', "") # 공백은 empty로 변경
train_data['Reviews'].replace('', np.nan, inplace=True)
print(train_data.isnull().sum())

## null 샘플 제거
train_data = train_data.dropna(how = 'any')
print(len(train_data))

## Test 데이터 전처리

test_data['Reviews'] = test_data['Reviews'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
test_data['Reviews'] = test_data['Reviews'].str.replace('^ +', "")
test_data['Reviews'].replace('', np.nan, inplace=True)
test_data = test_data.dropna(how='any') # Null 값 제거
print('전처리 후 테스트용 샘플의 개수 :',len(test_data))

## 토큰화

## 불용어 제거

stopwords = ['의','가','이','은','들','는','과','도','를','으로','자','에','와','한','하다',
            '베어','베어더뮤지컬','뮤지컬','연극','비스티','사의찬미','사찬','글루미데이','그라피티','그랖','광주','인터뷰','인텁','뮤텁',
            '마지막사건','막사','미스트','미슽','니진스키','니진','박정희','그판사','그림자를판사나이','슬루스','스모크','스뫀','더데빌','더뎁',
            '트레인스포팅','트스','배니싱','밴싱','위윌락유','첫공','막공','인터파크']
