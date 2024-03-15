#/// making text correction with python, using basic modul re and difflib.
import difflib

text = "helew werld"
word = ["hello alip","hello world","hehe saya tamvan", "saya alif", "aku cinta python", "aku benci java script"]

print("Did you means?");data = list(filter(lambda w: int(str(str(difflib.SequenceMatcher(None, text.lower(), w.lower()).ratio()).split(".")[1])[0:1]) >= 4, word));[print(i + 1,". ",x) for i,x in enumerate(data)]
