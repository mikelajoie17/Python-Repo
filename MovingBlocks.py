#Messing around with Pygame
#trying to move some objects

#initialize pygame
import pygame
pygame.init()

def main():
    #initialize display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Moving Blocks")

    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((255, 0, 0))

    box2 = pygame.Surface((50, 50))
    box2 = box2.convert()
    box2.fill((0, 255, 0))

    box3 = pygame.Surface((50, 50))
    box3 = box3.convert()
    box3.fill((0, 0, 255))

    myFont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myFont.render("Sample Text Label", 1,(255,255,0))

    #key variables
    clock = pygame.time.Clock()
    keepGoing = True
    box_x = 0
    box_y = 200
    box2_x = 0
    box2_y = 300
    box3_x = 0
    box3_y = 100

    #Set up main loop
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        #modify box value
        box_x += 5
        if box_x > screen.get_width():
            box_x = 0
        box2_x += 3
        if box2_x > screen.get_width():
            box2_x = 0
        box3_x -= 7
        if box3_x < 0: 
            box3_x = screen.get_width()
            
        #refresh screen        
        screen.blit(background, (0,0))
        screen.blit(box, (box_x, box_y))
        screen.blit(box2, (box2_x, box2_y))
        screen.blit(box3, (box3_x, box3_y))
        screen.blit(label, (200, 20))
        pygame.display.flip()

#runs the "main()" paragraph (called a fuction in python)
if __name__ == "__main__":
    main()


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

    
