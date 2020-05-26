import pygame
import os.path

#initialize pygame
pygame.init ()

#create the screen
(screen_width, screen_height) = (1550, 790)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Cleo's World")

filepath = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(filepath, "practicebk.png")).convert()

R1 = pygame.image.load(os.path.join(filepath, "R1.png")).convert()
R2 = pygame.image.load(os.path.join(filepath, "R2.png")).convert()
R3 = pygame.image.load(os.path.join(filepath, "R3.png")).convert()
R4 = pygame.image.load(os.path.join(filepath, "R4.png")).convert()
R5 = pygame.image.load(os.path.join(filepath, "R5.png")).convert()
R6 = pygame.image.load(os.path.join(filepath, "R6.png")).convert()
R7 = pygame.image.load(os.path.join(filepath, "R7.png")).convert()
R8 = pygame.image.load(os.path.join(filepath, "R8.png")).convert()
R9 = pygame.image.load(os.path.join(filepath, "R9.png")).convert()

L1 = pygame.image.load(os.path.join(filepath, "L1.png")).convert()
L2 = pygame.image.load(os.path.join(filepath, "L2.png")).convert()
L3 = pygame.image.load(os.path.join(filepath, "L3.png")).convert()
L4 = pygame.image.load(os.path.join(filepath, "L4.png")).convert()
L5 = pygame.image.load(os.path.join(filepath, "L5.png")).convert()
L6 = pygame.image.load(os.path.join(filepath, "L6.png")).convert()
L7 = pygame.image.load(os.path.join(filepath, "L7.png")).convert()
L8 = pygame.image.load(os.path.join(filepath, "L8.png")).convert()
L9 = pygame.image.load(os.path.join(filepath, "L9.png")).convert()

char = pygame.image.load(os.path.join(filepath, "standing.png")).convert()




favicon = pygame.image.load(os.path.join(filepath, "cat-fav.png"))

pygame.display.set_icon(favicon)

walkRight = [R1, R2, R3, R4, R5, R6, R7, R8, R9]
walkLeft = [L1, L2, L3, L4, L5, L7, L7, L8, L9]
#bg = pygame.image.load('background_image')
#char = pygame.image.load('standing')

clock = pygame.time.Clock()

x = 50
y = 450
width = 64 #change this with different sprite
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    screen.blit(background_image, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        screen.blit(char, (x,y))    
    pygame.display.update()



#Loop to keep displaying the window
running = True
#How fast the screen reloads
#clock = pygame.time.Clock()
while running:
    clock.tick(27)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False 
    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0    

    if not (isJump):    
        # if keys[pygame.K_UP] and y > vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < screen_height - height:  
        #     y += vel
        if keys[pygame.K_SPACE]:
           isJump = True   
           right = False
           left = False
           walkCount = 0
    else: 
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10       

    redrawGameWindow()


pygame.quit()  