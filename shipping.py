weight = float(input("Enter weight of item: "))
shipping = input("Regular or Overnight?: ").upper()

if shipping == "REGULAR":
    if weight < 5:
        print("Total price is $7.")
    elif weight > 10:
        print("Total price is $20.")
    else:
        print("Total price is $14.")

if shipping == "OVERNIGHT":
    if weight < 5:
        print("Total price is $15.")
    elif weight > 10:
        print("Total price is $40.")
    else:
        print("Total price is $25.")
            
    



