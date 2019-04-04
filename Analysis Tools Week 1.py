# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 00:30:58 2019

@author: Voltas
"""

import pandas
import numpy
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi
nesarc = pandas.read_csv ('nesarc_pds.csv' , low_memory=False)     # load NESARC dataset

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

nesarc.columns = map(str.upper , nesarc.columns)

pandas.set_option('display.float_format' , lambda x:'%f'%x)

# Change my variables to numeric

nesarc['AGE'] = nesarc['AGE'].convert_objects(convert_numeric=True)
nesarc['S3BQ4'] = nesarc['S3BQ4'].convert_objects(convert_numeric=True)
nesarc['S3BQ1A5'] = nesarc['S3BQ1A5'].convert_objects(convert_numeric=True)
nesarc['S3BD5Q2B'] = nesarc['S3BD5Q2B'].convert_objects(convert_numeric=True)
nesarc['S3BD5Q2E'] = nesarc['S3BD5Q2E'].convert_objects(convert_numeric=True)
nesarc['MAJORDEP12'] = nesarc['MAJORDEP12'].convert_objects(convert_numeric=True)
nesarc['GENAXDX12'] = nesarc['GENAXDX12'].convert_objects(convert_numeric=True)

# Subset my sample

subset5 = nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30) & (nesarc['S3BQ1A5']==1)]    # Cannabis users, ages 18-30
subsetc5 = subset5.copy()


# Setting missing data for quantity of cannabis (measured in joints), variable S3BQ4

subsetc5['S3BQ4']=subsetc5['S3BQ4'].replace(99, numpy.nan)
subsetc5['S3BQ4']=subsetc5['S3BQ4'].replace('BL', numpy.nan)

sub1 = subsetc5[['S3BQ4', 'MAJORDEP12']].dropna()

# Using ols function for calculating the F-statistic and the associated p value
# Depression (categorical, explanatory variable) and joints quantity (quantitative, response variable) correlation

model1 = smf.ols(formula='S3BQ4 ~ C(MAJORDEP12)', data=sub1)
results1 = model1.fit()
print (results1.summary())

# Measure mean and spread for categorical variable MAJORDEP12, major depression

print ('Means for joints quantity by major depression status')
m1= sub1.groupby('MAJORDEP12').mean()
print (m1)

print ('Standard deviations for joints quantity by major depression status')
sd1 = sub1.groupby('MAJORDEP12').std()
print (sd1)

sub2 = subsetc5[['S3BQ4', 'GENAXDX12']].dropna()

# Using ols function for calculating the F-statistic and the associated p value
# Anxiety (categorical, explanatory variable) and joints quantity (quantitative, response variable) correlation

model2 = smf.ols(formula='S3BQ4 ~ C(GENAXDX12)', data=sub2)
results2 = model2.fit()
print (results2.summary())

# Measure mean and spread for categorical variable GENAXDX12, general anxiety

print ('Means for joints quantity by major general anxiety status')
m2= sub2.groupby('GENAXDX12').mean()
print (m2)

print ('Standard deviations for joints quantity by general anxiety status')
sd2 = sub2.groupby('GENAXDX12').std()
print (sd2)

#################################################################################

# Setting missing data for frequency of cannabis use, variable S3BD5Q2E

subsetc5['S3BD5Q2E']=subsetc5['S3BD5Q2E'].replace(99, numpy.nan)
subsetc5['S3BD5Q2E']=subsetc5['S3BD5Q2E'].replace('BL', numpy.nan)

sub3 = subsetc5[['S3BQ4', 'S3BD5Q2E']].dropna()

# Using ols function for calculating the F-statistic and associated p value
# Frequency of cannabis use (10 level categorical, explanatory variable) and joints quantity (quantitative, response variable) correlation

model3 = smf.ols(formula='S3BQ4 ~ C(S3BD5Q2E)', data=sub3).fit()
print (model3.summary())

# Measure mean and spread for categorical variable S3BD5Q2E, frequency of cannabis use

print ('Means for joints quantity by frequency of cannabis use status')
mc2= sub3.groupby('S3BD5Q2E').mean()
print (mc2)

print ('Standard deviations for joints quantity by frequency of cannabis use status')
sdc2 = sub3.groupby('S3BD5Q2E').std()
print (sdc2)

# Run a post hoc test (paired comparisons), using Tukey HSDT

mc1 = multi.MultiComparison(sub3['S3BQ4'], sub3['S3BD5Q2E'])
res1 = mc1.tukeyhsd()
print(res1.summary())







