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
def Converge_a_Verdadeiro_Cpf(string):
    if string == "99999999999":
        raise ValueError("Topo gerado reinicie o gerador")
    """
    Converte a string para uma versão de lista em que se pode sobrepor conteúdo visto que por mais que a linguagem seja
    te deixe um pouco livre ela ainda te prende em uma coisa besta (Eu sei que tem motivo para isso mas, eu ainda odeio)
    """
    conteudo = list(string)
    CPFint = [0] * 11
    indice = 0

    for c in conteudo:
        CPFint[indice] = int(c)
        indice += 1

    while True:
        """
        Valida se o numero possui os 9 primeiros dígitos iguais caso positivo inválida automáticamente (Não encontrei 
        regras que deixe isso explicito porém outros validadores de cpf também não validam e acredito que se trate de
        uma regra descoberta por teste com a receite se alguém souber o por que de forma oficial me avise hehehe)
        """
        Iguais = False
        for c in CPFint[0:10]:
            if c != CPFint[9]:
                Iguais = True

        """Para referencia https://clubes.obmep.org.br/blog/a-matematica-nos-documentos-a-matematica-dos-cpfs/"""
        # Valida primeiro digito
        Primeiro = False
        multi = 10
        primeiro_digito_verificador = 0
        for c in CPFint[0:9]:
            primeiro_digito_verificador += c * multi
            multi -= 1
        resto_da_divisao = primeiro_digito_verificador % 11
        if resto_da_divisao < 2:
            if CPFint[-2] == 0:
                Primeiro = True
        else:
            if CPFint[-2] == 11 - resto_da_divisao:
                Primeiro = True


        # Valida segundo digito
        Segundo = False
        multi = 10
        segundo_digito_verificador = 0
        for c in CPFint[1:10]:
            segundo_digito_verificador += c * multi
            multi -= 1
        resto_da_divisao = segundo_digito_verificador % 11
        if resto_da_divisao < 2:
            if CPFint[-2] == 0:
                Segundo = True
        else:
            if CPFint[-1] == 11 - resto_da_divisao:
                Segundo = True
        if Iguais and Primeiro and Segundo:
            break
        else:
            CPFint = incrementa_int(CPFint)

    indice = 0
    for c in CPFint:
        conteudo[indice] = str(c)
        indice += 1

    return "".join(conteudo)

def Gera_proximo_numero(string):
    conteudo = list(string)
    CPFint = [0] * 11
    indice = 0

    for c in conteudo:
        CPFint[indice] = int(c)
        indice += 1

    CPFint = incrementa_int(CPFint)
    indice = 0
    for c in CPFint:
        conteudo[indice] = str(c)
        indice += 1

    return "".join(conteudo)


def Gera_cpf(Gera_novo=False):
    """
    Gera_novo define se o gerador irá reiniciar no primeiro cpf válido existente.

    O algoritmo valida apenas a consistência matemática do CPF caso o parametro realista seja ligado.
    A existência real do número no nosso mundo depende exclusivamente da base da Receita Federal.
    Quero deixar claro que o cpf pode existir e coincidir com alguma pessoa real, por se tratar de uma validação
    matemática que coincide com a realidade, este dentre todos os geradores é o mais particularmente sensível então tome
    o devido cuidado para não usar os geradores para falsificar informações ou prejudicar alguém me eximo de qualquer
    mau uso desta ferramenta de forma criminosa.
    """
    if Gera_novo == True:
        with open("CPFs", "w") as file:
            conteudo = "00000000000"
            file.write(conteudo)
    else:
        try:
            with open("CPFs", "r") as file:
                conteudo = file.read()
            conteudo = Converge_a_Verdadeiro_Cpf(conteudo)
            CPF = conteudo
            conteudo = Gera_proximo_numero(conteudo)
            with open("CPFs", "w") as file:
                file.write(conteudo)
            print(CPF)

        except:
            with open("CPFs", "w") as file:
                conteudo = "00000000000"
                file.write(conteudo)
                raise ValueError("Arquivo não pré criado, tente novamente, já inclui um novo para você")
for c in range(200):
    Gera_cpf()
