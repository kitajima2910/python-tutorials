s = '    phaM       XuAn    hoaI     '

def toiUu(s):
    s = s.lower().strip()
    strArr = s.split(' ')
    s = ''
    for i in strArr:
        word = i
        if len(word.strip()) != 0:
            s = s + word + ' '
    return  s.strip()

s = toiUu(s)
print(s)