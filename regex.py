import re
import pyperclip


txt = pyperclip.paste()
phone = r"[+234][0-9]{13}"
mail = r"[a-zA-Z0-9]*@[a-zA-Z]*.[a-zA-Z]*"
mail_org = r"[a-zA-Z0-9\s]*@[a-zA-Z]*.[a-zA-Z]*.[edu|org|io]"
match_phone = re.findall(phone, txt)
match_mail = re.findall(mail, txt)
match_org = re.findall(mail_org, txt)

print(f"Phone numbers: {match_phone}, Mail: {match_mail}, School mail : {match_org}")
