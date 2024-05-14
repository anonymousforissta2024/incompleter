#Source: https://stackoverflow.com/questions/17002379/checking-collisions-for-each-sprite-in-a-group-attribute-error
if not game_over:
    move_coins()
    move_pointer()
    if pygame.sprite.spritecollideany(pointer, coin_group):
        print_text(pygame.font.Font(None,16), 0, 0, "Collision!")
        check_collision()