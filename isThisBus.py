class Vehicle :
    def __init__(self, vehicle_type , maxspeed , millage):
        self.vehicle_type = vehicle_type
        self.maxspeed = maxspeed
        self.millage = millage

class Bus(Vehicle):
    pass

SchoolBus = Bus("Bus", 180, 12)
print("Vehicle Type:", SchoolBus.vehicle_type , " Max Speed:", SchoolBus.maxspeed , " Millage:", SchoolBus.millage)
