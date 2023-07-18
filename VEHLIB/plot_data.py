import pandas as pd
import numpy as np
import exploiting_vehlib as exploit

import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats
import os
from scipy import stats
from sklearn.metrics import mean_squared_error
import itertools
import statsmodels.api as sm
import statsmodels.formula.api as smf
sns.set_theme()
sns.set_palette("colorblind")

def plot_consumption(results_path,leader_speed,setting,fuel_density):
    """plot consumption vs position in platton using VehLib simulation results"""
    listfiles = sorted(os.listdir(results_path))
    fig1, ax1 = plt.subplots(figsize=(20, 16))
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    for k in listfiles:
        if leader_speed in k and setting in k :
            data = exploit.import_results(results_path,k)
            if 'nb_1' in k : 
                ax2.plot(data['time'],data['speed (km/h)']/3.6, label = 'leader speed profile')
            conso = exploit.compute_consumption(data,fuel_density)
            ax1.plot(data['time'],data['instant consumption'], label = 'veh '+str(k[-1])+' mean consumption = '+str(conso))
            plt.title('Instant consumption temporal evolution')
            ax1.set_xlabel('time (s)')
            ax1.set_ylabel('instant consuption')
            ax2.set_ylabel("speed (m/s)")
            fig1.legend(loc='lower center', bbox_to_anchor=(0.5, 1.05),
            ncol=3, fancybox=True, shadow=True)
    plt.show()
    return

def compute_consumption_regression(results_path,speed,setting,fuel_density):
    """plot consumption vs position in platton linear regression using VehLib simulation results"""
    results_path = 'Vehlib_results/consumption/'
    listfiles = sorted(os.listdir(results_path))
    conso_list = []
    veh_list = []
    for k in listfiles : 
        if speed in k and setting in k :
            data = exploit.import_results(results_path,k)
            conso_list.append(exploit.compute_consumption(data,fuel_density))
            veh_list.append(int(k[-5]))
    slope, intercept, r_value1, p_value1, std_err1 = stats.linregress(veh_list,conso_list)
    veh_list_computation = np.array([k for k in range(len(conso_list))])
    y_pred = intercept + slope * veh_list_computation
    RMSE = mean_squared_error(conso_list, y_pred)    
    sns.regplot(x = veh_list,y= conso_list,label = setting + ' '+r'$\ RMSE$'+'='+str(round(RMSE,2)))   
    return np.array([int(len(veh_list)),slope, intercept, RMSE])

def compute_CO2_regression(results_path,speed,setting,MOTH_co2carb):
    """plot CO2 emissions vs position in platton linear regression using VehLib simulation results"""    
    results_path = 'Vehlib_results/consumption/'
    listfiles = sorted(os.listdir(results_path))
    conso_list = []
    veh_list = []
    for k in listfiles : 
        if speed in k and setting in k :
            data = exploit.import_results(results_path,k)
            conso_list.append(exploit.compute_co2_emission(data,MOTH_co2carb))
            veh_list.append(int(k[-5]))
    slope, intercept, r_value1, p_value1, std_err1 = stats.linregress(veh_list,conso_list)
    veh_list_computation = np.array([k for k in range(len(conso_list))])
    y_pred = intercept + slope * veh_list_computation
    RMSE = mean_squared_error(conso_list, y_pred)    
    sns.regplot(x = veh_list,y= conso_list,label = setting + ' '+r'$\ RMSE$'+'='+str(round(RMSE,2)))   
    return np.array([int(len(veh_list)),slope, intercept, RMSE])
