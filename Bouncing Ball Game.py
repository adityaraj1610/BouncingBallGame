import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_pos = [100, 100]
ball_radius = 30
ball_speed = [4, 4]

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    
    if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH - ball_radius:
        ball_speed[0] *= -1
    if ball_pos[1] <= ball_radius or ball_pos[1] >= HEIGHT - ball_radius:
        ball_speed[1] *= -1

    
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
