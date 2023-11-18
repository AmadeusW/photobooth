import picamera

class CameraAdapter:

    def capture(path):
        camera = picamera.PiCamera()

        try:
            camera.resolution = (1280, 720)
            camera.vflip = True
            camera.contrast = 10

            print(f"Capturing photo to {path}")
            camera.capture(f"{path}")
            print(f"Done!")

        finally:
            camera.close()
