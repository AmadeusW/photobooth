import cv2
import os
import numpy
import prototype

def go():
    with os.scandir("source") as entries:
        for entry in entries:
            if entry.is_file():
                processImage("source/" + entry.name, "out/" + entry.name)

def processImage(model):
    sourceImage = cv2.imread(model['sourcePath'])
    greyImage = cv2.cvtColor(sourceImage,  cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(greyImage)
    blur = cv2.GaussianBlur(greyImage, (model['blur'], model['blur']), 0)
    sketch = cv2.divide(greyImage, blur, scale = 256.0)

    erosion = numpy.ones((model['erosion'], model['erosion']), numpy.uint8)
    if (model['erodeFirst']):
        eroded = cv2.erode(sketch, erosion, iterations=1)
        _, threshold = cv2.threshold(eroded, model['thresholdValue'], 255, model['thresholdType'])
        return threshold
    else:
        _, threshold = cv2.threshold(sketch, model['thresholdValue'], 255, model['thresholdType'])
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
        key = cv2.waitKey(0)
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
