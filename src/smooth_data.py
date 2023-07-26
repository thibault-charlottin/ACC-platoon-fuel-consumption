import pandas as pd
import numpy as np
from statsmodels.nonparametric.kernel_regression import KernelReg
from tqdm.notebook import trange

def extract_speed_profiles(df):
    """keep only the columns of the OpenACC dataframes that are speed profiles
     Inputs
    ----------
    dataframe that contains all the speed profiles
    
    -------
    Returns
    -------
    
    unique vector of sped vs time 
    """
    
    speed_list = [k for k in df.columns if 'Speed' in k]
    return speed_list

def Kernel_regression_basic(speed,time) : 
    """kernel regression algortithm
    smooths s=f(t) functions
     Inputs
    ----------
    spped and time arrays
    
    -------
    Returns
    -------
    smotthened speed
    """
    kr = KernelReg(speed,time,'c')
    speedpred = kr.fit(time)
    return speedpred

def interpolate(dataframe) : 
    """interpolates the speed columns
    so that the Kernel regression algorithm can run
     Inputs
    ----------
    speed dataframe
    
    -------
    Returns
    -------
    interpolated speed dataframe
    """
    for k in list(dataframe.columns) : 
        if 'Speed' in k :
            dataframe[k] = dataframe[k].interpolate()
            dataframe[k][0] = 0
    return dataframe

def smoothing(dataframe,traj_list,out_name):
    """process of running the kernel regression on a whole dataframe
    does 1st an interpolation of speed columns
    then smooths the data
     Inputs
    ----------
    speed dataframe
    list of trajectories to be smoothened
    export name
    -------
    Returns
    -------
    
    None
    """
    dico = {}
    for k in trange(len(traj_list)) : 
        array = Kernel_regression_basic(dataframe[traj_list[k]],dataframe['Time'])
        dico[traj_list[k]] = array[0]
    speed_profiles_fit = pd.DataFrame(dico)
    speed_profiles_fit['Time'] = dataframe['Time']
    speed_profiles_fit.to_csv(out_name+'.csv')
    return 
