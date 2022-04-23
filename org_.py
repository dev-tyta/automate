import shutil
import zipfile
from pathlib import Path

path = r"C:\Users\Testys\Documents"
exam_path = path + r"\exam.zip"
example_zip = zipfile.ZipFile(exam_path)
new_zip = zipfile.ZipFile("new_zip", "w")

new_zip.write(exam_path, compress_type= zipfile.ZIP_DEFLATED)
new_zip.close()
