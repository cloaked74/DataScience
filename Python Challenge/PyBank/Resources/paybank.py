import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('budget_data.csv')

Month = 0
Total = 0
Last_Month = 0
Month_Change = 0
Total_Mon_Change = 0
Best_Inc_Change = 0
Worst_Inc_Change = 0

with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
            
        Total = Total + int(row[1])

        Month_Change = int(row[1]) - Last_Month 
        if Month > 0:
            Total_Mon_Change = Total_Mon_Change + Month_Change

        if Month_Change >= Best_Inc_Change:
            Best_Inc_Change = Month_Change
            Best_Mon_Change = row[0]

        if Month_Change <= Worst_Inc_Change:
            Worst_Inc_Change = Month_Change
            Worst_Mon_Change = row[0]

        Last_Month = int(row[1])
        Month = Month + 1
    # Print out the wrestler's name and their percentage stats

    Avg = Total_Mon_Change / (Month - 1)
summary = f"""  
    Financial Analysis
    ----------------------------
    Total Months: {Month}
    Total: ${Total}
    Average  Change: {float(Avg)}
    Greatest Increase in Profits: {Best_Mon_Change} ({Best_Inc_Change}) 
    Greatest Decrease in Profits: {Worst_Mon_Change} ({Worst_Inc_Change})
    """
file = open('paybank.txt','w') 
file.write(summary)
