This repository contains the codes of the TRB paper "Examing the impact of ACC vehicles over fuel consumption, an engine based experiment". <br>

## File structure
```
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
```

## Installation
To install the necessary packages follow the guidelines, be aware that they differ wheteher you are a Windows user or a Unix kernel based OS user.
### Unix distributions/MacOS installation

### From sources

Using [conda](https://docs.conda.io/en/latest/miniconda.html), create a new environment:

````bash
conda env create -f conda/env.yaml
````

To activate the environment, run the following command:
````bash
conda activate engine_ACC_TRB_2023
````

Finally install the sources in the activated environment:

Activate it:
````bash
conda activate engine_ACC_TRB_2023
````


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

We advise you to run this code using a global IDE (VScode like) 