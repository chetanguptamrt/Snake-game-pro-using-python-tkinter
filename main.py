from tkinter import *
import lvl_1
import lvl_2
import lvl_3
import lvl_4
import lvl_5
import lvl_6
import lvl_7
import lvl_8
import lvl_9
import lvl_10

def side_up(event):
    global turn
    if turn=='LEFT' or turn=='RIGHT' or turn=='UP':
        turn='UP'
def side_down(event):
    global turn
    if turn=='LEFT' or turn=='RIGHT' or turn=='DOWN':
        turn='DOWN'
def side_left(event):
    global turn
    if turn=='UP' or turn=='DOWN' or turn=='LEFT':
        turn='LEFT'
def side_right(event):
    global turn
    if turn=='UP' or turn=='DOWN' or turn=='RIGHT':
        turn='RIGHT'

def run():
    global root,turn,snake_x,snake_y,life,frame_2,check_snake,active_fruit,fruit_x,fruit_y,level_manage,next_level
    #for delete old snake
    canvas.delete('snake')

    #-----------------------------------get fruit--------------------------------------------------------
    if active_fruit==1:
        canvas.delete('fruit')
        if level_manage==1:
            fruit_x,fruit_y,active_fruit=lvl_1.getfruit(snake_x,snake_y)
        elif level_manage==2:
            fruit_x,fruit_y,active_fruit=lvl_2.getfruit(snake_x,snake_y)
        elif level_manage==3:
            fruit_x,fruit_y,active_fruit=lvl_3.getfruit(snake_x,snake_y)
        elif level_manage==4:
            fruit_x,fruit_y,active_fruit=lvl_4.getfruit(snake_x,snake_y)
        elif level_manage==5:
            fruit_x,fruit_y,active_fruit=lvl_5.getfruit(snake_x,snake_y)
        elif level_manage==6:
            fruit_x,fruit_y,active_fruit=lvl_6.getfruit(snake_x,snake_y)
        elif level_manage==7:
            fruit_x,fruit_y,active_fruit=lvl_7.getfruit(snake_x,snake_y)
        elif level_manage==8:
            fruit_x,fruit_y,active_fruit=lvl_8.getfruit(snake_x,snake_y)
        elif level_manage==9:
            fruit_x,fruit_y,active_fruit=lvl_9.getfruit(snake_x,snake_y)
        elif level_manage==10:
            fruit_x,fruit_y,active_fruit=lvl_10.getfruit(snake_x,snake_y)

        canvas.create_rectangle(fruit_x*10+8,fruit_y*10+8,fruit_x*10+8,fruit_y*10+8,width=10,tag='fruit',outline='#E8290B')

    i=len(snake_x)-1
    while i>0:
        snake_x[i]=snake_x[i-1]
        snake_y[i]=snake_y[i-1]
        i-=1

    #------------------------------------next step--------------------------------------------------------
    if turn=='LEFT' and snake_x[0]==0 and (snake_y[0]==18 or snake_y[0]==19 or snake_y[0]==20 or snake_y[0]==21 or snake_y[0]==22 or snake_y[0]==23):
        snake_x[0]=41
    elif turn=='RIGHT' and snake_x[0]==41 and (snake_y[0]==18 or snake_y[0]==19 or snake_y[0]==20 or snake_y[0]==21 or snake_y[0]==22 or snake_y[0]==23):
        snake_x[0]=0
    elif turn=='RIGHT':
        snake_x[0]+=1
    elif turn=='LEFT':
        snake_x[0]-=1
    elif turn=='UP':
        snake_y[0]-=1
    elif turn=='DOWN':
        snake_y[0]+=1

    canvas.create_oval(snake_x[0]*10+3,snake_y[0]*10+3,snake_x[0]*10+13,snake_y[0]*10+13,width=2,tag='snake',fill='#000000')
    for i in range(len(snake_x)-1):
        canvas.create_oval(snake_x[i+1]*10+3,snake_y[i+1]*10+3,snake_x[i+1]*10+13,snake_y[i+1]*10+13,width=2,tag='snake')


    #----------------------------------for condition for all level----------------------------------------
    if level_manage==1:
        check_snake=lvl_1.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_1.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==2:
        check_snake=lvl_2.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_2.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==3:
        check_snake=lvl_3.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_3.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==4:
        check_snake=lvl_4.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_4.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==5:
        check_snake=lvl_5.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_5.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==6:
        check_snake=lvl_6.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_6.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==7:
        check_snake=lvl_7.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_7.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==8:
        check_snake=lvl_8.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_8.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==9:
        check_snake=lvl_9.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_9.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)
    elif level_manage==10:
        check_snake=lvl_10.check_condition(snake_x,snake_y)
        active_fruit,snake_x,snake_y=lvl_10.check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y)


    if active_fruit==1:
        fruit_variable.set(int(fruit_variable.get())-1)
        if fruit_variable.get()=='0':
            if level_manage<10:
                level_manage+=1
                status_variable.set("Good playing")
            elif level_manage==10:
                status_variable.set("congratulations")
                canvas.create_text(180,180,text='Congratulations',font='lucida 28 bold')
                level_manage=1
            canvas.delete('fruit')
            canvas.delete('snake')
            restart()
            next_level=True

    if check_snake==True:
        if life==1:
            status_variable.set("Game Over")
            life=3
            level_manage=1
            restart()
        else:
            status_variable.set("Try again")
            check_snake=False
            life-=1
            restart()

    elif next_level==False:
        root.after(200,run) 
    if next_level==True:
        next_level=False

