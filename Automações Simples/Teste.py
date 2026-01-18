from time import sleep


def ValidaCpf(string):
    conteudo = list(string)
    CPFint = [0] * 11
    indice = 0
    for c in conteudo:
        CPFint[indice] = int(c)
        indice += 1

    while True:
        for c in range(11):
            if CPFint[0] == CPFint[c]:

                #################################################################################


    indice = 0
    for c in CPFint:
        conteudo[indice] = str(c)
        indice += 1
    return "".join(conteudo)

def Gerando_cpf(Gera_novo=None):
    if Gera_novo == True:
        with open("CPFs", "w") as file:
            conteudo = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4']
            file.write(conteudo)
    else:
        while(True):

            with open("CPFs", "r") as file:
                conteudo = file.read()


            conteudo = ValidaCpf(conteudo)


            with open("CPFs", "w") as file:
                file.write(conteudo)
            break
    print(conteudo)

for c in range(3):
    Gerando_cpf()
