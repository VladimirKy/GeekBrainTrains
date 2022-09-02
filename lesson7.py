# coding : utf-8

import turtle
import random

turtle.speed(0)

def goto_xy(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
def fill_color(x, y, z, r):
    turtle.fillcolor(x, y, z)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

answer = ''
i = 0
j = 1
is_right = False
while (answer != 'N') or (is_right == True):
    answer = turtle.textinput("Нарисовать окружность?", "Y/N ")
    if (answer == 'Y') and (j < 256):
        for i in range(j):
            goto_xy(random.randrange(-300,300), random.randrange(-300,300))
            fill_color(random.random(), random.random(), random.random(), random.randrange(1,100))
        j += j
    elif answer == 'N':
        turtle.textinput("Нажмите любую клавишу для выхода", "")
    elif (answer != 'Y') and (answer != 'N'):
        is_right == True
    elif (answer == 'Y') and (j > 255):
        turtle.textinput("Экран заполнен, нажмите любую клавишу для выхода", "")
        break
        