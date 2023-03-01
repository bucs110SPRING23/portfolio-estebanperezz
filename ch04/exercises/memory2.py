import pygame 
import random
pygame.init() 
screen = pygame.display.set_mode() 
width, height = screen.get_window_size(500,500) 
hitbox_width = width/2 
hitbox_height = height/2 
hitboxes = { "red":pygame.Rect(0,0,hitbox_width,hitbox_height),
            "green":pygame.Rect(0,0,hitbox_width,hitbox_height),
            "blue":pygame.Rect(0,0,hitbox_width,hitbox_height),
            "purple":pygame.Rect(0,0,hitbox_width,hitbox_height)}
hitboxes["blue"].topleft = hitboxes["red"].topright
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].topleft
font = pygame.font.SysFont( 24)
done = False 
result = []
turns = 0 
order = list(hitboxes.keys())
random.shuffle(order)
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type ==pygame.MOUSEBUTTONDOWN:

while True:
    for event in pygame.event.get():
        if event.type ==pygame.K_SPACE:
            random.shuffle(order)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            turns = turns - 1 
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["green"].collidepoint(event.pos):
                    result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            elif hitboxes["purple"].collidepoint(event.pos):
                    result.append("purple")

if turns == 0:
     if result == order:
            font.read
for c, hb in hitboxes.items():
     box = pygame.draw.rect(screen,c,hb)
     screen
## X and y cordinates 
##width and height=
#Rectangles do not track visuals 
#pygame.rect 
#done = false 