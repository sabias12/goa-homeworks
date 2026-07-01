from turtle import*

speed(30)
color("red")
width("2")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200) 


#door
penup()
goto(70, 0)
pendown()

begin_fill()
color("green")
right(180)
forward(75)
right(90)
forward(60)
right(90)
forward(75)
end_fill()


penup()
goto(200, 200)
pendown()

begin_fill()
color("blue")
right(145)
forward(180)
left(110)
forward(173)
end_fill()


penup()
goto(200, 100)
pendown()


begin_fill()
right(55)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(0, 100)
pendown()

begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(659,339)
pendown()

color("red")
begin_fill()
forward(557)
left(125)
forward(172)
right(35)
forward(201)
right(90)
forward(202)
right(90)
forward(202)
left(40)
forward(5)
right(74)
forward(170)
left(124)
forward(765)
left(90)
forward(675)
left(90)
forward(1345)
left(90)
forward(665)
left(90)
forward(10)
end_fill()












exitonclick()