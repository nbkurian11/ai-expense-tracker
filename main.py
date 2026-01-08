import csv

def save_expense(vendor_name, amount):
    with open('expenses.csv','a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([vendor_name, amount])


vendor_name = input("What is the vendor name of the expense?")

amount = input("What is the amount of the expense?")

save_expense(vendor_name, amount)





