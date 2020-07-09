# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import numpy as np
import seaborn as sns 
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf 

c_data=pd.read_csv("C:\\Users\\suraj baraik\\Desktop\\Data Science\\Suraj\\New folder (12)\\Module 08 Multi Linear Regression\\Assignment problems\\Computer_data.csv")
c_data.describe()
sns.pairplot(c_data.iloc[:,:])
c_data.corr()
         
ml1 = smf.ols('trend~price+speed+ram',data=c_data).fit()
ml1.summary()
rsq_hp = smf.ols('trend~price+speed+ram',data=c_data).fit().rsquared  
vif_hp = 1/(1-rsq_hp) 
vif_hp #2.04

rsq_wt = smf.ols('price~speed+trend+ram',data=c_data).fit().rsquared  
vif_wt = 1/(1-rsq_wt)
vif_wt#2.79

rsq_vol = smf.ols('speed~price+trend+ram',data=c_data).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 
vif_vol #1.57

rsq_sp = smf.ols('ram~trend+price+speed',data=c_data).fit().rsquared  
vif_sp = 1/(1-rsq_sp) 
vif_sp #2.42

d1 = {'Variables':['ram','trend','speed','price'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame

final_ml= smf.ols('trend~ram+price+speed',data = c_data).fit()
final_ml.summary()


c_train,c_test  = train_test_split(c_data,test_size = 0.3) 

model_train = smf.ols("trend~price+ram+speed",data=c_train).fit()

train_pred = model_train.predict(c_train)

train_resid  = train_pred - c_train.trend

train_rmse = np.sqrt(np.mean(train_resid*train_resid))  
train_rmse#5.515

test_pred = model_train.predict(c_test)

test_resid  = test_pred - c_test.trend

test_rmse = np.sqrt(np.mean(test_resid*test_resid))
test_rmse#5.491
