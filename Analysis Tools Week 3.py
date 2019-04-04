# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:00:39 2019

@author: Voltas
"""

import pandas
import numpy
import seaborn
import scipy
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
nesarc['S4AQ6A'] = pandas.to_numeric(nesarc['S4AQ6A'], errors='coerce')
nesarc['S3BD5Q2F'] = pandas.to_numeric(nesarc['S3BD5Q2F'], errors='coerce')
nesarc['S9Q6A'] = pandas.to_numeric(nesarc['S9Q6A'], errors='coerce')
nesarc['S4AQ7'] = pandas.to_numeric(nesarc['S4AQ7'], errors='coerce')
nesarc['S3BQ1A5'] = pandas.to_numeric(nesarc['S3BQ1A5'], errors='coerce')

# Subset my sample

subset1 = nesarc[(nesarc['S3BQ1A5']==1)]    # Cannabis users
subsetc1 = subset1.copy()

# Setting missing data

subsetc1['S3BQ1A5']=subsetc1['S3BQ1A5'].replace(9, numpy.nan)
subsetc1['S3BD5Q2F']=subsetc1['S3BD5Q2F'].replace('BL', numpy.nan)
subsetc1['S3BD5Q2F']=subsetc1['S3BD5Q2F'].replace(99, numpy.nan)
subsetc1['S4AQ6A']=subsetc1['S4AQ6A'].replace('BL', numpy.nan)
subsetc1['S4AQ6A']=subsetc1['S4AQ6A'].replace(99, numpy.nan)
subsetc1['S9Q6A']=subsetc1['S9Q6A'].replace('BL', numpy.nan)
subsetc1['S9Q6A']=subsetc1['S9Q6A'].replace(99, numpy.nan)

# Scatterplot for the age when began using cannabis the most and the age of first episode of major depression

plt.figure(figsize=(12,4))      # Change plot size 
scat1 = seaborn.regplot(x="S3BD5Q2F", y="S4AQ6A", fit_reg=True, data=subset1)
plt.xlabel('Age when began using cannabis the most')
plt.ylabel('Age when expirenced the first episode of major depression')
plt.title('Scatterplot for the age when began using cannabis the most and the age of first the episode of major depression')
plt.show()

data_clean=subset1.dropna()

# Pearson correlation coefficient for the age when began using cannabis the most and the age of first the episode of major depression

print ('Association between the age when began using cannabis the most and the age of the first episode of major depression')
print (scipy.stats.pearsonr(data_clean['S3BD5Q2F'], data_clean['S4AQ6A']))

# Scatterplot for the age when began using cannabis the most and the age of the first episode of general anxiety

plt.figure(figsize=(12,4))      # Change plot size 
scat2 = seaborn.regplot(x="S3BD5Q2F", y="S9Q6A", fit_reg=True, data=subset1)
plt.xlabel('Age when began using cannabis the most')
plt.ylabel('Age when expirenced the first episode of general anxiety')
plt.title('Scatterplot for the age when began using cannabis the most and the age of the first episode of general anxiety')
plt.show()

# Pearson correlation coefficient for the age when began using cannabis the most and the age of the first episode of general anxiety

print ('Association between the age when began using cannabis the most and the age of first the episode of general anxiety')
print (scipy.stats.pearsonr(data_clean['S3BD5Q2F'], data_clean['S9Q6A']))



















