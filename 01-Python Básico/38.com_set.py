letras = set()
palavra_secreta = set('perfume')

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if letra in palavra_secreta:
        print('PARABÉNS')
        print('A palavra secreta está assim:')

        secreto_temporario = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'
        print(secreto_temporario)

        break

    print(letras)
