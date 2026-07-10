
import turtle

tina = turtle.Turtle()
tina.shape("turtle")
tina_path = [1,2,3,4,5]
tina_progress = 0

screen = turtle.Screen()
screen.setup(500,500)

cam_colors = ('red', 'black', 'white', 'blue', 'green')

def show_animatronics(cam_num):
    #tina show
    if(cam_num == tina_path[tina_progress]):
        tina.showturtle()
    else


def open_cam1():
    print ("cam 1 open")
    screen. bgcolor(cam_colors[0])

def open_cam2():
    print ("cam 2 open")
    screen. bgcolor(cam_colors[1])

def open_cam3():
    print ("cam 3 open")
    screen. bgcolor(cam_colors[2])

def open_cam4():
    print ("cam 4 open")
    screen. bgcolor(cam_colors[3])

def open_cam5():
    print ("cam 5 open")
    screen. bgcolor(cam_colors[4])

exit_cam

screen.listen()
screen.onkay(open_cam1,"1")
screen.onkay(open_cam2,"2")
screen.onkay(open_cam3,"3")
screen.onkay(open_cam4,"4")
screen.onkay(open_cam5,"5")




screen.exitonclick()