import cv2
import os
import numpy
import prototype

def processImage(model):
    sourceImage = cv2.imread(model['sourcePath'])
    greyImage = cv2.cvtColor(sourceImage,  cv2.COLOR_BGR2GRAY)

    # Detect eyes
    # Detect faces with "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    matches = cascade.detectMultiScale(
        greyImage,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    blur = cv2.GaussianBlur(greyImage, (model['blur'], model['blur']), 0)
    sketch = cv2.divide(greyImage, blur, scale = 256.0)
    erosion = numpy.ones((model['erosion'], model['erosion']), numpy.uint8)
    if (model['erodeFirst']):
        eroded = cv2.erode(sketch, erosion, iterations=1)
        _, threshold = cv2.threshold(eroded, model['thresholdValue'], 255, model['thresholdType'])
        sketch = threshold
    else:
        _, threshold = cv2.threshold(sketch, model['thresholdValue'], 255, model['thresholdType'])
        eroded = cv2.erode(threshold, erosion, iterations=1)
        sketch = eroded

    print(f"Found {len(matches)} Faces!")
    for (x, y, w, h) in matches:
        cv2.rectangle(sketch, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return sketch    

def play():
    print(f"Play...")
    cv2.namedWindow('Prototype', cv2.WINDOW_NORMAL)
    model = prototype.Model({
            "sourcePath": prototype.Data(["source/image2.jpg", "source/image3.jpg", "source/image4.jpg", "source/image5.jpg", "source/image6.jpg", "source/image7.jpg"], 5, ['o', 'p']),
            "blur": prototype.Data([11, 21, 41, 61, 91, 121, 151], 5, ['q','w']),
            "erosion": prototype.Data([1, 2, 3, 4, 5, 6, 7], 1, ['a','s']),
            "thresholdType": prototype.Data([cv2.THRESH_TOZERO, cv2.THRESH_TOZERO + cv2.THRESH_OTSU, cv2.THRESH_BINARY + cv2.THRESH_OTSU, cv2.THRESH_BINARY], 1, ['z','x']),
            "thresholdValue": prototype.Data([150, 175, 200, 210, 220, 230, 240, 250], 1, ['c','v']),
            "erodeFirst": prototype.Data([False, True], 0, ['d','f']),
        })

    while True:
        model.Dump()
        sketch = processImage(model)
        cv2.imshow('Prototype', sketch)

        key = cv2.waitKey(0)
        print(f"...")
        if (key == 27): #escape
            print(f"Exit...")
            model.Dump()
            break
        model.TryNavigate(chr(key))

    cv2.destroyAllWindows()


# TODO: normalize images so that the processing produces roughly the same result for various kinds of raw input

play()
