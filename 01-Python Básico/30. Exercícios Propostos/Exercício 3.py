nome = input( 'Digite seu primeiro nome: ' ) 

if '0' in nome:
    print('Como assim você tem números no nome?')
elif '1' in nome:
    print('Como assim você tem números no nome?')
elif '2' in nome:
    print('Como assim você tem números no nome?')
elif '3' in nome:
    print('Como assim você tem números no nome?')
elif '4' in nome:
    print('Como assim você tem números no nome?')
elif '5' in nome:
    print('Como assim você tem números no nome?')
elif '6' in nome:
    print('Como assim você tem números no nome?')
elif '7' in nome:
    print('Como assim você tem números no nome?')
elif '8' in nome:
    print('Como assim você tem números no nome?')
elif '9' in nome:
    print('Como assim você tem números no nome?')
else:
    tamanho = len(nome)
    if tamanho <= 4:
        print( 'Seu nome é curto' )
    elif 5 <= tamanho <=6:
        print( 'Seu nome é normal' )
    elif 6 < tamanho:
        print( 'Seu nome é muito grande' )