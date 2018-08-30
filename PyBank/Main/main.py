#PYBANK
#---------------------------------------------------------------------

#importing necessary OS and CSV libraries
import os
import csv

#prepare empty lists to store CSV data
list_profitloss = []
list_months = []
list_minmax = []

#locate CSV file path
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
#open CSV file
with open(budget_data, newline='') as csvfile:

    #declare filename with specified delimiter as comma, using reader function
    csvreader = csv.reader(csvfile, delimiter = ',')
    #ignore the header to avoid counting this row as month
    next(csvfile)

    for row in csvreader:
        #append only profit/loss to list for row count and average between month analysis
        list_months.append(str(row[0]))
        list_profitloss.append(int(row[1]))

#declare variables from populated lists
total_revenue = sum(list_profitloss)
total_months = len(list_months)
max_val = max(list_profitloss)
min_val = min(list_profitloss)
#zipped the profit/loss and month list with profit/loss first, so I can grab the row with either min/max value
list_minmax = list(zip(list_profitloss, list_months))

#use list comprehension to structure and populate a newly calculated net change list
#net change = difference between the current record - previous record
#use zip to compare: P/L list at index[0] with same P/L list at index[1] 
#subtract y-x for each record in list to get net change. 
# No value will be calculated for 10-Jan
net_change = [y - x for x, y in zip(list_profitloss, list_profitloss[1:])]


#declare a function to calculate straight average
def straight_average(num_list):
    total = 0.0
    length = len(num_list)
    for num in num_list:
        total += float(num)
    return(total / length)

#output results to console
print(f'\nFinancial Analysis\n--------------------------------')
print(f'Total Months:    {total_months}\nTotal Revenue:   ${total_revenue}')
print(f'Average Change:  ${round(straight_average(net_change),2)}')
print(f'Greatest Increase in Profits: {max(list_minmax)[1]}: {max(list_minmax)[0]}')
print(f'Greatest Decrease in Profits: {min(list_minmax)[1]}: {min(list_minmax)[0]}')

#output results to CSV (in same path as main.py)
output_path = os.path.join("Financial_Results.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Months:', total_months])
    csvwriter.writerow(['Total Revenue:', total_revenue])
    csvwriter.writerow(['Average Change:', round(straight_average(net_change),2)])
    csvwriter.writerow(['Greatest Increase in Profits:', max(list_minmax)[1], max(list_minmax)[0]])
    csvwriter.writerow(['Greatest Decrease in Profits:', min(list_minmax)[1], min(list_minmax)[0]])