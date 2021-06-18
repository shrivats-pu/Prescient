# run_ideal_all.py: run scenarios for each asset where all assets except for it are deterministic
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 16, 2021

import os
import run_scripts.run_helpers as rh
import numpy as np
import pandas as pd
import sys
from output_analysis.analyze_prescient_output import CVaR

path_template = "./scenario_ideal_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 100

#deterministic_assets = sys.argv[1]

def run(i, det_assets):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+str(i))
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, deterministic_assets=det_assets)
        rh.run_prescient(i, True)
        os.chdir("..")

# program body
os.chdir("..")
os.chdir("./downloads")
assets = ['./timeseries_data_files/101_PV_1_forecasts_actuals.csv','./timeseries_data_files/101_PV_2_forecasts_actuals.csv',
              './timeseries_data_files/101_PV_3_forecasts_actuals.csv','./timeseries_data_files/101_PV_4_forecasts_actuals.csv',
              './timeseries_data_files/102_PV_1_forecasts_actuals.csv','./timeseries_data_files/102_PV_2_forecasts_actuals.csv',
              './timeseries_data_files/103_PV_1_forecasts_actuals.csv','./timeseries_data_files/104_PV_1_forecasts_actuals.csv',
              './timeseries_data_files/113_PV_1_forecasts_actuals.csv','./timeseries_data_files/118_RTPV_1_forecasts_actuals.csv',
              './timeseries_data_files/118_RTPV_2_forecasts_actuals.csv','./timeseries_data_files/118_RTPV_3_forecasts_actuals.csv',
              './timeseries_data_files/118_RTPV_4_forecasts_actuals.csv','./timeseries_data_files/118_RTPV_5_forecasts_actuals.csv',
             './timeseries_data_files/119_PV_1_forecasts_actuals.csv', './timeseries_data_files/215_PV_1_forecasts_actuals.csv',
             ]



for deterministic_assets in assets
        path_template = "id_" + deterministic_assets[24:-5] + "_"
        for j in range(runs):
                run(j, [deterministic_assets])

all_files = os.listdir()

dictionary = {}
for dir in all_files:
        if (dir.startswith("id_")):
                dictionary.setdefault(dir[4:-5], [])
                output_data = pd.read_csv("./"+dir+"/output/overall_simulation_output.csv")
                dictionary[dir[4:-5]].append(output_data)
os.chdir("..")
os.chdir("./our_scripts/collated_outputs")
table = pd.read_csv('./all_stochastic_test.csv')
baseline = table['Total costs']
dct = {}
dct['asset'] = []
dct['CVaR'] = []
dct['mean'] = []
dct['quartile_1'] = []
dct['quartile_3'] = []
dct['max'] = []
dct['min'] = []
for val in dictionary:
        output = pd.concat(dictionary[val], ignore_index = True)
        # TODO: Add the functionality to make the subfolder if it doesn't already exist
        output.to_csv("./outputs/collated_"+val+".csv")
        dct['asset'].append(val)
        dct['mean'].append(output['Total costs'].mean())
        dct['quartile_1'].append(output['Total costs'].quantile(0.25))
        dct['quartile_3'].append(output['Total costs'].quantile(0.75))
        dct['max'].append(output['Total costs'].max())
        dct['min'].append(output['Total costs'].min()) 
        dct['CVaR'].append(CVaR(output['Total costs'], 0.05) - CVaR(baseline, 0.05))
df = pd.DataFrame(dct)

df.to_csv("./summary.csv")