def square_matrix(square):
    """ This function will calculate the value x 
       (i.e. blurred pixel value) for each 3 * 3 blur image.
    """
    tot_sum = 0
    for i in range(3):
        for j in range(3):
            tot_sum += square[i][j]
    return tot_sum // 9

def boxBlur(image):
    """
    This function will calculate the blurred 
    image for given n * n image. 
    """
    square = []
    square_row = []
    blur_row = []
    blur_img = []
    n_rows = len(image)
    n_col = len(image[0])
    rp, cp = (0, 0)
    while rp <= n_rows - 3:
        while cp <= n_col - 3:
            for i in range(rp, rp + 3):
                for j in range(cp, cp + 3):
                    square_row.append(image[i][j])
                square.append(square_row)
                square_row = []
            blur_row.append(square_matrix(square))
            square = []
            cp = cp + 1
        blur_img.append(blur_row)
        blur_row = []
        rp = rp + 1
        cp = 0
    return blur_img
print(boxBlur(image))