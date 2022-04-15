import re
import pyperclip

text = str(pyperclip.paste())
url = r"[http|https][://]+"

match_url = re.findall(url, text)
