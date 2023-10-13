import pygame, time

pygame.init()

W = 900
H = 600

window = pygame.display.set_mode((W, H))

window.fill((255, 255, 255))
bg = pygame.image.load("fon.jpg")


size = (200, 100)
sprite0 = pygame.transform.scale(pygame.image.load('0.png'), size)
sprite1 = pygame.transform.scale(pygame.image.load('1.png'), size)
sprite2 = pygame.transform.scale(pygame.image.load('2.png'), size)
sprite3 = pygame.transform.scale(pygame.image.load('3.png'), size)
sprite4 = pygame.transform.scale(pygame.image.load('4.png'), size)
sprite5 = pygame.transform.scale(pygame.image.load('5.png'), size)


sprite = [sprite0, sprite1, sprite2, sprite3, sprite4, sprite5,]
sp = 0

sprite_rect = sprite1.get_rect()
ballrect = pygame.Rect(W-200, 0, 40, 40)


sprite_rect.x = 0 
sprite_rect.y = 0

speed_x = 0 
speed_y = 0
speed = 7
speed_b = [5, 5]


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -speed
            if event.key == pygame.K_RIGHT:
                speed_x = speed
            if event.key == pygame.K_UP:
                speed_y = -speed
            if event.key == pygame.K_DOWN:
                speed_y = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0


    sprite_rect.x += speed_x
    sprite_rect.y += speed_y
    
    if speed_x != 0:
        if sp == len(sprite)-1:
            sp = 0
        sp += 1

    ballrect = ballrect.move(speed_b)
    if ballrect.left < 0 or ballrect.right >= W:
        speed_b[0] = -speed_b[0]
    if ballrect.top < 0 or ballrect.bottom >= H:
        speed_b[1] = -speed_b[1]
        
    if sprite_rect.colliderect(ballrect):
        running = False
    
    window.blit(bg, (-400, -200))
    window.blit(sprite[sp], sprite_rect)
    pygame.draw.circle(window, (0,0,0), (ballrect.x, ballrect.y), ballrect.h)
    time.sleep(0.01)
    pygame.display.flip()
    
pygame.quit()
