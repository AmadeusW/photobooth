import cv2
import os
import numpy
import prototype

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

def processImage(model):
    sourceImage = cv2.imread(model.GetValue('sourcePath'))
    greyImage = cv2.cvtColor(sourceImage,  cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(greyImage)
    blur = cv2.GaussianBlur(greyImage, (model.GetValue('blur'), model.GetValue('blur')), 0)
    sketch = cv2.divide(greyImage, blur, scale = 256.0)

    erosion = numpy.ones((model.GetValue('erosion'), model.GetValue('erosion')), numpy.uint8)
    if (model.GetValue('erodeFirst')):
        eroded = cv2.erode(sketch, erosion, iterations=1)
        x, threshold = cv2.threshold(eroded, model.GetValue('thresholdValue'), 255, model.GetValue('thresholdType'))
        return threshold
    else:
        x, threshold = cv2.threshold(sketch, model.GetValue('thresholdValue'), 255, model.GetValue('thresholdType'))
        eroded = cv2.erode(threshold, erosion, iterations=1)
        return eroded

def play():
    print(f"Play...")
    cv2.namedWindow('Prototype', cv2.WINDOW_NORMAL)
    model = prototype.PrototypeModel()
    while True:
        sketch = processImage(model)
        cv2.imshow('Prototype', sketch)
        model.Dump()
        key = cv2.waitKey(0);
        print(f"...")
        if (key == 27): #escape
            print(f"Exit...")
            model.Dump()
            break
        model.TryNavigate(chr(key))

    cv2.destroyAllWindows()


# TODO: normalize images so that the processing produces roughly the same result for various kinds of raw input

#go()
play()
