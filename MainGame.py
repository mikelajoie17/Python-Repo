#Messing around with Pygame
#trying to move some objects

#initialize pygame
import pygame
import time
import random
pygame.init()

pygame.display.set_caption("Block Dodger")
screen = pygame.display.set_mode((640, 480))

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
    
def main():

    #key variables
    clock = pygame.time.Clock()
    keepGoing = True
    player_x = 0
    player_y = 200
    box_x = 800
    box_y = 200
    box2_x = 800
    box2_y = 300
    box3_x = 800
    box3_y = 100
    x_speed = 0
    y_speed = 0
    boxesdodged = 0
    count = 0
    
    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()   
    background.fill(black)
    player = pygame.Surface((25, 25))
    player = player.convert()
    player.fill(green)
    myFont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myFont.render("Avoid the Blocks", 1,(255,255,0))
    floor = pygame.Surface((800,800))
    floor = floor.convert()
    floor.fill(blue)

    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill(red)

    box2 = pygame.Surface((50, 50))
    box2 = box2.convert()
    box2.fill(red)

    box3 = pygame.Surface((50, 50))
    box3 = box3.convert()
    box3.fill(red)

    #Set up main loop
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            # User pressed down on a key
            if event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                if event.key == pygame.K_RIGHT:
                    x_speed = 5
                if event.key == pygame.K_UP:
                    y_speed = -5
                if event.key == pygame.K_DOWN:
                    y_speed = 5
         
            # User let up on a key
            if event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT:
                    x_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP:
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    y_speed = 0

        #Move player according to speed
        if player_x < 0 and event.key == pygame.K_LEFT:
            x_speed = 0
        if player_x > 615 and event.key == pygame.K_RIGHT:
            x_speed = 0
        if player_y < 0 and event.key == pygame.K_UP:
            y_speed = 0
        if player_y > 320 and event.key == pygame.K_DOWN:
            y_speed = 0
        player_x += x_speed
        player_y += y_speed

        #modify box value 
        box_x -= 5
        if box_x <= 0:
            box_x = screen.get_width()
            boxesdodged += 1
        box2_x -= 3
        if box2_x <= 0:
            box2_x = screen.get_width()
            boxesdodged += 1
        box3_x -= 7
        if box3_x <= 0: 
            box3_x = screen.get_width()
            boxesdodged += 1 

      #  if player
       #     background.fill(red)
                       
        #Draw the screen
        screen.blit(background, (0,0))
        screen.blit(floor, (0,350))
        screen.blit(player, (player_x, player_y))
        screen.blit(label, (200, 20))
        blockcounter = myFont.render("Blocks Avoided : " + str(boxesdodged), 1,(255,255,0))
        screen.blit(blockcounter, (200, 400))
        screen.blit(box, (box_x, box_y))
        screen.blit(box2, (box2_x, box2_y))
        screen.blit(box3, (box3_x, box3_y))       
        pygame.display.flip() 

#runs the "main()" paragraph (called a fuction in python)
if __name__ == "__main__":
    main()

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
