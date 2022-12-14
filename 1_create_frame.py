import pygame

pygame.init()  # Initialize

# Display setting
screen_width = 480
screen_height = 640

# Set the title
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Samuel Game")  # Game Title

# Load background image
background = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\background.png")

# Event Loop
running = True  # The game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

# pygame quit
pygame.quit
