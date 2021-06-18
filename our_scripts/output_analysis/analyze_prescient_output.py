# analyze_prescient_output.py: creates graphs from collated Prescient data
# author: Arvind Shrivats
# email: shrivats@princeton.edu
# created: June 2021
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


def average_runs(df):
    return df.mean()


def produce_hist(lst, desc, plot_var=True):
    plt.figure()
    plt.hist(lst, bins=math.floor(len(lst)/20))
    plt.xlabel(desc)
    plt.ylabel("Frequency")
    plt.title("Histogram of " + desc + " over Fictitious Scenarios")
    if plot_var:
        plt.axvline(VaR(lst, 0.05, True), color='r')
    plt.show()


def produce_scatter(lst_x, lst_y, desc_x, desc_y):
    plt.figure()
    plt.scatter(lst_x, lst_y)
    plt.xlabel(desc_x)
    plt.ylabel(desc_y)
    plt.title(desc_x + " vs " + desc_y)
    plt.show()


def VaR(lst, alpha, upper_tail = True):
    # lst: list that we are interested in finding the VaR of
    # alpha: the level of VaR we are interested in
    # upper_tail: if true, then we will report the upper tail at alpha. if false, we will report the lower tail

    lst = sorted(lst)
    ecdf = (np.arange(len(lst)) + 1)/len(lst)
    if upper_tail:
        return lst[np.where(ecdf >= 1 - alpha)[0][0]]
    else:
        return lst[np.where(ecdf >= alpha)[0][0]]


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

# formed as a function to support imports
def run():
        os.chdir("..")
        os.chdir("./collated_outputs")

        data = pd.read_csv("collated_output_2.csv")
        baseline = pd.read_csv("collated_output_baseline.csv", index_col=0)

        baseline_avg = average_runs(baseline)
        print(VaR(data['Total costs'] - baseline_avg['Total costs'], 0.05, True))
        produce_hist(data['Total costs'] - baseline_avg['Total costs'], 'Total costs')


