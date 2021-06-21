# run_drop_single.py: run scenarios where one asset is dropped out and the rest are stochatic
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 16, 2021

import os
import run_scripts.run_helpers as rh
import sys

path_template = "./scenario_dropped_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 1

dropped_asset = "./timeseries_data_files/101_PV_2_forecasts_actuals.csv"

def run(i):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+'%03d'%i)
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, dropped_assets=[dropped_asset])
        rh.run_prescient(i, False)
        os.chdir("..")

# program body
os.chdir("..")
os.chdir("./downloads")


for j in range(runs):
        run(j)

