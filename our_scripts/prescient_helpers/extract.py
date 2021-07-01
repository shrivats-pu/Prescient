# extract.py: extracts data from runs and computes summary statistics into folder output in collated_outputs folder. Summary in summary.csv
# requirements: have already run iterations of prescient and saved the files to download folder, starting with prefix compilation_prefix
# intended system: Tiger or local
# dependencies: analyze_prescient_output
# created by: Ethan Reese
# email: ereese@princeton.edu
# date: June 21, 2021

import os
import pandas as pd
from prescient_helpers.analyze_prescient_output import CVaR
import numpy as np



def output_summary(compilation_prefix = "scen"):
        os.chdir("..")
        os.chdir("./downloads")


        all_files = os.listdir()

        dictionary = {}
        for dir in all_files:
                if (dir.startswith(compilation_prefix) and os.path.exists("./"+dir+"/output/overall_simulation_output.csv")):
                        dictionary.setdefault(dir[3:-3], [])
                        output_data = pd.read_csv("./"+dir+"/output/overall_simulation_output.csv")
                        dictionary[dir[3:-3]].append(output_data)
        os.chdir("..")
        os.chdir("./our_scripts/collated_outputs")
        table = pd.read_csv('./all_stochastic_test.csv')
        baseline = table['Total costs']
        dct = {}
        dct['asset'] = []
        
        for i in np.linspace(0.05, 1, 20):
                dct['CVaR ' + str(i) + ' Differential'] = []
        dct['CVaR 0.01 Differential'] = []
        dct['mean'] = []
        dct['quartile_1'] = []
        dct['quartile_3'] = []
        dct['max'] = []
        dct['min'] = []
        if not os.path.exists('outputs'):
                os.makedirs('outputs')

        for val in dictionary:
                output = pd.concat(dictionary[val], ignore_index = True)
                output.to_csv("./outputs/collated_"+val+".csv")
                dct['asset'].append(val)
                dct['mean'].append(output['Total costs'].mean())
                dct['quartile_1'].append(output['Total costs'].quantile(0.25))
                dct['quartile_3'].append(output['Total costs'].quantile(0.75))
                dct['max'].append(output['Total costs'].max())
                dct['min'].append(output['Total costs'].min()) 
                dct['CVaR 0.01 Differential'].append(CVaR(output['Total costs'], 0.01) - CVaR(baseline, 0.01))
                for i in np.linspace(0.05, 1, 20):
                        dct['CVaR ' + str(i) + ' Differential'].append(CVaR(output['Total costs'], i) - CVaR(baseline, i))
                df = pd.DataFrame(dct)

                df.to_csv("./summary.csv")
