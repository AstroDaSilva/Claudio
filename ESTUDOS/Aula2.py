with open('text.txt', 'r') as t:
    text = t.read()

def func1(text):
    '''retomar dict 
    dict[char] = quatidade que char aparece em text'''
    chars = []
    for c in text:
        if not c in chars:
            chars.append(c)
    print(chars)

func1(text)