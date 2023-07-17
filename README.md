This reposit contains the codes of the TRB paper Examing the impact of ACC vehicles over fuel consumption, an engine based experiment<br>

    Examing the impact of ACC vehicles over fuel consumption, an engine based experiment
    │   console.ipynb
    │   install.yml
    │   Readme.md 
    │   .gitignore
    ├── individual_trajectories
    ├── data_dor_engine
        ├── *various csv files used in the engine bench*
    ├── engine_results
        ├── 1_test_serie
        └── 2_test_serie
    ├── HighD_corrected_data
        └──  *HighD dataset trajectories smotthened via kernel regression*
    ├── data
        ├── long_setting
        ├── medium_setting
        ├── mixed
        └── no_ACC
    ├── src
        │   compare_trajectories.py
        │   examine_HighD.py
        │   exploit_engine_data.py
        │   exploiting_vehib.py
        │   export_data.py
        │   plot_data.py
        │   read_data.py
        │   smooth_data.py
    └── article
        └── *material for the article*

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


## Tutorials

Tutorials can be found in the doc/tutorials folder as jupyter notebook.

## Tests

To launch tests run the following command at the root of the project:
```bash
pytest tests --cov=mnms -v
```


## Documentation

### Build

To build the documentation using mkdocs, first update your conda environment with the doc dependencies:

```bash
conda activate mnms
conda env update --file conda/doc.yaml
```

Then build the doc:

```bash
mkdocs serve 
```
