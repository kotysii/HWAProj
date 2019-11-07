#import mmap
#import sys
from Functions.BMP_Preparation import *


def matrixadder(mat33):
    sum = 0
    n = 0

    while n < 9:  # image size
        x = 0;
        y = 0;
        while x < 3:
            sum += mat33[y][x]
            if (x == 3):
                x = 0
                y += 1
            x += 1
            n += 1
    return(sum)

#may possibly only work on big-endian systems

file_location = ["/home/dan/PyFiles/Images/redblackstripey.bmp", "/home/dan/PyFiles/Images/kobe.bmp", "/home/dan/PyFiles/Images/Testimg2.bmp"]

grayimagearray = importimage(file_location[1]) #file import function, returns 2d array of the grayscale image (from importfun)

tempheight = 938 #TODO replace
tempwidth = 1251
#               x                y
kernel = [[4] * 3 for i in range(3)]
buffer = [[2] * 3 for i in range(3)]
sobelimg = [[0] * tempheight for i in range(tempwidth)] #TODO Find a way to get the height and width
#TODO make the kernel SOBEL

#             y  x        ugh, low priority TODO switch the x and y (low priority)
#      kernel[0][3])
topy=0;topx=0;

print("Begin Sobel")
#this sobels the dude up
while topy < tempheight -2: #image size TODO Find a way to get the image height and width
    n = 0;x = 0;y = 0;
    while n < 9:
        buffer[y][x] = grayimagearray[topy + y][topy + x]
        buffer2 = by3multi(buffer,kernel) #multiplies the grayscale image in the buffer by the kernel
        n += 1
        x += 1
        print(tempheight)
        if (x == 3):
            x = 0
            y += 1
    sobelimg[topy+1][topx+1] = int(matrixadder(buffer2)/9)  # sums the values in the matrix
    topx += 1
    if topx == tempwidth-2:#image_width
        topy +=1
        topx = 0


by3multi(kernel, buffer) #returns multiplication


