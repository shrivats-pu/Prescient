# run_ideal_all.py: run scenarios for zone 1 solar assets where everything is stochastic except each asset.
# requirements: proper install of Prescient and download of rts-gmlc data. saves outputs in non-collated form in downloads folder.
# intended system: Tiger
# dependencies: run_helpers.py
# author: Ethan Reese
# email: ereese@princeton.edu
# Created: June 16, 2021

import os
import prescient_helpers.run_helpers as rh
import numpy as np
import pandas as pd
import sys


path_template = "./scenario_ideal_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 100

#deterministic_assets = sys.argv[1]

def run(i, det_assets):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+'%03d'%i)
        rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path, deterministic_assets=det_assets)
        rh.run_prescient(i, True)
        os.chdir("..")

# program body
os.chdir("..")
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



for deterministic_assets in assets:
        path_template = "id_" + deterministic_assets[24:-4] + "_"
        for j in range(runs):
                run(j, [deterministic_assets])

