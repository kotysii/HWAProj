import mmap
import sys

def endian_rev(bytesarr):
    list_length = len(bytesarr)  # length of the input *bytes* type in bytes

    arr = bytearray(list_length)  # creates a *bytesarray* type of the same length

    i = 0
    while i < list_length:
        arr[(list_length - 1) - i] = bytesarr[i]
        i += 1

    return (arr)

# combine bytes to form one binary number
def byte_combine(bytesarr):
    list_length = len(bytesarr)
    arr = 0

    i = 0
    while i < list_length:
        arr = arr << 8
        arr = arr + bytesarr[i]
        i += 1
    return (arr)
# import the image #returns a 2D array of the
def importimage(file_location):
    if sys.byteorder == "little":
        is_little = True

    with open(file_location, "r+b") as image:  # with statement for file opening

        mm = mmap.mmap(image.fileno(),
                       0)  # mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset]) 	fileno is the file handle of the file (image)

        # **********From Header*****************
        image_width = byte_combine(endian_rev(mm[
                                              18:22]))  # enters the 18:22 bytes of the byte array --> endian reverser --> combine bytes into one integer
        image_height = byte_combine(endian_rev(mm[22:26]))
        image_offset = byte_combine(endian_rev(mm[10:14]))
        header_image_size = byte_combine(endian_rev(mm[2:6]))
        bits_per_px = byte_combine(endian_rev(mm[28:30]))
        # ************Properties******************
        image_size = mm.size()  # size of the memmap file
        padding = image_width % 4
        bytes_wide = image_width * 3 + padding  # byte range of a row of pixels including padding
        row_image = image_offset + 3 * image_width  # bytes number in a row that are representative of image pixels vs padding
        # ****************************************

        print("image width:\t", image_width, "\nimage height:\t", image_height, "\nimage offset:\t", image_offset,
              "\npadding width:\t", padding, "\nfile location:\t", file_location)
        print("\n")

        # input("Press Enter to Continue")

        row = 0
        n = 0
        non_padding_counter = 0
        arrcounter = 0
        imagearr = [[0] * image_width for i in range(image_height)]
        # image[col][row]

        while row < image_height:
            col = image_offset + bytes_wide * row

            while col < (row + 1) * bytes_wide + image_offset:
                if col < (row + 1) * bytes_wide + image_offset - padding:
                    # print(mm[col], "\t\t")
                    print(int(100 * col / image_size), "%", end="\r")  # loading percentage

                    #	for the purpose of averaging for grayscaling
                    if (non_padding_counter + 1) % 3 == 0:  # finds multiples of 3 in
                        imagearr[row][arrcounter] = int((mm[col] + mm[col - 1] + mm[col - 2]) / 3)
                        arrcounter += 1  # arrcounter increments when the average of the 3px is added to the array
                    non_padding_counter += 1
                else:
                    # print("padding:",mm[col])
                    n = 0;
                    non_padding_counter = 0
                    arrcounter = 0
                col += 1
                n += 1
                if col == 643:  # debug stopper
                    arrcounter = arrcounter
            row += 1
            arrcounter = 0

        print("Import Successful")
        imagearr  # the product of my hardwork! A GRAYSCALED 2D LIST!

        # 3x3 matrix locations
        # imagearr[n][m], imagearr[n+1][m], imagearr[n+2][m], imagearr[n][m+1], imagearr[n+1][m+1], imagearr[n+2][m+1], imagearr[n][m+2], imagearr[n+1][m+2], imagearr[n+2][m+2]
        # iterate through every part of the 2d list, until bottom right is at image_width * image_height

        mm.close()

        return (imagearr)
#3x3 multiplier
def by3multi(a,b):
    product = [[0] * 3 for i in range(3)]
    n=0; x=0; y=0

    while n<9:
        product[y][x] = a[y][x] * b[y][x]

        n += 1
        x += 1
        if(x==3):
            x=0
            y+=1

    return(product)