import pgzrun
from random import randint
from time import time
satalites=[]
next_satalite=0
lines=[]
WIDTH=800
HEIGHT=600  
TITLE="Connecting the satalites"
number_of_satalite=10
def create_satalite():
    for i in range(0,number_of_satalite):
        satalite=Actor("satalite")
        satalite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satalites.append(satalite)
def draw():
    screen.blit("background",(0,0))
    number=1
    for element in satalites:
        screen.draw.text(str(number),(element.pos[0],element.pos[1]+20))
        element.draw()
        number=number+1
    for element in lines:
        screen.draw.line(element[0],element[1],("white"))
        

        
    

def update():
    pass
def on_mouse_down(pos):
    global next_satalite,lines
    if next_satalite<number_of_satalite:
        if satalites[next_satalite].collidepoint(pos):
            if next_satalite:
                lines.append((satalites[next_satalite-1].pos,satalites[next_satalite].pos))
            next_satalite+=1
        else:
            lines=[]
            next_satalite=0
            









create_satalite()
pgzrun.go()