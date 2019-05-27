import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("background.gif")

#register the shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("ship.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()
# set score 0
score = 0

# draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="Left", font=("Arial", 12, "normal"))
score_pen.hideturtle()
# create the player turtle

player = turtle.Turtle()
player.color("blue")    
player.shape("ship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

# choose how many enemies

nr_enemies = 5
enemies = []
# add enemies to the list
for i in range(nr_enemies):
    # create the enemie      s
    enemies.append(turtle.Turtle())

# create the enemey
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemy_speed = 2

# create weapon

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup  ()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20




# define bullet state
# ready 
# fire

bullet_state = "ready"


def fire_bullet():
    global bullet_state 
    if bullet_state == "ready":
        os.system("afplay laser.wav&")
        bullet_state = "fire"
        # move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y   )
        bullet.showturtle()


# move the player
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


# collision check
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+ math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# main game loop

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)    

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy_speed *= -1

        if enemy.xcor() < -280:
            # move enemies down
            for e in enemies:
                y = e.ycor()
                y -=40
                e.sety(y)
            # change direction of move
            enemy_speed *= -1

        # check collision
        if isCollision(bullet, enemy):
            os.system("afplay explosion.wav&")
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400) 
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # update score
            score += 10
            score_pen.clear()
            score_string = "Score: {}".format(score)
            score_pen.write(score_string, False, align="Left", font=("Arial", 12, "normal"))


        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break       
    # move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # check if bullet has reached top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"    








delay = input("Press enter to finish:")