import glob
import pandas as pd
import numpy as np
import json

def strvec2npy(data):
    data=[np.array(json.loads(dd)) for dd in data]
    return data

def tracking_data(location,pid):
    print('loading data files...')
    files = glob.glob(location+pid+'*tracking*.csv')
    data = pd.DataFrame()
    li = []
    for file in files: 
        print(file)
        li.append(pd.read_csv(file)) # load files

    data = pd.concat(li, axis=0, ignore_index=True)
    
    keep_keys = ['mouse.x','mouse.y','mouse.time','target.x','target.y','imageFile','expName','participant','session']
    data = data[keep_keys]
    
    
    
    # drop nan rows
    data = data.dropna()
    
    # convert to numpy arrays
    for key in keep_keys[:5]:      
        data[key] = strvec2npy(data[key].values) 
       
    # convert list of blob files to condition #s
    conditions = []
    for file in data['imageFile'].values:
        if file == 'images/blob.jpg':
            conditions.append(0)
        elif file == 'images/blob-medium.jpg':
            conditions.append(1)
        elif file == 'images/blob-big.jpg':
            conditions.append(2)
            
    data['condition'] = conditions

    tt = np.arange(0,20,1/60) 
    data['time'] = [[]]*data.shape[0]
    # convert everything to the same frame rate
    for dd in range(data.shape[0]):
        data.at[dd,'mouse.x']=np.interp(tt,data['mouse.time'][dd], data['mouse.x'][dd])
        data.at[dd,'mouse.y']=np.interp(tt,data['mouse.time'][dd], data['mouse.y'][dd])
        data.at[dd,'target.x']=np.interp(tt,data['mouse.time'][dd], data['target.x'][dd][:-1])
        data.at[dd,'target.y']=np.interp(tt,data['mouse.time'][dd], data['target.y'][dd][:-1])
        data.at[dd,'time'] = tt
        
    return data

def twoAFC_data(location,pid):
    files = glob.glob(location+pid+'*2afc*.csv')
    data = pd.DataFrame()
    print('loading data files...')
    for file in files: 
        print(file)
        data = pd.concat((data,pd.read_csv(file))) # load files
    
    keep_keys = ['key_resp.keys', 'key_resp.rt', 'offset', 'imageFile', 'participant', 'session']
    data = data[keep_keys]
    
    
    # remove rows that are not trials
    not_trials = list(np.where(data.offset.isna().values)[0])
    data = data.drop(not_trials)
    
    # convert list of blob files to condition #s
    conditions = []
    for file in data['imageFile'].values:
        if file == 'images/blob.jpg':
            conditions.append(0)
        elif file == 'images/blob-medium.jpg':
            conditions.append(1)
        elif file == 'images/blob-big.jpg':
            conditions.append(2)
    data['condition'] = conditions
            

    return data
