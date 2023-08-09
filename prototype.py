import cv2

class PrototypeModel:
    def __init__(self):
        self.map = {
            "blur": ModelData([11, 21, 41, 61, 91, 121, 151], 5, ['q','w']),
            "erosion": ModelData([1, 2, 3, 4, 5, 6, 7], 1, ['a','s']),
            "thresholdType": ModelData([cv2.THRESH_TOZERO, cv2.THRESH_TOZERO + cv2.THRESH_OTSU, cv2.THRESH_BINARY + cv2.THRESH_OTSU, cv2.THRESH_BINARY], 1, ['z','x']),
            "thresholdValue": ModelData([150, 175, 200, 210, 220, 230, 240, 250], 1, ['c','v']),
            "erodeFirst": ModelData([False, True], 0, ['d','f']),
        }
    
    def Dump(self):
        print("Model dump:")
        for key, value in self.map.items():
            print(f"Key {key}, Value {value.GetValue()}")

    def GetValue(self, key):
        return self.map[key].GetValue()
    
    def TryNavigate(self, char):
        for key, value in self.map.items():
            if (value.keyPrevious == char):
                value.SetIndex(value.index - 1)
                print(f"Decrementing {key} to {self.GetValue(key)}")
                return True
            if (value.keyNext == char):
                value.SetIndex(value.index + 1)
                print(f"Incrementing {key} to {self.GetValue(key)}")
                return True
        print(f"Unknown gesture {char}")
        return False

class ModelData:
    def __init__(self, choices, index, navigationKeys):
        self.choices = choices
        self.index = index
        self.keyPrevious = navigationKeys[0]
        self.keyNext = navigationKeys[1]

    def GetValue(self):
        return self.choices[self.index]

    def SetIndex(self, newIndex):
        maxValue = len(self.choices) - 1
        self.index = max(min(newIndex, maxValue), 0)
        return self.index

model = PrototypeModel()
model.Dump()
print(f"Blur = {model.GetValue('blur')}")