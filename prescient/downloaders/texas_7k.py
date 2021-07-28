# texas_7k.py: An adaption of rts_gmlc.py from Prescient to package texas 7k data
# into a form proper for Prescient
# author: Ethan Reese
# email: ereese@princeton.edu
# date: July 26, 2021

import os

this_file_path = os.path.dirname(os.path.realpath(__file__))
tx_download_path = os.path.realpath(os.path.join(this_file_path, os.path.normcase('../../downloads/texas-7k')))

def populate_input_data():
    from prescient.downloaders.texas_7k_prescient.process_texas_7k_data import create_timeseries
    from prescient.downloaders.texas_7k_prescient.tx7k_to_dat import write_template

    create_timeseries(tx_download_path)

    print("\nWriting dat template file...")
    write_template(dir=os.path.join(tx_download_path,'TEXAS-7K/TX_Data'),
                   file_name= os.path.join(tx_download_path,os.path.normcase('templates/tx_with_network_template_hotstart.dat')))

def copy_templates():
    from distutils.dir_util import copy_tree
    cur_path = os.path.join(this_file_path,os.path.normcase('texas_7k_prescient/runners'))
    new_path = tx_download_path

    copy_tree(cur_path, new_path)

# probably download it in a smoother way in the future
def download(branch='HEAD'):
    '''
    Clones Texas-7k data from https://github.com/EthanReese/texas_7k_data
    '''
    
    cur_path = os.getcwd()

    tx_path = os.path.realpath(os.path.join(tx_download_path,'TEXAS-7K'))

    if os.path.exists(tx_path):
        print('Texas-7k already downloaded to {0}. If you would like re-download it, delete the directory {0}.'.format(tx_path))
        return False

    print('Downloading Texas-7k into '+tx_path)

    url = 'https://github.com/EthanReese/texas_7k_data'

    clone_cmd = 'git clone '+url+' '+tx_path
    ret = os.system(clone_cmd)
    if ret:
        raise Exception('Issue cloning Texas-7k repository; see message above.')

    os.chdir(tx_path)

    os.chdir(cur_path)
    return True

if __name__ == '__main__':
    did_download = download()
    if did_download:
        copy_templates()
    populate_input_data()
    print('Set up Texas-7k data in {0}'.format(tx_download_path))