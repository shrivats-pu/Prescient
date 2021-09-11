# parallel_drop.py: Runs dropout tests based on command line argument
# intended system: Tiger
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 29, 2021

import os
import prescient_helpers.run_helpers as rh
import sys


solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 1000

dropped_asset = [sys.argv[1]]
path_template = "./scenario_dropped_" + dropped_asset[0][24:-21]

def run(i):
        rh.copy_directory(i, path_template, dir_path="./rts_gmlc")
        os.chdir(path_template+'%03d'%i)
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, dropped_assets=dropped_asset)
        rh.run_prescient(i, True)
        os.chdir("..")

# program body
os.chdir("..")
os.chdir("..")
os.chdir("./downloads")

for j in range(runs):
        run(j)
