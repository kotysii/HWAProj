#import mmap
#import sys

from Functions.BMP_Preparation import *

def matadder(by3):
    x=0;y=0;sum=0;p=0
    while p < 8:
        while x<3:
            sum += by3[y][x]

            x+=1
            p+=1
            if (x == 3) & (p != 9):
                x=0
                y+=1
        print(sum)
    return sum

file_location = ["/home/dan/PyFiles/Images/redblackstripey.bmp", "/home/dan/PyFiles/Images/kobe.bmp", "/home/dan/PyFiles/Images/Testimg2.bmp"]

grayimagearray, image_width, image_height = importimage(file_location[1]) #file import function, returns 2d array of the grayscale image (from importfun)

#               x                y
kernel = np.zeros((3,3))
buffer = np.zeros((3,3))
sobelimg = np.zeros((image_height,image_width))
 #the kernel ****************************************
kernel[0][0] = 1; kernel[0][1] = 2; kernel[0][2] = 3
kernel[1][0] = 4; kernel[1][1] = 5; kernel[1][2] = 6
kernel[2][0] = 7; kernel[2][1] = 8; kernel[2][2] = 9
#*****************************************************
topy=0;topx=0;

print("Begin Sobel")
#this convolves
while topy < image_height -2:

    #loading of gscale image into 3x3 buffer
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
            sobelimg[topy + 1][topx + 1] = matadder(mulbuf)     # sum of values in the product
    topx += 1




