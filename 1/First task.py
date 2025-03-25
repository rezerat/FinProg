import pygame
import random
import sys

pygame.init()

# Создание окна
width, height = 800, 600

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Мартынов Егор")

white = (255, 255, 255)
red = (255, 0, 0)

screen.fill(white)


circle_radius = 100
circle_position = (width // 2, height // 2)

def draw_house(surface):
    pygame.draw.rect(surface, (139, 69, 19), (100, 400, 200, 200))
    pygame.draw.polygon(surface, (255, 0, 0), [(80, 400), (200, 250), (320, 400)])


def draw_random_shape(surface):
    points = [(random.randint(100, 700), random.randint(100, 500)) for _ in range(5)]
    pygame.draw.polygon(surface, (0, 255, 0), points)


running = True


pygame.draw.circle(screen, red, circle_position, circle_radius)
pygame.draw.circle(screen, red, (circle_position[0], circle_position[1]), circle_radius, 15)

pygame.draw.rect(screen, (0, 0, 255), (50, 50, 300, 200))


for _ in range(5):
    rect_width = random.randint(50, 150)
    rect_height = random.randint(50, 150)
    rect_x = random.randint(0, width - rect_width)
    rect_y = random.randint(0, height - rect_height)    
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, random_color, (rect_x, rect_y, rect_width, rect_height))


try:
    image = pygame.image.load("1/1.png")
    screen.blit(pygame.transform.scale(image, (100, 100)), (600, 100))
except pygame.error:
    print("Не удалось загрузить изображение.")

draw_house(screen)

draw_random_shape(screen)
pygame.display.flip()

pygame.time.delay(2000)
pygame.draw.rect(screen, "white", [600, 100, 100, 100])
screen.blit(pygame.transform.scale(image, (100, 100)), (0, 200))
pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()







