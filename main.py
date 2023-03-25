import numpy as np
from PIL import Image


def run():
    """ MAIN FUNCTIONALITY"""
    mat = np.matrix([[1, 2, 2, 2],
                    [2, 2, 2, 2],
                    # [2, 2, 2, 2],
                    [1, 0, 0, 2]])
    rleDarray = traverseArray("satır", encode()).__str__()
    # print("rleDarray -----> " , rleDarray)
    print("compressed size ----> " + len(rleDarray).__str__())



def encode():
    """ INPUT - drop like its hot! """
    # path = input("path lütfen (resmi sürükle bırak konsola): ")
    # bmp = Image.open(path[1:-1])  # "" deletion

    """ NON-INPUT """
    bmp = Image.open('../../Desktop/School/Uni v5.2/VeriSıkıştırma/odev1/diagonal_flag.bmp')

    ''' BMP TO ARRAY '''
    print(bmp.info)
    arrayBMP = np.asarray(bmp)
    print(arrayBMP)
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


def RLE(array):
    """ RETURNS RUN-LENGTH ENCODED ARRAY (1D)"""


def RLD(array):
    """ RETURNS RUN-LENGTH DECODED ARRAY (2D) """


def ratio(num1, num2):
    """ TO BE DETERMINED """

    print(num1/num2)


def traverseArray(mode, arr):
    """ RETURNS TRAVERSED ARRAY """
    rleDarray = []
    match mode:
        case "zigzag":
            print("zigzag")

        case "satır":
            print("satır satır okuma gerçekleşecek, snake-formation!")
            counter = 1
            currentValRighttoLeft = -1
            currentValLefttoRight = -1
            for i in range(arr.shape[0]):
                # print("i ->>>>> " + i.__str__())
                # print("rleDarray ->>>>> " + rleDarray.__str__())
                # print("currentValRighttoLeft ->>>>> " + currentValRighttoLeft.__str__())
                # print("currentValLefttoRight ->>>>> " + currentValLefttoRight.__str__())
                # Snake formation traverse
                if i % 2 == 0:
                    if currentValLefttoRight == arr[i, 0]:
                        counter+=1
                    else:
                        if i != 0:
                            rleDarray.append(counter)
                            rleDarray.append(currentValLefttoRight)
                            counter = 1

                    currentValRighttoLeft = arr[i, -1]
                    for j in range(arr.shape[1]-1):
                        if arr[i, j] == arr[i, j+1]:
                            counter += 1
                        else:
                            rleDarray.append(counter)
                            rleDarray.append(arr[i, j])
                            counter = 1

                else:
                    if currentValRighttoLeft == arr[i,-1]:
                        counter += 1
                    else:
                        rleDarray.append(counter)
                        rleDarray.append(currentValRighttoLeft)
                        counter = 1

                    currentValLefttoRight = arr[i, 0]
                    for j in range(arr.shape[1]-1, -1, -1):
                        if arr[i, j] == arr[i, j - 1]:
                            counter += 1
                        else:
                            rleDarray.append(counter)
                            rleDarray.append(arr[i, j])
                            counter = 1

            return rleDarray
        case "sütun":
            print("sütun sütun")


if __name__ == '__main__':
    run()
