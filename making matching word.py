#/// making text correction with python, using basic modul re and difflib.
import re, difflib

text = "helew werld"
word = [
    "hello alip",
    "hello world",
    "hehe saya tamvan",
    ]
ret = "Did you means?"
cnt = 0
data = []
for x in word:
    ratiomatch = difflib.SequenceMatcher(None, text.lower(), x.lower()).ratio()
    #/// making some ratio for presentation match
    cnt += 1
    #/// you need to add count for mapping word data
    rm = str(forratio).split(".")[1]
    if int(rm[0:1]) >= 4: #>> 1-9
    #/// if ratio > 0.6, it means presentation of match is more than 60%
    #/// bcoz if ratio == 1.0 its mean 100%
    #/// simple test below:
        #text = "alif budiman"
        #import difflib
        #text = "alif budiman"
        #word = "alif budiman"
        #ratiomatch = difflib.SequenceMatcher(None, text.lower(), word.lower()).ratio()
        #print(ratiomatch)
        result = re.match(word[cnt-1], x.lower())
        #/// matching with module re.match
        if result:
        #/// if result make some data, back to Bool True
            data.append(word[cnt-1])
if data != []:
    no = 0
    #/// if data not empty, it means mechine has get match word
    for y in data:
        no += 1
        ret += f"\n{no}. {y}"
        #/// adding match word to comment
    print(ret)
    #/// print you ratio
else:
    print(f"{text} not in list data")
