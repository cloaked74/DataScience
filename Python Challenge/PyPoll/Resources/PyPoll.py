import os
import csv

# Path to collect data from the Resources folder
pollCSV = os.path.join('election_data_sm.csv')

Total_Votes = 0
High_Vote = 0
Candidate = {}

with open(pollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)

    for row in csvreader:
        Total_Votes = Total_Votes + 1
        if row[2] in Candidate:
            #print (f"Key in")
            for name in Candidate:
               
                if row[2] == name:
                    Candidate[name] = Candidate.get(name) +1
                    #print(f"adding {name} {Candidate}")
        
        else:    
            #print(f"Key Not in")
            name = row[2]
            Candidate[name]=1
            #print(Candidate)
            
#print(Candidate)

file = open('pypoll.txt','w')
file.write(f"Election Results\n")
file.write(f"----------------------------\n")
file.write(f"Total Votes: {Total_Votes}\n")
file.write(f"----------------------------\n")

for name in Candidate:
    if Candidate.get(name) >= High_Vote:
        Winner = name
        High_Vote = Candidate.get(name)
    

counts = [f"Candidate: {name}: {round(Candidate.get(name)/Total_Votes*100,4)}% ({Candidate.get(name)})\n" for name in Candidate]
for counts in counts:
    file.write(counts)

file.write(f"----------------------------\n")
file.write(f"Winner: {Winner}\n")
file.write(f"----------------------------\n")
file.close()