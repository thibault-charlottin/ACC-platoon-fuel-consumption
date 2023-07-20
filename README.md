This reposit contains the codes of the TRB paper Examing the impact of ACC vehicles over fuel consumption, an engine based experiment<br>

## File structure

'''
Main branch   
    ├── console.ipynb
    ├── setup.py
    ├── Readme.md 
    ├── .gitignore
    ├── data
        ├── Extracted_data
        ├── Engine_results
        ├── OpenACC_data
        ├── *HighD_data*
        └──  *ExiD_data*
    ├── conda
        └──  env.yaml
        ├── medium_setting
        ├── mixed
        └── no_ACC
    ├── VEHLIB
        └── VEHLIB_Simulation_analysis.ipynb
        ├── .mat_files
        ├── Vehlib_results
        ├── plot_data.py
        └── exploiting_vehlib.py
    └── src
        ├── __init__.py
        ├── compare_trajectories.py
        ├── examine_HighD.py
        ├── exploit_engine_data.py
        ├── exploiting_vehib.py
        ├── export_data.py
        ├── extract_event.py
        ├── plot_data.py
        ├── read_data.py
        └── smooth_data.py
'''
## Installation
To install the necessary packages follow the guidelines, be aware that they differ wheteher you are a Windows user or a Unix kernel based OS user.
### Unix distributions/MacOS installation

Copy your local path to this repository
THen open the command prompt
````bash
cd %paste your path
````

````bash
conda env create -f conda/env.yaml
````

Activate it:
````bash
conda activate engine_ACC_TRB_2023
````

You can then run the commands in the console.ipynb file 

### Windows installation
Copy your local path to this repository
Open Powershell and type
````bash
cd %paste your path
````

then type 
````bash
conda env create -f conda/env.yaml
````

Activate it:
````bash
conda activate engine_ACC_TRB_2023
````

You can then run the commands in the console.ipynb file 

## How to use this code

The data of the experiment using the engine bench and the OpenACC data is present in the data folder<br>
YOu can visualize it using the console.ipynb file<br>
⚠️ some cells are time consuming<br>
They are marked with the message 	'⚠️ next cell is time consuming' right above<br>
### Selecting the datasets
Run the cells in the console.ipynb file in the 'Selecting data' section<br>
### Plotting the engine bench results
Run the cells in the console.ipynb file in the 'data selected for the engine experiment' section to plot the speed profiles that we used<br>
Run the cells in the console.ipynb file in the 'Exploiting engine results' section to import the engine results and compute the mixed linear model<br>

### Using HighD and ExiD data to assess how often the triggering event occurs

First you need to get those two datasts<br>
Those two datasetys can be found at https://www.highd-dataset.com/#download and https://www.exid-dataset.com/#download<br>
To get them you need to make a request using the request box in the websites<br>

Then you can run the last cells of the console.ipynb file
## OPTIONAL : Recreating the engine results using VEHLIB 

Vehlib can be installed at https://gitlab.univ-eiffel.fr/eco7/vehlib<br>
you need to run the '#export data for engine' cell to get the input trajectories<br>
In VEHLIB select the **Renault_Kadjar_TCE130** vehicule to run the trajectories<br>
documentation about how to run VEHLIB can be found in the above reposit<br>
To analyze the data you can use the VEHLIB_Simulation_analysis notebook in the VEHLIB folder.<br>
Matlab scripts that you need to run are in ther VEHLIB/.mat_files folder<br>
Please order your simulation result files in the VEHLIB/Vehlib_results folder<br>

Already computed results are already present in the 'Vehlib result' folder within the VEHLIB folder

## Additional remarks

We advise you to run this code using a global IDE (VScode like) <br>
Good coding !