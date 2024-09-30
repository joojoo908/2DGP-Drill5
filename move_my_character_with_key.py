from pico2d import *
import math

move=1;
key = False;
x=300
y=400
up,down,r,l = 0,0,0,0

TUK_WIDTH, TUK_HEIGHT = 1280 , 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

back = load_image('TUK_GROUND.png')
character = load_image('move_ani2.png')

def move_all(frame,move,x,y, rad):
    rad=rad/180* math.pi
    clear_canvas()
    back.draw(TUK_WIDTH/2, TUK_HEIGHT/2)
    if move==0 or move==1:
        character.clip_composite_draw(frame*55, move*80 ,55,80 ,rad,'i',x,y,100,150)
    elif move==2 or move==3:
        character.clip_composite_draw(55*4+frame*105, (move-2)*160 ,105,160 ,rad,'i',x,y,100,150)
    #character.clip_composite_draw(frame*100,0,100,100 ,rad,'v',x,y,100,100)
    update_canvas()
    delay(0.1)
    
def run(frame,direction,x,y):
    move_all(frame,direction,x,y,0)

def stand(x,y):
    run(0,3,x,y)

def handle_events():
    global move
    global key
    global up, down , r ,l
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            move=5
        elif event.type == SDL_KEYDOWN:
            key =True
            if event.key==SDLK_RIGHT:
                r=1;
            if event.key==SDLK_LEFT:
                l=1
            if event.key==SDLK_UP:
                up=1
            if event.key==SDLK_DOWN:
                down =1
            if event.key==SDLK_ESCAPE:
                move=5
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                r=0
            if event.key==SDLK_LEFT:
                l=0
            if event.key==SDLK_UP:
                up=0
            if event.key==SDLK_DOWN:
                down =0
            if up==0 and down==0 and r==0 and l==0:
                key=0;

frame=0
while 1:
    handle_events()
    if move==5:
        break
    else:
       if key:
           run(frame,move,x,y)
           if r:
               move=0
               x+=20;
           if l:
               move=1
               x-=20;
           if up:
               move=2
               y+=20;
           if down:
               move=3
               y-=20;
       else:
            stand(x,y)
            
       
    frame = (frame+1)%4
    #print(move)

    
close_canvas()
