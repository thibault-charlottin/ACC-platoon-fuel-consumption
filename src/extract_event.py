import pandas as pd
import numpy as np
from dtaidistance import dtw

def extract_event(path,dataframe_name,time_in,time_out):
    '''extract speed within a selected time slot in an OpenACC datasheet'''
    df = pd.read_csv(path+dataframe_name)
    df_trunc = df[(df['Time']>time_in) & (df['Time']<time_out)]
    df_out = pd.DataFrame({'Time' : list(df_trunc['Time']), 'Speed' : list(df_trunc['Speed'])})
    return df_out

def characterize_singular_event(path,dataframe_name,time_in,time_out):
    """computes speed difference in the deceleration and acceleration phase 
    computes decceleration period and acceleration period
    for one speed profile"""
    df = extract_event(path,dataframe_name,time_in,time_out)
    dv2 = df['Speed'][df['Speed'].argmax()]-df['Speed'][df['Speed'].argmin()]
    dt2 = df['Time'][df['Speed'].argmax()]-df['Time'][df['Speed'].argmin()]
    truncated_df = df.head(df['Speed'].argmin())
    dv1 = truncated_df['Speed'][truncated_df['Speed'].argmin()]-truncated_df['Speed'][truncated_df['Speed'].argmax()]
    dt1 = truncated_df['Time'][truncated_df['Speed'].argmin()]-truncated_df['Time'][truncated_df['Speed'].argmax()]
    return dv1,dt1,dv2,dt2

def characterize_mean_event(path, dataframe_list,time_in_list,time_out_list):
    """using characterize_singular_event function computes the mean
    speed difference in the deceleration and acceleration phase 
    decceleration period and acceleration period
    for all the first follower trajectories
    """
    dv1_list,dv2_list,dt1_list,dt2_list = [],[],[],[]
    for k in range(len(dataframe_list)):
        dv1,dv2,dt1,dt2 = characterize_singular_event(path,dataframe_list[k],time_in_list[k],time_out_list[k])
        dv1_list.append(dv1);dv2_list.append(dv2);dt1_list.append(dt1);dt2_list.append(dt2)
    dv1_mean = np.mean(dv1_list) ; dv2_mean = np.mean(dv2_list)
    dt1_mean = np.mean(dt1_list) ; dt2_mean = np.mean(dt2_list)
    return np.array([dv1_mean,dv2_mean,dt1_mean,dt2_mean])

def extract_event_array(path,dataframe_name,time_in,time_out):
    """extract the trigering event from a speed profile
    returns it as an array"""
    df = extract_event(path,dataframe_name,time_in,time_out)
    max = df['Speed'].argmax()
    truncated_df = df.head(df['Speed'].argmin())
    min = truncated_df['Speed'].argmax()
    speed_array = np.array([df['Speed'][k] for k in range(min,max)])
    time_array = np.array([df['Time'][k] for k in range(min,max)])
    df_out = pd.DataFrame({'Time' : time_array,'Speed' : speed_array})
    return df_out

def get_distance(path,dataframe_name1,dataframe_name2,time_in1,time_in2,time_out1,time_out2):
    """compare the dtw distance from to triggering event"""
    df1 =  extract_event_array(path,dataframe_name1,time_in1,time_out1)
    df2 =  extract_event_array(path,dataframe_name2,time_in2,time_out2)
    d, paths = dtw.warping_paths(df1['Speed'], df2['Speed'], window=25, psi=2)
    return d

def get_mean_distance(path,dataframe_list,time_in_list,time_out_list):
    """using get_distance funciton computes the mean distance from one triggering event to another
    this will be sued as the reference to say if one ExiD speed profile of 15s is close enough to the triggering event"""
    distance_list = []
    for k in range(len(dataframe_list)):
        try :
            dataframe_trunc = dataframe_list[k+1:]
            time_in_trunc = time_in_list[k+1:]
            time_out_trunc = time_out_list[k+1:]
        except IndexError:
            pass
        for n in range(len(dataframe_trunc)):
            distance_list.append(get_distance(path,dataframe_list[k],dataframe_trunc[n],time_in_list[k],time_in_trunc[n],time_out_list[k],time_out_trunc[n]))
    mean = np.mean(distance_list)
    std_err = np.std(distance_list)
    return mean, std_err

