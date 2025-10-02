def cube(number) :
    return number * number * number


def byThree(number):
    if number % 3 == 0 :
        return cube(number)
    else :
        return False
    
print(byThree(50))
print(byThree(405))
print(byThree(90))
