# import pygame 
# import random
# pygame.init() 
# screen = pygame.display.set_mode() 
# width, height = screen.get_window_size(500,500) 
# hitbox_width = width/2 
# hitbox_height = height/2 
# hitboxes = { "red":pygame.Rect(0,0,hitbox_width,hitbox_height),
#             "green":pygame.Rect(0,0,hitbox_width,hitbox_height),
#             "blue":pygame.Rect(0,0,hitbox_width,hitbox_height),
#             "purple":pygame.Rect(0,0,hitbox_width,hitbox_height)}
# hitboxes["blue"].topleft = hitboxes["red"].topright
# hitboxes["green"].topright = hitboxes["red"].bottomright
# hitboxes["purple"].topleft = hitboxes["red"].topleft
# font = pygame.font.SysFont( 24)
# done = False 
# result = []
# turns = 0 
# order = list(hitboxes.keys())
# random.shuffle(order)
# # while not done:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             done = True
# #         elif event.type ==pygame.MOUSEBUTTONDOWN:

# while True:
#     for event in pygame.event.get():
#         if event.type ==pygame.K_SPACE:
#             random.shuffle(order)
#         elif event.type ==pygame.MOUSEBUTTONDOWN:
#             turns = turns - 1 
#             if hitboxes["red"].collidepoint(event.pos):
#                 result.append("red")
#             elif hitboxes["green"].collidepoint(event.pos):
#                     result.append("green")
#             elif hitboxes["blue"].collidepoint(event.pos):
#                 result.append("blue")
#             elif hitboxes["purple"].collidepoint(event.pos):
#                     result.append("purple")

# if turns == 0:
#      if result == order:
#             font.read
# for c, hb in hitboxes.items():
#      box = pygame.draw.rect(screen,c,hb)
#      screen
# ## X and y cordinates 
# ##width and height=
# #Rectangles do not track visuals 
# #pygame.rect 
# #done = false 
# #3/6/23
# #Vending machine
# #black boxing
print("Welcome to the vending machine")
code = input("Please enter a code")
money = input("Enter me money")
def my_vending_machine(code,money):
    if code =="A":
        if money >= 1 :
            print("You got money")
        else:
            print("You got no money")
    elif code =="B":
        if money>= 1.5:
            print("You got water")
        else:
            print("You got no money")
    elif code== "C":
        if money>= 2:
            print("you got juice")
        else:
            print("You got no money")
    else: 
        print("Invalid Code")
    ##Functions are always defined in global scope
##Write a function that will let us determine the maximum value
def find_max(x,y,z):
    max = a 
    if b< max :
        max = b 
    if c > max:
        max = c 
    print(max)
for _ in range (0,3):
    print("Please enter 3 numbers")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
find_max(a,b,c)
find_max() 
find_max()
def foo(var):
    var +=1 
    print(var) ## This var is a different one
var = 5 
print(var)
foo(var)
#Single Responsibility principle 
#A function should do one thing 
#FUnction should never be responsible for ou