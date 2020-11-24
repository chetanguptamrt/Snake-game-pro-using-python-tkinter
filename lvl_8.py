import random

def design(obj):
    obj.delete('design')
    obj.create_rectangle(8,8,418,418,width=10,outline='#781414',tag='design')
    obj.create_line(8,208,173,208,width=10,fill='#781414',tag='design')
    obj.create_line(254,208,418,208,width=10,fill='#781414',tag='design')

def snake():
    snake_x=[9,8,7,6,5,4,3,2,1]
    snake_y=[19,19,19,19,19,19,19,19,19]
    turn='RIGHT'
    return snake_x,snake_y,turn


def check_condition(snake_x,snake_y):
    if snake_x[0]<1 or snake_y[0]<1 or snake_x[0]>40 or snake_y[0]>40:
        return True
    for i in range(1,17):
        if snake_x[0]==i and snake_y[0]==20:
            return True
    for i in range(25,41):
        if snake_x[0]==i and snake_y[0]==20:
            return True
    return False

def getfruit(snake_x,snake_y):
    j=0
    while j==0:    
        fruit_x=random.randint(1,40)
        fruit_y=random.randint(1,40)
        for i in range(len(snake_x)):
            if fruit_x==snake_x[i] and fruit_y==snake_y[i]:
                j=0
                break
            else:
                j=1
        for i in range(1,17):
            if fruit_x==i and fruit_y==20:
                j=0
                break
            else:
                j=1
        for i in range(25,41):
            if fruit_x==i and fruit_y==20:
                j=0
                break
            else:
                j=1
    return fruit_x,fruit_y,0

def check_fruit_condition(snake_x,snake_y,fruit_x,fruit_y):
    if snake_x[0]==fruit_x and snake_y[0]==fruit_y:
        snake_x.append(snake_x[len(snake_x)-1])
        snake_y.append(snake_y[len(snake_y)-1])
        return 1,snake_x,snake_y
    return 0,snake_x,snake_y

