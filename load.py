import glob
import pandas as pd
import numpy as np

def strvec2npy(data):
    data=data.apply(lambda x: 
        np.array(x.strip('[]').split(',')).astype(np.float)[:300])
    return data

def tracking_data(location,pid):
    print('loading data files...')
    files = glob.glob(location+pid+'*.csv')
    data = pd.DataFrame()
    li = []
    for file in files: 
        print(file)
        li.append(pd.read_csv(file)) # load files

    data = pd.concat(li, axis=0, ignore_index=True)
    data = data[~data['blobHeight'].isnull()] # remove wait for start
    keys = ['blobHeight','blobWidth','frameRate','response_mouse.x','response_mouse.y','blob.x','blob.y','response_mouse.time'] # return only the interesting stuff
    data = data[keys]
    for key in keys[3:]:
        data[key] = strvec2npy(data[key])
        
    data = data.rename(columns={'response_mouse.x':'response_x', 'response_mouse.y':'response_y','blob.x':'stimulus_x','blob.y':'stimulus_y','response_mouse.time':'response_time' })
    data = data.reset_index()

    for dd in range(data.shape[0]):
        tt = np.arange(0,15,1/60)
        data.at[dd,'response_x']=np.interp(tt,data['response_time'][dd], data['response_x'][dd])
        data.at[dd,'response_y']=np.interp(tt,data['response_time'][dd], data['response_y'][dd])
        data.at[dd,'stimulus_x']=np.interp(tt,data['response_time'][dd], data['stimulus_x'][dd])
        data.at[dd,'stimulus_y']=np.interp(tt,data['response_time'][dd], data['stimulus_y'][dd])
        data.at[dd,'response_time']=tt
        
    return data

def twoAFC_data(location,pid):
    files = glob.glob(location+pid+'*.csv')
    data = pd.DataFrame()
    print('loading data files...')
    for file in files: 
        print(file)
        data = pd.concat((data,pd.read_csv(file))) # load files
    
    data = data[~data['blobHeight'].isnull()] # remove wait for start
    
    keys = ['blobHeight','blobWidth','offset','key_resp.keys'] # return only the interesting stuff
    data = data[keys]
    data = data.rename(columns={'key_resp.keys':'response'})
    return data
