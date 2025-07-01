from turtle import Turtle, Screen


t = Turtle()
t.shapesize(1,1)
color_list = ["red", "white", "blue", "green", "black", "yellow"]


for _ in range(10):
    t.forward(50)
    t.color(color_list[_ % 6])
    


s = Screen()

s.exitonclick()
