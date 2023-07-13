import pandas as pd
import numpy as np
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import src.extract_event as extract
from tqdm.notebook import trange
import os


def get_distance(path,dataframe_name1,time_in1,time_out1,speed_array):
    """compare distance that exist between openACC leaders acceleration/decceleration event speed profile
    and a speed array taken from HighD
    used algorithm dtw"""
    df =  extract.extract_event_array(path,dataframe_name1,time_in1,time_out1)
    d, _ = dtw.warping_paths(df['Speed'], speed_array, window=25, psi=2)
    return d

def plot_distance(path,dataframe_name1,time_in1,time_out1,speed_array):
    """plot distance that exist between openACC leaders acceleration/decceleration event speed profile
    and a speed array taken from HighD
    used algorithm dtw"""
    df =  extract.extract_event_array(path,dataframe_name1,time_in1,time_out1)
    d, paths = dtw.warping_paths(df['Speed'], speed_array, window=25, psi=2)
    best_path = dtw.best_path(paths)
    dtwvis.plot_warpingpaths(df['Speed'], speed_array, paths, best_path)
    return 


def analyse_window(path,dataframe_list,time_in_list,time_out_list,speed_array,mean_distance, std):
    """get_distance function used between all the leaders event speed profile and a speed profile taken from HighD
    if the mean distance is smaller than the mean distance between all the leaders speed events
    then the test is considered as successfull
    Then the algorithm returns if the trajectories can be considered as being the same kind of event"""
    distance_list = []
    for k in range(len(dataframe_list)):
            distance_list.append(get_distance(path,dataframe_list[k],time_in_list[k],time_out_list[k],speed_array))
    if np.mean(distance_list)<=5*(mean_distance+std) :
        return True
         
        
def analyzing_trajectory(df,tau,time_window,
                         path,dataframe_list,time_in_list,time_out_list,
                         mean_distance, std):
    """use analyze_window method to """
    veh = df.id.unique()
    event_occurence_time = 0
    total_time = 0
    for id in trange(len(veh)):
        Current = df[df.id == veh[id]]
        init_time = min(Current['time'])
        while init_time+time_window<max(Current['time']):
            speed_array = np.array([np.abs(list(Current['x_speed'])[k]+list(Current['yspeed'])[k]) for k in range(len(list(Current['x_speed']))) if list(Current['time'])[k]>init_time and list(Current['time'])[k]<init_time+time_window])
            if analyse_window(path,dataframe_list,time_in_list,time_out_list,speed_array,mean_distance, std)==True : 
                 event_occurence_time += time_window
            total_time += max(Current['time'])-min(Current['time'])
            init_time+=tau
    return event_occurence_time/total_time

def running_all_datasets (path_HighD,tau,time_window,
                         path_OpenACC,dataframe_list,time_in_list,time_out_list,
                         mean_distance, std):
    """"""
    files = sorted(os.listdir(path_HighD))
    proportions_out = np.zeros(len(files))
    for f in trange(len(files)) :
        df = pd.read_csv(path_HighD+files[f])
        proportions_out[f] = analyzing_trajectory(df,tau,time_window,
                         path_OpenACC,dataframe_list,time_in_list,time_out_list,
                         mean_distance, std)
        print(np.mean(np.abs(df['x_speed']+df['yspeed'])),proportions_out[f])
    return proportions_out

def count_time(path):
    files = os.listdir(path)
    total_time = 0
    for f in trange(len(files)) : 
        df = pd.read_csv(path+files[f])
        ids = list(pd.unique(df['id']))
        for id in ids : 
            df_test = df[df['id']==id]
            total_time +=  max(list(df_test['time']))-list(df_test['time'])[0]
    return total_time