import pandas as pd
import numpy as np
import os

def read_data(path,file):
    """read OpenACC csv files and transforms them by
    - deleting the first rows that do not contains the used data
    - changing the temporal referential
     Inputs
    ----------
    path of the dataframes
    name of the dataframe that contains the leader/first follower trajectory to be compared
    
    -------
    Returns
    -------
    pd dataframe with the good format 
    """
    df = pd.read_csv(path+file, skiprows=range(5, 20000))
    df = df.tail(-1).T
    df_out = pd.read_csv(path+file, skiprows=range(0, 5))
    ref_time = min(df_out['Time'])
    df_out['Time'] = df_out['Time']-ref_time
    return df_out


def read_all_data(path,setting):
    """routine to read all the OpenACC data"""
    Path = path+ setting+'/'
    files = os.listdir(Path)
    dico = {}
    for file in files : 
        df = read_data(Path,file)
        if type(df) == pd.core.frame.DataFrame :
            dico[file] = df
    return dico

def extract_vectors(df) : 
    """extract speed profile of the leader
     Inputs
    ----------
    speed dataframe
    
    -------
    Returns
    -------
    leader/first trajectory speed array"""
    Time = np.array(df['Time'])
    try :
        Speed = np.array(df['Speed1'])
    except KeyError : 
        Speed = np.array(df['Speed2'])
    return Time, Speed

def max_speed(df) : 
    """return maximal speed of the leader in an OpenACC csv file
     Inputs
    ----------
    speed dataframe

    
    -------
    Returns
    -------
    max speed of the leader/first trajectory """
    Time, Speed = extract_vectors(df)
    return max(Speed)
