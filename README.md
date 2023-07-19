This reposit contains the codes of the TRB paper Examing the impact of ACC vehicles over fuel consumption, an engine based experiment<br>

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

### From sources

Using [conda](https://docs.conda.io/en/latest/miniconda.html), create a new environment:

````bash
conda env create -f conda/env.yaml
````

Activate it:
````bash
conda activate engine_ACC_TRB_2023
````

Finally install the sources in the activated environment:

````bash
python -m pip install -e .
````


## Recreating the engine results using VEHLIB 

Vehlib can be installed at https://gitlab.univ-eiffel.fr/eco7/vehlib
you need to run the '#export data for engine' cell to get the input trajectories
In VEHLIB select the **Renault_Kadjar_TCE130** vehicule to run the trajectories
documentation about how to run VEHLIB can be found in the above reposit
To analyze the data you can use the VEHLIB_Simulation_analysis notebook in the VEHLIB folder.
Matlab scripts that you need to run are in ther VEHLIB/.mat_files folder
Please order your simulation result files in the VEHLIB/Vehlib_results folder

## How to get HighD and ExiD data

Those two datasetys can be found at https://www.highd-dataset.com/#download and https://www.exid-dataset.com/#download
To get them you need to make a request using the request box in the websites