def start(event=0):
    global turn
    canvas.delete('status')
    canvas.delete('fruit')
    root.unbind('<space>')
    status_variable.set("Playing")
    turn='RIGHT'
    run()

def restart():
    global snake_x,snake_y,turn,active_fruit,next_level

    active_fruit=1
    root.bind('<space>',start)
    for i in life_frame:
        i.destroy()
    for i in range(life):
        i=Label(frame_2_life,image=img)
        i.pack(side='left')
        life_frame.append(i)
    canvas.delete('design')

    #-------------------------------------start the level----------------------------------------------------
    if level_manage==1:
        snake_x,snake_y,turn=lvl_1.snake()
        level_variable.set(level[0])
        fruit_variable.set(Fruit[0])
        lvl_1.design(canvas)
    elif level_manage==2:
        snake_x,snake_y,turn=lvl_2.snake()
        level_variable.set(level[1])
        fruit_variable.set(Fruit[1])
        lvl_2.design(canvas)
    elif level_manage==3:
        snake_x,snake_y,turn=lvl_3.snake()
        level_variable.set(level[2])
        fruit_variable.set(Fruit[2])
        lvl_3.design(canvas)
    elif level_manage==4:
        snake_x,snake_y,turn=lvl_4.snake()
        level_variable.set(level[3])
        fruit_variable.set(Fruit[3])
        lvl_4.design(canvas)
    elif level_manage==5:
        snake_x,snake_y,turn=lvl_5.snake()
        level_variable.set(level[4])
        fruit_variable.set(Fruit[4])
        lvl_5.design(canvas)
    elif level_manage==6:
        snake_x,snake_y,turn=lvl_6.snake()
        level_variable.set(level[5])
        fruit_variable.set(Fruit[5])
        lvl_6.design(canvas)
    elif level_manage==7:
        snake_x,snake_y,turn=lvl_7.snake()
        level_variable.set(level[6])
        fruit_variable.set(Fruit[6])
        lvl_7.design(canvas)
    elif level_manage==8:
        snake_x,snake_y,turn=lvl_8.snake()
        level_variable.set(level[7])
        fruit_variable.set(Fruit[7])
        lvl_8.design(canvas)
    elif level_manage==9:
        snake_x,snake_y,turn=lvl_9.snake()
        level_variable.set(level[8])
        fruit_variable.set(Fruit[8])
        lvl_9.design(canvas)
    elif level_manage==10:
        snake_x,snake_y,turn=lvl_10.snake()
        level_variable.set(level[9])
        fruit_variable.set(Fruit[9])
        lvl_10.design(canvas)

