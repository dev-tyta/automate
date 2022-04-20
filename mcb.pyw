#! python3
# mcb.pyw - Saves and Loads pieces of text to the clipboard
# How to use: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#             py.exe mcb.pyw <keywords> - Loads keyword to clipboard
#             py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

mcbShelf = shelve.open(r"C:\Users\Testys\Documents\GitHub\automate\mcb_data\mcb")

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[f"{sys.argv[2]}"] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()


