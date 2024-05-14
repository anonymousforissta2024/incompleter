#Source: https://stackoverflow.com/questions/25674812/typeerror-cannot-concatenate-str-and-int-objects-need-help-fixing
ItemName = 0.0
Pounds = 0.0
Ounces = 0.0
Unit_Price = 0.0
Pound_Price = 0.0
Total_Price = 0.0

ItemName = raw_input("Enter ItemName")
Pounds = int(input("Enter amount of Pounds"))
Ounces = int(input("Enter amuont of Ounces"))
Pound_Price = int(input("Enter Pound_Price"))
Unit_Price = int(input("Enter Unit_Price"))

Total_Price = Pound_Price * (Pounds + Ounces / 16)

print("Item name is: " + ItemName)
print("Your Unit price is: $" + Unit_Price)
print("Your Total Comes To: $" + Total_Price)