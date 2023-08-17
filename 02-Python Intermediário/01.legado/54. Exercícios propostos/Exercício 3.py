"""Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex.:10%). Retorne o valor do primeiro número soma do aumento percentual do mesmo."""

def aumento(n1,n2):
    return (((n2/100) + 1) * n1) 
resultado = aumento( int(input('Digite um número: ')) , int(input('Digite outro número: ')) )
print(f'{resultado:.0f}')