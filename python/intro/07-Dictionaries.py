#dictionaries en JS sono gli oggetti

#crear

esempioDict = {
    'a' : 3,
    'b' : 0,
    'z' : 34
}


# Accedere a un elemento dentro il dizionario

print (esempioDict ['a'])

#Loop
for elemento in esempioDict:
    print(elemento)

#Item & Values
esempioDict.keys()
esempioDict.Values()

print(esempioDict.ites())

# controllare se esiste
if 3 in esempioDict:
    print('existe')

#aggiungere un elemento
esempioDict['y'] = 16


#eliminare un elemento
del esempioDict ['y']