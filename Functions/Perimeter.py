def PerSqr(side):
    perimeter = 4 * side
    return perimeter
def PerRec(length, width):
    perimeter = 2 * (length + width)  
    return perimeter  

print('pick any of the two shapes to calculate the perimeter of')
print('A - square')
print('B - rectangle')

choice = input('Enter choice A/B: ')

if choice.upper() == 'A' :
    side = int(input('Enter the length of the side of the square: '))
    print('The perimeter of the square is: ', PerSqr(side))
elif choice.upper() == 'B' :
    length = int(input('Enter the length of the rectangle: '))
    width = int(input('Enter the width of the rectangle: '))
    print('The perimeter of the rectangle is: ', PerRec(length, width))