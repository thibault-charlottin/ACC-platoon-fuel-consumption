import pandas as pd
import numpy as np
import src.read_data as read
import src.smooth_data as smooth
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

def select_by_speed(dictionnary, speed):
    """group OpenACC result files based on the maximum speed that has been reccorded
    
    -------
    Input
    -------
    dictionnary containing all of the datasheet names of OpenACC
    reference speed
    -------
    Returns
    -------
    dictionnary that contains all the files containing speed trajectories around the reference speed
    """
    dico = {}
    keys = list(dictionnary.keys())
    for key in range(len(keys)) : 
        Time, Speed = read.extract_vectors(dictionnary[keys[key]])
        if speed-1<max(Speed)<speed+1 :
            dico[keys[key]] = dictionnary[keys[key]]
    return dico


def compare_trajectory(dfA, dfB,plotting): 
    """compare the shape of the leaders curves from one dataframe to another
    used algorithm: dtw that focuses on the deviations of the curves without dealing with the numerical values
    option to plot
    -------
    Input
    -------
    the two dataframes to be plotted
    plotting option
    -------
    Returns
    -------
    dtw distance
    """
    df1 = smooth.interpolate(dfA)
    df2 = smooth.interpolate(dfB)
    TIMEA,SPEEDA = read.extract_vectors(df1)
    TIMEB, SPEEDB = read.extract_vectors(df2)
    d, paths = dtw.warping_paths(SPEEDA, SPEEDB, window=25, psi=2)
    best_path = dtw.best_path(paths)
    if plotting == True :
        dtwvis.plot_warpingpaths(SPEEDA, SPEEDB, paths, best_path)
    return d


def compare_dictionnaries(dicoA, dicoB, keyA, keyB, plotting) : 
    """compare_trajectory function extended to the whole set of OpenACC csv files within the same speed interval
    -------
    Input
    -------
    two dictionnaries containing the selected speed types,
    key A key B : setting types
    plotting option
    -------
    Returns
    -------
    dataframe that contains all dtw distances"""
    df_out = pd.DataFrame({keyA : [], keyB : [], 'distance' : []})
    for k in list(dicoA.keys()) :
        for l in list(dicoB.keys()):
            distance = compare_trajectory(dicoA[k],dicoB[l],plotting)
            df_one_result = pd.DataFrame({keyA : [k], keyB : [l], 'distance' : [distance]})
            df_out = pd.concat([df_out,df_one_result], sort = False)
    return df_out

def routine (dicoA, dicoB, dicoC, dicoD, dicoE, keyA, keyB, keyC, keyD, keyE) : 
    """funciton to run compare dictionaries on the whole set of OpenACC csv files
    It uses compare_dictionnaries function"""
    df_compareAB = compare_dictionnaries(dicoA, dicoB, keyA, keyB, plotting = False)
    df_compareAC = compare_dictionnaries(dicoA, dicoC, keyA, keyC, plotting = False)
    df_compareAD = compare_dictionnaries(dicoA, dicoD, keyA, keyD, plotting = False)
    df_compareAE = compare_dictionnaries(dicoA, dicoE, keyA, keyE, plotting = False)
    df_compareBC = compare_dictionnaries(dicoB, dicoC, keyB, keyC, plotting = False)
    df_compareBD = compare_dictionnaries(dicoB, dicoD, keyB, keyD, plotting = False)
    df_compareBE = compare_dictionnaries(dicoB, dicoE, keyB, keyE, plotting = False)
    df_compareCD = compare_dictionnaries(dicoC, dicoD, keyC, keyD, plotting = False)
    df_compareCE = compare_dictionnaries(dicoC, dicoE, keyC, keyE, plotting = False)
    df_compareDE = compare_dictionnaries(dicoD, dicoE, keyD, keyE, plotting = False)
    df_results = pd.concat([df_compareAB,df_compareAC,df_compareAD,df_compareAE, df_compareBC,df_compareBD,df_compareBE,df_compareCD,df_compareCE,df_compareDE])
    return  df_results
