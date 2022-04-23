import shutil
import zipfile
from pathlib import Path

# shutil.move(r".\mcb_data\mydata.dat", r".\capital")
path = r"C:\Users\Testys\Documents"

example_zip = zipfile.ZipFile(path + r"\exam.zip")
print(example_zip.namelist())
