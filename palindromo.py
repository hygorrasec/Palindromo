'''
Encontre o maior palíndromo, resultado do produto de 2 números com 4 dígitos.
Linguagem utilizada: Python
'''

n1 = palin = 0
while n1 <= 9999:
    n2 = n1
    while n2 <= 9999:
        tmp = str(n1 * n2)
        if tmp == tmp[::-1]:
            if int(tmp) > palin:
                palin = int(tmp)
        n2 += 1
    n1 += 1

print(f'Maior palíndromo encontrado pelo resultado do produto de 2 número com 4 dígitos foi: {palin}')
