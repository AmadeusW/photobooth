import cv2

class Model:
    def __init__(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError("Parameter needs to be a dictionary of raw values or Data for prototyping support")
        self.dictionary = dictionary
    
    def Dump(self):
        print("Model dump:")
        for key, value in self.dictionary.items():
            print(f"Key {key}, Value {value.GetValue()}")

   
    def __getitem__(self, key):
        return self.dictionary[key].GetValue()
    
    def TryNavigate(self, char):
        for key, value in self.dictionary.items():
            if not isinstance(value, Data):
                continue;
            if (value.keyPrevious == char):
                value.SetIndex(value.index - 1)
                print(f"Decrementing {key} to {self[key]}")
                return True
            if (value.keyNext == char):
                value.SetIndex(value.index + 1)
                print(f"Incrementing {key} to {self[key]}")
                return True
        print(f"Unknown gesture {char}")
        return False

class Data:
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

