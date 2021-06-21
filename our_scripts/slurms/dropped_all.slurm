#!/bin/bash
#SBATCH --job-name=dropped_all    # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # how many instances of your command are run, total, across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)
#SBATCH --time=100:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=ereese@princeton.edu

module purge
module load anaconda3/2020.11
module load gurobi
conda activate prescient_env
cd /tigress/ereese/some/Prescient/our_scripts

python run_drop_all.py
python extract.py