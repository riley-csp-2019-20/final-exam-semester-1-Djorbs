#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Alex Reyes
#Date
#  12/12/19
#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#
#Bonus
#Add a feature to change colors
#
#import required libraries
import turtle as trtl
import random
#create turtle
shape = "arrow"
etch = trtl.Turtle(shape = shape)
#Variables
pen_size = 10
current_pen_state = 1
etch.pensize(3)
#movement functions
def Up():
    etch.setheading(90)
    etch.forward(3)
def Down():
    etch.setheading(270)
    etch.forward(3)
def Right():
    etch.setheading(0)
    etch.forward(3)
def Left():
    etch.setheading(180)
    etch.forward(3)
#color/drawing functions
def clear(): # Clear function
    etch.clear()
def up_size(): # Function makes the pensize bigger everytime the key is pressed
    global pen_size
    pen_size += 1
    etch.pensize(pen_size)
def down_size(): # Function makes the pensize smaller everytime the key is pressed
    global pen_size
    pen_size -= 1 
    etch.pensize(pen_size)
def change_pen(): # Checks a variable and then changes the state of the pen. Pendown is 1 and Penup is 0
    global current_pen_state
    if current_pen_state == 1:
        etch.penup()
        current_pen_state -= 1 
    elif current_pen_state == 0:
        etch.pendown()
        current_pen_state += 1
def random_color(): # Credit to Connor (he didn't help me during the final, but a long time ago he came up with this function :P )
  r = random.random()
  g = random.random()
  b = random.random()
  return (r,g,b)
def turtle_party(): # Might not be exactly what you want, but hey, you can change colors
    etch.pencolor(random_color())
#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(clear, "space")
wn.onkeypress(up_size, "o")
wn.onkeypress(down_size, "p")
wn.onkeypress(change_pen, "u")
wn.onkeypress(turtle_party, "r")
#listen
wn.listen()
#mainloop
wn.mainloop()