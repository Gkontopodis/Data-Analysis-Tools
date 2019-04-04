# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:20:15 2019

@author: Voltas
"""

import pandas
import numpy
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

nesarc = pandas.read_csv ('nesarc_pds.csv' , low_memory=False)

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

nesarc.columns = map(str.upper , nesarc.columns)

pandas.set_option('display.float_format' , lambda x:'%f'%x)

# Change my variables to numeric

nesarc['AGE'] = pandas.to_numeric(nesarc['AGE'], errors='coerce')
nesarc['S3BQ4'] = pandas.to_numeric(nesarc['S3BQ4'], errors='coerce')
nesarc['S3BQ1A5'] = pandas.to_numeric(nesarc['S3BQ1A5'], errors='coerce')
nesarc['S3BD5Q2B'] = pandas.to_numeric(nesarc['S3BD5Q2B'], errors='coerce')
nesarc['S3BD5Q2E'] = pandas.to_numeric(nesarc['S3BD5Q2E'], errors='coerce')
nesarc['MAJORDEP12'] = pandas.to_numeric(nesarc['MAJORDEP12'], errors='coerce')
nesarc['GENAXDX12'] = pandas.to_numeric(nesarc['GENAXDX12'], errors='coerce')

# Subset my sample

subset1 = nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30)]      # Ages 18-30
subsetc1 = subset1.copy()

subset2 = nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30) & (nesarc['S3BQ1A5']==1)]    # Cannabis users, ages 18-30
subsetc2 = subset2.copy()

# Setting missing data for frequency and cannabis use, variables S3BD5Q2E, S3BQ1A5

subsetc1['S3BQ1A5']=subsetc1['S3BQ1A5'].replace(9, numpy.nan)
subsetc2['S3BD5Q2E']=subsetc2['S3BD5Q2E'].replace('BL', numpy.nan)
subsetc2['S3BD5Q2E']=subsetc2['S3BD5Q2E'].replace(99, numpy.nan)

## Contingency table of observed counts of major depression diagnosis (response variable) within cannabis use (explanatory variable), in ages 18-30

contab1=pandas.crosstab(subsetc1['MAJORDEP12'], subsetc1['S3BQ1A5'])
print (contab1)

# Column percentages

colsum=contab1.sum(axis=0)
colpcontab=contab1/colsum
print(colpcontab)

# Chi-square calculations for major depression within cannabis use status

print ('Chi-square value, p value, expected counts, for major depression within cannabis use status')
chsq1= scipy.stats.chi2_contingency(contab1)
print (chsq1)

## Contingency table of observed counts of geberal anxiety diagnosis (response variable) within cannabis use (explanatory variable), in ages 18-30

contab2=pandas.crosstab(subsetc1['GENAXDX12'], subsetc1['S3BQ1A5'])
print (contab2)

# Column percentages

colsum2=contab2.sum(axis=0)
colpcontab2=contab2/colsum2
print(colpcontab2)

# Chi-square calculations for general anxiety within cannabis use status

print ('Chi-square value, p value, expected counts, for general anxiety within cannabis use status')
chsq2= scipy.stats.chi2_contingency(contab2)
print (chsq2)

############################################################################################################################################
# Contingency table of observed counts of major depression diagnosis (response variable) within frequency of cannabis use (10 level explanatory variable), in ages 18-30

contab3=pandas.crosstab(subset2['MAJORDEP12'], subset2['S3BD5Q2E'])
print (contab3)

# Column percentages

colsum3=contab3.sum(axis=0)
colpcontab3=contab3/colsum3
print(colpcontab3)

# Chi-square calculations for mahor depression within frequency of cannabis use groups

print ('Chi-square value, p value, expected counts for major depression associated frequency of cannabis use')
chsq3= scipy.stats.chi2_contingency(contab3)
print (chsq3)

recode1 = {1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1}       # Dictionary with details of frequency variable reverse-recode
subsetc2['CUFREQ'] = subsetc2['S3BD5Q2E'].map(recode1)     # Change variable name from S3BD5Q2E to CUFREQ

subsetc2["CUFREQ"] = subsetc2["CUFREQ"].astype('category')

# Rename graph labels for better interpretation

subsetc2['CUFREQ'] = subsetc2['CUFREQ'].cat.rename_categories(["2 times/year","3-6 times/year","7-11 times/years","Once a month","2-3 times/month","1-2 times/week","3-4 times/week","Nearly every day","Every day"])

# Graph percentages of major depression within each cannabis smoking frequency group

plt.figure(figsize=(12,4))      # Change plot size 
ax1 = seaborn.factorplot(x="CUFREQ", y="MAJORDEP12", data=subsetc2, kind="bar", ci=None)
ax1.set_xticklabels(rotation=40, ha="right")    # X-axis labels rotation
plt.xlabel('Frequency of cannabis use')
plt.ylabel('Proportion of Major Depression')
plt.show()

## Post hoc test, pair comparison of frequency groups 1 and 9, 'Every day' and '2 times a year'

recode2 = {1: 1, 9: 9}
subsetc2['COMP1v9']= subsetc2['S3BD5Q2E'].map(recode2)

# Contingency table of observed counts
ct4=pandas.crosstab(subsetc2['MAJORDEP12'], subsetc2['COMP1v9'])
print (ct4)

# Column percentages
colsum4=ct4.sum(axis=0)
colpcontab4=ct4/colsum4
print(colpcontab4)

# Chi-square calculations for pair comparison of frequency groups 1 and 9, 'Every day' and '2 times a year'

print ('Chi-square value, p value, expected counts, for pair comparison of frequency groups -Every day- and -2 times a year-')
cs4= scipy.stats.chi2_contingency(ct4)
print (cs4)

## Post hoc test, pair comparison of frequency groups 2 and 6, 'Nearly every day' and 'Once a month'

recode3 = {2: 2, 6: 6}
subsetc2['COMP2v6']= subsetc2['S3BD5Q2E'].map(recode3)

# Contingency table of observed counts

ct5=pandas.crosstab(subsetc2['MAJORDEP12'], subsetc2['COMP2v6'])
print (ct5)

# Column percentages

colsum5=ct5.sum(axis=0)
colpcontab5=ct5/colsum5
print(colpcontab5)

# Chi-square calculations for pair comparison of frequency groups 2 and 6, 'Nearly every day' and 'Once a month'

print ('Chi-square value, p value, expected counts for pair comparison of frequency groups -Nearly every day- and -Once a month-')
cs5= scipy.stats.chi2_contingency(ct5)
print (cs5)


