'''
Programa de concatenacion de datos Uyuni
'''
# importando bibliotecas
import pandas as pd
import numpy as np

def lectura(path, file,skiprows):
    '''
    Lectura del archivo excel
    '''
    source = path+'/'+file
    df = pd.read_excel(source,skiprows=skiprows)
    print(df)
    print(df.info())
