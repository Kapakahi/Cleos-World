import pygame
import os.path

#initialize pygame
pygame.init ()

#create the screen
(width, height) = (1550, 800)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Cleo-chan')

filepath = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(filepath, "Xmas.png")).convert()


favicon = pygame.image.load(os.path.join(filepath, "cat-fav.png"))

pygame.display.set_icon(favicon)

def redrawGameWindow():
  screen.blit(background_image,(0,0))
  pygame.draw.circle(screen, (0,0,255), (150,50), 15, 1)
  pygame.display.update()


#Loop to keep displaying the window
running = True
#How fast the screen reloads
#clock = pygame.time.Clock()
while running:
  pygame.time.delay(50)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #clock.tick(20)

  redrawGameWindow()


pygame.quit()  