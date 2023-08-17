"""
Usar estrutura de repetição para criar dois contadores. Um deve contar de maneira progressiva e outro deve contar de maneira regressiva.
"""

contador_prog = 0
contador_regr = 10
while True:
    if contador_regr < 2: break
    print( contador_prog , contador_regr)
    contador_prog += 1
    contador_regr -= 1

    """
    Solução dada no curso:

    for p, r in enumerate(range(10, 1, -1))
        print(p, r)
    """