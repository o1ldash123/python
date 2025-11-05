import array as arr

array_num = arr.array('i' , [1 , 2 , 3 , 4 , 5 , 4 , 9 ,3 ,7] )
print('Original array : ' , str(array_num))

print('Number of occurences of the number 3 in the said array : ' , str(array_num.count(3)))

array_num.reverse() 
print('Array after reversing : ' , str(array_num)) 