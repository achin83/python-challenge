#importing necessary OS and CSV libraries to read CSV file
import os
import csv
#locate CSV file path
pyBankFile = os.path.join('..', 'Resources', 'budget_data.csv')
#open CSV file
with open(pyBankFile, newline='') as csvfile:

    #declare filename with specified delimiter as comma
    csvreader = csv.reader(csvfile, delimiter = ',')
    #ignore the header
    next(csvfile)
    for row in csvreader:
        print(row)