# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:46:03 2021

@author: bharghava
"""

import pandas as pd
import numpy as np
bigmart=pd.read_csv('C:/Users/bharghava/Downloads/bigmart..csv')

# 
bigmart.describe()
print('bigmart data sale all information(EDA)', bigmart.describe())
# to describe information about objects
bigmart.info()
print( 'bigmart object information', bigmart.info())

# to show first five rows of the data
bigmart.head()
print('to show first 5 rows ',bigmart.head())
# here we cannot remove the columns

#handling the missing values 
pd.isnull(bigmart).sum()
print('to show the null values of bigmart',pd.isnull(bigmart).sum())

# removing columsn
bigmart.drop('Item_Identifier',axis=1, inplace=True)

# removing the na values# displaying no null values , null values fill the na
bigmart_nona=bigmart.dropna()
pd.isnull(bigmart_nona).sum()
print(pd.isnull(bigmart_nona).sum())

#Imputaion Techiniques: mean /median/mode
bigmart.Item_Weight.head()
print ( 'first five columns of item_weight',bigmart.Item_Weight.head() )

#How to find Outliner by using boxplot
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
plt.boxplot(bigmart_nona.Item_Weight)

# since there is no outlyer we can use mean by using imputation
bigmart.Item_Weight.mean()
print('mean of the item weight',bigmart.Item_Weight.mean())
# To fill the na/nan values # by  using mean is 12.69
bigmart.Item_Weight.fillna(12.69, inplace=True)

#  imputation with median if  there is a Outlyer
#DATA IS CONTINEOUS
bigmart.Item_Weight.median()
print('median of the item weight',bigmart.Item_Weight.median())
# To fill the na/nan values # by  using median is 12.69
bigmart.Item_Weight.fillna(12.69, inplace=True)
#print('outlet size of bigmart',bigmart["Outlet_Size "])
# to find unique values of the data item is Outlet_Size
bigmart.Outlet_Size.unique()
print(bigmart.Outlet_Size.unique())
# to find unique data counts 
bigmart.Outlet_Size.value_counts()
print(bigmart.Outlet_Size.value_counts())
#imputation with mode # when the is data  discreate 
bigmart.Outlet_Size.fillna("others",inplace=True)
print(bigmart.Outlet_Size.fillna("others",inplace=True))
## FEATURE ENGINEERING
bigmart.Outlet_Size.unique()
print(bigmart.Outlet_Size.unique())
# check for the unique value of Item_Fat_Content # ERROR NOT GETTING 
bigmart.Item_Fat_Content.unique()
print(bigmart.Item_Fat_Content.unique())
bigmart.Item_Fat_Content.value_counts()
print(bigmart.Item_Fat_Content.value_counts())
bigmart.Item_Fat_Content = bigmart.Item_Fat_Content.str.replace('low fat', "LF")
bigmart.Item_Fat_Content = bigmart.Item_Fat_Content.str.replace('LF', "Low Fat").replace('reg', "Regular")
print(bigmart.Item_Fat_Content)
## Replace  with medain val is 0.054
bigmart.Item_Visibility.describe()
bigmart.Item_Visibility = bigmart.Item_Visibility.replace(0,bigmart.Item_Visibility.median())
print(bigmart.Item_Visibility)
#ITEM_TYPE
bigmart.Item_Type.unique()
bigmart.drop("Outlet_Identifier",axis =1,inplace = True)
#OUTLET_LOCATION
bigmart.Outlet_Location_Type.unique()
#OUTLET_TYPE
bigmart.Outlet_Type.unique()

#visualization # using bar graph
plt.bar(bigmart.Item_Fat_Content.unique(),bigmart.Item_Fat_Content.value_counts())









































































