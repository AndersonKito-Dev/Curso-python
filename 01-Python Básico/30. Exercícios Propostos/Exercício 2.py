hr = input( 'Digite a hora exata (formato 24h): ' )

if hr.isnumeric() : # Outra possibilidade é 'try:'
    hr = int( hr )
    if 24 == hr:
        print('Bom dia')
    elif 1 <= hr <= 11:
        print( 'Bom dia' )
    elif 12 <= hr <= 17:
        print( 'Boa tarde' )
    elif 18 <= hr <= 23:
        print( 'Boa noite' )
    elif hr < 0 or hr > 23:
        print( 'Deve ser entre 0 e 24 horas' )
else:  # Outra possibilidade é 'except:'
    print( 'Não foi possível prosseguir.' )