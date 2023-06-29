# Import libraries
import csv
from pathlib import Path

#Set file paths for budget_data.csv
budget_filepath = Path('./Resources/budget_data.csv')

# define inital variables
total_months = 0
net_total_revenue = 0 

prev_month_revenue = 0
cur_month_revenue_change = 0
monthly_revenue_change_arr = []
month_of_revenue_change_arr = []



# Open the file in "read" mode ('r') and store the contents in the variable "csvfile"
with open(budget_filepath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

# loop thru the csv file and make calculation needed and store it in various variables 
    for row in reader:
        #Add 1 for the total number of months 
        total_months += 1
        
        #adding profits/losses to net total variable.
        net_total_revenue = net_total_revenue + int(row[1])
        
        # gathering the info needed to calculate average changes, max and min profits over a period
        cur_month_revenue_change = float(row[1]) - prev_month_revenue
        prev_month_revenue = float(row[1])
        monthly_revenue_change_arr.append(cur_month_revenue_change)
        month_of_revenue_change_arr.append(row[0])
        
#Remove the first elements in monthly_revenue_change_arr because the first month is a change of 0
monthly_revenue_change_arr.pop(0)
month_of_revenue_change_arr.pop(0)

#Grab the index and revenue of the greatest increase in profits. The index will be used to get the month
max_revenue_index = monthly_revenue_change_arr.index(max(monthly_revenue_change_arr))
max_revenue = max(monthly_revenue_change_arr)

#month of max revenue
max_revenue_month = month_of_revenue_change_arr[max_revenue_index]


#Grab the index and revenue of the greatest decrease in losses. The index will be used to get the month
min_revenue_index = monthly_revenue_change_arr.index(min(monthly_revenue_change_arr))
min_revenue = min(monthly_revenue_change_arr)

#month of max revenue
min_revenue_month = month_of_revenue_change_arr[min_revenue_index]

#calculate average and round to two decimal places
monthly_revenue_avg = round(sum(monthly_revenue_change_arr)/len(monthly_revenue_change_arr),2)




# print to terminal
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total_revenue}')
print(f'Average Monthly Change: ${monthly_revenue_avg}')
print(f'Greatest Increase in Profits: {max_revenue_month} (${int(max_revenue)})')
print(f'Greatest Decrease in Profits: {min_revenue_month} (${int(min_revenue)})')


# output analysis summary to file
summary = open("Summary_Financial_Analysis.txt", 'w')
summary.write(f'''Financial Analysis
------------------
Total Months: {total_months}
Total: ${net_total_revenue}
Average Monthly Change: ${monthly_revenue_avg}
Greatest Increase in Profits: {max_revenue_month} $({int(max_revenue)})
Greatest Decrease in Profits: {min_revenue_month} $({int(min_revenue)})''')

summary.close()
