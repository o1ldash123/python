class Bird :
    def __init__(self):
        print("Bird is ready")

    def whoThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird) :
            
   def  __init__(self):
    super().__init__()
    print("Penguin is ready")

   def whoThis(self):
     print("Penguin")
   def Eun(self):
     print("Run faster")
Peggy = Penguin()
Peggy.whoThis()     
Peggy.swim()
Peggy.Eun()
