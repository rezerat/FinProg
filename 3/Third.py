import pygame
import sys
import random
import os


pygame.init()

# Упражнение 1: Настройки окна и фона
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аркада с фоновым изображением")

# Загрузка фонового изображения
try:

    background_img = pygame.image.load('3/3.png').convert()
    background_img = pygame.transform.scale(background_img, (WIDTH * 2, HEIGHT))
except:
    background_img = pygame.Surface((WIDTH * 2, HEIGHT))
    background_img.fill((0, 100, 200)) 
    for i in range(0, WIDTH * 2, 100):
        pygame.draw.rect(background_img, (0, 200, 100), (i, HEIGHT-50, 50, 50))

bg_x = 0
bg_speed = 5

# Упражнение 2: Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('3/image.png').convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 4
        
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed


        elif keys[pygame.K_LEFT] and self.rect.left <= 0:
            global bg_x
            bg_x += self.speed
            
        print(WIDTH, self.rect.right)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        elif keys[pygame.K_RIGHT] and self.rect.right > WIDTH:
            for enemy in enemies:
                enemy.speed = self.speed + 2
            bg_x -= self.speed
    
        elif self.rect.right == WIDTH + 1:
            for enemy in enemies:
                enemy.speed = self.speed - 2
            
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Упражнение 3: Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замените на изображение врага
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  # Зеленый квадрат
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 500)
        self.rect.y = random.randint(0, HEIGHT - 30)
        self.speed = random.randint(2, 4)
        
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(WIDTH, WIDTH + 500)
            self.rect.y = random.randint(0, HEIGHT - 30)
            self.speed = random.randint(2, 4)


# Класс стрелы
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill((255, 255, 240))  # Белая стрела
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speed = 10
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()

# Создание спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
arrows = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Создаем стрелу при нажатии пробела
                arrow = Arrow(player.rect.right, player.rect.centery)
                all_sprites.add(arrow)
                arrows.add(arrow)
    
    all_sprites.update()
    
    hits = pygame.sprite.groupcollide(arrows, enemies, True, True)
    for hit in hits:
        # Создаем нового врага при уничтожении существующего
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    
    screen.fill((0, 0, 0))

    screen.blit(background_img, (bg_x, 0))

    # Если фон сместился слишком далеко, рисуем его вторую часть
    if bg_x < -WIDTH:
        screen.blit(background_img, (bg_x + WIDTH * 2, 0))
    elif bg_x > 0:
        screen.blit(background_img, (bg_x - WIDTH * 2, 0))
    
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()