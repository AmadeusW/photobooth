import picamera
import time

class CameraAdapter:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1280, 720)
        self.camera.vflip = True
        self.camera.contrast = 10
    
    def capture(self):
        filename = f"/home/ama/Pictures/img{str(time.time())}.jpg"
        print(f"Capturing photo to {filename}")
        time.sleep(1)
        self.camera.capture(filename)
        print(f"Done!")
        return filename
