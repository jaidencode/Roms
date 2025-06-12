import pygame
import sys

# Game constants
WIDTH, HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 4, 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Entities
player = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
enemy = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_vel = pygame.Vector2(BALL_SPEED_X, BALL_SPEED_Y)

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
    # Simple NPC AI to follow the ball
    if enemy.centery < ball.centery:
        enemy.y += PADDLE_SPEED
    elif enemy.centery > ball.centery:
        enemy.y -= PADDLE_SPEED
    enemy.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))


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

        ball.x += int(ball_vel.x)
        ball.y += int(ball_vel.y)

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel.y *= -1
        if ball.left <= 0 or ball.right >= WIDTH:
            reset_ball()
            ball_vel.x *= -1

        if ball.colliderect(player) and ball_vel.x < 0:
            ball_vel.x *= -1
        if ball.colliderect(enemy) and ball_vel.x > 0:
            ball_vel.x *= -1

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, enemy)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
