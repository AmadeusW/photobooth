import camera
import print

print(f"Taking a photo")
c = camera.CameraAdapter()
filename = c.capture()

print(f"Processing {filename}")


print(f"Printing {filename}")
commandLine = f"lp -d \"Brother_HL_L2350DW_series\" {filename}"
print.PrinterAdapter().print(filename)
