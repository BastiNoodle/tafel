import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
position = pygame.mouse.get_pos()
color = pygame.Color(255,255,255)
framenumber = 1
color_r = 255
color_g = 255
color_b = 255
size = 10
while running:
    #closing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
      screen.fill("black")
    if keys[pygame.K_1]:
      color_r = 255
      color_g = 0
      color_b = 0
    if keys[pygame.K_2]:
      color_r = 255
      color_g = 255
      color_b = 0
    if keys[pygame.K_3]:
      color_r = 0
      color_g = 255
      color_b = 0
    if keys[pygame.K_4]:
      color_r = 0
      color_g = 255
      color_b = 255
    if keys[pygame.K_5]:
      color_r = 0
      color_g = 0
      color_b = 255
    if keys[pygame.K_6]:
      color_r = 255
      color_g = 0
      color_b = 255
    if keys[pygame.K_7]:
      color_r = 255
      color_g = 255
      color_b = 255
    if keys[pygame.K_8]:
      color_r = 128
      color_g = 128
      color_b = 128
    if keys[pygame.K_9]:
      color_r = 64
      color_g = 64
      color_b = 64
    if keys[pygame.K_0]:
      color_r = 0
      color_g = 0
      color_b = 0
    if keys[pygame.K_q]:
      size = 5
    if keys[pygame.K_w]:
      size = 10
    if keys[pygame.K_e]:
      size = 20
    if keys[pygame.K_r]:
      size = 40
    if keys[pygame.K_t]:
      size = 80

    color = pygame.Color(color_r, color_g, color_b)
    #drawing:
    listofmousebuttons = pygame.mouse.get_pressed()
    if listofmousebuttons[0] == True:
        pygame.draw.circle(screen, color, position, size)
    position = pygame.mouse.get_pos()

    #push:
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
