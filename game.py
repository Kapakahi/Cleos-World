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


favicon = pygame.image.load(os.path.join(filepath, "cat-fav.png"))

pygame.display.set_icon(favicon)


x = 50
y = 450
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10


# def redrawGameWindow():
#   screen.blit(background_image,(0,0))
#   pygame.draw.circle(screen, (0,0,255), (150,50), 15, 1)



#   pygame.display.update()


#Loop to keep displaying the window
running = True
#How fast the screen reloads
#clock = pygame.time.Clock()
while running:
    pygame.time.delay(50)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:

        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
    if not (isJump):    
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - height:  
            y += vel
        if keys[pygame.K_SPACE]:
           isJump = True   
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

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
  #clock.tick(20)

  # redrawGameWindow()


pygame.quit()  