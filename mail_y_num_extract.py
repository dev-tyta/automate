import re
import pyperclip


txt = str(pyperclip.paste())

phone = r"[+234]" \
        r"[0-9]{13}"
mail = r"[a-zA-Z0-9._%+-]+@[a-zA-Z.]+"

match_phone = re.findall(phone, txt)
match_mail = re.findall(mail, txt)

matches = []
for num in match_phone:
    matches.append(num)
for mails in match_mail:
    matches.append(mails)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
