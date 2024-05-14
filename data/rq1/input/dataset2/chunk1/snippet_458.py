#Source: https://stackoverflow.com/questions/62823806/random-brick-color-typeerror-pygame-color-object-is-not-callable
    # brick init
brick = pygame.Surface([brick_width, brick_height]),brick_color # surface for a single brick
pygame.draw.rect(brick[0], brick[1], [0, 0, brick_width, brick_height])



bricks = [] # list of *coordinates* of the bricks

# initialize coordinates of bricks

for y in range(num_brick_rows):
    brickY = (y * brick_row_height) + brick_offset_y    
    for x in range(num_bricks_in_row):
        brickX = (x * brick_column_width) + brick_offset_x
        color_of_brick = brick_color()
        bricks.append((brickX, brickY),color_of_brick) # coordinates are in fact tuples (x,y)