# Princeton PERFORM Prescient Scripts

A set of scripts that allow Prescient to be run on numerous scenarios that can be controlled with a variety of parameters and can produce various useful statistical output. Forked from Grid Parity Exchange's Prescient project.

## Installation and Setup
1. Navigate to installation directory (my recommendation is /scratch/gpfs/*your NETID*/)
2. Clone git repository: 
```
git clone https://github.com/shrivats-pu/Prescient/
```
3. Install a frozen version of Egret from our github repository. The new version of Egret causes unexplained errors so we have saved an old version that is still functional.
```
git clone https://github.com/shrivats-pu/Egret
```
4. Activate Anaconda if not done already. On Princeton computing cluster:
```
module load anaconda3/2020.11
```
5. Enter the Prescient directory to begin configuring the virtual environment.
```
cd Prescient/our_scripts/
```
6. Create and activate an anaconda virtual environment from the .yml file included in the repository:
```
conda env create -f prescient_env.yml
conda activate prescient_env
```
7. Now, navigate back to the Egret directory and install the relevant libraries:
```
cd ..
cd ..
cd Egret/
pip install -e .
```
8. Activate the Gurobi commercial optimizer already installed on Princeton computers:
```
module load gurobi/9.0.1 
```

9. Test the Egret Installation by navigating to testing folder and running the Python Scripts:
```
cd examples/unit_commitment/
python uc_test_example.py
```
It should give the objective score of 490825.69978187. If you're using a solver other than Gurobi it is possible that the score might differ.

10. Navigate back to the Prescient folder to complete install of those libraries
```
cd ../../..
cd Prescient/
```
11. Confirm there is a file named `setup.py` in this directory using `ls`. Run:
```
python setup.py develop
```
12. Move to `our_scripts` directory to install our helper library:
```
cd our_scripts/
python setup.py install
```

## Testing functionality with RTS-GMLC Data
1. Start from the root Prescient directory and use the downloader that ships with Prescient to download the RTS-GMLC data:
```
cd prescient/downloaders
python rts_gmlc.py
```
This should take a few minutes but will install the relevant data set. There will be warnings that appear like errors but there should be no true errors.

2. Test out the installation by running a single run:
```
cd ../../our_scripts/run_scripts
python run_all_Tiger_rts.py
```
This should run without errors. Again, there may be warnings from Prescient that appear to be errors.

## Testing Functionality With Texas-7k Data
The Texas-7k data is large and very complex. This should be run only on high performance computing clusters to make the execution time reasonable. Even on the clusters, the runtime for each of these steps will far exceed the 10 minute limit for processes on the login node (the command line). Thus, we will have to use the job scheduler to run these jobs.

1. Create a file called t7k.slurm using your text editor of choice (emacs or vim) and add the following preamble, replacing 'NETID' with your own netid and 'INSTALLATION DIRECTORY' with the path from root of the directory you chose in step 1 of the installation. Leave this file open. (Note: Where you choose to create this slurm file is entirely irrelevant).
```
#!/bin/bash
#SBATCH --job-name=7k_test    # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # how many instances of your command are run, total, across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=20G         # memory per cpu-core (4G is default)
#SBATCH --time=10:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=begin        # send email when job begins
#SBATCH --mail-type=end          # send email when job ends
#SBATCH --mail-type=fail         # send email if job fails
#SBATCH --mail-user=NETID@princeton.edu

module purge
module load anaconda3/2020.11
module load gurobi
conda activate prescient_env
cd INSTALLATION DIRECTORY/Prescient/prescient/downloaders
```

2. Add the following line to your file in order to activate our python downloader to download our cleaned and properly formatted version of the Texas-7k data:
```
python texas_7k.py
```

3. Add the two following lines to the slurm file to move to our scripts directory and run our script that intiates Prescient:
```
cd ../../our_scripts/run_scripts
python run_all_tiger.py $startdate$ $enddate$ $ndays$
```

4. Now close and save the file and enter the following command in the command line:
```
sbatch t7k.slurm
```
This will add the two tasks to the cluster's queue. They should take a few hours to complete.
## Usage
### Extraction Scripts
1. Activate Anaconda environment:
```
module load anaconda
conda activate prescient_env
```
2. Navigate to `our_scripts` folder
3. Enter the commands:
```
python
from prescient_helpers.extract import *
output_summary()
```
4. Navigate to folder `collated_output` to see the output. It will be a file named `summary.csv`.

## Authors

- Ethan Reese (ereese@princeton.edu)
- Arvind Shrivats (shrivats@princeton.edu)
