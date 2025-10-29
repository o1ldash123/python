def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = ('H','E','L','L','E','H')
if palind(r):
    print("This tuple is flip-flop")
else:
    print("This tuple is not flip-flop")