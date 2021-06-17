# run_ideal_all.py: run scenarios for each asset where all assets except for it are deterministic
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 16, 2021

import os
import run_helpers as rh
import numpy as np
import pandas as pd

path_template = "./scenario_ideal_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 25

deterministic_assets = ['./timeseries_data_files/101_PV_1_forecasts_actuals.csv']

def run(i, det_assets):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+str(i))
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, deterministic_assets=det_assets)
        rh.run_prescient(i, True)
        os.chdir("..")

def CVaR(lst, alpha, upper_tail = True):
    # lst: list that we are interested in finding the VaR of
    # alpha: the level of VaR we are interested in
    # upper_tail: if true, then we will report the upper tail at alpha. if false, we will report the lower tail

    lst = sorted(lst)
    ecdf = (np.arange(len(lst)) + 1)/len(lst)
    if upper_tail:
        idx = np.where(ecdf >= 1 - alpha)[0][0]
        return np.mean(lst[idx:])
    else:
        idx = np.where(ecdf >= alpha)[0][0]
        return np.mean(lst[0:idx+1])

# program body
os.chdir("..")
os.chdir("..")
os.chdir("./downloads")


for asset in rh.file_paths_combined:
        path_template = "id_" + asset[24:-4] + "_"
        for j in range(runs):
                run(j, [asset])

all_files = os.listdir()

dictionary = {}
for dir in all_files:
        if (dir.startswith("id_")):
                dictionary.setdefault(dir[4:-2], [])
                output_data = pd.read_csv("./"+dir+"/output/overall_simulation_output.csv")
                dictionary[dir[4:-2]].append(output_data)

baseline = 1869231.707616
CVaRs = []
for val in dictionary:
        output = pd.concat(dictionary[val], ignore_index = True)
        output.to_csv("./outputs/collated_"+val+".csv")
        CVaRs.append(CVaR((x - baseline for x in output['Total costs']), 0.05))
df = pd.DataFrame(CVaRs)

df.to_csv("./CVaRs.csv")