import pandas as pd
from sklearn import preprocessing
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree

columnNames = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', \
               'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
census_train = pd.read_csv("adult.data.csv", header=None, names=columnNames)
census_train = census_train[['age', 'workclass', 'education-num', 'marital-status', 'occupation', \
               'race', 'sex', 'hours-per-week', 'native-country', 'income']]
census_train_notnull = census_train[(census_train['workclass'] != ' ?') & (census_train['occupation'] != ' ?') & (census_train['native-country'] != ' ?')]

encoder = preprocessing.OrdinalEncoder()
encoder.fit(census_train_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', 'native-country']])
census_train_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', 'native-country']] = \
encoder.transform(census_train_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', 'native-country']])

corr = census_train_notnull.corr()
#plt.figure(figsize=(12, 9))
#sns.heatmap(corr, annot=True)

census_train_notnull_x = census_train_notnull[['age', 'education-num', 'marital-status', 'sex', 'hours-per-week']]
census_train_notnull_y = census_train_notnull[['income']]
############

census_test = pd.read_csv("adult.test", header=None, names=columnNames)
census_test = census_test[['age', 'workclass', 'education-num', 'marital-status', 'occupation', \
               'race', 'sex', 'hours-per-week', 'native-country', 'income']].dropna()
census_test_notnull = census_test[(census_test['workclass'] != ' ?') & (census_test['occupation'] != ' ?') \
                                  & (census_test['native-country'] != ' ?')]

encoder_test = preprocessing.OrdinalEncoder()
encoder_test.fit(census_test_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', 'native-country']])
census_test_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', 'native-country']] = \
encoder_test.transform(census_test_notnull[['workclass', 'marital-status', 'occupation', 'race', 'sex', \
                                             'native-country']])

census_test_notnull_x = census_test_notnull[['age', 'education-num', 'marital-status', 'sex', 'hours-per-week']]
census_test_notnull_y = census_test_notnull[['income']]

sns.boxplot(x='income', y='age', data=census_train_notnull, orient='v').set_title('Box Plot for Income against age')
sns.set(rc={'figure.figsize':(5,5)})

age_plot_path = 'age_plot.png'
plt.savefig(age_plot_path)