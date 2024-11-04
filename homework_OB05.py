import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Основные параметры окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра на выживание")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Параметры игрока
player_size = 50
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5

# Параметры врагов
enemy_size = 50
enemy_speed = 3
enemy_spawn_time = 2000  # Время появления врагов в миллисекундах
enemies = []

# ФПС
clock = pygame.time.Clock()
fps = 60

# Создание врага
def create_enemy():
    x = random.randint(0, screen_width - enemy_size)
    y = random.randint(0, screen_height - enemy_size)
    return pygame.Rect(x, y, enemy_size, enemy_size)

# Запуск основного цикла игры
running = True
pygame.time.set_timer(pygame.USEREVENT, enemy_spawn_time)  # Таймер для появления врагов
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            enemies.append(create_enemy())  # Добавление нового врага

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_speed

    # Проверка столкновений
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            print("Вы проиграли!")
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование игрока
    pygame.draw.rect(screen, WHITE, player_rect)

    # Рисование врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Обновление экрана
    pygame.display.flip()

    # Контроль ФПС
    clock.tick(fps)

pygame.quit()
sys.exit()

