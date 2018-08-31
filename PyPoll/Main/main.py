#PYPOLL
#---------------------------------------------------------------------

#importing necessary OS and CSV libraries
import os
import csv

list_voter = []
vote_khan = []
vote_correy = []
vote_li = []
vote_otooley = []

#locate CSV file path
election_data = os.path.join('..', 'Resources', 'election_data.csv')
#open CSV file
with open(election_data, newline='') as csvfile:

    #declare filename with specified delimiter as comma, using reader function
    csvreader = csv.reader(csvfile, delimiter = ',')
    #ignore the header to avoid counting this row as month
    next(csvfile)

    for row in csvreader:
        #append each row in voter file to list_voter list
        list_voter.append(row)

#loop through and build separate lists per candidate
for i in list_voter:
    if i[2] == "Khan":
        vote_khan.append(i[2])
    elif i[2] == "Correy":
        vote_correy.append(i[2])
    elif i[2] == "Li":
        vote_li.append(i[2])
    elif i[2] == "O'Tooley":
        vote_otooley.append(i[2])

#build a dictionary for built lists to derive winner
dict_votes = {"Khan": len(vote_khan), "Correy": len(vote_correy), "Li": len(vote_li), "O'Tooley": len(vote_otooley)}
winner = max(zip(dict_votes.values(), dict_votes.keys()))

#output results
print(f'\nElection Results\n-------------------------')
print(f'Total Votes: {len(list_voter)}\n-------------------------')
print(f'Khan: {round((len(vote_khan) / len(list_voter) * 100), 2)}% ({len(vote_khan)})')
print(f'Correy: {round((len(vote_correy) / len(list_voter) * 100), 2)}% ({len(vote_correy)})')
print(f'Li: {round(len(vote_li) / len(list_voter) * 100, 2)}% ({len(vote_li)})')
print(f'O\'Tooley: {round(len(vote_otooley) / len(list_voter) * 100, 2)}% ({len(vote_otooley)})')
print(f'------------------------')
print(f'Winner: {winner[1]}\n------------------------')

#output results to CSV (in same path as main.py)
output_path = os.path.join("Election_Data.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Election Results:'])
    csvwriter.writerow(['Khan:', len(vote_khan) / len(list_voter), len(vote_khan)])
    csvwriter.writerow(['Correy:', len(vote_correy) / len(list_voter), len(vote_correy)])
    csvwriter.writerow(['Li:', len(vote_li) / len(list_voter), len(vote_li)])
    csvwriter.writerow(['O\'Tooley:', len(vote_otooley) / len(list_voter), len(vote_otooley)])
    csvwriter.writerow(['Winner:', winner[1]])