# Exploring Statistical Interactions

## Preview
This assignment aims to statistically assess the evidence, provided by NESARC codebook, in favour of or against the association between cannabis use and major depression, in U.S. adults. More specifically, I examined the statistical interaction between frequency of cannabis use (10-level categorical explanatory, variable **”S3BD5Q2E”**) and major depression diagnosis in the last 12 months (categorical response, variable **”MAJORDEP12”**), moderated by variable **“S1Q231“** (categorical), which indicates the total number of the people who lost a family member or a close friend in the last 12 months. This effect is characterised statistically as an interaction, which is a third variable that affects the direction and/or the strength of the relationship between the explanatory and the response variable and help us understand the moderation. Since I have a categorical explanatory variable (frequency of cannabis use) and a categorical response variable (major depression), I ran a Chi-square Test of Independence (crosstab function) to examine the patterns of the association between them (C->C), by directly measuring the chi-square value and the p-value. In addition, in order visualise graphically this association, I used factorplot function (seaborn library) to produce a bivariate graph. Furthermore, in order to determine which frequency groups are different from the others, I performed a post hoc test, using Bonferroni Adjustment approach, since my explanatory variable has more than 2 levels. In the case of ten groups, I actually need to conduct 45 pair wise comparisons, but in fact I examined indicatively two and compared their p-values with the Bonferroni adjusted p-value, which is calculated by dividing p=0.05 by 45. By this way it is possible to identify the situations where null hypothesis can be safely rejected without making an excessive type 1 error.

 Regarding the third variable, I examined if the fact that a family member or a close friend died in the last 12 months, moderates the significant association between cannabis use frequency and major depression diagnosis. Put it another way, is frequency of cannabis use related to major depression for each level of the moderating variable (1=Yes and 2=No), that is for those whose a family member or a close friend died in the last 12 months and for those whose they did not? Therefore, I set new data frames (**sub1** and **sub2**) that include either individuals who fell into each category (Yes or No) and ran a Chi-square Test of Independence for each subgroup separately, measuring both chi-square values and p-values. Finally, with factorplot function (seaborn library) I created two bivariate line graphs, one for each level of the moderating variable, in order to visualise the differences and the effect of the moderator upon the statistical relationship between frequency of cannabis use and major depression diagnosis. For the code and the output I used Spyder (IDE). 

The moderating variable that I used for the statistical interaction is:

![scshot](https://github.com/Gkontopodis/Data-Analysis-Tools/blob/master/Assignment%20Week%204/Output%20-%20Graphs/Untitled.png)

## Output
![out1](https://github.com/Gkontopodis/Data-Analysis-Tools/blob/master/Assignment%20Week%204/Output%20-%20Graphs/out1.png)
![out2](https://github.com/Gkontopodis/Data-Analysis-Tools/blob/master/Assignment%20Week%204/Output%20-%20Graphs/out2.png)

A Chi Square test of independence revealed that among cannabis users aged between 18 and 30 years old **(subsetc1)**, the frequency of cannabis use (explanatory variable collapsed into 9 ordered categories) and past year depression diagnosis (response binary categorical variable) were significantly associated, X2 =29.83, 8 df, p=0.00022.

![graph](https://github.com/Gkontopodis/Data-Analysis-Tools/blob/master/Assignment%20Week%204/Output%20-%20Graphs/out3.png)

In the bivariate graph (C->C) presented above, we can see the correlation between frequency of cannabis use (explanatory variable) and major depression diagnosis in the past year (response variable). Obviously, we have a left-skewed distribution, which indicates that the more an individual (18-30) smoked cannabis, the better were the chances to have experienced depression in the last 12 months.

![out4]()
