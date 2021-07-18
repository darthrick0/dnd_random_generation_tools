import pandas
import os
from pathlib import Path
import json




#this may change depending on how files are structured
current_dir = Path.cwd()
print(current_dir)
# parent_dir = current_dir.parent()
# print(parent_dir)
json_dir = current_dir
# print(json_dir)
file_index = 0
for file in current_dir.rglob('*.xlsx'):

    current_excel = pandas.ExcelFile(file)
    for x in current_excel.sheet_names:
        print(x)
        current_dataframe = pandas.read_excel(file, sheet_name=x)
        print(current_dataframe)
        current_json = current_dataframe.to_json(str(file_index)+'.json',indent=4)

        print(current_json)
        file_index = file_index + 1

#for list of xlsx files
    #for get each sheet from each xlsx
        #create json
