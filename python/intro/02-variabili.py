#variabili
# la differenza è che python non
#ha bisogno di definire la variabile

x = 300
nome = 'Alessio'

#ci sono due tipi di scope, locale e globali


#Globale
y = 30

# Locale

def myFunc():
    x = 30 #variable locale, esiste solo in questa funzione
    print(x)

    #Il vantaggip è che ci possono essere 
    #due variabile uguale

print(x) #300 questa stampa la variabile globale
myFunc() # 30 questa stampa la variabile dentro la funzione