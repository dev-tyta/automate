import re
import pyperclip

text = str(pyperclip.paste())
url = r"(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+"

match_url = re.findall(url, text)
print(match_url)
urls = []
for ur in match_url:
    urls.append(ur)

if len(urls) > 0:
    pyperclip.copy('\n'.join(urls))
    print('Copied to clipboard:')
    print('\n'.join(urls))
else:
    print('No Url addresses found.')
