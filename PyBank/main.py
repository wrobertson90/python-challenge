import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
#variables to track financial data
total_months = 0
total_net = 0
net_profit = 0
net_loss= 0
profit_change=0
loss_change=0
greatest_increase=0
greatest_loss=0
