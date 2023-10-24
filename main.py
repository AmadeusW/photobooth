from camera import CameraAdapter
from print import PrinterAdapter
import processor
import time

directory = "/home/ama/Pictures"
currentTime = time.strftime("%Y%m%dT%H%M%S");
input = f"img{currentTime}.jpg"
output = f"out{currentTime}.jpg"
inputPath = f"{directory}/{input}";
outputPath = f"{directory}/{output}";

print(f"Photobooth @ {currentTime}")
print(f"Taking a photo")
c = CameraAdapter()
filename = c.capture(inputPath)

print(f"Processing {inputPath}")
image = processor.processImageWithDefaultSettings(inputPath, outputPath)

print(f"Printing {outputPath}")
PrinterAdapter().print(outputPath)
