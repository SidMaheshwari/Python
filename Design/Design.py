import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.speed(10)
    for c in range(0,7):
        if(c ==0):
            brad.color("blue")
        elif(c==1):
            brad.color("green")
        elif(c==2):
            brad.color("violet")
        elif(c==3):
            brad.color("red")
        elif(c==4):
            brad.color("yellow")
        elif(c==5):
            brad.color("white")
        elif(c==6):
            brad.color("black")

        for a in range(0,36):
            for b in range(0,4):
                brad.forward(155 - c*25)
                brad.right(90)
              
            brad.right(10)
    brad.hideturtle()
    window.exitonclick()
    
draw_square() 
    
