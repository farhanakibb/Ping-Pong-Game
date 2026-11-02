import pygame

pygame.init()
screen_height = 620
screen_width = 400

screen = pygame.display.set_mode((screen_width, screen_height))
player1 = pygame.Rect((screen_width//2, 15, 49, 10))
player2 = pygame.Rect((screen_width//2, 600, 49, 10))
ball = pygame.Rect((screen_width//2, screen_width//2, 17, 17))
run = True
clock = pygame.time.Clock()
speed_y = 4
score = 0
scoree = 0
font = pygame.font.Font('freesansbold.ttf', 32)
op = pygame.Rect(( 38, 290, 100, 50))
op2 = pygame.Rect(( 238, 290, 100, 50))

speed_x = 5
start = False
while run:

    screen.fill('black')
    text = font.render(str(scoree), True, 'blue', 'black')
    textt = font.render(str(score), True, 'red', 'black')
    textRect = text.get_rect()
    textRect.center = (10, screen_height//2)
    texttRect = textt.get_rect()
    texttRect.center = (390, screen_height//2)
    screen.blit(text, textRect)
    screen.blit(textt, texttRect)
    pygame.draw.rect(screen, 'blue', player1)
    pygame.draw.rect(screen, 'red', player2)
    pygame.draw.rect(screen, (255, 255, 255), ball, border_radius=19)

   # pygame.draw.rect(screen, "white", op)
    #pygame.draw.rect(screen, "white", op2)
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        start = True
    if start:

       ball.y += speed_y
       ball.x += speed_x

       if ball.y <= 0:
           score += 1
           ball.center = (screen_width//2, screen_height//2)
           start = False
       if ball.y >= 620:
           scoree += 1
           ball.center = (screen_width//2, screen_height//2)
           start= False

       if ball.x > 400:
           speed_x *= -1
       if ball.x < 0:
          speed_x *= -1
       if ball.y >= 620:
          speed_y *= -1

       if ball.y <= 0:
          speed_y *= -1

       if ball.colliderect(player1) or ball.colliderect(player2):
           speed_y *= -1
       if key[pygame.K_d] == True and player1.x < 350:
           player1.x += 10
       if key[pygame.K_s] == True  and player1.x > 0:
          player1.x -= 10
       if key[pygame.K_RIGHT] == True and player2.x < 350:
          player2.x += 10
       if key[pygame.K_LEFT] == True and player2.x > 0:
          player2.x -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()