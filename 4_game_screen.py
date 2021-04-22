import pygame
from random import *
#set level
def setup(level):
    number_count = (level//3) + 5
    number_count = min(number_count, 20)

    #draw number in grid
    shuffle_grid(number_count)

def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130
    button_size = 110
    screen_left_margin = 55
    screen_top_margin = 20


    grid = [[0 for col in range(columns)] for row in range(rows)]
    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            button = pygame.Rect(0,0,button_size,button_size)
            button.center = (center_x, center_y)
            number_buttons.append(button)
    print(grid)



def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        pygame.draw.rect(screen, GRAY, rect)

        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text, text_rect)

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
game_font = pygame.font.Font(None, 120)

#Start button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

#color
BLACK = (0,0,0) # RGB
WHITE = (255,255,255)
GRAY = (50,50,50)

number_buttons = []

#Flag of game starting.
start = False

#call setup function
setup(1)

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