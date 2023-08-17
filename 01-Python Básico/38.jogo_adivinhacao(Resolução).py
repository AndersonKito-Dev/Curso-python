#!/usr/bin/env python
"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
SECRETO = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    
    if letra in SECRETO:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
        digitadas.append(letra)
    
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
    
    secreto_temporario = ''
    
    for letra_secreta in SECRETO:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == SECRETO:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    print()
