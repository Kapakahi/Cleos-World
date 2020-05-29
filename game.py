import pygame, sys, random
import os.path
#initialize pygame
pygame.init ()

#create the screen
(screen_width, screen_height) = (1550, 790)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Cleo's World")

filepath = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(filepath, "images/jungle2.jpg")).convert()

width = 100
height = 100

cheese = pygame.image.load(os.path.join(filepath, "images/cheese.png"))
cheese = pygame.transform.scale(cheese, (30, 30))

mouse = pygame.image.load(os.path.join(filepath, "images/gray.png"))
mouse = pygame.transform.scale(mouse, (50, 50))

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

V1 = pygame.image.load(os.path.join(filepath, "images/Run (4).png"))
V1 = pygame.transform.scale(V1, (width, height))
V2 = pygame.image.load(os.path.join(filepath, "images/Run (5).png"))
V2 = pygame.transform.scale(V2, (width, height))
V3 = pygame.image.load(os.path.join(filepath, "images/Run (6).png"))
V3 = pygame.transform.scale(V3, (width, height))
V4 = pygame.image.load(os.path.join(filepath, "images/Run (7).png"))
V4 = pygame.transform.scale(V4, (width, height))
V5 = pygame.image.load(os.path.join(filepath, "images/Run (8).png"))
V5 = pygame.transform.scale(V5, (width, height))

char = pygame.image.load(os.path.join(filepath, "images/Idle (1).png"))
char = pygame.transform.scale(char, (width, height))

favicon = pygame.image.load(os.path.join(filepath, "images/cat-fav.png"))
pygame.display.set_icon(favicon)

walk_right = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]
walk_left = [L1, L2, L3, L4, L5, L7, L7, L8, L9, L10]
jump_up = [J1,J1,J2,J2,J3,J3,J4 ,J4,J5,J5,J6,J6,J7,J7,J8,J8,J9,J9,J10,J10]
verticle = [V1, V2, V3, V4, V5, V1, V2, V3, V4, V5]

clock = pygame.time.Clock()

score = 0
meow = pygame.mixer.Sound("sounds/catmeow.wav")
purr = pygame.mixer.Sound("sounds/cat_purr.wav")

SONG_END = pygame.USEREVENT + 0

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load("sounds/TownTheme.mp3")
pygame.mixer.music.play()

font = pygame.font.SysFont('times', 30, True)

