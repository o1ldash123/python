testDict = {'Codingal': 2 , 'is': 2 , 'best' : 2 , 'for' : 2 , 'Coding' : 5}

print("Original Dictionary: " + str(testDict))

K = 'A'

res = 0 

for key in testDict :
    if testDict[key] == K :
        res += 1

print('Frequency of K is : ' + str(res))