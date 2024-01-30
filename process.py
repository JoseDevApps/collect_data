from funciones import *
import os
'''
concatenacion de archivos excel
'''
# Identifying the files to merge
path = "E:/CPERv/TallerTransferencia/Datos/EGSA/Concatenar/Uyuni/GIZ/800-823/"
files = os.listdir(path)
files_xlsx = [f for f in files if f.endswith('.xlsx')]

# Reading the Excel files and concatenate them
mydf_list = [pd.read_excel(os.path.join(path, f),skiprows=2) for f in files_xlsx]
mydf = pd.concat(mydf_list)
print(mydf)
# Writing the merged data frame to a new Excel file
myoutput_path = "./output801_823.xlsx"
mydf.to_excel(myoutput_path, index=False)
