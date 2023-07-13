# MnMS :candy:

`MnMS` (**M**ultimodal **n**etwork **M**odelling and **S**imulation) is a multimodal dynamic traffic simulator designed for large-urban scale. It results from all research activites carried out within the ERC MAGnUM project. In a nutshell, users make travelling decisions considering all multimodal options on the city transportation network but motions are governed by regional multimodal MFD (macroscopic fundamental diagram) curves. So, all users share the same speed within a region and a transportation mode at a given time.

The research activities that led to this simulation package have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (grant agreement No 646592 – MAGnUM project)

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
