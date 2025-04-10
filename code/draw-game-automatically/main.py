import pygame
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('square game!')
game_over=False
location_x=200
location_y=100

left_x=0
top_y=0

change_interval = 240
change_timer=0
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
    change_timer += 1

    position=random.randint(0,3)
    if change_timer >= change_interval:
        change_timer = 0
        location_x = random.randint(0,dis_width)
        location_y = random.randint(0,dis_height)
        pygame.draw.rect(dis,red,[location_x, location_y, 1, 1])
        pygame.display.update()
        if position == 0: # left
            left_x = -10
            top_y = 0
        elif position == 1: #right
            left_x = 10
            top_y = 0
        elif position == 2: #up
            top_y = -10 
            left_x = 0
        elif position == 3: # down
            top_y = 10
            left_x = 0
    location_x += left_x
    location_y += top_y
    if location_x >= dis_width:
        location_x = 0
    elif location_x < 0:
        location_x = dis_width-50
    if location_y >= dis_height:
        location_y = 0
    elif location_y < 0:
        location_y = dis_height-50
#    pygame.draw.rect(dis,black,[location_x-left_x,location_y-top_y,50,50])
    pygame.draw.rect(dis,red,[location_x, location_y, 0.1, 0.1])
    pygame.display.update()
    clock.tick(120) 
pygame.quit()
quit()
