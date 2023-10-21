#from camera import camera
from print import PrinterAdapter
import processor

#print(f"Taking a photo")
#c = camera.CameraAdapter()
#filename = c.capture()

filename = "source/image3.jpg"
outname = "source/out.png"
# TODO: validate if file exists
print(f"Processing {filename}")
image = processor.processImageWithDefaultSettings(filename, outname)

print(f"Wrote {outname}")

print(f"Printing {outname}")
#commandLine = f"lp -d \"Brother_HL_L2350DW_series\" {outname}"
PrinterAdapter().print(outname)
