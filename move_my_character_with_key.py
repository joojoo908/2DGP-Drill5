from pico2d import *
import math

open_canvas()

back = load_image('TUK_GROUND.png')
character = load_image('move_ani.png')

def move_all(frame,move,x,y, rad):
    rad=rad/180* math.pi
    clear_canvas()
    back.draw(300,400)
    character.clip_composite_draw(frame*100, move*150 ,100,150 ,rad,'i',x,y,100,150)
    #character.clip_composite_draw(frame*100,0,100,100 ,rad,'v',x,y,100,100)
    update_canvas()
    delay(0.05)
    
def run_forward(s,e):
    frame=0
    for x in range(s,e,10):
        move_all(frame,3,x,90,0)
        frame = (frame+1)%4



run_forward(0,800)

    
close_canvas()
