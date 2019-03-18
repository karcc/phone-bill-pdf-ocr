#!/usr/bin/python3
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import pandas as pd
import sys
import re


def main(argv):
    convertPdfToImage(argv)
    # hardcoded to see this file only
    #table = pytesseract.image_to_data(Image.open('1_out.jpg'), output_type='data.frame')
    #print(pytesseract.image_to_data(Image.open('1_out.jpg')))
    #ableh = pd.DataFrame(table[123:217]['text'])
    #print(tableh['text'])
    #tabley = table[(table['line_num'] >= 4) & (table['line_num'] <= 14)]
    #print(tabley)

    tableString = pytesseract.image_to_string(Image.open('1_out.jpg'))
    firstIdx = tableString.find('Group 1')
    lastIdx = tableString.find('Devices') - 11
    tableData = tableString[firstIdx:lastIdx].strip()
    tableAry = [data for data in tableData.split('\n') if data]

    testAry = np.zeros(shape=(12,7), dtype=object)

    print(tableData)
    print(tableAry)

    for i in range(len(tableAry)):
        accountAry = tableAry[i].split(' ')
        # insert another data to Total row since it's missing a column
        if accountAry[0] == 'Total':
            accountAry.insert(1, str(0))

        for j in range(len(accountAry)):
            cellValue = accountAry[j]
            # clean up cell data
            if cellValue[0] == '$':
                cellValue = accountAry[j][1:]
            if cellValue[0] == '-' or cellValue[0] == '=' or cellValue[0] == chr(8220):
                cellValue = 0

            testAry[i][j] = cellValue


    print(testAry)

    return 0


def convertPdfToImage(input):
    filePath = input[0]
    # pdfFile = convert_from_path(filePath, 300)
    # This part is hard coded to look extract page 2 only since the data
    # we are interested in is in page 2
    pdfFile = convert_from_path(filePath, 300, first_page=2, last_page=2)
    i = 1
    for page in pdfFile:
        page.save(str(i) + '_out.jpg', 'JPEG')
        i += 1


if __name__ == "__main__":
    main(sys.argv[1:])
