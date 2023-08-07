import cv2
import os
import numpy

def go():
    with os.scandir("source") as entries:
        for entry in entries:
            if entry.is_file():
                processImage("source/" + entry.name, "out/" + entry.name)

def processImage(sourcePath, outputPath):
    sourceImage = cv2.imread(sourcePath)
    greyImage = cv2.cvtColor(sourceImage,  cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(greyImage)
    blur = cv2.GaussianBlur(greyImage, (91, 91), 0)
    sketch = cv2.divide(greyImage, blur, scale = 256.0)

    erosion = numpy.ones((5, 5), numpy.uint8)
    eroded = cv2.erode(sketch, erosion, iterations=1)
    x, threshold = cv2.threshold(sketch, 200, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    cv2.imwrite(outputPath+"threshold.jpg", threshold)
    cv2.imwrite(outputPath+"eroded.jpg", eroded)
    cv2.imwrite(outputPath, sketch)


# TODO: normalize images so that the processing produces roughly the same result for various kinds of raw input

go()