if __name__ == "__main__":
    root=Tk()
    root.geometry('690x428+200+100')
    root.resizable(False,False)
    root.title('Snake game by Chetan Gupta')
    root.config(bg='black')
    root.bind('<Up>',side_up)
    root.bind('<w>',side_up)
    root.bind('<W>',side_up)
    root.bind('<Down>',side_down)
    root.bind('<s>',side_down)
    root.bind('<S>',side_down)
    root.bind('<Left>',side_left)
    root.bind('<a>',side_left) 
    root.bind('<A>',side_left)
    root.bind('<Right>',side_right)
    root.bind('<d>',side_right)
    root.bind('<D>',side_right)

    #--------------------------------------------------------------------------------
    level=[1,2,3,4,5,6,7,8,9,10]
    Fruit=[10,10,8,8,7,7,6,6,8,10]
    life=5
    life_frame=[]
    level_variable=StringVar() 
    fruit_variable=StringVar()
    status_variable=StringVar()
    level_manage=1
    next_level=False
    status_variable.set("Starting")
    #-------------------------------------------------------------------------------------
    canvas=Canvas(root,bg='#FFEA9F',height=421,width=421,bd=1,relief='ridge')
    canvas.pack(side=LEFT)
    frame_2=Frame(root,bg='#EAF0F1',width=250,height=400,bd=4,relief='sunken')
    frame_2.pack(side=RIGHT)

    #---------------------------------------------------------------------------
    l1=Label(frame_2,text='Snake Game',font='lucida 28 bold underline',width=11,heigh=2,fg='#2B2B52',bg='#EAF0F1')
    l1.pack()

    Label(frame_2,text='Status -    ',font='lucida 18 bold',fg='#000000',bg='#EAF0F1').pack()
    Label(frame_2,textvariable=status_variable,font='lucida 12 bold',fg='#0530DC',bg='#EAF0F1').pack(pady=(0,10))

    Label(frame_2,text='Press space for start',font='lucida 14',fg='#FF3031',bg='#EAF0F1').pack()
    Label(frame_2,text='Press up to move',fg='#2B2B52',bg='#EAF0F1').pack()
    Label(frame_2,text='Press down to move',fg='#2B2B52',bg='#EAF0F1').pack()
    Label(frame_2,text='Press left to move',fg='#2B2B52',bg='#EAF0F1').pack()
    Label(frame_2,text='Press right to move',fg='#2B2B52',bg='#EAF0F1').pack()
    Label(frame_2,text='You can also use A,S,W,D for move.',fg='#2B2B52',bg='#EAF0F1').pack(pady=(0,16))

    frame_2_level=Frame(frame_2,bg='#EAF0F1')
    frame_2_level.pack()
    Label(frame_2_level,text='Level - ',font='arial 16 bold',fg='#2B2B52',bg='#EAF0F1').pack(side='left')
    Label(frame_2_level,textvariable=level_variable,font='arial 16 bold',fg='#2B2B52',bg='#EAF0F1').pack(side='left')
    
    frame_2_fruit=Frame(frame_2,bg='#EAF0F1')
    frame_2_fruit.pack()
    Label(frame_2_fruit,text='Fruit - ',font='arial 16 bold',fg='#2B2B52',bg='#EAF0F1').pack(side='left')
    Label(frame_2_fruit,textvariable=fruit_variable,font='arial 16 bold',fg='#2B2B52',bg='#EAF0F1').pack(side='left')

    frame_2_life=Frame(frame_2,bg='#EAF0F1')
    frame_2_life.pack(pady=14)
    img=PhotoImage(file='assets\\life.png')

    restart()

    canvas.create_oval(snake_x[0]*10+3,snake_y[0]*10+3,snake_x[0]*10+13,snake_y[0]*10+13,width=2,tag='snake',fill='#000000')
    for i in range(len(snake_x)-1):
        canvas.create_oval(snake_x[i+1]*10+3,snake_y[i+1]*10+3,snake_x[i+1]*10+13,snake_y[i+1]*10+13,width=2,tag='snake')
    root.mainloop()