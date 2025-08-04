import turtle 
t=turtle.Turtle()
t.speed(1)
t.color("blue")
def draw_rect(w,l):
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(l)
        t.left(90)
draw_rect(100,200)
turtle.done()

