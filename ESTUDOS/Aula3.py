'''a = (i for i in range(600_000_000))

for i in a:
    print(i)
    break'''

def a():
    n = 0
    while True:
        n += 1
        yield n

for i in a():
    print(i)