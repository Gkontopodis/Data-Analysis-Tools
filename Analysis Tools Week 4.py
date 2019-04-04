# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:11:22 2019

@author: Voltas
"""

import pandas
import numpy 
import seaborn
import scipy
import matplotlib.pyplot as plt

nesarc = pandas.read_csv ('nesarc_pds.csv', low_memory=False)

# Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns' , None)

# Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows' , None)

nesarc.columns = map(str.upper , nesarc.columns)

pandas.set_option('display.float_format' , lambda x:'%f'%x)

# Change my variables to numeric

nesarc['AGE'] = nesarc['AGE'].convert_objects(convert_numeric=True)
nesarc['MAJORDEP12'] = nesarc['MAJORDEP12'].convert_objects(convert_numeric=True)
nesarc['S1Q231'] = nesarc['S1Q231'].convert_objects(convert_numeric=True)
nesarc['S3BQ1A5'] = nesarc['S3BQ1A5'].convert_objects(convert_numeric=True)
nesarc['S3BD5Q2E'] = nesarc['S3BD5Q2E'].convert_objects(convert_numeric=True)

# Subset my sample

subset1 = nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30) & nesarc['S3BQ1A5']==1]     # Ages 18-30, cannabis users
subsetc1 = subset1.copy()

# Setting missing data

subsetc1['S1Q231']=subsetc1['S1Q231'].replace(9, numpy.nan)
subsetc1['S3BQ1A5']=subsetc1['S3BQ1A5'].replace(9, numpy.nan)
subsetc1['S3BD5Q2E']=subsetc1['S3BD5Q2E'].replace(99, numpy.nan)
subsetc1['S3BD5Q2E']=subsetc1['S3BD5Q2E'].replace('BL', numpy.nan)

recode1 = {1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1}     # Frequency of cannabis use variable reverse-recode
subsetc1['CUFREQ'] = subsetc1['S3BD5Q2E'].map(recode1)     # Change the variable name from S3BD5Q2E to CUFREQ

subsetc1['CUFREQ'] = subsetc1['CUFREQ'].astype('category')

# Raname graph labels for better interpetation

subsetc1['CUFREQ'] = subsetc1['CUFREQ'].cat.rename_categories(["2 times/year","3-6 times/year","7-11 times/year","Once a month","2-3 times/month","1-2 times/week","3-4 times/week","Nearly every day","Every day"])


## Contingency table of observed counts of major depression diagnosis (response variable) within frequency of cannabis use groups (explanatory variable), in ages 18-30

contab1 = pandas.crosstab(subsetc1['MAJORDEP12'], subsetc1['CUFREQ'])
print (contab1)

# Column percentages

colsum=contab1.sum(axis=0)
colpcontab=contab1/colsum
print(colpcontab)

# Chi-square calculations for major depression within frequency of cannabis use groups

print ('Chi-square value, p value, expected counts, for major depression within cannabis use status')
chsq1= scipy.stats.chi2_contingency(contab1)
print (chsq1)

# Bivariate bar graph for major depression percentages with each cannabis smoking frequency group

plt.figure(figsize=(12,4))     # Change plot size
ax1 = seaborn.factorplot(x="CUFREQ", y="MAJORDEP12", data=subsetc1, kind="bar", ci=None)
ax1.set_xticklabels(rotation=40, ha="right")    # X-axis labels rotation
plt.xlabel('Frequency of cannabis use')
plt.ylabel('Proportion of Major Depression')
plt.show()

recode2 = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}   # Frequency of cannabis use variable reverse-recode
subsetc1['CUFREQ2'] = subsetc1['S3BD5Q2E'].map(recode2)     # Change the variable name from S3BD5Q2E to CUFREQ2

sub1=subsetc1[(subsetc1['S1Q231']== 1)]
sub2=subsetc1[(subsetc1['S1Q231']== 2)]

print ('Association between cannabis use status and major depression for those who lost a family member or a close friend in the last 12 months')
contab2=pandas.crosstab(sub1['MAJORDEP12'], sub1['CUFREQ2'])
print (contab2)

# Column percentages

colsum2=contab2.sum(axis=0)
colpcontab2=contab2/colsum2
print(colpcontab2)

# Chi-square

print ('Chi-square value, p value, expected counts')
chsq2= scipy.stats.chi2_contingency(contab2)
print (chsq2)

# Line graph for major depression percentages within each frequency group, for those who lost a family member or a close friend

plt.figure(figsize=(12,4))     # Change plot size
ax2 = seaborn.factorplot(x="CUFREQ", y="MAJORDEP12", data=sub1, kind="point", ci=None)
ax2.set_xticklabels(rotation=40, ha="right")     # X-axis labels rotation
plt.xlabel('Frequency of cannabis use')
plt.ylabel('Proportion of Major Depression')
plt.title('Association between cannabis use status and major depression for those who lost a family member or a close friend in the last 12 months')
plt.show()

#####################################################################################

print ('Association between cannabis use status and major depression for those who did NOT lose a family member or a close friend in the last 12 months')
contab3=pandas.crosstab(sub2['MAJORDEP12'], sub2['CUFREQ2'])
print (contab3)

# Column percentages

colsum3=contab3.sum(axis=0)
colpcontab3=contab3/colsum3
print(colpcontab3)

# Chi-square

print ('Chi-square value, p value, expected counts')
chsq3= scipy.stats.chi2_contingency(contab3)
print (chsq3)

# Line graph for major depression percentages within each frequency group, for those who did NOT lose a family member or a close friend

plt.figure(figsize=(12,4))     # Change plot size
ax3 = seaborn.factorplot(x="CUFREQ", y="MAJORDEP12", data=sub2, kind="point", ci=None)
ax3.set_xticklabels(rotation=40, ha="right")     # X-axis labels rotation
plt.xlabel('Frequency of cannabis use')
plt.ylabel('Proportion of Major Depression')
plt.title('Association between cannabis use status and major depression for those who did NOT lose a family member or a close friend in the last 12 months')
plt.show()

















