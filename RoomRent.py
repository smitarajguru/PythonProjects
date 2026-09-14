
rent = int(input("Enter your rent : " ))
foodorder = int(input("Enter the food Order amount :"))
Electricity = int(input("Enter the total of Electricity spend :"))
Charge = int(input("Enter the per Unit Charge : "))
persons = int(input("Enter the number of persons living in room:" ))

Electricity = Electricity * Charge;
Total = (rent + foodorder + Electricity  ) // persons

print("Each persons must pay amount is : ",Total)

Total = Total *persons
print("The Total amount is ",Total)