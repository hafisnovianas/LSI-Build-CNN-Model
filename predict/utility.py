import numpy as np
import pandas as pd
import os
import pickle
import shutil

def saveToExcel(data,file_name, folder_path):
    file_path = os.path.join(folder_path, file_name + '.xlsx')
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False, header=False)
    print(f'Data kontras telah disimpan ke {file_path}')

def saveToNpy(data, file_name, folder_path):
    file_path = os.path.join(folder_path, file_name + '.npy')
    np.save(file_path, data)

def saveToPickel(data,file_name,folder_path):
    file_path = os.path.join(folder_path, file_name + '.pkl')
    with open(file_path, 'wb') as file:
        pickle.dump(data,file)
    print(f'Data kontras telah disimpan ke {file_path}')

def pickle_load(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
    
def cetak(data):
    pd.set_option('display.max_rows', None)
    df = pd.DataFrame(data)
    print(df)
