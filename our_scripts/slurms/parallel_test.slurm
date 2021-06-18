#!/bin/bash
#SBATCH --job-name=Parallel test    # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=2               # how many instances of your command are run, total, across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)
#SBATCH --time=1:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=ereese@princeton.edu

module purge
module load anaconda3/2020.11
module load gurobi
conda activate prescient_env
cd /tigress/ereese/Prescient/our_scripts/run_scripts

srun -N 1 -n 1 python run_ideal_all.py ./timeseries_data_files/101_PV_1_forecasts_actuals.csv &
srun -N 1 -n 1 python run_ideal_all.py ./timeseries_data_files/101_PV_2_forecasts_actuals.csv &
wait

