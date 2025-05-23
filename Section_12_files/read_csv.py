import csv

# This approach is expensive and it uses arrays to find the data
# with open('country.csv','r') as file:
#     csv_reader = csv.reader(file)
#     for index,val in enumerate(csv_reader):
#         print(index,val)
        
    # to skip a line in csv use 
    #next(csv_reader)

#DictReader
# this uses dictionary to map values
# use same import csv
fieldnames = ['country_name', 'area', 'code2', 'code3'] # to rename header of csv
with open('country.csv','r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line)
        break
    



