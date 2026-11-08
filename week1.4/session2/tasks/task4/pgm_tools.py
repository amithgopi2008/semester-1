def writePGM(filename, image):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width, height, max_gray, pixels = image  # unpack the tuple

    with open(filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")

        for row in pixels:
            f.write(" ".join(str(value) for value in row) + "\n")

    return


def invertPGM(image):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width, height, max_gray, pixels = image  

    inverted = [[255 - pixels[i][j] for j in range(width)] for i in range(height)]

    return width, height, max_gray, inverted