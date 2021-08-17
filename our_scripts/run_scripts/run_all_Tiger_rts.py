# run_all_tiger.py: simple way to run batch operations on tiger
# authors: Ethan Reese
# email: ereese@princeton.edu
# created: June 14, 2021

import os
import our_scripts.prescient_helpers.run_helpers as rh

path_template = "./scenario_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 1


def run(i):
        rh.copy_directory(i, path_template, dir_path="./rts_gmlc")
        os.chdir(path_template+'%03d'%i)
        #rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path)
        rh.run_prescient(i, False, start_date="2020-07-10", end_date="2020-07-16", ndays=6)
        os.chdir("..")


# program body
os.chdir("..")
os.chdir("..")
os.chdir("./downloads")

for j in range(runs):
        run(j)