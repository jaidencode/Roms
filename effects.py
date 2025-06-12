import random
import pygame
from constants import BALL_SIZE, WHITE, TRAIL_LIFE, PARTICLE_LIFE, PARTICLE_COUNT

trail_segments = []
particles = []


def add_trail(position):
    trail_segments.append({'pos': pygame.Vector2(position), 'life': TRAIL_LIFE})


def update_trail():
    for seg in trail_segments[:]:
        seg['life'] -= 1
        if seg['life'] <= 0:
            trail_segments.remove(seg)


def draw_trail(surface):
    for seg in trail_segments:
        alpha = int(255 * seg['life'] / TRAIL_LIFE)
        surf = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(
            surf,
            (*WHITE, alpha),
            (BALL_SIZE // 2, BALL_SIZE // 2),
            BALL_SIZE // 2,
        )
        surface.blit(surf, (seg['pos'].x - BALL_SIZE // 2, seg['pos'].y - BALL_SIZE // 2))


class Particle:
    def __init__(self, position):
        self.pos = pygame.Vector2(position)
        self.vel = pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        self.life = PARTICLE_LIFE
        self.radius = random.randint(2, 4)

    def update(self):
        self.pos += self.vel
        self.life -= 1

    def draw(self, surface):
        alpha = int(255 * self.life / PARTICLE_LIFE)
        surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            surf,
            (*WHITE, alpha),
            (self.radius, self.radius),
            self.radius,
        )
        surface.blit(surf, (self.pos.x - self.radius, self.pos.y - self.radius))


def spawn_particles(position):
    for _ in range(PARTICLE_COUNT):
        particles.append(Particle(position))


def update_particles():
    for p in particles[:]:
        p.update()
        if p.life <= 0:
            particles.remove(p)


def draw_particles(surface):
    for p in particles:
        p.draw(surface)
