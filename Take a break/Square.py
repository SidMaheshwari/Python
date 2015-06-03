import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    sid = 3
    x=0
    y=0
    z=0
    for y in range(0,20):
        for x in range(0,4):
            brad.color(x,y,z)
            brad.forward(100)
            brad.right(90)
            x = (x)%256
            y = (y+50)%256
            z = (z+100)%256
           
        brad.right(20)

    
    window.exitonclick()
    

draw_square() 
    
