import pygame
import random
import math
from pygame import mixer
import time
import sys
from tkinter import *

import mysql.connector
myDb = mysql.connector.connect(user='root', password='ashu3797', host='localhost',port=3306,database='helper',auth_plugin='mysql_native_password')
cur = myDb.cursor();

# cur.execute("CREATE DATABASE Scores");
cur.execute("use Scores")
# cur.execute("create table scores(Name varchar(100), score_value INT)")

speed_change = 16

pygame.init()
cur.execute("SELECT Name, score_value from scores where score_value = (select max(score_value) from scores)")
max_score_username, max_score_so_far  = (cur.fetchall()[0])

screen = pygame.display.set_mode((1550,800))

score_value = 0
max_scores_array = []
font = pygame.font.Font('freesansbold.ttf',26)
textX=10
textY=10

over_font = pygame.font.Font('freesansbold.ttf',20)

background = pygame.image.load("gotham.png")

    #background music
mixer.music.load("harry_potter.mp3")
mixer.music.play(-1)

    #title
pygame.display.set_caption("Gotham City Invaders")

    #player
playerImg = pygame.image.load("batman.png")
playerX = 370
playerY = 720
playerX_change = 0

    #Enemy details
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 14


for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load("superman.png"))
        enemyX.append(random.randint(0,735))
        enemyY.append(random.randint(50,150)) 
        enemyX_change.append(10)
        enemyY_change.append(40)

def enemy_position():
    for i in range(num_of_enemies):
        enemyX.append(random.randint(0,1400))
        enemyY.append(random.randint(50,150)) 
        enemyX_change.append(3)
        enemyY_change.append(40)


    #bullet details
    #ready state - You can't see the bullet
    #fire state - the bullet is currently moving
bulletImg = pygame.image.load("batrang.png")
bulletX = 0
bulletY = 700
bulletX_change = 0
bulletY_change = 28
bullet_state = "ready"


def show_max_score():
    score = over_font.render("Highest Score : "+ str(max_score_so_far),True,(255,255,255))
    name = over_font.render("Username : "+ str(max_score_username),True,(255,255,255))
    screen.blit(score,(1200,20));
    screen.blit(name,(1200,50))

def show_score(x,y):
    score = font.render("Score : "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# def game_ended():
#     print(score_value)
    # over_text = over_font.render("GAME OVER",True,(255,255,255))
    # screen.blit(over_text,(200,250))


def player(x,y):
    screen.blit(playerImg,(x,y)) # blit ~ to draw


def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y)) # blit ~ to draw

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    #Screen Colour
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))
    show_max_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            print(running)
            running = False

            # Which arrow key is pressed if pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -22
            if event.key == pygame.K_RIGHT:
                playerX_change = 22
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('shoot.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        #Boundries of Batman
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1495:
        playerX = 1500

        #ENEMY MOVEMENT
    for i in range(num_of_enemies):

            #Game over
        if enemyY[i] > 650:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            # game_ended()
            running = False

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = speed_change
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1495:
            enemyX_change[i] = -speed_change
            enemyY[i] += enemyY_change[i]

            #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound("batman.wav")
            explosion_sound.play()
            bulletY=700
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)

        #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)

    pygame.display.update()


root =Tk()
root.geometry("655x333")

def getvals():
    s = "INSERT INTO scores(Name, score_value) VALUES(%s, %s)"
    name = f"{namevalue.get()} ";
    if(len(name) <= 1): name = 'John Doe'
    b1 = [name, score_value]
    cur.execute(s,b1)
    myDb.commit();
    sys.exit()

game_over = Label(root, text="GAME OVER" , font="Helvetica 30 bold")
game_over.grid(row = 1, column = 3)

your_score = Label(root, text="Your Score: " + str(score_value), font="Helvetica 16 bold")
name =Label(root, text="Enter your Name" , font="Helvetica 16 bold")

your_score.grid(row = 3, column = 2)
name.grid(row=5, column=2)

namevalue = StringVar()

nameentry = Entry(root, textvariable=namevalue)
nameentry.grid(row=5, column=3)

btn = Button(root, text="Submit", command=getvals)
btn.grid(row = 7, column= 4)

root.mainloop()

