import pygame

pygame.init()  # Initialize

# Display setting
screen_width = 480
screen_height = 640

# Set the title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Samuel Game")  # Game Title

# Load background image
background = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\background.png")

# Load sprite(character)
character = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\character.png")
character_size = character.get_rect().size # Get Image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width/2 # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height #화면 세로크기 가장 아래에 위치

# Event Loop
running = True  # The game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))  # Paint Background
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # Game display re-paint!

# pygame quit
pygame.quit()
