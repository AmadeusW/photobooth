import subprocess

class PrinterAdapter:
    def print(self, directory, filename):
        subprocess.call(["lp", f"-d Brother_HL_L2350DW_series {directory}/{filename}"])
