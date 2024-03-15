#/// making text correction with python, using basic modul re and difflib.
import difflib

def matchword(text:str, *word:str) -> str:
    ret = ["Did you means?"];data = list(filter(lambda w: int(str(str(difflib.SequenceMatcher(None, text.lower(), w.lower()).ratio()).split(".")[1])[0:1]) >= 4, word));[ret.append(f"{i+1}. {x}") for i,x in enumerate(data)];return ret

data = matchword("helew werld", "hello alip","hello world","hehe saya tamvan", "saya alif", "aku cinta python", "aku benci java script")
[print(x) for x in data]
