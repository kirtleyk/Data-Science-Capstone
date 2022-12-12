# Adapated from method at https://www.kaggle.com/code/aslanlion/failed-salary-prediction
import warnings
import numpy as np
import pandas as pd
warnings.filterwarnings('ignore')
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


def regr(x,y, x_test, y_test):
    
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
       
    r_score=[]
    mse=[]
    mae=[]
    rmse=[]
    r_score_test=[]
    mse_test=[]
    mae_test=[]
    rmse_test=[]
    
    result = pd.DataFrame(columns=['R2','MSE','MAE', 'RMSE'],index=algos_names)
    result_test = pd.DataFrame(columns=['R2 Test', 'MSE Test', 'MAE Test', 'RMSE Test'],index=algos_names)
    
    for algo in algos:
        algo.fit(x,y)
        pred=algo.predict(x)
        r_score.append(r2_score(y,pred))
        mse_value = mean_squared_error(y,pred)
        mse.append(mse_value)
        mae.append(mean_absolute_error(y,pred))
        rmse.append(np.sqrt(mse_value))
        
        pred=algo.predict(x_test)
        r_score_test.append(r2_score(y_test,pred))
        mse_value = mean_squared_error(y_test,pred)
        mse_test.append(mse_value)
        mae_test.append(mean_absolute_error(y_test, pred))
        rmse_test.append(np.sqrt(mse_value))
   
    result.R2=r_score
    result.MSE=mse
    result.MAE=mae
    result.RMSE=rmse
    result_test['R2 Test'] = r_score_test
    result_test['MSE Test'] = mse_test
    result_test['MAE Test'] = mae_test
    result_test['RMSE Test'] = rmse_test
    
    return (result, result_test)