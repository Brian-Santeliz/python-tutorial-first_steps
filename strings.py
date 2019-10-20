name = 'brian leandro'

# print(dir(name))   metodos y propiedas


print(name.upper()) #todo mayuscula
print(name.lower()) #todo minuscula
print(name.swapcase()) #invierte lo que esta en minuscula en mayuscula
print(name.capitalize()) #la primera letra la coloca en mayuscula
print(name.replace('leandro', 'santeliz').upper()) #remplace una letra o palabra, metodos encadenados
print(name.count(' ')) #cuenta las letras 
print(name.startswith('brian')) #empieza con ... busca caracteres y devuelve un booleano
print(name.endswith('leandro')) #termina con ... busca caracteres y devuelve un booleano
print(name.split('n')) #separa o divide el texto basado en las letras o palabras, sino por espacio
print(name.find('leandro')) #busca una letra o palabra y devuelve el indice de su posicion 
print(len(name)) #longitud de una cadena
print(name.index('n')) #busca una letra o palabra y devuelve el indice de su posicion 
print(name.isnumeric()) #verifica si el dato es numerico
print(name.isalpha()) #verifica si el dato es alpha numerico
print(name[1]) #busca una letra en especifico basado en su indice

print(name +' como estas?') #concatetena texto, simepre dejando un espacio blanco al inico
print(name, 'como estas') #concatena sin necesidad del espacio
print(f'como estas {name}?') #dentro del string agrego una variable agregando la f y los "{}"
print('como estas? {0}'.format(name)) #parecidop al anterior pero mas extenso


