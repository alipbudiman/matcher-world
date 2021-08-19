import difflib

text = "alif budiman"
word = "alif budiman"
ratiomatch = difflib.SequenceMatcher(None, text.lower(), word.lower()).ratio()
print(ratiomatch)