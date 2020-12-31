#################### smiley emoji##################################

import turtle
root=turtle.Turtle()
root.up()
root.goto(0,-100) #turtle will start from the center to -160
root.down()

root.begin_fill()
root.fillcolor("yellow")
root.circle(110) #size of circle you need
root.end_fill()

root.up()
root.goto(-67,-40) # from where your smile starts
root.setheading(-60)
root.width(5)
root.down()
root.circle(80,120) # for drawing mouth
root.fillcolor("") # fill color in eye is non

for i in range(-35,105,70):
    root.up()
    root.goto(i,35)
    root.setheading(0)
    root.down()
    root.begin_fill()
    root.circle(10) #for eyes
    root.end_fill()

turtle.mainloop()

