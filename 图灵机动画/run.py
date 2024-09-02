import pygame
import time
import random
from turing_machine import TuringMachine

# 定义图灵机参数
tape = list("".join(random.choice(["0", "1"]) for _ in range(19)))

pygame.init()

width, height = len(tape) * 40 + 20, 200
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Turing Machine Animation")

black = "#000000"
white = "#FFFFFF"

font = pygame.font.Font(None, 36)


# 道具框
input_rect = pygame.Rect(200, 250, 140, 32)
input_color = ""


def running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    else:
        return True


def position(index: int, y: int):
    def arrow(x: int, y: int):
        return [
            (xx + x, yy + y)
            for xx, yy in [
                (10, 0),
                (10, 20),
                (0, 20),
                (20, 40),
                (40, 20),
                (30, 20),
                (30, 0),
            ]
        ]

    x = 10 + index * 40
    pygame.draw.polygon(screen, black, arrow(x, y))
    y = y + 50
    pygame.draw.rect(screen, black, (x, y, 40, 40), width=2)
    for i, v in enumerate(tape):
        rect = pygame.Rect(10 + i * 40, y, 40, 40)
        if v == "1":
            pygame.draw.rect(screen, black, rect)
            text = font.render(v, True, white)
            screen.blit(text, text.get_rect(center=(rect.centerx, rect.centery)))
        else:
            text = font.render(v, True, black)
            screen.blit(text, text.get_rect(center=(rect.centerx, rect.centery)))


tm = TuringMachine(len(tape))
tm.add_state("A", [("1", 1, "A"), ("0", -1, "B")])
tm.add_state("B", [("1", 1, "B"), ("0", 1, "A")])
tm.current_state = "A"
tm.index = 5
while running():
    screen.fill(white)
    index = tm.index
    data = tm.run(tape[index])
    if not data:
        time.sleep(3)
        pygame.quit()
        exit()
    write, offset = data
    tape[index] = write
    screen.blit(font.render(f"Next {tm.current_state}", True, black), (10, 10))
    screen.blit(font.render(" >> " if offset == 1 else " << ", True, black), (10, 40))
    position(index, 80)
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()
