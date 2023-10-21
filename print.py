import subprocess

class PrinterAdapter:
    def print(self, filename):
        subprocess.call(["lp", "-d Brother_HL_L2350DW_series", filename])
