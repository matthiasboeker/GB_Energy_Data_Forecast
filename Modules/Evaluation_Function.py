#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:54:51 2019

@author: matthiasboeker
Evaluation functions"""

def test_train_split(dataframe, scale=0.75):
    train_size=int(len(dataframe) *scale)
    train, test  = dataframe[:train_size].dropna(), dataframe[train_size:].dropna()
    return train, test, train_size

def interval_test_train_split(dataframe ,interval=96):
    train_size=len(dataframe)-interval
    train, test  = dataframe[:train_size-1].dropna(), dataframe[train_size-1:].dropna()
    return train, test, train_size

def frmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())
def fmape(predictions, targets):
    mape = np.mean(np.abs(predictions - targets)/np.abs(targets))
    return mape
def fmae(predictions, targets):
    mae = np.mean(np.abs(predictions-targets))
    return mae
def fcorrbetw(predictions, targets):
    corr = np.corrcoef(predictions, targets)[0,1]
    return corr
def res(prediction, target):
    res = (predictions-target)^2


def forecast_accuracy(forecast, actual):
    mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
    me = np.mean(forecast - actual)             # ME
    mae = np.mean(np.abs(forecast - actual))    # MAE
    mpe = np.mean((forecast - actual)/actual)   # MPE
    rmse = np.mean((forecast - actual)**2)**.5  # RMSE
    corr = np.corrcoef(forecast, actual)[0,1]   # corr

    return({'mape':mape, 'me':me, 'mae': mae, 
            'mpe': mpe, 'rmse':rmse,  
            'corr':corr})
    

    
def evaluate_prediction2(test, prediction):
    act= pd.DataFrame(test)
    predictions = pd.DataFrame(prediction.predicted_mean)
    low_val  = pd.DataFrame(prediction.conf_int().iloc[:,0])
    high_val = pd.DataFrame(prediction.conf_int().iloc[:,1])
    predictions['Actual'] = act
    predictions['Low Bound'] = low_val
    predictions['High Bound'] = high_val
    predictions.rename(columns={0:'Pred'}, inplace=True)
    predictions.index = test.index
    predictions['Actual'].plot(figsize=(10,5), legend=True, color='lightblue')
    predictions['Pred'].plot(legend=True, color='orange', figsize=(10,5))
    predictions['Low Bound'].plot(legend=True, color='grey', linestyle='dashed',figsize=(10,5))
    predictions['High Bound'].plot(legend=True, color='grey',linestyle='dashed', figsize=(10,5))
    rmse = frmse(predictions['Pred'], predictions['Actual'])
    mape = fmape(predictions['Pred'], predictions['Actual'])
    mae  = fmae(predictions['Pred'], predictions['Actual'])
    corr = fcorrbetw(predictions['Pred'], predictions['Actual'])
    print('Residual Mean Square Error:',rmse)
    print('Mean Absolute Error:', mae)
    print('Mean Absolute Percentage Error:', mape)
    print('Correlation Coef:', corr)
    

def evaluate_prediction(test, prediction):
    act= pd.DataFrame(test)
    predictions=pd.DataFrame(prediction)
    predictions.reset_index(drop=True, inplace=True)
    predictions['Actual'] = act
    predictions.rename(columns={0:'Pred'}, inplace=True)
    predictions['Actual'].plot(figsize=(10,5), legend=True, color='blue')
    predictions['Pred'].plot(legend=True, color='red', figsize=(10,5))
    rmse = frmse(predictions['Pred'], predictions['Actual'])
    mape = fmape(predictions['Pred'], predictions['Actual'])
    mae  = fmae(predictions['Pred'], predictions['Actual'])
    corr = fcorrbetw(predictions['Pred'], predictions['Actual'])
    print('Residual Mean Square Error:',rmse)
    print('Mean Absolute Error:', mae)
    print('Mean Absolute Percentage Error:', mape)
    print('Correlation Coef:', corr)
    
    
    

def merg_predicition(data, prediction):
    cname = data.columns[0]
    merg = pd.DataFrame(prediction,columns={cname} )
    data = data.append(merg,ignore_index=True)
    return data

def exp_smoothing_forecast(history, config,k):
	t,d,s,p,b,r = config
	# define model
	history = np.array(history)
	model = ExponentialSmoothing(history, trend=t, damped=d, seasonal=s, seasonal_periods=p)
	# fit model
	model_fit = model.fit(optimized=True, use_boxcox=b, remove_bias=r)
	# make one step forecast
	yhat = model_fit.predict(start=len(history),end=len(history)+k-1)
	return yhat
 
def wavelet_signal_select(data, wavelet, levels=5, plot=False, select=1, output=[0,1] ):
    wtdf = modwt(data, wavelet, levels)
    wtdf = pd.DataFrame(wtdf)
    
    if plot == True:
    
        for i in range(0,wtdf.shape[0]):
            plt.plot(wtdf.iloc[i,:])
            plt.show()
            
    elif output == 0: 
        
        return wtdf.iloc[select,:]
    elif output == 1:
        #Backtransformation 
        z=np.zeros(wtdf.shape[1])
        trans_dat_base = [z,z,z,z,z,z,z]
        trans_dat_base.insert(select,wtdf.iloc[select,:])
        trans_base = pd.DataFrame(trans_dat_base)
        wtmra = modwtmra(trans_base.values, wavelet)
        wtmra = pd.DataFrame(wtmra)
        
        return wtmra.iloc[select,:]

    
    
