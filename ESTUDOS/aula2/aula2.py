with open('texto.txt', 'r') as t:
    text = t.read()

def func1(text):
    char = []
    for c in text:
        if not c in char:
            char.append(c)
    print(char)

func1(text)