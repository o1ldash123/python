import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("cyan")
my_wn.title("Turtle Maze")
myPen = turtle.Turtle()
myPen.color("blue")
size = 0
while True :
    for i in range(4) :
        myPen.fd(size + 1)
        myPen.left(90)
        size = size -5
    size += 1

