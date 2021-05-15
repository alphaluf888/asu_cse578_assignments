import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

df = pd.read_csv('adult.data', names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', \
                                      'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', \
                                      'hours-per-week', 'native-country', 'income'])
df = df[['marital-status', 'occupation', 'income']]

maritalDf = pd.DataFrame(columns=['marital_status', 'gt50k', 'lt50k'])
for s in df['marital-status'].unique():
    gt50k = df[df['marital-status']==s]['income'].value_counts(normalize=True)[' >50K']
    lt50k = df[df['marital-status'] == s]['income'].value_counts(normalize=True)[' <=50K']
    maritalDf = maritalDf.append({'marital_status': s, 'gt50k': gt50k, 'lt50k': lt50k}, ignore_index=True)
print(maritalDf)
print(df['marital-status'].unique())
print(df['occupation'].unique())
occupationDf = pd.DataFrame(columns=['occupation', 'gt50k', 'lt50k'])
for s in df['occupation'].unique():
    gt50k = df[df['occupation']==s]['income'].value_counts(normalize=True)[' >50K']
    lt50k = df[df['occupation'] == s]['income'].value_counts(normalize=True)[' <=50K']
    occupationDf = occupationDf.append({'occupation': s, 'gt50k': gt50k, 'lt50k': lt50k}, ignore_index=True)
print(occupationDf)

#mosaic(df, ['marital-status', 'income'], label_rotation=90, labelizer=lambda k: "{:.0%}".format(maritalDf[maritalDf.marital_status==k[0]]['lt50k'].values[0]) if k[1] == " <=50K" else "", \
#       title="Income range by marital statuses")
#print(maritalDf.iloc[maritalDf[maritalDf.marital_status==' Never-married'], 2])
#mosaic(df, ['marital-status', 'income'], label_rotation=90, labelizer=lambda k: "", title="Income range by marital statuses")
#plt.show()
#plt.rcParams["figure.figsize"]=(250,250)
maritalDf.set_index("")
maritalDf.plot.bar(stacked=True)
plt.show()
#occupationDf.plot(x="occupation", kind='barh', stacked=False, title='Income range by occupation')
#plt.show()
