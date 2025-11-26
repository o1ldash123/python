class Computer :
    def __init__(self) :
        self.__maxprice = 900
    def sell(self) :
        print('selling Price : {}'.format(self.__maxprice))
    def setMXPrice(self , price) :
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()

c.setMXPrice(1000)
c.sell()