# extract.py: extracts data from runs and computes summary statistics
# created by: Ethan Reese
# email: ereese@princeton.edu
# date: June 21, 2021
import os
import pandas as pd
from output_analysis.analyze_prescient_output import CVaR
import numpy as np

os.chdir("..")
os.chdir("./downloads")


all_files = os.listdir()

dictionary = {}
for dir in all_files:
        if (dir.startswith("id_") and os.path.exists("./"+dir+"/output/overall_simulation_output.csv")):
                dictionary.setdefault(dir[3:-2], [])
                output_data = pd.read_csv("./"+dir+"/output/overall_simulation_output.csv")
                dictionary[dir[3:-2]].append(output_data)
os.chdir("..")
os.chdir("./our_scripts/collated_outputs")
table = pd.read_csv('./all_stochastic_test.csv')
baseline = table['Total costs']
dct = {}
dct['asset'] = []
dct['CVaR 0.05'] = []
dct['CVaR 0.01'] = []
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
        dct['CVaR 0.01'].append(CVaR(output['Total costs'], 0.01) - CVaR(baseline, 0.01))
        dct['CVaR 0.05'].append(CVaR(output['Total costs'], 0.01) - CVaR(baseline, 0.01))
df = pd.DataFrame(dct)

df.to_csv("./summary.csv")
