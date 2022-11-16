import warnings
import numpy as np
import pandas as pd
warnings.filterwarnings('ignore')
from sklearn.decomposition import PCA
from sklearn.ensemble import (GradientBoostingRegressor)
#Regression
from sklearn.linear_model import ElasticNet, Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Sklearn
from sklearn.model_selection import train_test_split
# Classification
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import (LabelEncoder, MinMaxScaler, OneHotEncoder,
                                   StandardScaler, normalize, scale)
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.utils import resample


def regr(x,y):
    
    lr=LinearRegression()
    r=Ridge()
    l=Lasso()
    e=ElasticNet()
    kn=KNeighborsRegressor()
    et=ExtraTreeRegressor()
    gb=GradientBoostingRegressor()
    dt=DecisionTreeRegressor()
       
    algos=[lr,r,l,e,kn,et,gb,dt]
    algos_names=['LinearRegressor','Ridge','Lasso','ElasticNet','KNeighbors','ExtraTree','GradientBoosting','DecisionTree']
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=42)
    
    r_score=[]
    mse=[]
    mae=[]
    rmse=[]
    
    result=pd.DataFrame(columns=['R_square','MSE','MAE', 'RMSE'],index=algos_names)
    
    for algo in algos:
        pred=algo.fit(x,y).predict(x)
        r_score.append(r2_score(y,pred))
        mse_value = mean_squared_error(y,pred)**.5
        mse.append(mse_value)
        mae.append(mean_absolute_error(y,pred))
        rmse.append(np.sqrt(mse_value))
   
    result.R_square=r_score
    result.MSE=mse
    result.MAE=mae
    result.RMSE=rmse
    
    return result.sort_values('R_square',ascending=False)