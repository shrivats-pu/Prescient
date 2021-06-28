#!/bin/bash
#SBATCH --job-name=Parallel_ideal    # create a short name for your job 
#SBATCH --nodes=3                # node count
#SBATCH --ntasks=80               # how many instances of your command are run, total, across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G         # memory per cpu-core (4G is default)
#SBATCH --time=50:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=ereese@princeton.edu
module purge
module load anaconda3/2020.11
module load gurobi
conda activate prescient_env
cd /scratch/gpfs/ereese/big_run_ideal/Prescient/our_scripts/parallel_versions
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/101_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/101_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/101_PV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/101_PV_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/102_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/102_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/103_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/104_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/113_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_5_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_6_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_7_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_8_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_9_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/118_RTPV_10_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/119_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/215_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/213_RTPV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/201_HYDRO_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/RTPV_zone2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/215_HYDRO_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/Hydro_zone2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/215_HYDRO_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_6_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/222_HYDRO_5_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/PV_zone2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/215_HYDRO_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_7_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_10_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/310_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/309_WIND_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_5_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_12_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/314_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/314_PV_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/PV_zone3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/322_HYDRO_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_6_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/324_PV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/308_RTPV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/322_HYDRO_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/324_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/317_WIND_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_9_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/322_HYDRO_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_6_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/314_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_11_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/303_WIND_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/WIND_zone3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/310_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_4_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_13_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/314_PV_3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/324_PV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/Hydro_zone3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_2_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/RTPV_zone3_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/312_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/319_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_PV_1_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/313_RTPV_8_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/320_RTPV_5_forecasts_actuals.csv &
srun --exclusive -N 1 -n 1 python parallel_ideal.py ./timeseries_data_files/322_HYDRO_2_forecasts_actuals.csv &
wait