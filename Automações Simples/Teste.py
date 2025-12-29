from random import randint

def Gerador():
    Lista = []
    for c in range(7):
        d = randint(1, 60)
        while d in Lista:
            d = randint(1, 60)
        Lista.append(d)
    print(Lista)

for c in range(1):
    Gerador()
