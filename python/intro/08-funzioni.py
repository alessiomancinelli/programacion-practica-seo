#dichiarara una funzione
def fnEsempio(args):
    #qui la logica
    return

def sum(a,b):
    return a + b

#built-in functions
#print()
#len()

#eseguire una funzione

#print(sum(1, 2))

# Default parameter
#def sum(a,b=2):

#args
def sumAll(*args):
    for i in args:
        print(i)

print(sumAll(1,2,3,4))

#**kwargs
def esempio (**kwargs):
    print(kwargs)

print(esempio(a=1, b=4, z=34))

#Lambda