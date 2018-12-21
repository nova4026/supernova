import pygame 
pygame.init()
#          R    G     B
black = (  0,   0,    0)
white = (255, 255 , 255)
green = (  0, 255,    0)
blue =  (  0,   0,  255)

size = [800,600]
screen = pygame.display.set_mode(size)

#rectegle position

rect_x =50
rect_y =50

#vector of rectangle
rect_change_x= 2
rect_change_y= 2

pygame.display.set_caption("Super Nova!")
font = pygame.font.Font("C:/Windows/Fonts/ARIAL.TTF",25)
#primary game loop
done=False

clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT:# if user clicked close
            print("user wants to leave")
            done = True
    #game logic
    
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    if rect_x > 749 or rect_x < 0:
        rect_change_x *=-1
    if rect_y > 549 or rect_y < 0:
        rect_change_y *=-1
    
   
    screen.fill(white)      
    
    pygame.draw.rect(screen, black, [rect_x,rect_y,50,50])
    
    
    
   
    
    pygame.display.flip()
    
    # limits to 60 frames a second
    clock.tick(60)

pygame.quit()