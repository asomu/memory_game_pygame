import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    print("Game start")

def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True


#init
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#Start button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

#color
BLACK = (0,0,0) # RGB
WHITE = (255,255,255)

#Flag of game starting.
start = False

#game loop
running = True #게임실행 중인지 확인.
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

        screen.fill(BLACK)
        if start:
            display_game_screen()
        else:
            display_start_screen()

        #if it have click_pos value
        if click_pos:
            check_buttons(click_pos)

        display_start_screen()

        pygame.display.update()

pygame.quit()