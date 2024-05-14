#Source: https://stackoverflow.com/questions/44741865/name-error-help-in-a-loop
    # Main Logic, Direction Buttons

while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('r'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('l'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('u'):
                changeto = 'UP' 
            if event.key == pygame.K_DOWN or event.key == ord('d'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event(QUIT))