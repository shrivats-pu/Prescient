# Princeton PERFORM Prescient Scripts

A set of scripts that allow Prescient to be run on numerous scenarios that can be controlled with a variety of parameters and can produce various useful statistical output. Forked from Grid Parity Exchange's Prescient project.

## Installation and Setup
1. Navigate to installation directory
2. Clone git repository: 
```
git clone https://github.com/shrivats-pu/Prescient/
```
3. Install a frozen version of Egret from our github repository. The new version of Egret causes unexplained errors so we have saved an old version that is still functional.
```
git clone https://github.com/EthanReese/Egret
```
4. Activate Anaconda if not done already. On Princeton computing cluster:
```
module load anaconda3/2020.11
```
5. Enter the Prescient directory to begin configuring the virtual environment.
```
cd Prescient/
```
6. Create and activate an anaconda virtual environment from the .yml file included in the repository:
```
conda env create -f prescient_env.yml
conda activate prescient_env
```
7. Now, navigate back to the Egret directory and install the relevant libraries:
```
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
cd examples/unit_committment/
python uc_test_example.py
```
It should give the objective score of 490825.69978187. If you're using a solver other than Gurobi it is possible that the score might differ.

10. Navigate back to the Prescient folder to complete install of those libraries
```
cd ..
cd ..
cd ..
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
13. Now, use the downloader that ships with Prescient to download the RTS-GMLC data:
```
cd ..
cd prescient/downloaders
python rts-gmlc.py
```
This should take a few minutes but will install the relevant data set. There will be warnings that appear like errors but there should be no true errors.

14. Test out the installation by running a single run:
```
cd ..
cd ..
cd our_scripts/dev_tests
python run_ideal_single.py
```
This should run without errors. Again, there may be warnings from Prescient that appear to be errors.

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