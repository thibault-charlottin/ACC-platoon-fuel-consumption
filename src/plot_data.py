import pandas as pd
import numpy as np
import src.compare_trajectories as compare
import src.exploit_engine_data as exploit_engine
import src.read_data as read
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

def plot_speed_profile_one_experiment(dataframe) : 
    """plot the leader speed profiule for a given OpenACC dataframe"""
    TimeA, speedA = read.extract_vectors(dataframe)
    plt.plot(TimeA,speedA)
    plt.plot(TimeA, np.array(dataframe['Speed2']))
    plt.ylim(0,20)
    return

def plot_multiple_profiles(dictionnary, Color, Label, speed):
    """Plot the platoon speed type as defined in the read_data.py file 
    outputs a scatter plot file vs speed type"""
    speed_list = [read.max_speed(dictionnary[k]) for k in list(dictionnary.keys())]
    plt.plot(list(dictionnary.keys()),speed_list,'x', color = Color, label = Label)
    plt.axhline(y=speed, xmin=0.0, xmax=1.0,linestyle = '-')
    plt.xlabel('experiment')
    plt.ylabel('max speed (m/s)')
    plt.tick_params(axis='x', rotation=90)
    plt.legend(loc=2, prop={'size': 15})
    plt.rcParams['figure.figsize'] = [10, 10]
    return

def plot_speed_profile(dictionnary, label_curve) :
    """plot the speed profile of each car of a platoon decribed in a specific OpenACC dataset"""
    keys = list(dictionnary.keys())
    for key in range(len(keys)) : 
        df = dictionnary[keys[key]]
        Time, Speed = read.extract_vectors(df)
        plt.plot(Time,Speed, label = label_curve+' '+keys[key])
    plt.ylim(0,20)
    return

def plot_selected_speed(dataframe_name, xlim, ylim, speed, timegap) : 
    """plot the speeds profiles of the car belonging to one platoon selected for the experiment"""
    dataframe = pd.read_csv(dataframe_name)
    for k in list(dataframe.columns):
        if 'Speed' in k:
            plt.plot(dataframe['Time'],dataframe[k], alpha = 0.7)
    plt.plot(dataframe['Time'],dataframe['Speed2'],color = 'blue',  label = 'first recorded vehicle')
    plt.legend(fontsize="15")
    plt.xlim(0,xlim)
    plt.ylim(0,ylim)
    plt.xlabel('time (seconds)', size = 15)
    plt.ylabel('vehicle speed (m/s)', size = 15)
    if timegap == 'HDV':
        plt.title('selected trajectories for HDV platoon' , size = 20)
    else :
        plt.title('selected trajectories for '+str(timegap) +' timegap setting' , size = 20)
    return

def plot_selected_speed_mixed_case(dataframe_name, xlim, ylim, speed, timegap,setting_list) : 
     
    """plot the speeds profiles of the car belonging to one platoon selected for the experiment
    cas of the mixed time gap acceptance platoon
    displays in addition to the plot a legend describing the setting of one's car"""   
    dataframe = pd.read_csv(dataframe_name)
    plt.plot(dataframe['Time'],dataframe['Speed2'],color = 'blue', label = '1st vehicle \n'+ setting_list[0]+' setting')
    for k in range(1,len(list(dataframe.columns))):
        if 'Speed' in list(dataframe.columns)[k]:
            plt.plot(dataframe['Time'],dataframe[list(dataframe.columns)[k]], alpha = 0.7,label = setting_list[k])
    plt.plot(dataframe['Time'],dataframe['Speed2'],color = 'blue')
    plt.legend(fontsize="12")
    plt.xlim(0,xlim)
    plt.ylim(0,ylim)
    plt.xlabel('time (seconds)', size = 15)
    plt.ylabel('vehicle speed (m/s)', size = 15)
    plt.title('selected trajectories for  '+str(timegap) +' timegap setting', size = 20)
    return

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


def plot_consumption_regression_engine(results_path,setting_list,MOTH_co2carb,marker_style_list,veh_list, label_list):
    """plot fuel consumtion vs position in platton mixed linear model regression using Engine experiments results"""

    df = engine.compute_df_emission_consumption(results_path,setting_list,MOTH_co2carb,veh_list)
    palette = itertools.cycle(sns.color_palette())
    for k in range(len(setting_list)): 
        data = df[df['setting']==setting_list[k]]
        data.columns = ['position','setting','consumption','CO2_emission']
        # Run LMER

        md = smf.mixedlm("consumption~position", data, groups=data["position"], re_formula='~position')
        mdf = md.fit()

        c = next(palette)
        performance = pd.DataFrame()
        performance["consumption"] = mdf.resid.values
        performance["position"] = data.position
        performance["predicted"] = mdf.fittedvalues

        sns.regplot(x = "position", y = "predicted",scatter=False, data = performance, color = c)
    plt.legend()
    return


def plot_consumption_regression_engine(df,formula, set_hue):
    """plot fuel consumtion vs position in platton mixed linear model regression using Engine experiments results"""

    data = df
 
    data["grp"] = data["setting"].astype(str) + data["position"].astype(str)
    md = smf.mixedlm(formula, data, groups=data["grp"])
    mdf = md.fit()

    performance = pd.DataFrame()
    performance["position"] = data.position
    performance["predicted"] = mdf.fittedvalues
    performance[set_hue] = data[set_hue]
    plt.rcParams["figure.figsize"] = (9,5)
    sns.lmplot(x = "position", y = "predicted",scatter=False,hue = set_hue, data = performance,legend_out=False,height=5, aspect=1.4)
    plt.xticks([k for k in range(1,12)],size = 14)
    plt.yticks(size = 14)
    plt.xlabel('position', size = 15)
    plt.ylabel('consumption [L/100km]', size = 15)
    plt.legend(fontsize = 15)
    return