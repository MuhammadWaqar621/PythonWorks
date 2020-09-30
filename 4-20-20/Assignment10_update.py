

import csv


#CT Sales Tax

def loadCSV():
    print("Loading CSV File.......")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

tax_rate = 6.35


print("1. Enter Receipt Data")
print("2. Load CSV Receipt Data")
print("3. Exit")
selection = int(input("Enter choice: "))
while True:
    if (selection<1 or selection>3):
        print("Your Enter the wrong number ,try again !!")
        selection = int(input("Enter choice: "))
    else:
        break 


if selection == 1:
    print("Enter Receipt ID Number Below")
    Year = input("Enter the date in the format of (YYYYMMDD):  ")
    ID = input("Enter seller/merchant/store/vendor_name:  ")
    Name_One = input("Enter the name of person one:  ")
    Name_Two = input("Enter the name of person two:  ")
    print("-------------------------------------------------------")
    item_one = int(input("Enter the price of the Xbox One:  "))
    item_two = int(input("Enter the price for the Flash Light:  "))
    item_three = int(input("Enter the price for the Apple MacBook:  "))

    tax = item_one + item_two + item_three * tax_rate
    split_bill = tax / 2
    print("-------------------------------------------------------")
    print("This is youre receipt below")
    print(Year, ID)
    print("Person One:", Name_One, "Person Two", Name_Two)
    print("Xbox One =", item_one)
    print("Flash Light =", item_two)
    print("Apple MacBook =", item_three)
    print("-------------------------------------------------------")
    print("Total Bill =", tax)
    print("Split Bil Total", split_bill)
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "ID", "Name_One","Name_Two","item_one","item_two","item_three","tax","split_bill"])
        writer.writerow([Year,ID,Name_One,Name_Two,item_one,item_two,item_three,tax,split_bill])
        
elif selection == 2:
    loadCSV()
elif selection == 3:
    exit 
