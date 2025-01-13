import csv
import os
os.makedirs("analysis", exist_ok= True)
file_to_load = os.path.join("PyBank/Resources", '../Resources/budget_data.csv' )  # Input file path
file_to_output = os.path.join("../analysis", '../budget_analysis.txt')  # Output file path
#variables to track financial data
total_months = 0
total_net = 0
previous_net=0
changes=[]
greatest_increase=["", 0]
greatest_decrease=["", 99999999]

with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_row=next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    for row in reader:
        date = row[0]
        net = int(row[1])
        total_months += 1
        total_net += net
        net_change = net-previous_net
        previous_net=net
        changes.append(net_change)

        if net_change>greatest_increase[1]:
            greatest_increase[0]=date
            greatest_increase[1]=net_change

        if net_change<greatest_decrease[1]:
            greatest_decrease[0]=date
            greatest_decrease[1]=net_change

average_change= sum(changes)/ len(changes)
output= (f"Financial Analysis"
         f"--------------\n"
         f"Total Months: {total_months}\n"
         f"Total: ${total_net:,}\n"
         f"Average Change: ${average_change:,}\n"
         f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]:,})\n"
         f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,})\n"
         )
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)