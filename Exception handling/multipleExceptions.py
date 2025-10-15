try:
   num1 , num2 = eval(input("Enter two numbers separated by a comma: "))
   result = num1 / num2
   print("Result:", result)
except ZeroDivisionError :
   print("Error: Division by zero is not allowed.")
except SyntaxError :
   print('Comma is missing . enter numbers seperated by a comma like this :  ')
except :
   print('Wrong input')
else :
    print("No exceptions occurred.")
finally:
 print("This will execute no matter what.")