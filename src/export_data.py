import pandas as pd
import numpy as np
import os

def adapt_data_to_bench(dataframe) : 
    columns_list = list(dataframe.columns)
    dataframe['Time'] = dataframe['Time']+150
    time_adapt = np.array([t/10 for t in range(149)])
    data_out = pd.DataFrame({'Time' : time_adapt})
    for k in range(len(columns_list)) : 
        if 'Speed' in columns_list[k] :
            speed_init = np.array(dataframe[columns_list[k]][0])
            speed_target = np.zeros(149)
            speed_target[0] = 0
            for t in range(1,100):
                speed_target[t] = (speed_init/(100-k))
            for t in range(100,len(speed_target)):
                speed_target[t] = speed_init
            data_out[columns_list[k]] = speed_target
    dataframe_out = pd.concat([data_out,dataframe], sort = False)
    return dataframe_out

def export_trajectories(dataframe,out_dir,experiment_name):
    columns_list = list(dataframe.columns)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for k in range(len(columns_list)) : 
        if 'Speed' in columns_list[k] :
            data_out = pd.DataFrame({'Time' : dataframe['Time'],'Speed' : dataframe[columns_list[k]]})
            data_out.to_csv(out_dir+experiment_name+'_Veh_nb_'+str(k)+'.csv')
    return

def export_1Hz_trajectories(dataframe,out_dir,experiment_name):
    columns_list = list(dataframe.columns)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for k in range(len(columns_list)) : 
        if 'Speed' in columns_list[k] :
            time = np.array([dataframe['Time'][t] for t in range(len(dataframe['Time'])) if t%10 == 0])
            speed = np.array([dataframe[k][t] for t in range(len(dataframe['Time'])) if t%10 == 0])
            data_out = pd.DataFrame({'Time' : time,'Speed' : speed})
            data_out.to_csv(out_dir+experiment_name+'_Veh_nb_'+str(k)+'.csv')
            del(time);del(speed)
    return