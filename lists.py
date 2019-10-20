demoList = [1, 'lista', False, [1,2,3]]
colors = ['green', 'blue', 'red', 'black']

numbersList = list((1, 2,3,4,5,)) #constructor para crear listas


print(numbersList)

ran = list(range(1, 10)) #crear una lista basado en un rango y un constructor.
print(ran)

print(len(colors)) #imprme la longitud de la lista

print(colors[-2])  #obtener elemto de la lista basado en su indice

print('blue' in colors)  #saber si existe un valor en la lista. devuelve un booleano

colors[0] = 'yellow' #remplaza un elemento basado en su indice
print(colors)

print(dir(colors))
colors.append('violet') #agrega un elemento a lista solo uno

colors.extend(('violet', 'yellow')) #agrega varios elementos a una lista, siempre como lista o tupla

colors.extend(('purple', 'white'))
colors.insert(len(colors), 'pink') #inseta un elemento, en el indice que se quiere

print(colors)

colors.pop(0) #elimina el ultimo item y tambien por indice
colors.remove('blue') #elimina un item especifico de la lista
colors.clear() #elimina todos los elementos
colors.sort(reverse = True) #orderna alfabeticamente, reverse lo odena al inverso
print(colors.index('blue')) #busca el indice del elemento
print(colors.count('blue')) # cuenta cuneta veces aparece un elemento
