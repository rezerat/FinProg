import pygame
import random
 
 
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация фигур")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 193, 12), (0, 218, 247)]


class Shape:
    def __init__(self, x, y, width, height, color, shape_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape_type = shape_type
        self.speed = 2
        self.direction = 1

    def move(self):
        self.x += self.speed * self.direction

        # Проверка на столкновение с границами окна
        if self.x + self.width > WIDTH or self.x < 0:
            self.direction *= -1
            self.color = random.choice(COLORS)

    def draw(self):
        if self.shape_type == "square":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.shape_type == "rectangle":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.shape_type == "circle":
            pygame.draw.circle(screen, self.color, (self.x + self.width // 2, self.y + self.height // 2), self.width // 2)
        elif self.shape_type == "triangle":
            pygame.draw.polygon(screen, self.color, [(self.x + self.width // 2, self.y), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height)])

    def is_clicked(self, mouse_pos):
        if self.shape_type == "square" or self.shape_type == "rectangle":
            return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height
        elif self.shape_type == "circle":
            distance = ((mouse_pos[0] - (self.x + self.width // 2)) ** 2 + ((mouse_pos[1] - (self.y + self.height // 2)) ** 2))
            return distance <= (self.width // 2) ** 2
        elif self.shape_type == "triangle":
            return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

shapes = [
    Shape(100, 100, 50, 50, random.choice(COLORS), "square"),
    Shape(200, 200, 100, 50, random.choice(COLORS), "rectangle"),
    Shape(300, 300, 50, 50, random.choice(COLORS), "circle"),
    Shape(400, 400, 50, 50, random.choice(COLORS), "triangle")
]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for shape in shapes:
                if shape.is_clicked(mouse_pos):
                    shape.color = random.choice(COLORS)

    for shape in shapes:
        shape.move()
        shape.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
