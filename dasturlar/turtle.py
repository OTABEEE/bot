from turtle import*
bgcolor("black")
speed(0)
hideturtle()

for i in range(120):
	color("red")
	circel(i)
	color("orange")
	circel(i*0.8)
	right(3)
	forward(3)


done()