from time import sleep

def incrementa_int(array):
    array[-1] += 1
    while True:
        if 10 in array:
            indice = array.index(10)
            array[indice] = 0
            array[indice-1] += 1
        if 10 not in array:
            break
    return array

def ValidaCpf(string):
    if string == "99999999999":
        raise ValueError("Topo gerado reinicie o gerador")
    conteudo = list(string)
    CPFint = [0] * 11
    indice = 0
    for c in conteudo:
        CPFint[indice] = int(c)
        indice += 1
    while True:
        #Valida se todos os números são iguais
        sair = False
        while True:
            if sair == False:
                for c in CPFint:
                    #checa até o ultimo digito:
                    if c != CPFint[-1]:
                        sair = True
                        break
            elif sair:
                break
            CPFint = incrementa_int(CPFint)
        if sair == True:
            break
        #Valida primeiro digito
        while True:
            sair = False
            multi = 10
            primeiro_digito_verificador = 0
            for c in CPFint[0:9]:
                primeiro_digito_verificador += c*multi
                multi -=1
            resto_da_divisao = primeiro_digito_verificador%11
            if resto_da_divisao < 2:
                if CPFint[-2] == 0:
                    break
            else:
                if CPFint[-2] == 11-resto_da_divisao:
                    break
                CPFint = incrementa_int(CPFint)
                sair = True
                break
        if sair == True:
            continue
        #Valida segundo digito
        while True:
            multi = 11
            segundo_digito_verificador = 0
            for c in CPFint[0:10]:
                segundo_digito_verificador += c*multi
                multi -=1
            resto_da_divisao = segundo_digito_verificador%11
            if resto_da_divisao < 2:
                if CPFint[-2] == 0:
                    return CPFint
            else:
                if CPFint[-1] == 11-resto_da_divisao:
                    return CPFint
            CPFint[-1] += 1
            break
    indice = 0
    for c in CPFint:
        conteudo[indice] = str(c)
        indice += 1

    return "".join(conteudo)

def Gerando_cpf(Gera_novo=None):
    if Gera_novo == True:
        with open("CPFs", "w") as file:
            conteudo = "00000000000"
            file.write(conteudo)
    else:
        try:
            with open("CPFs", "r") as file:
                conteudo = file.read()
                print(conteudo)
                sleep(2)
            conteudo = ValidaCpf(conteudo)
            with open("CPFs", "w") as file:
                print(conteudo)
                sleep(2)
                file.write(conteudo)
        except:
            with open("CPFs", "w") as file:
                conteudo = "00000000000"
                file.write(conteudo)
                raise ValueError("Arquivo não pré criado, tente novamente, já inclui um novo para você")
