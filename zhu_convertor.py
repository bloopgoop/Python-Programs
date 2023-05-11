def toPints(gallons):
    return gallons * 8

def toOunces(gallons):
    return gallons * 128

def toLiters(gallons):
    return gallons * 3.7854

def displayMenu():
    print("\n1. Choice 1: Convert Gallons to Pints\n"
          "2. Choice 2: Convert Gallons to Ounces\n"
          "3. Choice 3: Convert Gallons to Liters\n"
          "4. Choice 4: Exit the Program\n")

def getGallons():
    gallons = -1
    while gallons <= 0:
        gallons = float(input("Please enter your measure in Gallons: "))
    return gallons
          
def main():
    name = input("What is your name?: ")
    choice = 0
    while choice != 4:
        displayMenu()
        choice = int(input("Enter a choice: "))
        if choice == 1:
            print("The measure in Pints is", toPints(getGallons()))
        elif choice == 2:
            print("The measure in Ounces is", toOunces(getGallons()))
        elif choice == 3:
            print("The measure in Liters is", toLiters(getGallons()))
        elif choice == 4:
            print("Thanks for using the Metric Units Converter Application.")
        else:
            print("That is not an option.")
            
        
        
main()
