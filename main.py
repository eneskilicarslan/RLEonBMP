import numpy as np
import zigzag
from PIL import Image


def run():
    """ MAIN FUNCTIONALITY"""
    # print("rleDarray -----> " , rleDarray)

    rleDarray = traverseArray("row", encode())
    print("row by row compressed size ----> " + len(rleDarray).__str__())

    rleDarray = traverseArray("col", encode())
    print("col by col compressed size ----> " + len(rleDarray).__str__())

    rleDarray = traverseArray("zigzag", encode())
    print("zigzag compressed size ----> " + len(rleDarray).__str__())


def encode():
    """ INPUT - drop like its hot! """
    # path = input("path please (drop like its hot!): ")
    # bmp = Image.open(path[1:-1])  # "" deletion

    """ NON-INPUT """
    bmp = Image.open('../../Desktop/School/Uni v5.2/VeriSıkıştırma/odev1/cicek.bmp')

    ''' BMP TO ARRAY '''
    arrayBMP = np.asarray(bmp)
    # print(arrayBMP)
    print("first size -----> " + (arrayBMP.shape[0]*arrayBMP.shape[1]).__str__())
    return arrayBMP

    # RLE(traverseArray(1, arrayBMP))


def decode(arrayBMP):
    RLD(arrayBMP)

    ''' ARRAY TO IMAGE '''

    bmpEncoded = Image.fromarray(arrayBMP)
    print(bmpEncoded.info)

    ''' SAVE IMAGE AS BMP '''
    bmpEncoded.save('result.bmp')


def RLD(arr):
    """ RETURNS RUN-LENGTH DECODED ARRA (2D)"""

def RLE(arr):
    """ RETURNS RUN-LENGTH ENCODED ARRAY (1D)"""

    rleDarray = []
    counter = 1
    currentValRighttoLeft = -1
    currentValLefttoRight = -1

    for i in range(arr.shape[0]):
        # print("i ->>>>> " + i.__str__())
        # print("rleDarray ->>>>> " + rleDarray.__str__())
        # print("currentValRighttoLeft ->>>>> " + currentValRighttoLeft.__str__())
        # print("currentValLefttoRight ->>>>> " + currentValLefttoRight.__str__())

        """ Snake formation traverse """
        if i % 2 == 0:
            if currentValLefttoRight == arr[i, 0]:
                counter += 1
            else:
                if i != 0:
                    rleDarray.append(counter)
                    rleDarray.append(currentValLefttoRight)
                    counter = 1

            currentValRighttoLeft = arr[i, -1]
            for j in range(arr.shape[1] - 1):
                if arr[i, j] == arr[i, j + 1]:
                    counter += 1
                else:
                    rleDarray.append(counter)
                    rleDarray.append(arr[i, j])
                    counter = 1

        else:
            if currentValRighttoLeft == arr[i, -1]:
                counter += 1
            else:
                rleDarray.append(counter)
                rleDarray.append(currentValRighttoLeft)
                counter = 1

            currentValLefttoRight = arr[i, 0]
            for j in range(arr.shape[1] - 1, -1, -1):
                if arr[i, j] == arr[i, j - 1]:
                    counter += 1
                else:
                    rleDarray.append(counter)
                    rleDarray.append(arr[i, j])
                    counter = 1

    return rleDarray


def RLE2D(array):
    """ RETURNS RUN-LENGTH ENCODED ARRAY (2D) """
    counter = 1
    rleDarray = []
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            counter += 1
        else:
            rleDarray.append(counter)
            rleDarray.append(array[i])

    return rleDarray


def ratio(num1, num2):
    """ TO BE DETERMINED """

    print(num1/num2)


def traverseArray(mode, arr):
    """ RETURNS TRAVERSED ARRAY """
    match mode:
        case "row":
            print("row by row traverse, snake-formation!")
            return RLE(arr)

        case "col":
            print("col by col traverse, snake-formation!")
            return RLE(np.rot90(arr))

        case "zigzag":
            print("zigzag traverse!")
            return RLE2D(zigzag.traverse(arr))

if __name__ == '__main__':
    run()
