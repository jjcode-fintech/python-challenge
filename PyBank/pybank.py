# Import libraries
import csv
from pathlib import Path

#Set file paths for budget_data.csv
budget_filepath = Path('./Resources/budget_data.csv')

# define inital variables
total_months = []
total_amount = []
monthly_change_profit = []

monthly_change = 0
monthly_change_total = 0
initial_profit_counter = 0

# Open the file in "read" mode ('r') and store the contents in the variable "csvfile"
with open(budget_filepath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

# loop thru the csv file and make calculation needed and store it in various variables 
    for row in reader:
        total_months.append(row[0])
        sum_months = len(total_months)
        total_amount.append(float(row[1]))
        profit_for_month = int(row[1])
        monthly_change = float(profit_for_month)
        monthly_change_total = monthly_change_total + monthly_change
        initial_profit_counter = int(row[1])
        monthly_change_profit.append(monthly_change)
        max_profit = max(monthly_change_profit)
        max_index = monthly_change_profit.index(max_profit)
        min_profit = min(monthly_change_profit)
        min_index = monthly_change_profit.index(min_profit)
        avg_change_profit = round(monthly_change_total/sum_months)
        sum_amount = sum(total_amount)

# print analysis to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {sum_months}')
print(f'Total Amount: ${sum_amount}')
print(f'Average Monthly Change: ${sum_amount}')
print(f'Greatest Increase in Profits: {total_months[max_index]} ${max_profit}')
print(f'Greatest Decrease in Profits: {total_months[min_index]} ${min_profit}')

# output analysis summary to file
summary = open("Summary_Financial_Analysis.txt", 'w')
summary.write(f'''Financial Analysis
------------------
Total Months: {sum_months}
Total: ${sum_amount}
Average Monthly Change: ${avg_change_profit}
Greatest Increase in Profits: {total_months[max_index]} (${max_profit})
Greatest Decrease in Profits: {total_months[min_index]} (${min_profit})''')

summary.close()
