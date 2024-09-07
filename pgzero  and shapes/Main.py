import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="SHAPES"


def draw():
    r=255
    g=randint(0,255)
    b=0
    width=500
    height=300
    for i in range(20):
        square=Rect((0,0),(width,height))
        square.center=250,250
        screen.draw.rect(square,(r,g,b))
        r-=10
        b+=10
        width-=10
        height+=10



pgzrun.go()
