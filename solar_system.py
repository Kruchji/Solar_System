import turtle
import math

#Window setup
wn = turtle.Screen()
wn.title("50% of the Solar System")
wn.bgcolor("black")
wn.setup(width=900, height=800)
wn.tracer(0)

#Planet movement method
def movement(self, radius, speed):
    self.setx(0 + math.cos(self.angle)*radius)
    self.sety(0 + math.sin(self.angle)*radius)
    self.angle += speed
turtle.Turtle.movement = movement

#Planet setup method
def setup(self, color, size):
    self.penup()
    self.color(color)
    self.shape("circle")
    self.shapesize(size,size)
    self.speed(0)
    self.angle = 0
turtle.Turtle.setup = setup

#I řekl Bůh: „Budiž světlo!“ A bylo světlo. (create the Sun)
sun = turtle.Turtle()
sun.color("yellow")
sun.dot(20*2.85)

#Mercury
mercury = turtle.Turtle()
mercury.setup("#BBB2AB", 1)

#Venus
venus = turtle.Turtle()
venus.setup("#DE9239", 2.48)

#Earth
earth = turtle.Turtle()
earth.setup("#69C4F1", 2.61)

#Mars
mars = turtle.Turtle()
mars.setup("#B04A34", 1.39)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)

#Some variables
baseSpeed = 0.0006
distMultiplier = 1.5

#Simulation loop
while True:
    #Planet specs
    mercury.movement(58*distMultiplier, baseSpeed*7.81)
    venus.movement(108*distMultiplier, baseSpeed*3.05)
    earth.movement(150*distMultiplier, baseSpeed*1.88)
    mars.movement(228*distMultiplier, baseSpeed*1)
    
    #Years and days counter (Earth)
    pen.clear()
    pen.write(str(math.floor(earth.angle/(2*math.pi))) + " Years    " + str(math.floor((360*earth.angle/(2*math.pi))%360)) + " Days", align="center", font=("Courier", 24, "bold"))
    
    #Next frame, please?
    wn.update()

#Copyright © 2003-2021 kruchi.cz a.s.