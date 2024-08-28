import pygame
from set_stack import set_stack


def draw_card(x,y,card_width,card_height,image, image_width, image_height, number, screen, is_selected):
    x_offset = 0.07
    color = "white"
    if is_selected:
        color = "light gray"
    card_hitbox = pygame.draw.rect(screen,color, (x,y,card_width,card_height))
    if number ==1 or number == 3:
        screen.blit(image,(x+int(card_width*x_offset),y+int(card_height*0.05)+image_height))
    
    if number == 3:
        screen.blit(image,(x+int(card_width*x_offset),y+int(card_height*0.05)))
        screen.blit(image,(x+int(card_width*x_offset),y+int(card_height*0.05)+2*image_height))
    
    if number == 2:
        screen.blit(image,(x+int(card_width*x_offset),y+int(card_height*0.2)))
        screen.blit(image,(x+int(card_width*x_offset),y+int(card_height*0.2)+image_height))
    return card_hitbox



def draw_cards(cards, selected_cards):
    ret_cards = []
    n = len(cards)
    for j in range(int(n/3)):
        for i in range(3):
            x_pos = inital_x+j*(offset+card_width)
            y_pos = inital_y+i*(offset+card_height)
            c = cards[3*j+i]
            image = images[c.get_color()][c.get_filling()][c.get_shape()]
            ret_cards.append(draw_card(x_pos, y_pos, card_width, card_height, image, img_width,img_height, c.get_number(),screen, 3*j+i in selected_cards))
    return ret_cards

selected_cards = []
game_stack = set_stack()
card_width = 120
img_width = int(card_width*0.8)
img_height = int(img_width/400*220)
img_size = (img_width,img_height)
images = {}
for color in ["red", "green", "blue"]:
    images[color] = {}
    for filling in ["empty", "filled", "striped"]:
        images[color][filling] = {}
        for shape in ["snake", "oval", "diamond"]:
            images[color][filling][shape]  = pygame.transform.scale(pygame.image.load(f"images/{shape[0]}_{filling[0]}_{color[0]}.jpg"), img_size)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
offset = 50
card_width = 120
card_height = int(card_width*1.4)
inital_x = 50
inital_y = 70

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            pos = pygame.mouse.get_pos()
            for card in gui_cards:
                if card.collidepoint(pos):
                    i = gui_cards.index(card)
                    print(i)
                    print(game_cards[i])
                    if i in selected_cards:
                        selected_cards.remove(i)
                    else:
                        selected_cards.append(i)
                    if len(selected_cards) == 3:
                        game_stack.check_selected_cards(selected_cards)
                        selected_cards = []
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")
    game_cards = game_stack.shown
    # RENDER YOUR GAME HERE
    gui_cards = draw_cards(game_cards, selected_cards)
    #for i in range(3):
    #    for j in range(4):
    #        cards.append(pygame.draw.rect(screen,"white", (inital_x+j*(offset+card_width),inital_y+i*(offset+card_height),card_width,card_height)))
    #a = draw_card(inital_x, inital_y,card_width, card_height, blue_dia, img_width, img_height, 1,screen)
    #b = draw_card(inital_x+1*(offset+card_width), inital_y,card_width, card_height, blue_dia, img_width, img_height, 2,screen)
    #c = draw_card(inital_x+2*(offset+card_width), inital_y,card_width, card_height, blue_dia, img_width, img_height, 3,screen)

    pygame.display.flip()



    clock.tick(60)  # limits FPS to 60

pygame.quit()