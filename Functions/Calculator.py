def add(P,Q) :
    return P + Q

def subtract(P,Q) :
    return P - Q

def multiply(P,Q) :
    return P * Q

def divide(P,Q) :
    return P / Q

print('Please select the operation')
print('A - add')
print('B - subtract')
print('C - multiply')
print('D - divide')

choice = input('Enter choice A/B/C/D: ')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if choice.upper() == 'A' :
    print('The result of the addition is: ', add(num1,num2))
elif choice.upper() == 'B' :
    print('The result of the subtraction is: ', subtract(num1,num2))
elif choice.upper() == 'C' :
    print('The result of the multiplication is: ', multiply(num1,num2))
elif choice.upper() == 'D' :
    print('The result of the division is: ', divide(num1,num2))
else :
    print('Invalid input')
