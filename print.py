import subprocess

class PrinterAdapter:
    def print(self, path):
        subprocess.call(["lp", "-d", "Brother_HL_L2350DW_series", "-o", "landscape", "-o", "ppi=180", f"{path}"])
