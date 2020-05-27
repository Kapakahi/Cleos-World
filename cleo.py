import pygame
import os.path
#initialize pygame
pygame.init ()

#create the screen
(screen_width, screen_height) = (1550, 790)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Cleo's World")

filepath = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(filepath, "images/practicebk.png")).convert()

width = 100
height = 100

cheese = pygame.image.load(os.path.join(filepath, "images/cheese.png"))
cheese = pygame.transform.scale(cheese, (30, 30))


R1 = pygame.image.load(os.path.join(filepath, "images/Walk (1).png"))
R1 = pygame.transform.scale(R1, (width, height))
R2 = pygame.image.load(os.path.join(filepath, "images/Walk (2).png"))
R2 = pygame.transform.scale(R2, (width, height))
R3 = pygame.image.load(os.path.join(filepath, "images/Walk (3).png"))
R3 = pygame.transform.scale(R3, (width, height))
R4 = pygame.image.load(os.path.join(filepath, "images/Walk (4).png"))
R4 = pygame.transform.scale(R4, (width, height))
R5 = pygame.image.load(os.path.join(filepath, "images/Walk (5).png"))
R5 = pygame.transform.scale(R5, (width, height))
R6 = pygame.image.load(os.path.join(filepath, "images/Walk (6).png"))
R6 = pygame.transform.scale(R6, (width, height))
R7 = pygame.image.load(os.path.join(filepath, "images/Walk (7).png"))
R7 = pygame.transform.scale(R7, (width, height))
R8 = pygame.image.load(os.path.join(filepath, "images/Walk (8).png"))
R8 = pygame.transform.scale(R8, (width, height))
R9 = pygame.image.load(os.path.join(filepath, "images/Walk (9).png"))
R9 = pygame.transform.scale(R9, (width, height))
R10 = pygame.image.load(os.path.join(filepath, "images/Walk (10).png"))
R10 = pygame.transform.scale(R10, (width, height))

L1 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (1).png"))
L1 = pygame.transform.scale(L1, (width, height))
L2 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (2).png"))
L2 = pygame.transform.scale(L2, (width, height))
L3 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (3).png"))
L3 = pygame.transform.scale(L3, (width, height))
L4 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (4).png"))
L4 = pygame.transform.scale(L4, (width, height))
L5 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (5).png"))
L5 = pygame.transform.scale(L5, (width, height))
L6 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (6).png"))
L6 = pygame.transform.scale(L6, (width, height))
L7 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (7).png"))
L7 = pygame.transform.scale(L7, (width, height))
L8 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (8).png"))
L8 = pygame.transform.scale(L8, (width, height))
L9 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (9).png"))
L9 = pygame.transform.scale(L9, (width, height))
L10 = pygame.image.load(os.path.join(filepath, "images/WalkLeft (10).png"))
L10 = pygame.transform.scale(L10, (width, height))

J1 = pygame.image.load(os.path.join(filepath, "images/Jump (1).png"))
J1 = pygame.transform.scale(J1, (width, height))
J2 = pygame.image.load(os.path.join(filepath, "images/Jump (2).png"))
J2 = pygame.transform.scale(J2, (width, height))
J3 = pygame.image.load(os.path.join(filepath, "images/Jump (3).png"))
J3 = pygame.transform.scale(J3, (width, height))
J4 = pygame.image.load(os.path.join(filepath, "images/Jump (4).png"))
J4 = pygame.transform.scale(J4, (width, height))
J5 = pygame.image.load(os.path.join(filepath, "images/Jump (5).png"))
J5 = pygame.transform.scale(J5, (width, height))
J6 = pygame.image.load(os.path.join(filepath, "images/Jump (6).png"))
J6 = pygame.transform.scale(J6, (width, height))
J7 = pygame.image.load(os.path.join(filepath, "images/Jump (7).png"))
J7 = pygame.transform.scale(J7, (width, height))
J8 = pygame.image.load(os.path.join(filepath, "images/Jump (8).png"))
J8 = pygame.transform.scale(J8, (width, height))
J9 = pygame.image.load(os.path.join(filepath, "images/Jump (9).png"))
J9 = pygame.transform.scale(J9, (width, height))
J10 = pygame.image.load(os.path.join(filepath, "images/Jump (10).png"))
J10 = pygame.transform.scale(J10, (width, height))

char = pygame.image.load(os.path.join(filepath, "images/Idle (1).png"))
char = pygame.transform.scale(char, (width, height))

favicon = pygame.image.load(os.path.join(filepath, "images/cat-fav.png"))
pygame.display.set_icon(favicon)

walk_right = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]
walk_left = [L1, L2, L3, L4, L5, L7, L7, L8, L9, L10]
jump_up = [J1,J1,J2,J2,J3,J3,J4 ,J4,J5,J5,J6,J6,J7,J7,J8,J8,J9,J9,J10,J10]
#jump_up = [J1,J1,J1,J2,J2,J2,J3,J3,J3,J4,J4 J4,J5,J5,J5,J6,J6,J6,J7,J7,J7,J8,J8,J8,J9,J9,J9,J10,J10,J10]
clock = pygame.time.Clock()

class Player (object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0

    def draw(self, screen):
        if self.walk_count + 1 >= 30:
            self.walk_count = 0
        elif self.is_jump:
            for i in jump_up:
                screen.blit(i, (self.x, self.y))
        elif self.left:
            screen.blit(walk_left[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        #     jump_count +=1
        # screen.blit(jump_up[(jump_count + 10)//3], (x,y))
        # jump_count +=1    
        else:
            screen.blit(char, (self.x,self.y))    


def redrawGameWindow():
    screen.blit(background_image, (0,0))
    cleo.draw(screen)
    food.draw(screen)
    food2.draw(screen)
    pygame.display.update()

class Reward(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(cheese, (self.x, self.y))

#Loop to keep displaying the window
cleo = Player(300, 410, width, height)

food = Reward(400, 500, 30, 30)
food2 = Reward (500, 600, 100, 100)
running = True 
while running:
    clock.tick(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cleo.x > cleo.vel:
        cleo.x -= cleo.vel
        cleo.left = True
        cleo.right = False 
        cleo.down = False
        cleo.up = False
    elif keys[pygame.K_RIGHT] and cleo.x < screen_width - cleo.width - cleo.vel:
        cleo.x += cleo.vel
        cleo.right = True
        cleo.left = False
        cleo.down = False
        cleo.up = False
    else:
        cleo.right = False
        cleo.left = False
        cleo.walk_count = 0    

    if not (cleo.is_jump):    
        if keys[pygame.K_UP] and cleo.y > cleo.vel:
            cleo.y -= cleo.vel
            cleo.right = False
            cleo.left = False
            cleo.walk_count = 0   
            cleo.down = False
            cleo.up = True
        if keys[pygame.K_DOWN] and cleo.y < screen_height - cleo.height:  
            cleo.y += cleo.vel
            cleo.right = False
            cleo.left = False
            cleo.walk_count = 0 
            cleo.down = True
            cleo.up = False  
        if keys[pygame.K_SPACE]:
           cleo.is_jump = True   
           cleo.right = False
           cleo.left = False
           cleo.walk_count = 0
    else: 
        if cleo.jump_count >= -10:
            neg = 1
            if cleo.jump_count < 0:
                neg = -1
            cleo.y -= int((cleo.jump_count **2) * 0.5 * neg)
            cleo.jump_count -= 1
        else:
            cleo.is_jump = False
            cleo.jump_count = 10       

    redrawGameWindow()


pygame.quit()  