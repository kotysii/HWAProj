
from Functions.all import *
import time
import numpy as np
from matplotlib import pyplot as plt
from skimage.feature import peak_local_max
from scipy.ndimage import gaussian_filter


start_time = time.time() #time of start                                             1                               2                                       3                                           4                                           5                                   6                                           7                                       8                                                       9					10						11
file_location = ["/home/dan/HWAProj/images/realnoiseless.bmp", "/home/dan/HWAProj/images/ArtificialCircle.bmp","/home/dan/Pictures/tula.bmp","/home/dan/HWAProj/images/teste.bmp", "/home/dan/DIPProj/images/ImageProcessingDemo.bmp", "/home/dan/DIPProj/images/dot.bmp","/home/dan/DIPProj/images/artific4px.bmp","/home/dan/HWAProj/images/artific4xmulti.bmp","/home/dan/DIPProj/images/artific4xmultibigger.bmp","/home/dan/DIPProj/images/artificialnoise.bmp", "/home/dan/HWAProj/images/IRReportTest.bmp", "/home/dan/HWAProj/images/test3.bmp"]
usedimage = file_location[11]

image_width, image_height, image_offset = image_props(usedimage) #file import function, returns 2d array of the grayscale image (from importfun)

#### Parameter #####
threshold = 40          # grayscale threshold
radius_range = 1
radius_start = 3
circle_threshold = int(0.5*2*np.pi*radius_start)    # this will mean that the circle has have at least half the number of filled pixels in it's circumference
### end of params ###

#rgbimg[xcolumn][yrow]
rgbimg = plt.imread(usedimage)
x=gaussian_filter(rgbimg, sigma=0)

thresholdstarttime = time.time() # the time of threshold

# TODO I dont actually need this threshold image(?) if I have the list of edge point coordinates according to it? or gray_image?
thresimg, gray_image, edges = gray_and_threshold_image_maker(image_width, image_height, x, threshold)

print("threshold duration time: ", time.time()-thresholdstarttime)

x = np.arange(0, 2*np.pi, 2*np.pi/100)
msin = np.sin(x)
mcos = np.cos(x)

#   accumulator[r][h][w]
#accumulator = np.ndarray(shape=(radius_range,image_height,image_width), dtype=int, buffer=None)
accumulator = np.zeros(shape=(radius_range,image_height,image_width), dtype=int)
thresholded_accumulator = np.zeros(shape=(radius_range,image_height,image_width), dtype=int)
circle_coords = []

edgeslength = len(edges)

print("%s edges to evaluate, so be patient" %edgeslength)
print("radius range of %s" %radius_range)

# for every radius being evaluated
# for every edge point:
# draw circle (circle_coords)
#   for every coordinate in that circle
#   set accumulator to 1
# next edge point

i=0
r = radius_start
rar = 0

circlegenerationtime = time.time()

while rar < radius_range:
    for p in edges:
        i += 1
        x,y = p
        circle_coords = (circle(msin,mcos,x,y,r)) #takes msin,mcos,a,b,r in pixels, returns the coordinates of a circle of r radius about the points x, y
        for n in circle_coords:
            h, v = n
            if (h < image_width) & (h>0) & (v < image_height) & (v>0):
                accumulator[rar][v][h] += 1
        print("Houghing: ", 100 * i / edgeslength, "%", end="\r")
    r += 1
    rar+=1
print("Houghed!")

print("hough duration time: ", time.time()-circlegenerationtime)

maxi = np.amax(accumulator) #max value in array

#

localmaxcoords = []
planemaxcoords = []
r=radius_start
rar=0
while rar < radius_range:
    thresholded_accumulator[rar][:][:] = gaussian_filter((proportionalthreshold(accumulator[rar][:][:], circle_threshold)), sigma=0.01)
    planemaxcoords = peak_local_max(thresholded_accumulator[rar][:][:], min_distance=10)
    # discounts the coordinates that are too close together
    n=0
    while n+1 < len(planemaxcoords):
        y1,x1 = planemaxcoords[n]
        y2,x2 = planemaxcoords[n+1]
        if ( (abs(x1 - x2) > r) | (abs(y1-y2) > r) )|( n+2==len(planemaxcoords) ):
            localmaxcoords.append([x1,y1])
        n+=1
    r+=1
    rar+=1



######################## Plotting ###############################

print("You have", len(localmaxcoords), "circles with centre points at the following coordinates:\n", localmaxcoords)

xcoords, ycoords = zip(*localmaxcoords)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


ax3.imshow(accumulator[0][:][:], cmap="gray", vmin=0, vmax=maxi) #accumulator plane
ax1.imshow(gray_image,cmap="gray", vmin=0, vmax=255)		#original image
ax4.plot(xcoords,ycoords, 'r.')					#circle coords
ax2.imshow(thresimg,cmap="gray",vmax=1)				#thresholded image
ax4.imshow(thresholded_accumulator[0][:][:],cmap="gray",vmax=1)
plt.tight_layout()
plt.show()

print("\n\nRuntime: %s seconds" %(time.time()-start_time))

