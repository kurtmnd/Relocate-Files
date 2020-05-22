# Relocate Pictures
# Last update: 2020-05-22
# Developed in Python 3.8.1

import pandas as pd
import os
import shutil
from shutil import copy

#folder='c:\NS\INET\Survey\Database'
FILE_WITH_PICS = 'lista-postes-1.csv'
#DATABASE_FOLDER = r'c:\NS\INET\Survey\Database\Photos\FNOR_2400-MB\FNOR-L1'
#DATABASE_FOLDER = r'c:\NS\INET\Survey\Database\Photos\FNOR_2400-MB\FNOR-L2'
DATABASE_FOLDER = r'c:\NS\INET\Survey\Database\Photos\FNOR_2400-MB\FNOR-L3'
NEW_FOLDER = 'Photos_2020-05-22'

df = pd.read_csv(FILE_WITH_PICS)
error_list = []
qty_photos = 0
for i,row in df.iterrows():
    x = row['foto']
    y = row['foto_ocupa']
    if y==y: x = x + ',' + y
    for pic in x.split(','):
        src = os.path.join(DATABASE_FOLDER,pic)
        dst = os.path.join(NEW_FOLDER,pic)
        qty_photos += 1
        #print('\nEntidad # {}\n{}\n{}'.format(i+1,src,dst))
        try:
            shutil.copy(src,dst)
        except Exception as e: error_list.append(e)

print('\nThere are {} photos in total.'.format(qty_photos))

if len(error_list)>0:
    print('\nThere have occurred {} errors:\n'.format(len(error_list)))
    for e in error_list:
        ''#print(e)
else: print('\nSuccessful transfer of 100% of photos.')