running = True

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = char
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.up = False
        self.down = False
        self.up_count = 0
        self.down_count = 0
        self.rect.x = x
        self.rect.y = y
        self.height = height
        self.width = width

    def draw(self, screen):
        if self.walk_count + 1 >= 30:
            self.walk_count = 0   
        elif self.up_count + 1 >= 30:
                self.up_count = 0    
        elif self.down_count + 1 >= 30:
            self.down_count = 0
        elif self.up_count + 1 >= 30:
            self.up_count = 0
        elif self.is_jump:
            for i in jump_up:
                screen.blit(i, (self.rect.x, self.rect.y))
        elif self.left:
            screen.blit(walk_left[self.walk_count//3], (self.rect.x,self.rect.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right[self.walk_count//3], (self.rect.x,self.rect.y))
            self.walk_count += 1
        elif self.up:    
            screen.blit(verticle[self.up_count//3], (self.rect.x,self.rect.y))
            self.up_count += 1
        elif self.down:
            screen.blit(verticle[self.down_count//3], (self.rect.x,self.rect.y))
            self.down_count += 1    
        else:
            screen.blit(char, (self.rect.x,self.rect.y))   

    def update(self):         
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > self.vel:
            self.rect.x -= self.vel
            self.left = True
            self.right = False 
            self.down = False
            self.up = False
        elif keys[pygame.K_RIGHT] and self.rect.x < screen_width - self.width + self.vel + 55:
            self.rect.x += self.vel
            self.right = True
            self.left = False
            self.down = False
            self.up = False
        elif keys[pygame.K_UP] and self.rect.y > self.vel:
            self.rect.y -= self.vel
            self.up = True
            self.right = False
            self.left = False
            self.down = False
        elif keys[pygame.K_DOWN] and self.rect.y < screen_height - self.height + 35:  
            self.down = True
            self.rect.y += self.vel
            self.right = False
            self.left = False
            self.up = False  
        else:
            self.right = False
            self.left = False
            self.down = False
            self.up = False
            self.walk_count = 0    

        if not (self.is_jump):    
            if keys[pygame.K_SPACE]:
                self.is_jump = True   
                self.right = False
                self.left = False
                self.walk_count = 0
        else: 
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= int((self.jump_count **2) * 0.5 * neg)
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10  

class Reward(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, item):
        super().__init__()
        self.image = item
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

add_cheese_reward = pygame.USEREVENT + 1
pygame.time.set_timer(add_cheese_reward, 3000)        

add_mouse_reward = pygame.USEREVENT + 4
pygame.time.set_timer(add_mouse_reward, 4000)   
        

def splash_screen():
    # global running
    # if not running:
    #     return
    running = False
    screen.fill((15, 67, 52))
    draw_text("Welcome to Cleo's World", 48, (255, 255, 255), screen_width / 2, screen_height / 4)
    draw_text("Use the arrows to move and the space bar to jump", 26, (255, 255, 255), screen_width / 2, screen_height / 2 )
    draw_text("Collect treats to make Cleo purr!", 26, (255, 255, 255), screen_width / 2, (screen_height / 2) - 50 )
    draw_text("Press a key to play", 22, (255,255, 255), screen_width / 2, screen_height * 3 / 4)
    pygame.display.flip()   
    wait_for_key()

def redrawGameWindow():
    screen.blit(background_image, (0,0))
    text = font.render('Purr points: ' + str(score), 1, (0, 0, 0))
    screen.blit(text, (15, 15))
    all_sprites.draw(screen)
    cleo.draw(screen)
    cleo.update()

def end_screen():
    if not running:
        return

    screen.fill((15, 67, 52))
    draw_text("Game Over", 48, (255, 255, 255), screen_width / 2, screen_height / 4)
    draw_text("Purr points: " + str(score), 22, (255, 255, 255), screen_width / 2, screen_height / 2 )
    pygame.display.flip()
    wait_for_key()

def run():
    playing = True
    while playing:
        
        got_cheese = pygame.sprite.groupcollide(
        cleo_group, yummy_group, False, True, pygame.sprite.collide_mask)

        for hit in got_cheese:
            global score 
            score += 16
            meow.play()

        got_mouse = pygame.sprite.groupcollide(
        cleo_group, mouse_group, False, True, pygame.sprite.collide_mask)

        for hit in got_mouse:
            #global score 
            score += 19
            purr.play()    
        
        for event in pygame.event.get(): 
            if event.type == SONG_END:
                end_screen()
                print("the song ended!")
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == add_cheese_reward:
                new_reward = Reward(
                    random.randrange(50, screen_width), 
                    random.randrange(40, screen_height - 30),
                    cheese)
                yummy_group.add(new_reward)
                all_sprites.add(new_reward)    
            elif event.type == add_mouse_reward:
                new_mouse_reward = Reward(
                    random.randrange(50, screen_width), 
                    random.randrange(40, screen_height - 30),
                    mouse)
                mouse_group.add(new_mouse_reward)
                all_sprites.add(new_mouse_reward)    

        clock.tick(30)
        pygame.display.update()  
        cleo.update()  
        redrawGameWindow()
        yummy_group.update()
        mouse_group.update()

def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.KEYUP:
                waiting = False
                running = True  
                redrawGameWindow()                    

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(pygame.font.match_font("times"), size)    
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (int(x), int(y))
    screen.blit(text_surface, text_rect)


all_sprites = pygame.sprite.Group()
cleo = Player(800, 600, 150, 150)
all_sprites.add(cleo)

cleo_group = pygame.sprite.Group()
cleo_group.add(cleo)

yummy_group = pygame.sprite.Group()
for  target in range (8):
    new_yummy = Reward(
        random.randrange(50, screen_width), 
        random.randrange(40, screen_height - 30),
        cheese)
    yummy_group.add(new_yummy)
    all_sprites.add(new_yummy)

mouse_group = pygame.sprite.Group()
for  target in range (3):
    new_mouse = Reward(
        random.randrange(50, screen_width), 
        random.randrange(40, screen_height - 30),
        mouse)
    mouse_group.add(new_mouse)
    all_sprites.add(new_mouse)    

splash_screen()

while running:
    run()
    
pygame.quit()  
sys.exit()
