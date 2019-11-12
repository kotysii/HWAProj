
from Functions.BMP_Preparation import *

file_location = ["/home/dan/PyFiles/Images/redblackstripey.bmp", "/home/dan/PyFiles/Images/kobe.bmp", "/home/dan/PyFiles/Images/Testimg2.bmp"]

grayimagearray, image_width, image_height = importimage(file_location[1]) #file import function, returns 2d array of the grayscale image (from importfun)

sobelx = np.zeros((3,3));
sobelx[0][0] = -1;sobelx[0][1] = 0;sobelx[0][2] = 1
sobelx[1][0] = -2;sobelx[1][1] = 0;sobelx[1][2] = 2
sobelx[2][0] = -1;sobelx[2][1] = 0;sobelx[2][2] = 1

sobely = np.zeros((3,3))
sobely[0][0] = 1;sobely[0][1] = 2;sobely[0][2] = 1
sobely[1][0] = 0;sobely[1][1] = 0;sobely[1][2] = 0
sobely[2][0] = -1;sobely[2][1] = -2;sobely[2][2] = -1

# takes kernel, image, height, width
xsobelled = conv(sobelx,grayimagearray, image_height, image_width)
ysobelled = conv(sobely,grayimagearray, image_height, image_width)
