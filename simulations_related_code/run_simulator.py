import numpy as np
import pandas as pd
from scipy.stats import spearmanr
import random
import json
from paper_bursting_sim_for_many_runs import simulate
from multiprocessing import Pool

import multiprocessing
from time import sleep

#default parameter values are median from literature
params = {'k_on_TF': 0.27,
          'k_off_TF': 8.4,
          'burst_size_TF': 32,
          'k_on_Target': 0.25,
          'k_off_Target': 7.7,
          'burst_size_Target': 40,
          'splicing_half_life_minutes': 7,
          'mrna_half_life_TF': 2.5,
          'mrna_half_life_Target': 3.7,
          'protein_half_life': 24, 
          'protein_production_rate': 0.059,
          'labeling_efficiency': 0.8,
          'pulse_time': 60,
          'num_cells': 20_000,
          'dynamics': 'MM',
          'capture_efficiency': 1}
    
############ dictionaries for parameter values to test out #############
prot_thalf = {'Q1': 15, 'med': 28, 'Q3': 62}
mRNA_thalf_TF = {'Q1': 1.9, 'med': 2.5, 'Q3': 3.6}
tsn_rate = {'Q1': .022, 'med': .059, 'Q3': .179}
k_on_TF = {'Q1': .14, 'med': 0.27, 'Q3': .47}
k_off_TF = {'Q1': 1.5, 'med': 8.4, 'Q3': 48} ###ADJUST THESE? SWAP Q1 and Q3??
burst_size_TF = {'Q1': 20, 'med': 32, 'Q3': 59}
burst_size_Target = {'Q1': 23, 'med': 40, 'Q3': 74}
k_on_Target = {'Q1': 0.13, 'med': 0.25, 'Q3': 0.42}
k_off_Target = {'Q1': 2, 'med': 7.7, 'Q3': 77}
mRNA_thalf_Target = {'Q1': 2.67, 'med': 3.7, 'Q3': 5.16}
capture_efficiency = {'100': 1, '50': 0.5, '25': 0.25, '10': 0.1}

params_to_change = [capture_efficiency, prot_thalf, mRNA_thalf_TF, tsn_rate, k_on_TF, k_off_TF, burst_size_TF, burst_size_Target, k_on_Target, k_off_Target, mRNA_thalf_Target] 
param_names = ["capture_efficiency", "protein_half_life", "mrna_half_life_TF", "protein_production_rate", "k_on_TF", "k_off_TF", "burst_size_TF", "burst_size_Target", "k_on_Target", "k_off_Target", "mrna_half_life_Target"]

########################################################################

def caller(args_list):
    args, filename = args_list
    all_samples = simulate(**args)
    all_samples.to_csv(filename+".csv")

if __name__ == '__main__':
    #optional: run sim many times, vary parameter values
    num_runs = 25
    args_list = []
    for i in range(len(params_to_change)):
        param_to_change, param_name = params_to_change[i], param_names[i]
        print(param_name)
        for quartile in param_to_change:
            this_param_quartile_args = params.copy()
            this_param_quartile_args[param_name] = param_to_change[quartile]
            
            for sim_run in range(num_runs):
                filename = "sample_file"
                args_list.append((this_param_quartile_args, filename)
    
# loop over list of parameters
    with multiprocessing.Pool(processes=32) as pool:
        pool.map(caller, args_list)