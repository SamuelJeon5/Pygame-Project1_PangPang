import pygame
###############################################################################
# 기본 초기화(반드시 해야하는 것들)
pygame.init()  # Initialize

# 화면 크기 설정
screen_width = 480
screen_height = 640

# 화면 타이틀 설정
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Samuel Game")  # Game Title

# Frame Per Second
clock = pygame.time.Clock()
##############################################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True  # The game is running?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 2.이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. 게임 캐릭터 위치 정의
    # 4. 충돌 처리
    # 5. 화면에 그리기
    pygame.display.update() # Game display re-paint!

# pygame quit
pygame.quit()
