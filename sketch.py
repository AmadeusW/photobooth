import processor
import cv2
import prototype

def play():
    print(f"Play...")
    cv2.namedWindow('Prototype', cv2.WINDOW_NORMAL)
    model = prototype.Model({
            "sourcePath": prototype.Data(["source/image1.jpg", "source/image2.jpg", "source/image3.jpg"], 1, ['o', 'p']),
            "blur": prototype.Data([11, 21, 41, 61, 91, 121, 151], 5, ['q','w']),
            "erosion": prototype.Data([1, 2, 3, 4, 5, 6, 7], 1, ['a','s']),
            "thresholdType": prototype.Data([cv2.THRESH_TOZERO, cv2.THRESH_TOZERO + cv2.THRESH_OTSU, cv2.THRESH_BINARY + cv2.THRESH_OTSU, cv2.THRESH_BINARY], 1, ['z','x']),
            "thresholdValue": prototype.Data([150, 175, 200, 210, 220, 230, 240, 250], 1, ['c','v']),
            "erodeFirst": prototype.Data([False, True], 0, ['d','f']),
        })

    while True:
        model.Dump()
        sketch = processor.processImage(model)
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
