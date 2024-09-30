from pico2d import *
import math

move=1;
x=300
y=400

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
    
def run(frame,direction,x,y):
    move_all(frame,direction,x,y,0)

def handle_events():
    global move
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            move=5
        elif event.type == SDL_KEYDOWN and event.key==SDLK_RIGHT:
            move=0
        elif event.type == SDL_KEYDOWN and event.key==SDLK_LEFT:
            move=1
        elif event.type == SDL_KEYDOWN and event.key==SDLK_UP:
            move=2
        elif event.type == SDL_KEYDOWN and event.key==SDLK_DOWN:
            move=3

frame=0
while 1:
    handle_events()
    

    if move==5:
        break
    else:
       run(frame,move,x,y)
       
    frame = (frame+1)%4
    #print(move)

    
close_canvas()
