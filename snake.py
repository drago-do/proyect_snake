# This is a proyect of a game called Snake.
# This game is a simple game of snake.
# This game is made by: Drago

#importing libraries for the game
import pygame 
import random  #importing random library
import time 




pygame.init()
dis=pygame.display.set_mode((400,400))
pygame.display.update()
gameover = False

blue=(0,0,255)
red=(255,0,0)
#varibles for the snake position
snake_x = 200
snake_y = 200
snake_direction = "right"
snake_x += 10




def snake_move():
  global snake_x
  global snake_y
  if snake_direction == "right":
    snake_x += 10
  if snake_direction == "left":
    snake_x -= 10
  if snake_direction == "up":
    snake_y -= 10
  if snake_direction == "down":
    snake_y += 10





while not gameover:
  for event in pygame.event.get():
        print(event) 
        
        if event.type == pygame.QUIT:
            gameover = True
  pygame.draw.rect(dis,red,(snake_x,snake_y,10,10))
  pygame.display.update()
  time.sleep(0.1)
  
  # snake direction
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RIGHT:
      snake_direction = "right"
    if event.key == pygame.K_LEFT:
      snake_direction = "left"
    if event.key == pygame.K_UP:
      snake_direction = "up"
    if event.key == pygame.K_DOWN:
      snake_direction = "down"

  snake_move()
    






pygame.quit()
quit()


