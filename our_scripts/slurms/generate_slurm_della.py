# generate_slurm_della.py: should make it easier to put together more complicated slurm jobs with arrays on della
# created by: Ethan Reese
# email: ereese@princeton.edu
# July 2, 2021

path = "/scratch/gpfs/ereese/run_dropped/Prescient/our_scripts/parallel_versions"
assets = ['./timeseries_data_files/314_PV_2_forecasts_actuals.csv',
             './timeseries_data_files/314_PV_4_forecasts_actuals.csv', './timeseries_data_files/PV_zone3_forecasts_actuals.csv',
            './timeseries_data_files/313_RTPV_3_forecasts_actuals.csv',
            './timeseries_data_files/322_HYDRO_1_forecasts_actuals.csv',
            './timeseries_data_files/320_RTPV_6_forecasts_actuals.csv', './timeseries_data_files/324_PV_3_forecasts_actuals.csv',
            './timeseries_data_files/313_RTPV_1_forecasts_actuals.csv',
            './timeseries_data_files/308_RTPV_1_forecasts_actuals.csv', './timeseries_data_files/322_HYDRO_3_forecasts_actuals.csv',
            './timeseries_data_files/324_PV_1_forecasts_actuals.csv', './timeseries_data_files/317_WIND_1_forecasts_actuals.csv',
            './timeseries_data_files/313_RTPV_9_forecasts_actuals.csv', './timeseries_data_files/320_RTPV_4_forecasts_actuals.csv',
            './timeseries_data_files/322_HYDRO_4_forecasts_actuals.csv', './timeseries_data_files/313_RTPV_6_forecasts_actuals.csv',
            './timeseries_data_files/314_PV_1_forecasts_actuals.csv', './timeseries_data_files/313_RTPV_11_forecasts_actuals.csv',
            './timeseries_data_files/303_WIND_1_forecasts_actuals.csv', './timeseries_data_files/320_RTPV_3_forecasts_actuals.csv',
            './timeseries_data_files/WIND_zone3_forecasts_actuals.csv',
            './timeseries_data_files/310_PV_2_forecasts_actuals.csv', './timeseries_data_files/313_RTPV_4_forecasts_actuals.csv',
            './timeseries_data_files/313_RTPV_13_forecasts_actuals.csv', './timeseries_data_files/314_PV_3_forecasts_actuals.csv',
            './timeseries_data_files/320_RTPV_1_forecasts_actuals.csv',
            './timeseries_data_files/313_PV_1_forecasts_actuals.csv', './timeseries_data_files/324_PV_2_forecasts_actuals.csv',
            './timeseries_data_files/Hydro_zone3_forecasts_actuals.csv', './timeseries_data_files/313_RTPV_2_forecasts_actuals.csv', './timeseries_data_files/RTPV_zone3_forecasts_actuals.csv',
            './timeseries_data_files/312_PV_1_forecasts_actuals.csv', './timeseries_data_files/319_PV_1_forecasts_actuals.csv',
            './timeseries_data_files/320_PV_1_forecasts_actuals.csv', './timeseries_data_files/313_RTPV_8_forecasts_actuals.csv',
            './timeseries_data_files/320_RTPV_5_forecasts_actuals.csv',  './timeseries_data_files/322_HYDRO_2_forecasts_actuals.csv'
             ]
print(len(assets))
preface = ["#!/bin/bash\n",
"#SBATCH --job-name=parallel_drop    # create a short name for your job \n",
"#SBATCH --nodes=1                # node count\n",
"#SBATCH --ntasks=1               # how many instances of your command are run, total, across all nodes\n",
"#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)\n",
"#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)\n",
"#SBATCH --array=0-37 \n"
"#SBATCH --time=70:00:00          # total run time limit (HH:MM:SS)\n",
"#SBATCH --mail-type=begin        # send email when job begins\n",
"#SBATCH --mail-type=end          # send email when job ends\n",
"#SBATCH --mail-type=fail         # send email if job fails\n",
"#SBATCH --mail-user=ereese@princeton.edu\n",
"module purge\n",
"module load anaconda3/2020.11\n",
"module load gurobi\n",
"conda activate prescient_env\n",
"cd "+ path + "\n", "\n",
"arg=()\n"]

file = open("parallel_drop_della_arvind.slurm", "w")
file.writelines(preface)

for asset in assets:
        file.write("arg+=(" + asset + ")\n")

file.write("srun -N 1 -n 1 python parallel_drop.py  ${arg[$SLURM_ARRAY_TASK_ID]}")