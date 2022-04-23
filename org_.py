import zipfile
import pyinputplus as pyip
from pathlib import Path

inp_file = pyip.inputFilepath("Input path to file you would like to compress:")
# Collects Filepath to file to be compressed

path_to_file = Path(inp_file)

new_file = zipfile.ZipFile("file2zip", "w")  # Creates a writeable zipfile

new_file.write(path_to_file, compress_type= zipfile.ZIP_DEFLATED)
new_file.close()

print(fr"Zipped file is located under {Path.cwd()}")
