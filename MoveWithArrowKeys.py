#Messing around with Pygame
#trying to move some objects

#initialize pygame
import pygame
pygame.init()

def main():
    #initialize display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Mike Test Program")

    #key variables
    clock = pygame.time.Clock()
    keepGoing = True
    box_x = 0
    box_y = 200
    x_speed = 0
    y_speed = 0
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()   
    background.fill((0, 0, 0))
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill(red)
    myFont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myFont.render("Sample Text Label", 1,(255,255,0))

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

        #Move box according to speed
        if box_x < 0 and event.key == pygame.K_LEFT:
            x_speed = 0
        if box_x > 615 and event.key == pygame.K_RIGHT:
            x_speed = 0
        if box_y < 0 and event.key == pygame.K_UP:
            y_speed = 0
        if box_y > 455 and event.key == pygame.K_DOWN:
            y_speed = 0
        box_x += x_speed
        box_y += y_speed            

            
                       
        #Draw the screen
        screen.blit(background, (0,0))
        screen.blit(box, (box_x, box_y))
        screen.blit(label, (200, 20))
        pygame.display.flip() 

#runs the "main()" paragraph (called a fuction in python)
if __name__ == "__main__":
    main()

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
