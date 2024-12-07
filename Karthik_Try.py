# Import the Turtle Graphics module
import random
import turtle
import time

# Define program constants
WIDTH = 1000
HEIGHT = 800
DELAY = 200
FOOD_SIZE=32
SNAKE_SIZE=20

offsets={
"up":(0,SNAKE_SIZE),
"down":(0,-SNAKE_SIZE),
"left":(-SNAKE_SIZE,0),
"right":(SNAKE_SIZE,0),
}

def bind_directions():
    screen.onkey(lambda:set_snake_direction("up"),"Up")
    screen.onkey(lambda:set_snake_direction("right"),"Right")
    screen.onkey(lambda:set_snake_direction("down"),"Down")
    screen.onkey(lambda:set_snake_direction("left"),"Left")

def set_snake_direction(direction):
    global snake_direction
    if direction=="up":
        if snake_direction!="down":
            snake_direction="up"
    elif direction=="right":
        if snake_direction!="left":
            snake_direction="right"
    elif direction=="down":
        if snake_direction!="up":
            snake_direction="down"
    else:
        if snake_direction!="right":
            snake_direction="left"

def game_loop():
    stamper.clearstamps()
    newHead=snake[-1].copy()
    newHead[0]+=offsets[snake_direction][0]
    newHead[1]+=offsets[snake_direction][1]

    # Check collisions
    if newHead in snake or newHead[0] < -WIDTH/2 or newHead[0] > WIDTH/2 or  newHead[1] < -HEIGHT/2 or newHead[1] > HEIGHT/2:
        time.sleep(2)
        reset()
    else:

        snake.append(newHead)
        if not food_collision():
            snake.pop(0)
        stamper.shape("03_03/assets/snake-head-20x20.gif")
        stamper.goto(snake[-1][0],snake[-1][1])
        stamper.stamp()
        stamper.shape("circle")
        for segment in snake[:-1]:
            stamper.goto(segment[0],segment[1])
            stamper.stamp()
        screen.update()
        screen.title(f"Snake \t Score={score}")
        turtle.ontimer(game_loop,DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1],food_pos) < 20:
        food_pos=get_random_food_pos()
        for segment in snake:
            if get_distance(snake[-1],food_pos) < 20:
                food_pos=get_random_food_pos()
        food.goto(food_pos)
        score+=10
        return True
    return False

def get_random_food_pos():
    x=random.randint(int(-WIDTH/2)+FOOD_SIZE,int(WIDTH/2)-FOOD_SIZE)
    y=random.randint(int(-HEIGHT/2)+FOOD_SIZE,int(HEIGHT/2)-FOOD_SIZE)
    return (x,y)

def get_distance(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    return ((y1-y2)**2+(x1-x2)**2)**0.5

def reset():
    global score,snake,snake_direction,food_pos
    # Snake initialization
    snake=[[0,0],[SNAKE_SIZE,0],[2*SNAKE_SIZE,0],[3*SNAKE_SIZE,0]]
    snake_direction="up"
    score=0
    food_pos=get_random_food_pos()
    for segment in snake:
        if get_distance(snake[-1],food_pos) < 20:
            food_pos=get_random_food_pos()
    food.goto(food_pos)
    game_loop()

    # Draw initial snake
    stamper.shape("03_03/assets/snake-head-20x20.gif")
    stamper.goto(snake[-1][0],snake[-1][1])
    stamper.stamp()
    stamper.shape("circle")
    for segment in snake[:-1]:
        stamper.goto(segment[0],segment[1])
        stamper.stamp()

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake")
screen.bgpic("03_03/assets/bg2.gif")
screen.register_shape("03_03/assets/snake-food-32x32.gif")
screen.register_shape("03_03/assets/snake-head-20x20.gif")
screen.tracer(0) #turns off auto animation

# Event Handlers
screen.listen()
bind_directions()

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009ef1")
stamper.penup()

# Food
food=turtle.Turtle()
food.shape("03_03/assets/snake-food-32x32.gif")
food.shapesize(FOOD_SIZE/20)
food.penup()

reset()
# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()