import pygame

pygame.init()  # Initialize

# Display setting
screen_width = 480
screen_height = 640

# Set the title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Samuel Game")  # Game Title

# Load background image
background = pygame.image.load("/Pygame Basics/background.png")

# Event Loop
running = True  # The game is running?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))  # Paint Background
    pygame.display.update() # Game display re-paint!



# pygame quit
pygame.quit()
