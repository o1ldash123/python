num = int(input('Enter the number : '))
t = num 
numLen = 0

while t > 0 :
    numLen = numLen + 1
    t = int(t/10)

if numLen >=4 : 
    numLen = int(numLen / 2)
    chk = 0
    while num > 0 :
        rem = num% 10
        if chk == numLen :
            midOne = rem
        elif chk == (numLen - 1) :
            midTwo = rem
        num = int(num/10)
        chk = chk + 1
    prod = midOne * midTwo 
    print("\n Product of Mid digits (" + str(midOne) + "*" + str(midTwo) + ") =  "  , prod)
else :
  print('\nIt`s not a $ or more than a 4-digit number!!')


