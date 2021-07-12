# run_ideal_single.py: run scenarios where all assets except for one are deterministic. For testing purposes
# intended system: Tiger
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 16, 2021

import os
os.chdir("..")
import prescient_helpers.run_helpers as rh
import sys

path_template = "./scenario_ideal_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 1

deterministic_assets = [sys.argv[1]]
print(deterministic_assets)

def run(i):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+'%03d'%i)
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, deterministic_assets=deterministic_assets)
        rh.run_prescient(i, True)
        os.chdir("..")

# program body
os.chdir("..")
os.chdir("./downloads")

for j in range(runs):
        run(j)