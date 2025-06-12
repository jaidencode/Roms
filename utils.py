import pygame
from constants import WIDTH, HEIGHT, BALL_SPEED_X, BALL_SPEED_Y, PADDLE_SPEED, WHITE, BLACK
from entities import screen, font, enemy, ball, ball_vel


def draw_start_screen():
    screen.fill(BLACK)
    title = font.render("PONG", True, WHITE)
    prompt = font.render("Press SPACE to start", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()


def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_vel.x = BALL_SPEED_X if ball_vel.x > 0 else -BALL_SPEED_X
    ball_vel.y = BALL_SPEED_Y


def update_enemy():
    if enemy.centery < ball.centery:
        enemy.y += PADDLE_SPEED
    elif enemy.centery > ball.centery:
        enemy.y -= PADDLE_SPEED
    enemy.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
