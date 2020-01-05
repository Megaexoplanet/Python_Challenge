import os
import csv
#Define variable for month
month_total = 0
#Define variable for sum of Profit/Losses
total_sum = 0
#Create empty list to store Profit/Losses
profits = []
#Define variable to define first value Profit/Losses as a string called Not Yet
previous_value = str("Not Yet")
#Define variable for net changes in Profit/Losses a different way
#net_profit = 0
#Create an empty list to store months
month_count = []
month_names = []


#Create path to open CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

#Open CSV file, read it, and skip header
with open(csv_path) as budget_data:

    reader = csv.reader(budget_data)
    
    header = next(reader)


#Loop through reader
    for row in reader:
#Capture values of rows in second column       
        current_value = row[1]
        #print(row)
        #Add each row to get month total
        month_total += 1
        #Append each values in column one to month count empty list
        month_count.append(row[0])
        print(month_total)
        #Sum values of profit/losses
        total_sum += int(row[1])
        print(total_sum)
        month_names.append(row[0])
        #Another way to sum values of profit/losses
        #net_profit = net_profit + int(row[1])

        #A loop to check for first row value in second column
        #When previous value is not "Not Yet" then loop executes to calculate changes between values in column 2
        if previous_value is not "Not Yet":
            #Calculation to find differences in values in column 2
            net_change = int(current_value) - int(previous_value)
            #Puts values from calculation of net change into the profits list
            profits.append(net_change)
        previous_value = current_value
    #create variable for the total change in profits/losses over period
    total_change = 0
    #create variable for maximum increase in profits
    current_max_change = 0
    #create variable for minimum increase in profits
    current_min_change = 0
    
    #loop that adds differences between values in list to find the total change in profits
    for profit in profits:
        total_change += profit
    #if 

    #define average change as the total chnage in profits divided by the count of members within set of profits
    average_change = total_change/len(profits)
    print(average_change)
    # find max val and month
    max_chg = max(profits)
    max_index = profits.index(max_chg)
    max_month = month_names[max_index]
    # find min val and month
    min_chg = min(profits)
    min_index = profits.index(min_chg)
    min_month = month_names[min_index]

    print('max chg', max_chg, 'in', max_month)
    print('min chg', min_chg, 'in', min_month)
    #s = f"max ${max_chg:}"