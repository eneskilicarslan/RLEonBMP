import numpy as np
from PIL import Image


def run():
    """ MAIN FUNCTIONALITY"""

def encode():
    """ INPUT - drop like its hot! """
    # path = input("path lütfen: ")
    # bmp = Image.open(path[1:-1])  # "" deletion

    """ NON-INPUT """
    bmp = Image.open('../../Desktop/School/Uni v5.2/VeriSıkıştırma/cicek.bmp')

    ''' BMP TO ARRAY '''
    print(bmp.info)
    arrayBMP = np.asarray(bmp)
    print(arrayBMP)

    RLE(traverseArray(1, arrayBMP))


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

    match mode:
        case "zigzag":
            print("zigzag")
        case "satır":
            print("satır satır")
        case "sütun":
            print("sütun sütun")


if __name__ == '__main__':
    run()
