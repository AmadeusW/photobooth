import cv2
import numpy
import prototype

def processImageWithDefaultSettings(source, target):
    model = {
            "sourcePath": source,
            "blur": 121,
            "erosion": 1,
            "thresholdType": cv2.THRESH_TOZERO + cv2.THRESH_OTSU,
            "thresholdValue": 150,
            "erodeFirst": False,
        }
    image = processImage(model)
    cv2.imwrite(target, image)

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