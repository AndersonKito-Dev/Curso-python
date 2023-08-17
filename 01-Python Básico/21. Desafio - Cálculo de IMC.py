import datetime
date = datetime.date.today()
print()
#VARIAVEIS#
nome = str( input( 'Seu nome: ' ) )
idade = int( input( 'Sua idade: ' ) )
peso = str( input( 'Seu peso(Kg): ' ) ).replace( ',','.' ) #TROCA "," POR "."
altura = str( input( 'Sua altura(metros): ' ) ).replace( ',', '.' )  #TROCA "," POR "."
#TRANSFORMAÇOES-1#
peso = float( peso )  
altura = float( altura ) 
#CÁLCULOS#
imc = peso / (altura**2) 
#TRANSFORMAÇÕES-2#
peso = str( peso ).replace( '.', ',' )  
altura = str( altura ).replace( '.', ',' ) #
#CASOS POSSÍVEIS#
if imc<18.5:
    imc = str( imc ).replace( '.', ',' ) #TRANSFORMA O IMC DE "FLOAT" PARA "STR" E TROCA O "." POR ","
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, { altura } metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando: ABAIXO DO PESO.' )
elif 18.5<=imc<=24.9:
    imc = str( imc ).replace( '.', ',' ) 
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, { altura } metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando: PESO NORMAL.' )
elif 25<=imc<=29.9:
    imc = str( imc ).replace( '.', ',' ) 
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, {altura} metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando: SOBREPESO.' )
elif 30<=imc<=34.9:
    imc = str( imc ).replace( '.', ',' ) 
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, { altura } metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando: OBESIDADE DE GRAU I.' )
elif 35<=imc<=39.9:
    imc = str( imc ).replace( '.', ',' ) 
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, { altura } metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando OBESIDADE DE GRAU II.' )
elif 40<=imc:
    imc = str( imc ).replace( '.', ',' ) 
    print( f'{ nome }, nasceu em { date.year - idade } e hoje com { idade } anos, { altura } metros de altura e { peso }Kg, possui um IMC de {imc:.5s}. Indicando OBESIDADE DE GRAU III ou MÓRBIDA.' )