try :
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError as ex :
    print("Error details:", ex)