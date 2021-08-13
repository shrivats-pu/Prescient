# run_all_tiger.py: simple way to run batch operations on tiger
# authors: Ethan Reese
# email: ereese@princeton.edu
# created: June 14, 2021

import os
import prescient_helpers.run_helpers as rh
import sys

path_template = "./scenario_"
solar_path = "./solar_quotients.csv"
no_solar_path = "./no_solar_quotients.csv"
runs = 1

sd = sys.argv[1]
ed = sys.argv[2]
days = sys.argv[3]


def run(i):
        rh.copy_directory(i, path_template)
        os.chdir(path_template+'%03d'%i)
        #rh.perturb_data(rh.file_paths_combined, solar_path, no_solar_path)
        rh.run_prescient(i, True, start_date=sd, end_date=ed, ndays=days)
        os.chdir("..")


# program body
os.chdir("..")
os.chdir("..")
os.chdir("./downloads")

for j in range(runs):
        run(j)