
import pygame
pygame.init()

screen_width = 852
screen_height = 480
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game One!")

background = pygame.image.load('pygame\\bg.jpg')
still = pygame.image.load('pygame\standing.png')

clock = pygame.time.Clock()

score = 0

class Character():
    walk_right = [pygame.image.load('pygame\R1.png'), pygame.image.load('pygame\R2.png'), pygame.image.load('pygame\R3.png'), pygame.image.load('pygame\R4.png'), pygame.image.load('pygame\R5.png'), pygame.image.load('pygame\R6.png'), pygame.image.load('pygame\R7.png'), pygame.image.load('pygame\R8.png'), pygame.image.load('pygame\R9.png')]
    walk_left = [pygame.image.load('pygame\L1.png'), pygame.image.load('pygame\L2.png'), pygame.image.load('pygame\L3.png'), pygame.image.load('pygame\L4.png'), pygame.image.load('pygame\L5.png'), pygame.image.load('pygame\L6.png'), pygame.image.load('pygame\L7.png'), pygame.image.load('pygame\L8.png'), pygame.image.load('pygame\L9.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.numsaver = [18, 15, 25, 50]
        self.temp = (self.x + 18, self.y + 15, 25, 50)#player hitbox

    def move(self):
        #Example: pygame.draw.shape(which window is it on, color, (x_pos, y_pos, width, height))
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                window.blit(self.walk_left[self.walk_count//3], (self.x, self.y))#double slash is without decimal (int devision)
                self.walk_count += 1
            elif self.right:
                window.blit(self.walk_right[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                window.blit(self.walk_right[0], (self.x, self.y))
            else:
                window.blit(self.walk_left[0], (self.x, self.y))
    
        self.hitbox = (self.x + self.numsaver[0], self.y + self.numsaver[1], self.numsaver[2], self.numsaver[3])
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)#outline of hitbox

class Enemy(Character):
    walk_right = [pygame.image.load('pygame\R1E.png'), pygame.image.load('pygame\R2E.png'), pygame.image.load('pygame\R3E.png'), pygame.image.load('pygame\R4E.png'), pygame.image.load('pygame\R5E.png'), pygame.image.load('pygame\R6E.png'), pygame.image.load('pygame\R7E.png'), pygame.image.load('pygame\R8E.png'), pygame.image.load('pygame\R9E.png')]
    walk_left = [pygame.image.load('pygame\L1E.png'), pygame.image.load('pygame\L2E.png'), pygame.image.load('pygame\L3E.png'), pygame.image.load('pygame\L4E.png'), pygame.image.load('pygame\L5E.png'), pygame.image.load('pygame\L6E.png'), pygame.image.load('pygame\L7E.png'), pygame.image.load('pygame\L8E.png'), pygame.image.load('pygame\L9E.png')]
    standing = False

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = x #starts here
        self.end = end
        self.walk_count = 0
        self.speed = 3
        self.health = 10
        self.visible = True
        self.numsaver = [20, 0, 28, 60]
        self.hitbox = (self.x + 20, self.y, 28, 60)

    
    def epath(self):
        self.right = False
        self.left = False
        if self.speed > 0:
            if self.x + self.speed < self.end:#going right
                self.x += self.speed
                self.right = True
            else:
                self.speed = -self.speed
                self.walk_count = 0
        else: 
            if self.x - self.speed > self.start:#going left
                self.x += self.speed
                self.left = True
            else:
                self.speed = -self.speed
                self.walk_count = 0

        if self.visible:
            self.move()
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - 5 * (10 - self.health), 10))

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 16 * facing
    
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

def frame():
    window.blit(background, (0, 0))
    text = score_font.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(text, (screen_width - 100, 10))
    for bullet in bullets:
        bullet.draw(window)
    player.move()
    baddie.epath()
    pygame.display.update()

pheight = 64
pwidth = 64
px = 51
py = screen_height - pheight - 5 #making enemies even with player

bheight = 64
bwidth = 64
bx = 0
by = screen_height - bheight
bend =  screen_width - bwidth

player = Character(px, py, pwidth, pheight)
baddie = Enemy(bx, by, bwidth, bheight, bend)

bullets = []
shooter = 0

score_font = pygame.font.SysFont('comicsans', 30) #(font, size, bold?, italics?)

run = True
while run:
    clock.tick(27) #27 fps

    #Really basic timer
    if shooter > 0:
        shooter += 1
    if shooter > 10:
        shooter = 0

    for bullet in bullets:
        if bullet.y - bullet.radius < baddie.hitbox[1] + baddie.hitbox[3] and bullet.y + bullet.radius > baddie.hitbox[1]:
            if bullet.x + bullet.radius > baddie.hitbox[0] and bullet.x - bullet.radius < baddie.hitbox[0] + baddie.hitbox[2]:
                if baddie.visible:
                    baddie.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    #Allows you to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and len(bullets) < 20 and shooter == 0:
        if player.right:
            facing = 1
        else:
            facing = -1
        bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, (255, 0, 0), facing))
        
        shooter = 1

    if keys[pygame.K_a] and player.x > player.speed:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_d] and player.x < screen_width - player.width:
        player.x += player.speed
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.walk_count = 0
        player.standing = True

    if not player.is_jump:
        if keys[pygame.K_w]:
            player.is_jump = True
            #player.right = False
            #player.left = False
            player.walk_count = 0
    else:
        if player.jump_count >= -10:
            mult = 2
            if player.jump_count < 0:
                mult = -2
            player.y -= player.jump_count ** 2 / 8 * mult
            player.jump_count -= 1
        else:
            player.is_jump = False
            player.jump_count = 10
    frame()

