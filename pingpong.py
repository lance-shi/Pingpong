import pygame
import random

class Ball:
    def __init__(self, initPos):
        self.direction = 1
        self.x = initPos
        self.y = 100


class Game:
    def __init__(self):
        size = width, height = 600, 900
        self.screen = pygame.display.set_mode(size)
        self.colors = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "RED": (255, 0, 0),
            "YELLOW": (255, 255, 0),
            "BG": (173, 216, 230)
        }
        self.balls = []
        self.board = pygame.Rect(240, 800, 120, 10)
        self.mainLoop()

    def mainLoop(self):
        run = True
        vel = 2

        clock = pygame.time.Clock()
        pygame.display.set_caption("Ping Pong")
        pygame.mixer.init(44100, -16, 1, 512)
        interval = 3000
        time = 0
        next_interval = 0
        level = 30000
        next_level = level

        while run:
            timePassed = clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill(self.colors["BG"])

            time += timePassed
            if time >= next_interval:
                next_interval += interval
                new_ball = Ball(random.randint(50, 550))
                self.balls.append(new_ball)

            if time >= next_level:
                next_level += level
                vel += 1

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT] and self.board.x - 6 > 0:  # LEFT
                self.board.x -= 6
            if keys_pressed[pygame.K_RIGHT] and self.board.x + 6 + self.board.width < 600:  # RIGHT
                self.board.x += 6

            for b in self.balls:
                ball_rect = pygame.draw.circle(self.screen, self.colors["YELLOW"], (b.x, b.y), 20)
                if ball_rect.colliderect(self.board):
                    b.direction = -1
                b.y += vel * b.direction

            pygame.draw.rect(self.screen, self.colors["BLACK"], self.board)
            pygame.display.update()

        pygame.quit()

def main():
    game = Game()

if __name__ == "__main__":
    main()