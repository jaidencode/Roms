import pygame
import sys

from constants import WIDTH, HEIGHT, PADDLE_SPEED, WHITE, BLACK
from entities import screen, clock, player, enemy, ball, ball_vel
from utils import draw_start_screen, reset_ball, update_enemy
from effects import (
    add_trail,
    draw_particles,
    draw_trail,
    spawn_particles,
    update_particles,
    update_trail,
)


def main():
    in_start_screen = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if in_start_screen and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_start_screen = False
                reset_ball()

        if in_start_screen:
            draw_start_screen()
            clock.tick(60)
            continue

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            player.y += PADDLE_SPEED
        player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        update_enemy()

        add_trail(ball.center)
        update_trail()
        update_particles()

        ball.x += int(ball_vel.x)
        ball.y += int(ball_vel.y)

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel.y *= -1
        if ball.left <= 0 or ball.right >= WIDTH:
            spawn_particles(ball.center)
            reset_ball()
            ball_vel.x *= -1

        if ball.colliderect(player) and ball_vel.x < 0:
            ball_vel.x *= -1
        if ball.colliderect(enemy) and ball_vel.x > 0:
            ball_vel.x *= -1

        screen.fill(BLACK)
        draw_trail(screen)
        draw_particles(screen)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, enemy)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
