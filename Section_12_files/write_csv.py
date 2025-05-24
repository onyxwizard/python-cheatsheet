import csv
from os.path import exists

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
if not exists('countries.csv'):
    file = open('countries.csv','x')
    print("File Created")
    file.close()

file = open('countries.csv','w',newline='') # newline='' is added to eliminate new line
writer = csv.writer(file)
writer.writerow(header)
writer.writerow(data)    
file.close()


#Writing to CSV files using the DictWriter class

from pathlib import Path

# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']
file_name = Path('country_dict.csv')

# csv data
rows = [
        {
            'name': 'Albania',
            'area': 28748,
            'country_code2': 'AL',
            'country_code3': 'ALB'
        },
        {
            'name': 'Algeria',
            'area': 2381741,
            'country_code2': 'DZ',
            'country_code3': 'DZA'
        },
        {
            'name': 'American Samoa',
            'area': 199,
            'country_code2': 'AS',
            'country_code3': 'ASM'
        }
]
if not file_name.is_file():
    file = open('country_dict.csv', 'x')
    print("File Created")
    file.close()
    
with open('country_dict.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader() # if not used then CSV doesnt have header
    writer.writerows(rows)