from turtle import *
import turtle

#set background screen and size
backgroundScreen = Screen()
backgroundScreen.setup(500,500)
backgroundScreen.bgcolor('#FAFAA7')


#set font
fontStyle = ('Courier',32,'italic')
turtle.write('Hello',font=fontStyle,align='center')

# check postion - move mouse under word hello
turtle.write(turtle.pos())
turtle.pu()
turtle.goto(0,-150)
turtle.write(turtle.pos())

#draw circle
circleRadius = 50
turtle.pd()
turtle.circle(circleRadius)
turtle.pu()

#write text in the middle of M
turtle.goto(0,-100)
#turtle.write(turtle.pos())
turtle.write('Pui')
turtle.hideturtle() # hide turtle arrow 



#write number 7
turtle.reset()
turtle.color('blue')
turtle.pensize(3)
turtle.write(turtle.pos())
turtle.pd()
turtle.goto(50,0)
turtle.write(turtle.pos())
turtle.goto(25,-100)

#write number 8
turtle.pu()
turtle.goto(100,-50)
turtle.pd()

radian2 = 25
turtle.circle(radian2)

turtle.pu()
turtle.goto(100,-100)
turtle.pd()
turtle.circle(radian2)




input("Please enter any key to exit : ")