import picamera

class CameraAdapter:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.vflip = True
        self.camera.contrast = 10
    
    def capture(self, path):
        print(f"Capturing photo to {path}")
        self.camera.capture(f"{path}")
        print(f"Done!")
        return
