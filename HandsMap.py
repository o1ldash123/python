def sqr(n) :
    return n * n

list1 =  [1,2 , 5 ,6 ]
list2 = [3,4 , 5 , 6 , 7]
print(list1 , '&' , list2)
result =  map(lambda x , y : x + y , list1 , list2)
print('Addition of two lists')
print(list(result))


square = list(map(sqr , list2))
print('Square of numbers in list')
print(square)