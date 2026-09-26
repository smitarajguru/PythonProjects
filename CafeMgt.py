menu = {
'Pizza' : 110,
'Burger': 70,
'Cold-Coffee' : 35,
'Thick-Coffee' : 45,
'Pasta' : 50
}

print("......Welcome To Our Resturant........")
print(".....Order Now.....")
print(" Pizza : 110 Rs,Burger: 70Rs,Cold-Coffee : 35Rs,Thick-Coffee : 45Rs,Pasta : 50Rs")

order_total = 0

item = input("Enter you want to order an item : ")

if item in menu :
    order_total +=menu[item]
    print(f"your item {item} has been added to order")

else :
    print(f"Orderd item {item} is not in menu")

another_order = input(" Do you want any other item to add Yes/No : ")

if another_order == "Yes":
    item_2 = input(" Enter Second item :  ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"Item {item_2} has added to order ")

    else : 
        print(f"Ordered item {item_2} is not available !!")

print(f"The total amount the items to pay is {order_total}")

    

