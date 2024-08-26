'''a = 1
while a <= 10:
    print(a)
    a += 1

for i in range(1, 11):
    print(i)'''

a = 'udsuchuhuw uw6tysis'

for letras in a:
    print(letras)

nomes = ['maria', 'joao', 'roberto']
idades = [10, 30, 40]

for nomes, idades in zip(nomes, idades):
    print(f'{nomes} tem {idades} anos')