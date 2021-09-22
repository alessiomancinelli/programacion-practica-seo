#Crear listas
listaEsempio = ['pane', 'latte', 'frutta']
#lista di string

#Accedere a un elemento

print(listaEsempio [1])

#rangos
print(listaEsempio[0:2])

#cambiar un elemento
listaEsempio[1] = 'pane'

#loop fare un ciclo
for elemento in listaEsempio: 
    print(elemento)

#controllare se esiste
if 'frutta' in listaEsempio:
    print('Sii esiste')

#largo
print(len(listaEsempio))

#aggiungere elementi alla lista
listaEsempio.append('pianoforte')
print(listaEsempio)

listaEsempio.insert(1, 'Forchette')
print(listaEsempio)

#Eliminare elementi dalla lista
#listaEsempio.remove('Pane')
print(listaEsempio)

del listaEsempio[0]
print(listaEsempio)

#Eliminare una lista

#del lista
print(listaEsempio)

# Svuotare la lista
listaEsempio.clear()
print(listaEsempio)

#unire due liste
otralista = ['macchine', 'ristoranti']

listaNuova = listaEsempio + otralista
print(listaNuova)

