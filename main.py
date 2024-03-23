from pygame import *

WIDTH, HEIGHT = 700, 500

x1, y1 = 200, 300
x2, y2 = 400, 300
p_speed, m_speed = 10, 10
FPS = 60

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('da')
background = transform.scale(image.load('background.jpg'), (WIDTH, HEIGHT))

hero = transform.scale(image.load('hero.png'), (50, 50))
cyborg = transform.scale(image.load('cyborg.png'), (50, 50))
final = transform.scale(image.load('treasure.png'), (50, 50))
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer_music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 500:
            self.direction = 'right'
        if self.rect.x >= WIDTH - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('hero.png', 5, HEIGHT- 80, 4)
monster = Enemy('cyborg.png', WIDTH - 80, 280, 2)
final = GameSprite('treasure.png', WIDTH - 140, HEIGHT - 80, 0)

w1 = Wall(154, 205, 50, 100, 10, 590, 10)
w2 = Wall(154, 205, 50, 100, 480, 400, 10)
w3 = Wall(154, 205, 50, 100, 10, 10, 380)
w4 = Wall(154, 205, 50, 200, 100, 10, 380)
w5 = Wall(154, 205, 50, 200, 100, 100, 10)
w6 = Wall(154, 205, 50, 390, 10, 10, 390)
w7 = Wall(154, 205, 50, 300, 200, 100, 10)
w8 = Wall(154, 205, 50, 200, 300, 100, 10)
w9 = Wall(154, 205, 50, 300, 390, 100, 10)
w10 = Wall(154, 205, 50, 490, 100, 10, 380)
w11 = Wall(154, 205, 50, 680, 10, 10, 480)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()

        w1.draw()
        w2.draw()
        w3.draw()
        w4.draw()
        w5.draw()
        w6.draw()
        w7.draw()
        w8.draw()
        w9.draw()
        w10.draw()
        w11.draw()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        kick.play()


    display.update()
    clock.tick(FPS)
