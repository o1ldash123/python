class vehicle :
    def __init__(self , maxSpeed , mileage) :
        self.maxSpeed = maxSpeed
        self.mileage = mileage
modelX = vehicle(240 , 18)

print('Model Max speed :' , modelX.maxSpeed)
print('Model Mileage :' , modelX.mileage)
