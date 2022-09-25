## importing CSV file

from pathlib import Path
import csv

# setting file path to open
csvpath = Path("/Users/emreduman/desktop/python-homework/budget_data.csv")

## initializing variables and lists

num_months = 0
max_profit = 0
min_profit = 0
total_profitloss = 0
profitloss_list = []
dates = []

## open file path
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)

## calculate number of months and total PL, create lists 
    for row in csvreader:
        num_months += 1
        profitloss_list.append(int(row[1]))
        total_profitloss += int(row[1])
        dates.append(row[0])
        
## Set up formula to calculate change in Profit and Loss

change_pl = []

for i in range(1, len(profitloss_list)):
    x = profitloss_list[i] - profitloss_list[i - 1]
    change_pl.append(int(x))
    
    
## Set up formula to calculate average change in Profit and Loss

sum = 0

for i in range(0, len(change_pl)):
    sum += change_pl[i]
    avg_change_pl = round((sum / (len(change_pl))),2)
    
## For Loop to help identify months with max profit and min profit (biggest loss)

for pl in profitloss_list:
    
    if min_profit == 0:
        max_profit == pl
        min_profit == pl
    if pl > max_profit:
        max_profit = pl
    elif pl < min_profit:
        min_profit = pl
        
## Identify max and min profits amounts

max_profit_amount = profitloss_list.index(max_profit)
min_profit_amount = profitloss_list.index(min_profit)


## Identify months in which max and min profits occured

max_profit_date = dates[max_profit_amount]
min_profit_date = dates[min_profit_amount]

## Print Analysis

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {num_months} ")
print(f"Total: ${total_profitloss}")
print(f"Average Change: ${avg_change_pl}")
print(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_profit_date} (${min_profit})")

## Write and save output to a text file

output = Path('Financial_Analysis_Output.txt')

with open(output, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {num_months}\n")
    file.write(f"Total: ${total_profitloss}\n")
    file.write(f"Average Change: ${avg_change_pl}\n")
    file.write(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})\n")
    file.write(f"Greatest Decrease in Profits: {min_profit_date} (${min_profit})\n")