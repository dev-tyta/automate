def phone_num(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print("Is 415-456-6444 a phone number?")
print(phone_num("415-456-6444"))
print("Is Moshi moshi a phone number?")
print(phone_num("Moshi moshi"))
