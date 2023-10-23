from camera import CameraAdapter
from print import PrinterAdapter
import processor

print(f"Taking a photo")
directory = "/home/ama/Pictures/"
c = CameraAdapter()
filename = c.capture(directory)

print(f"Processing {filename}")
outname = "out.png"
image = processor.processImageWithDefaultSettings(directory, filename, outname)

print(f"Wrote {directory}/{outname}")

print(f"Printing {directory}/{outname}")
#commandLine = f"lp -d \"Brother_HL_L2350DW_series\" {outname}"
PrinterAdapter().print(directory, outname)
