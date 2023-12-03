# call in csv
import os
import csv

budget_data_csv = os.path.join(r"C:\Users\Lori Bissell\OneDrive\Documents\Data Analytics Bootcamp\python-challenge\Starter_Code\PyBank\Resources\budget_data.csv")

with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
# assign initial variables 
    months = 0
    total_net = 0
    total_change = 0

# skip the header row
    next(csv_reader)
    first_row = next(csv_reader)

# assign new variable to calculate requirements
    previous = int(first_row[1])
    months = months + 1
    total_net = total_net + previous
    greatest_increase = 0
    greatest_decrease = 0
  
# loop
    for row in csv_reader:
        months = months + 1
        current = int(row[1])
        total_net = total_net + current

# check the changes for increase and decrease
        change = current - previous
        if change > greatest_increase:
            greatest_increase = change
            increase_month = row[0]
        if change < greatest_decrease:
            greatest_decrease = change
            decrease_month = row[0]
        total_change = total_change + change
        previous = current
        
       
    avg_change = round(total_change / (months-1),2)
    #print(months)    
    #print(total_net)
    #print(avg_change)
    #print(greatest_increase)
    #print(greatest_decrease)
    #print(increase_month)

# print all the answers
print("Financial Analysis") 
print("-------------------------------------------")  
print(f"Total months: {months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits:: {decrease_month} ${greatest_decrease}")

# create the txt file
with open("PyBank/Analysis/pybank_result.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------------------------------\n")
    txt_file.write(f"Total months: {months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${avg_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {increase_month} ${greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profits: {decrease_month} ${greatest_decrease}\n")



    