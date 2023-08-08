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
    x, threshold1 = cv2.threshold(sketch, 200, 255, cv2.THRESH_TOZERO)
    x, threshold2 = cv2.threshold(sketch, 200, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    x, threshold3 = cv2.threshold(sketch, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    x, ethreshold1 = cv2.threshold(eroded, 200, 255, cv2.THRESH_TOZERO)
    x, ethreshold2 = cv2.threshold(eroded, 200, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    x, ethreshold3 = cv2.threshold(eroded, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    t1e = cv2.erode(threshold1, erosion, iterations=1)
    t2e = cv2.erode(threshold2, erosion, iterations=1)
    t3e = cv2.erode(threshold3, erosion, iterations=1)
    cv2.imwrite(outputPath+"threshold1.jpg", threshold1)
    cv2.imwrite(outputPath+"threshold2.jpg", threshold2)
    cv2.imwrite(outputPath+"threshold3.jpg", threshold3)
    cv2.imwrite(outputPath+"ethreshold1.jpg", ethreshold1   )
    cv2.imwrite(outputPath+"ethreshold2.jpg", ethreshold2)
    cv2.imwrite(outputPath+"ethreshold3.jpg", ethreshold3)
    cv2.imwrite(outputPath+"eroded.jpg", eroded)
    cv2.imwrite(outputPath+"t1e.jpg", t1e)
    cv2.imwrite(outputPath+"t2e.jpg", t2e)
    cv2.imwrite(outputPath+"t3e.jpg", t3e)
    cv2.imwrite(outputPath, sketch)


# TODO: normalize images so that the processing produces roughly the same result for various kinds of raw input

go()
