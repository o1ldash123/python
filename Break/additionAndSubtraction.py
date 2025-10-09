def add(a, b):
    return a + b
def subtract(a, b):
    return a - b



choice = input("Enter 'A' for addition or 'S' for subtraction: ").upper().strip()
def repeat():
 if choice == 'A':
    num1 =  int(input("Enter first number: "))
    num2 =  int(input("Enter second number: "))
    print(f"The result of addition is: {add(num1, num2)}")
 elif choice == 'S':
    num1 =  int(input("Enter first number: "))
    num2 =  int(input("Enter second number: "))
    print(f"The result of subtraction is: {subtract(num1, num2)}")
 else:
    print("Invalid choice. Please enter 'A' or 'S'.")
    repeat()
repeat()