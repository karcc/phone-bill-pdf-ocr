#!/usr/bin/python3
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import sys


def main(argv):
    # Code goes over here.
    convertPdfToImage(argv)
    return 0


def convertPdfToImage(input):
    filePath = input[0]
    pdfFile = convert_from_path(filePath, 300)
    i = 1
    for page in pdfFile:
        page.save(str(i) + '_out.jpg', 'JPEG')
        i += 1


if __name__ == "__main__":
    main(sys.argv[1:])
