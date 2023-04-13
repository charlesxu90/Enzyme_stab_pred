# Enzyme_stab_pred
Code for the Novozymes Enzyme Stability Prediction competition

## Create environment
```commandline
conda env create -f environment.yml
conda activate enzyme-pred-env
```

## Download data 
Following [this Notebook in Kaggle](https://www.kaggle.com/code/vslaykovsky/14656-unique-mutations-voxel-features-pdbs)

## Notebooks
- 0.14656-unique-mutations-voxel-features-pdbs.ipynb: prepare datasets for thermonet, need to install Rosetta and PyRosetta
- 0.explore_data.ipynb: explore the NESP dataset
- 1.0.EVmutation-0.264.ipynb
- 1.0.mutcompute-0.366.ipynb
- 1.2.plddt-and-ddg-0.399.ipynb
- 1.3.plldt-ddg-demask-sasa-0.451.ipynb
- 1.4.pyrosetta-scores.py
- 1.4.relaxed-rosetta-scores-0.546.ipynb
- 1.5.thermonet-v2-0.582.ipynb
- 1.6.pLDDT_diff-0.600.ipynb
- 1.7.rmsd-from-molecular-dynamics.ipynb
- 1.8.prot-bert-finetune-lb-0-30.ipynb
- 2.1.deletion_ensemble-0.603.ipynb
- 3.1.ensemble_ev_mc_ddg_demask_sasa_plddt-0.603-Copy1.ipynb
- 3.ensemble_1-0.603.ipynb
