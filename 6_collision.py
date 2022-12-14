import pygame

pygame.init()  # Initialize

# Display setting
screen_width = 480
screen_height = 640

# Set the title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Samuel Game")  # Game Title

# Frame Per Second
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\background.png")

# Load sprite(character)
character = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\character.png")
character_size = character.get_rect().size # Get Image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width/2 # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height #화면 세로크기 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# 적 캐릭터 만들기
enemy = pygame.image.load("C:\\Users\\souls\\PycharmProjects\\pythonProject\\enemy.png")
enemy_size = enemy.get_rect().size # Get Image size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width/2 # 화면 가로의 절반 크기에 위치
enemy_y_pos = (screen_height/2) - enemy_height/2 #화면 세로크기 가장 아래에 위치

# 이벤트 루프
running = True  # The game is running?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춘다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 Rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0))  # Paint Background
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기
    pygame.display.update() # Game display re-paint!

# pygame quit
pygame.quit()
