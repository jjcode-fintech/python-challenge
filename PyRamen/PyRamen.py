# Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []



# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
    # Initialize line_num variable
    row_count_menu = 0

    # Print the datatype of the file object
    # print(type(csvfile))

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    # print(type(csvreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    row_count_menu += 1
    
    # Print the header
    # print(f"{header} <---- HEADER")

    # Read each row of data after the header
    for row in csvreader:
        # Create an object to hold each row of data
        menu_obj = {
            "item": row[0],
            "category": row[1],
            "description": row[2],
            "price": float(row[3]),
            "cost": int(row[4])
        }
        # Append the menu object value to the list of menu array 
        menu.append(menu_obj)






# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function and (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # @TODO: Initialize dict object to hold our key-value pairs of items and metrics
    report = {}
    # Initialize a row counter variable
    row_count = 0
    
    # @TODO: Loop over every row in the sales list object




    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
