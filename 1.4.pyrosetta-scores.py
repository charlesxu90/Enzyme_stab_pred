import os
import pandas as pd

import pyrosetta
pyrosetta.init()
from pyrosetta.teaching import *



relaxed_path = 'data/thermonet_wildtype_relaxed/wildtypeA'
files = os.listdir(relaxed_path)
relaxed_pdbs = [file for file in files if file.endswith(".pdb")]
mutation_to_pdb = {}
mutation_to_pdb['mutation'] = [file.split('_')[1] for file in relaxed_pdbs]
mutation_to_pdb['path'] = [file for file in relaxed_pdbs]
mutation_to_pdb_df = pd.DataFrame(mutation_to_pdb)
mutation_to_pdb_df.head()

scores = []
sfxn = get_score_function(True)
for i in range(len(mutation_to_pdb_df)):
    if not i % 100:
        print(i)
    pose = pyrosetta.pose_from_pdb(os.path.join(relaxed_path, mutation_to_pdb_df.iloc[i]['path']))
    scores.append(sfxn(pose))

mutation_to_pdb_df['scores'] = scores
scores = mutation_to_pdb_df
scores.head()
