import numpy as np

def conv(grayimagearray,image_height,image_width):
    kernel = np.zeros((3, 3))
    buffer = np.zeros((3, 3))
    sobelimg = np.zeros((image_height, image_width))
    # the kernel ****************************************
    kernel[0][0] = -1;kernel[0][1] = 0;kernel[0][2] = 1
    kernel[1][0] = -2;kernel[1][1] = 0;kernel[1][2] = 2;
    kernel[2][0] = -1;kernel[2][1] = 0;kernel[2][2] = 1
    # *****************************************************
    topy = -1;topx = 0;

    print("Begin Sobel")
    #This convolves stuff
    #image loop
    while topy < (image_height -3):
        topy+=1
        topx = 0
        #row loop

        while topx < (image_width - 2):

            #matrix loop
            n = 0;xbuf = 0;ybuf = 0; buffer = np.zeros((3,3));
            while n < 9:
                buffer[ybuf][xbuf] = grayimagearray[topy + ybuf][topx + xbuf]
                n += 1
                xbuf += 1
                if (xbuf == 3):
                    xbuf = 0
                    ybuf += 1
                if (n == 9):
                    mulbuf = buffer*kernel                              # kernel x image buffer
                    sobelimg[topy + 1][topx + 1] = matadder(mulbuf)    # sum of values in the product
                    print(int(100 * topy / image_height), "%", end="\r")
            topx += 1
            if topy == image_height-3:
                topx = topx

    return sobelimg
