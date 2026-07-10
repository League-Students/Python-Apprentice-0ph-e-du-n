
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina_path = [1,2,4,5]
tina_progress = 0

screen = turtle.Screen()
screen.setup(500,500)

cam_colors = ('red', 'gray', 'white', 'blue', 'green')

def move_tina():

def show_animatronics(cam_num):
    #tina show
    if(cam_num == tina_path[tina_progress]):
        tina.showturtle()
    else:
        tina.hideturtle()

def open_cam1():
    print ("cam 1 open")
    screen. bgcolor(cam_colors[0])
    show.animatronics(1)

def open_cam2():
    print ("cam 2 open")
    screen. bgcolor(cam_colors[1])
    show.animatronics(2)

def open_cam3():
    print ("cam 3 open")
    screen. bgcolor(cam_colors[2])
    show.animatronics(3)

def open_cam4():
    print ("cam 4 open")
    screen. bgcolor(cam_colors[3])
    show.animatronics(4)

def open_cam5():
    print ("cam 5 open")
    screen. bgcolor(cam_colors[4])
    show.animatronics(5)

def exit_cam():
    print("cam exited")
    screen.bgcolor("yellow")
    show.animatronics(-1)

screen.listen()
screen.onkey(open_cam1, "1")
screen.onkey(open_cam2, "2")
screen.onkey(open_cam3, "3")
screen.onkey(open_cam4, "4")
screen.onkey(open_cam5, "5")
screen.onkey(exit_cam,"0")



turtle.exitonclick()