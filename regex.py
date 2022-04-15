import re
import pyperclip


txt = str(pyperclip.paste())

phone = r"[+234]" \
        r"[0-9]{13}"
mail = r"[a-zA-Z0-9._%+-]+@[a-zA-Z]+.[a-zA-Z]+"

match_phone = re.findall(phone, txt)
match_mail = re.findall(mail, txt)

print(f"Phone numbers: {match_phone}, Mail: {match_mail}")
