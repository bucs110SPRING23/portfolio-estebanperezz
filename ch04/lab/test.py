import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_size = pygame.display.get_window_size()
center = [screen_size[0] // 2, screen_size[1] // 2]

rect1 = pygame.draw.rect(screen, "yellow", [0, 0, 100, 100])
rect2 = pygame.draw.rect(screen, "green", [400, 0, 100, 100])

font = pygame.font.Font(None, 18)
text1 = font.render("Bet Player 1", True, "black")
text2 = font.render("Bet Player 2", True, "black")

screen.blit(text1, (0, 0))
screen.blit(text2, (400, 0))

pygame.display.flip()

play1bet = False
play2bet = False


def drawBoard():
    pygame.draw.circle(screen, color="red", center=center, radius=center[0])
    pygame.draw.line(screen, color="blue", start_pos=(0, 250), end_pos=[500, 250])
    pygame.draw.line(screen, color="blue", start_pos=(250, 0), end_pos=(250, 500))


def randcordinates():
    randomnx = random.randrange(1, screen_size[0])
    randomy = random.randrange(1, screen_size[1])
    return (randomnx, randomy)


def checkdistance(randx, randy):
    distance_from_center = math.hypot(randx - center[0], randy - center[1])
    is_in_circle = (distance_from_center <= center[0])
    print(is_in_circle)
    return is_in_circle


def dartGame():
    player1 = 0
    player2 = 0

    for _ in range(10):
        xcord1, ycord1 = randcordinates()
        xcord2, ycord2 = randcordinates()

        distanceCenter1 = checkdistance(xcord1, ycord1)
        distanceCenter2 = checkdistance(xcord2, ycord2)

        print(distanceCenter1)
        print(distanceCenter2)

        if distanceCenter1 == True:
            pygame.draw.circle(screen, "blue", (xcord1, ycord1), 5)
            player1 += 1
        else:
            pygame.draw.circle(screen, "green", (xcord1, ycord1), 5)

        if distanceCenter2 == True:
            pygame.draw.circle(screen, "black", (xcord2, ycord2), 5)
            player2 += 1
        else:
            pygame.draw.circle(screen, "yellow", (xcord2, ycord2), 5)

        pygame.display.flip()


events = True

while events:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawBoard()

            if rect1.collidepoint(event.pos):
                play1bet = True
                dartGame()

            elif rect2.collidepoint(event.pos):
                play2bet = True
                dartGame()

            pygame.display.flip()

        elif event.type == pygame.QUIT:
            events = False

pygame.quit()