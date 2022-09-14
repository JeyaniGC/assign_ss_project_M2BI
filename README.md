# Secondary structure assigment project
#### Auteur : Jeyani George Clement 

## Download this repository

```bash
git clone https://github.com/JeyaniGC/assign_ss_project_M2BIgit
cd assign_ss_project_M2BI
```

## Install dependencies

### Conda environment

Install [conda](https://docs.conda.io/en/latest/miniconda.html).

Install mamba:

```bash
conda install mamba -n base -c conda-forge
```

Create conda environment and install dependendies:

```bash
mamba env create -f environment.yml
```

Load conda environment:

```bash
conda activate Projet_DSSP
```
## Clean PDB file

Choose a pdb file and then clean it by using this command :

```bash
grep "^ATOM" filename.pdb > new_file.pdb
```

## Download HBPLUS

Install [HBPLUS]{https://www.ebi.ac.uk/thornton-srv/software/HBPLUS/).

Execute HBPLUS : 

```bash
./hbplus
```

This will generate an .hb2 file that you will use for your analyze.

## Install DSSP

Run 3D model construction:

Install [DSSP]{https://ssbio.readthedocs.io/en/latest/instructions/dssp.html}


```bash
dssp -i filename.pdb -o filename.dssp
```
