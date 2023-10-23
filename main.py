from camera import camera
from print import PrinterAdapter
import processor

print(f"Taking a photo")
c = camera.CameraAdapter()
filename = c.capture()

print(f"Processing {filename}")
outname = "source/out.png"
image = processor.processImageWithDefaultSettings(filename, outname)

print(f"Wrote {outname}")

print(f"Printing {outname}")
#commandLine = f"lp -d \"Brother_HL_L2350DW_series\" {outname}"
PrinterAdapter().print(outname)
