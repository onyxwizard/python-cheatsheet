#main.py

#from data_processing_project import cleaner,analyzer,utils
# from data_processing_project import clean_data,process_data,analyze_data

from data_processing_project import cleaner
from data_processing_project import analyzer
from data_processing_project import utils
raw_data = [1,2,3,4,4,5]
cleaned = cleaner.clean_data(raw_data)
processed = utils.process_data(cleaned)
length = analyzer.analyze_data(processed)

print(f"Final result length: {length}")

