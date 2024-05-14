#Source: https://stackoverflow.com/questions/77716362/typeerror-invalid-rect-assignment-in-class
while running:
    setup_background()
    spriteimg = plumberright

    screen.blit(spriteimg,(x1, y1))

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                 x1 = x1 + 0
                 y1 = y1 - 1
             elif event.key == pygame.K_DOWN:
                 x1 = x1 + 0
                 y1 = y1 + 1
             elif event.key == pygame.K_LEFT:
                 x1 = x1 - 1
                 y1 = y1 + 0
             elif event.key == pygame.K_RIGHT:
                 x1 = x1 + 1
                 y1 = y1 + 0

    pygame.display.flip()
    clock.tick(120)