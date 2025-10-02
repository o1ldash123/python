def add(num1 , num2) :
    return num1 + num2
def sub(num1 , num2) :
    return num1 - num2

firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))
print('pick between + or - ')
print('A - addition')
print('B - subtraction')
operation = input('Enter your choice: ')

if operation == 'A' :
    print(f'The result is : {add(firstNumber , secondNumber)}')
elif operation == 'B' :
    print(f'The result is : {sub(firstNumber , secondNumber)}')
else :
    print('Invalid operation')