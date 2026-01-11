import pyautogui
import winsound
import time
from random import randint, choice
import pyperclip


def NomeCompleto():
    """
    Retorna uma grande variação de nomes de ordem de grandeza alta na casa de trilhões então não se preocupe com
    Variedade.
    Embora o paradoxo do aniversário diminua o sonho de não haver colisões,
    acredito que ainda temos uma quantidade satisfatória:
    Aproximadamente 15.397.758.879.412 de combinações
    Probabilidade de colisão	Quantidade de nomes gerados
    25%	~                       2,6 milhões
    50%	~                       4,4 milhões
    75%	~                       6,2 milhões
    100% (praticamente certa)	18 milhões

    """
    PrimeiroNome = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
                    'Karina', 'Lucas', 'Mariana', 'Nicolas', 'Olívia', 'Paulo', 'Quésia', 'Rafael', 'Sofia', 'Thiago',
                    'Ursula', 'Victor', 'Wagner', 'Ximena', 'Yara', 'Zeca', 'Amanda', 'Bianca', 'Caio', 'Diego',
                    'Elaine',
                    'Fabiana', 'Gustavo',
                    'Hugo', 'Isabela', 'João', 'Kelly', 'Leonardo', 'Marta', 'Natália', 'Otávio', 'Patrícia', 'Quirino',
                    'Renata',
                    'Samuel', 'Tatiane', 'Ulisses', 'Valéria', 'William', 'Xavier', 'Yasmin', 'Zuleica', 'Alberto',
                    'Beatriz',
                    'Cristiano', 'Denise', 'Emerson', 'Flávia', 'Giovana', 'Henrique', 'Ingrid', 'José', 'Kátia',
                    'Larissa',
                    'Mateus', 'Nicole', 'Orlando', 'Priscila', 'Queila', 'Roberto', 'Simone', 'Talita', 'Ubirajara',
                    'Vânia',
                    'Wellington', 'Xisto', 'Yuri', 'Zilda', 'Arthur', 'Bruna', 'Cecília', 'Davi', 'Estela', 'Felipe',
                    'Heitor',
                    'Isabel', 'Jonas', 'Kamila', 'Luana', 'Marcelo', 'Noemi', 'Pedro', 'Quintino', 'Rogério', 'Sandra',
                    'Tereza',
                    'Vicente', 'Wesley', 'Zion', 'Alice', 'Camila', 'Daniel', 'Kevin', 'Marcos', 'Rafaela', 'Tatiana',
                    'Vanessa',
                    'André', 'Débora', 'Elias', 'Heloísa', 'Jéssica', 'Mônica', 'Natan', 'Vitor', 'Xuxa', 'Zélia',
                    'Maria',
                    'Antônio', 'Francisco', 'Luís', 'Rita', 'Sérgio', 'Cláudia', 'Carla', 'Silvia', 'Renato', 'Marcio',
                    'Eliane',
                    'Ricardo', 'Aline', 'Paula', 'Michele', 'Gisele']
    SegundoNome = [
        "José", "Maria", "Antônio", "Francisco", "Luís", "Paulo", "Rita", "Sérgio", "Cláudia", "Marta",
        "Fernanda", "Roberto", "Carla", "Eduardo", "Simone", "Carlos", "Silvia", "Gustavo", "Beatriz",
        "Renato", "Patrícia", "Marcio", "Eliane", "Valéria", "Henrique", "Tereza", "Ricardo", "Aline", "Paula",
        "Michele", "Victor", "Juliana", "Luana", "Eduardo", "Gisele", "Henrique", "Tatiana", "Daniel", "Fabiana"
    ]
    Sobrenome = [
        "Silva", "Souza", "Oliveira", "Pereira", "Lima", "Gonçalves", "Rodrigues", "Almeida", "Costa", "Martins",
        "Ferreira", "Ribeiro", "Barros", "Pinto", "Maciel", "Santana", "Carvalho", "Fonseca", "Melo", "Martins",
        "Gomes", "Nogueira", "Cunha", "Teixeira", "Castro", "Bueno", "Dias", "Macedo", "Lopes", "Faria",
        "Barbosa", "Santos", "Vieira", "Azevedo", "Paz", "Vasconcelos", "Moraes", "Pereira", "Cavalcante", "Siqueira",
        "Tavares"
    ]
    Probabilidade = randint(1, 100)
    Tamanho = 0
    Partes = []
    # 5% Tem mais de 3 Nomes, 20% tem 3 Nomes, 25% tem 2 nomes, 50% tem 1 nome
    if 1 <= Probabilidade <= 5:
        Tamanho = randint(4, 7)
    elif 6 <= Probabilidade <= 25:
        Tamanho = 3
    elif 26 <= Probabilidade <= 50:
        Tamanho = 2
    elif Probabilidade > 50:
        Tamanho = 1
    if Tamanho == 1:
        Partes.append(choice(PrimeiroNome))
        Partes.append(choice(Sobrenome))
        Nome = " ".join(Partes)
        return Nome
    elif Tamanho == 2:
        Partes.append(choice(PrimeiroNome))
        Partes.append(choice(SegundoNome))
        Partes.append(choice(Sobrenome))
        Nome = " ".join(Partes)
        return Nome
    elif Tamanho == 3:
        Partes.append(choice(PrimeiroNome))
        Partes.append(choice(SegundoNome))
        Nome3 = choice(SegundoNome)
        while Nome3 in Partes:
            Nome3 = choice(SegundoNome)
        Partes.append(Nome3)
        Partes.append(choice(Sobrenome))
        Nome = " ".join(Partes)
        return Nome
    elif Tamanho >= 4:
        while Tamanho >= 1:
            if not Partes:
                Partes.append(choice(PrimeiroNome))
                Tamanho -= 1
                continue
            Segundos = choice(SegundoNome)
            if Segundos in Partes:
                continue
            Tamanho -= 1
            Partes.append(Segundos)
        Partes.append(choice(Sobrenome))
        Nome = " ".join(Partes)
        return Nome


def NomedeRua():
    """
    Categoria	                                Probabilidade
    Homenagens a Pessoas	                    35%
    Geográficos	                                30%
    Árvores/Plantas/Flores	                    15%
    Animais	                                    5%
    Objetos/Ocorrências / Ocupações	            5%
    Temáticos (cores, minerais, elementos)	    5%
    Conceituais	                                5%
    Returns:
    """
    Probabilidade = randint(1, 100)
    Nome_da_rua = []
    Probtipologradouro = randint(1, 100)
    # Definindo qual o genêro caso a rua seja nome de Pessoas
    Genero = choice(["Masculino", "Feminino"])
    if 1 <= Probtipologradouro <= 80:
        TipoLogradouro = ["Rua", "Avenida"]
    else:
        TipoLogradouro = ["Travessa", "Alameda", "Estrada", "Rodovia", "Viela",
                          "Largo", "Praça", "Caminho", "Beco", "Passeio", "Viaduto", "Marginal",
                          "Ladeira", "Ciclovia", "Parque", "Boulevard", "Corredor", "Esplanada"
                          ]
    if 1 <= Probabilidade <= 35:
        """
        Homenagens a Pessoas	                    35%
            Destes 75% são Homenagens a Pessoas
            O restante de 25% é de Santos
        """
        Probabilidade = randint(1, 100)
        if 1 <= Probabilidade <= 75:
            """
            Homenagens a Pessoas
            """
            Probabilidade = randint(1, 100)

            if Genero == "Masculino":
                Prefixo = [
                    "Dom", "Prof.", "Dr.", "Pe.", "General",
                    "Capitão", "Coronel", "Marechal", "Comendador"
                ]
                NomeHomenagem = ["Getúlio Vargas", "Oswaldo Cruz", "Tiradentes", "Machado de Assis",
                                 "Rui Barbosa", "Castro Alves", "Carlos Gomes",
                                 "Heitor Villa-Lobos", "Carlos Drummond", "JK",
                                 "Zumbi dos Palmares", "Pelé", "Ayrton Senna", "Nelson Mandela",
                                 "Albert Einstein", "João Pessoa", "Santos Dumont",
                                 "Barão de Mauá", "José do Patrocínio",
                                 "Antonio Conselheiro", "Manoel Bandeira", "Gilberto Freyre", "Vital Brasil",
                                 "Paulo Freire", "Mário de Andrade"
                                 ]
                Sufixo = [
                    "Filho", "Neto", "Júnior", "Sobrinho", "Segundo", "Terceiro"
                ]
                Nome_da_rua.append(choice(TipoLogradouro))
                Proprefix = randint(1, 100)
                if 1 <= Proprefix <= 30:
                    Nome_da_rua.append(choice(Prefixo))
                Nome_da_rua.append(choice(NomeHomenagem))
                Prosufix = randint(1, 100)
                if 1 <= Prosufix <= 30:
                    Nome_da_rua.append(choice(Sufixo))
                Nome_da_rua = " ".join(Nome_da_rua)
                return Nome_da_rua
            elif Genero == "Feminino":
                Prefixo = [
                    "Dona", "Irmã", "Madre"
                ]
                NomeHomenagem = ["Chiquinha Gonzaga", "Clarice Lispector", "Maria Quitéria", "Anita Garibaldi",
                                 "Dona Ivone Lara", "Zilda Arns", "Lélia Gonzalez", "Nise da Silveira",
                                 "Malala Yousafzai", "Rosa Parks", "Frida Kahlo", "Carmen Miranda",
                                 "Tarsila do Amaral", "Rachel de Queiroz", "Zuzu Angel",
                                 "Beth Goulart", "Elis Regina", "Maria Bethânia", "Gal Costa", "Rita Lee"
                                 ]
                Nome_da_rua.append(choice(TipoLogradouro))
                Prosufix = randint(1, 100)
                if 1 <= Prosufix <= 30:
                    Nome_da_rua.append(choice(Prefixo))
                Nome_da_rua.append(choice(NomeHomenagem))
                Nome_da_rua = " ".join(Nome_da_rua)
                return Nome_da_rua
        elif 76 <= Probabilidade <= 100:
            """
                Santos
            """
            if Genero == "Masculino":
                PrefixoSantos = ["São", "Santo"]
                NomesSantos = ["Pedro", "Paulo", "João", "Tiago", "Mateus", "Marcos", "Lucas", "José", "Bento",
                               "Francisco", "Jorge", "Sebastião", "Cristóvão", "Lázaro", "Domingos", "Nicolau",
                               "Caetano", "Roque", "Vicente", "Tomé", "Bartolomeu", "Filipe", "Simão", "Judas Tadeu",
                               "Agostinho", "Jerônimo", "Martinho", "Gabriel", "Miguel", "Rafael", "Expedito",
                               "Antônio", "Alberto", "Amaro", "Afonso", "Inácio", "André"]
                Nome_da_rua.append(choice(TipoLogradouro))
                Nome_da_rua.append(choice(PrefixoSantos))
                Nome_da_rua.append(choice(NomesSantos))
                Nome_da_rua = " ".join(Nome_da_rua)
                return Nome_da_rua
            elif Genero == "Feminino":
                PrefixoSantos = [
                    "Dona", "Irmã", "Madre", "Santa"
                ]
                NomesSantos = ["Maria", "Rita", "Luzia", "Teresa", "Catarina", "Cecília", "Helena", "Clara", "Ana",
                               "Bárbara", "Bernadete", "Isabel", "Paulina", "Faustina", "Filomena", "Margarida",
                               "Delfina", "Natália", "Edwiges", "Cristina", "Dolores", "Apolônia", "Verônica"
                               ]
                Nome_da_rua.append(choice(TipoLogradouro))
                Nome_da_rua.append(choice(PrefixoSantos))
                Nome_da_rua.append(choice(NomesSantos))
                Nome_da_rua = " ".join(Nome_da_rua)
                return Nome_da_rua
    elif 36 <= Probabilidade <= 65:
        """
        Geográficos	                                30%
        """
        Geo = [
            "Amazonas", "Pernambuco", "Pará", "Ceará", "Bahia", "Minas Gerais",
            "Rio Branco", "Acre", "Ipanema", "Copacabana", "Leblon", "Botafogo",
            "Mooca", "Ipiranga", "Bangu", "Cambuci", "Paraíba", "Xingu", "Solimões",
            "Tocantins", "Amapá", "Guanabara", "Pinheiros", "Itapura", "Jabaquara",
            "Santana", "Butantã", "Liberdade", "Perdizes"
        ]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Geo))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua
    elif 66 <= Probabilidade <= 80:
        """
        Árvores/Plantas/Flores	                    15%
        """
        Arvores_Plantas_Flores = ["Ipê", "Jequitibá", "Jacarandá", "Araucária", "Cedro", "Mogno",
                                  "Angico", "Pau-Brasil", "Figueira", "Oitizeiro", "Sândalo", "Samambaia",
                                  "Aloe Vera", "Bromélia", "Cacto", "Suculenta", "Espada-de-São-Jorge", "Jiboia",
                                  "Hera", "Costela-de-Adão", "Antúrio", "Lírio-da-Paz", "Begônia", "Cróton", "Hortelã",
                                  "Manjericão", "Alecrim", "Lavanda", "Tomilho", "Arruda", "Capim-limão", "Gergelim",
                                  "Hibisco", "Amor-Perfeito", "Calêndula", "Crisântemo", "Sálvia", "Erva-do-Gato",
                                  "Rúcula", "Alface", "Espinafre", "Orégano", "Pimenteira", "Alecrim-do-Campo",
                                  "Dente-de-Leão", "Guaraná", "Erva-Mate", "Carqueja", "Jasmim-Manga", "Ipoméia",
                                  "Rosa", "Violeta", "Jasmim", "Magnólia", "Orquídea", "Hortênsia",
                                  "Azaleia", "Girassol", "Lótus", "Lavanda"]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Arvores_Plantas_Flores))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua
    elif 81 <= Probabilidade <= 85:
        """
        Animais	                                    5%
        """
        Animais = [
            "Andorinhas", "Araras", "Beija-Flores", "Borboletas", "Caititus", "Camaleões",
            "Cavalos", "Corujas", "Gaviões", "Garças", "Gatos", "Gralhas", "Jacarés",
            "Japins", "Jurus", "Lobos", "Lontras", "Macacos", "Onças", "Pardais",
            "Pavões", "Pica-Paus", "Pombas", "Quatis", "Raposas", "Sabias", "Saracuras",
            "Tamanduás", "Tartarugas", "Tucanos", "Urubus"
        ]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Animais))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua
    elif 86 <= Probabilidade <= 90:
        """
        Objetos/ Ocupações	            5%
        """
        Objetos_Ocupacoes = [
            "da Pedra", "das Pedras", "da Colina", "das Colinas", "da Fonte", "das Fontes",
            "do Sino", "dos Sinos", "da Serra", "das Serras", "do Lago", "dos Lagos", "da Ponte", "das Pontes",
            "do Moinho", "dos Moinhos", "da Torre", "das Torres", "do Castelo", "dos Castelos", "da Chave",
            "das Chaves", "do Martelo", "dos Martelos", "da Lança", "das Lanças", "da Forja", "das Forjas",
            "da Ferradura", "das Ferraduras", "da Âncora", "das Âncoras", "da Lamparina", "das Lamparinas",
            "da Estrela", "das Estrelas", "da Concha", "das Conchas", "dos Ferreiros", "dos Carpinteiros",
            "dos Padeiros", "dos Ceramistas", "dos Ourives", "dos Porteiros", "dos Agricultores", "dos Oleiros",
            "dos Tecelões", "dos Tanoeiros", "dos Ciclistas", "dos Navegadores", "dos Marinheiros",
            "dos Pescadores", "dos Guias", "dos Artistas", "dos Músicos", "dos Poetas", "dos Escribas", "dos Astrônomos"
        ]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Objetos_Ocupacoes))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua
    elif 91 <= Probabilidade <= 95:
        """
        Temáticos (cores, minerais, elementos)	    5%
        """
        Tematicos = [
            "Vermelho", "Azul", "Amarelo", "Verde", "Branco", "Preto",
            "Cinza", "Violeta", "Laranja", "Rosa",
            "Ouro", "Prata", "Bronze", "Cobre", "Granito", "Mármore",
            "Ferro", "Aço", "Quartzo", "Cristal",
            "Hidrogênio", "Hélio", "Carbono", "Oxigênio", "Nitrogênio"
        ]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Tematicos))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua
    elif 96 <= Probabilidade <= 100:
        """
        Conceituais	                                5%
        """
        Conceituais = [
            "Paz", "Esperança", "União", "Igualdade", "Justiça", "Liberdade",
            "Fraternidade", "Progresso", "Vitória", "Independência", "Renovação",
            "Sabedoria", "Harmonia", "Fortaleza", "Coragem", "Gratidão",
            "Caridade", "Benevolência", "Firmeza", "Amizade", "Lealdade",
            "Tranquilidade", "Clareza", "Honra", "Glória", "Virtude",
            "Concordia", "Bonança", "Prosperidade", "Dignidade",
            "Esperança Nova", "Novo Amanhecer", "Alvorada", "Aurora",
            "Horizonte", "Luz", "Brilho", "Estrela", "Sol", "Lua"
        ]
        Nome_da_rua.append(choice(TipoLogradouro))
        Nome_da_rua.append(choice(Conceituais))
        Nome_da_rua = " ".join(Nome_da_rua)
        return Nome_da_rua

def NomedoBairro():
    """
    Categoria	                                Probabilidade
    Homenagens a Pessoas	                    35%
    Geográficos	                                30%
    Árvores/Plantas/Flores	                    15%
    Animais	                                    5%
    Objetos/Ocorrências / Ocupações	            5%
    Temáticos (cores, minerais, elementos)	    5%
    Conceituais	                                5%
    Returns:
    """
    Probabilidade = randint(1, 100)
    Nome_de_bairro = []
    Probab_tipo = randint(1, 100)
    Genero = choice(["Masculino", "Feminino"])
    if 1 <= Probab_tipo <= 80:
        TipodeConjunto = ["Bairro"]
    else:
        TipodeConjunto = ["Conjunto habitacional", "Condomínio"]
    if 1 <= Probabilidade <= 35:
        """
        Homenagens a Pessoas	                    35%
            Destes 75% são Homenagens a Pessoas
            O restante de 25% é de Santos
        """
        Probabilidade = randint(1, 100)
        if 1 <= Probabilidade <= 75:
            """
            Homenagens a Pessoas
            """
            Probabilidade = randint(1, 100)

            if Genero == "Masculino":
                Prefixo = [
                    "Dom", "Prof.", "Dr.", "Pe.", "General",
                    "Capitão", "Coronel", "Marechal", "Comendador"
                ]
                NomeHomenagem = ["Getúlio Vargas", "Oswaldo Cruz", "Tiradentes", "Machado de Assis",
                                 "Rui Barbosa", "Castro Alves", "Carlos Gomes",
                                 "Heitor Villa-Lobos", "Carlos Drummond", "JK",
                                 "Zumbi dos Palmares", "Pelé", "Ayrton Senna", "Nelson Mandela",
                                 "Albert Einstein", "João Pessoa", "Santos Dumont",
                                 "Barão de Mauá", "José do Patrocínio",
                                 "Antonio Conselheiro", "Manoel Bandeira", "Gilberto Freyre", "Vital Brasil",
                                 "Paulo Freire", "Mário de Andrade"
                                 ]
                Sufixo = [
                    "Filho", "Neto", "Júnior", "Sobrinho", "Segundo", "Terceiro"
                ]
                Nome_de_bairro.append(choice(TipodeConjunto))
                Proprefix = randint(1, 100)
                if 1 <= Proprefix <= 30:
                    Nome_de_bairro.append(choice(Prefixo))
                Nome_de_bairro.append(choice(NomeHomenagem))
                Prosufix = randint(1, 100)
                if 1 <= Prosufix <= 30:
                    Nome_de_bairro.append(choice(Sufixo))
                Nome_de_bairro = " ".join(Nome_de_bairro)
                return Nome_de_bairro
            elif Genero == "Feminino":
                Prefixo = [
                    "Dona", "Irmã", "Madre"
                ]
                NomeHomenagem = ["Chiquinha Gonzaga", "Clarice Lispector", "Maria Quitéria", "Anita Garibaldi",
                                 "Dona Ivone Lara", "Zilda Arns", "Lélia Gonzalez", "Nise da Silveira",
                                 "Malala Yousafzai", "Rosa Parks", "Frida Kahlo", "Carmen Miranda",
                                 "Tarsila do Amaral", "Rachel de Queiroz", "Zuzu Angel",
                                 "Beth Goulart", "Elis Regina", "Maria Bethânia", "Gal Costa", "Rita Lee"
                                 ]
                Nome_de_bairro.append(choice(TipodeConjunto))
                Prosufix = randint(1, 100)
                if 1 <= Prosufix <= 30:
                    Nome_de_bairro.append(choice(Prefixo))
                Nome_de_bairro.append(choice(NomeHomenagem))
                Nome_de_bairro = " ".join(Nome_de_bairro)
                return Nome_de_bairro
        elif 76 <= Probabilidade <= 100:
            """
                Santos
            """
            if Genero == "Masculino":
                PrefixoSantos = ["São", "Santo"]
                NomesSantos = ["Pedro", "Paulo", "João", "Tiago", "Mateus", "Marcos", "Lucas", "José", "Bento",
                               "Francisco", "Jorge", "Sebastião", "Cristóvão", "Lázaro", "Domingos", "Nicolau",
                               "Caetano", "Roque", "Vicente", "Tomé", "Bartolomeu", "Filipe", "Simão", "Judas Tadeu",
                               "Agostinho", "Jerônimo", "Martinho", "Gabriel", "Miguel", "Rafael", "Expedito",
                               "Antônio", "Alberto", "Amaro", "Afonso", "Inácio", "André"]
                Nome_de_bairro.append(choice(TipodeConjunto))
                Nome_de_bairro.append(choice(PrefixoSantos))
                Nome_de_bairro.append(choice(NomesSantos))
                Nome_de_bairro = " ".join(Nome_de_bairro)
                return Nome_de_bairro
            elif Genero == "Feminino":
                PrefixoSantos = [
                    "Dona", "Irmã", "Madre", "Santa"
                ]
                NomesSantos = ["Maria", "Rita", "Luzia", "Teresa", "Catarina", "Cecília", "Helena", "Clara", "Ana",
                               "Bárbara", "Bernadete", "Isabel", "Paulina", "Faustina", "Filomena", "Margarida",
                               "Delfina", "Natália", "Edwiges", "Cristina", "Dolores", "Apolônia", "Verônica"
                               ]
                Nome_de_bairro.append(choice(TipodeConjunto))
                Nome_de_bairro.append(choice(PrefixoSantos))
                Nome_de_bairro.append(choice(NomesSantos))
                Nome_de_bairro = " ".join(Nome_de_bairro)
                return Nome_de_bairro
    elif 36 <= Probabilidade <= 65:
        """
        Geográficos	                                30%
        """
        Geo = [
            "Amazonas", "Pernambuco", "Pará", "Ceará", "Bahia", "Minas Gerais",
            "Rio Branco", "Acre", "Ipanema", "Copacabana", "Leblon", "Botafogo",
            "Mooca", "Ipiranga", "Bangu", "Cambuci", "Paraíba", "Xingu", "Solimões",
            "Tocantins", "Amapá", "Guanabara", "Pinheiros", "Itapura", "Jabaquara",
            "Santana", "Butantã", "Liberdade", "Perdizes"
        ]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Geo))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro
    elif 66 <= Probabilidade <= 80:
        """
        Árvores/Plantas/Flores	                    15%
        """
        Arvores_Plantas_Flores = ["Ipê", "Jequitibá", "Jacarandá", "Araucária", "Cedro", "Mogno",
                                  "Angico", "Pau-Brasil", "Figueira", "Oitizeiro", "Sândalo", "Samambaia",
                                  "Aloe Vera", "Bromélia", "Cacto", "Suculenta", "Espada-de-São-Jorge", "Jiboia",
                                  "Hera", "Costela-de-Adão", "Antúrio", "Lírio-da-Paz", "Begônia", "Cróton", "Hortelã",
                                  "Manjericão", "Alecrim", "Lavanda", "Tomilho", "Arruda", "Capim-limão", "Gergelim",
                                  "Hibisco", "Amor-Perfeito", "Calêndula", "Crisântemo", "Sálvia", "Erva-do-Gato",
                                  "Rúcula", "Alface", "Espinafre", "Orégano", "Pimenteira", "Alecrim-do-Campo",
                                  "Dente-de-Leão", "Guaraná", "Erva-Mate", "Carqueja", "Jasmim-Manga", "Ipoméia",
                                  "Rosa", "Violeta", "Jasmim", "Magnólia", "Orquídea", "Hortênsia",
                                  "Azaleia", "Girassol", "Lótus", "Lavanda"]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Arvores_Plantas_Flores))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro
    elif 81 <= Probabilidade <= 85:
        """
        Animais	                                    5%
        """
        Animais = [
            "Andorinhas", "Araras", "Beija-Flores", "Borboletas", "Caititus", "Camaleões",
            "Cavalos", "Corujas", "Gaviões", "Garças", "Gatos", "Gralhas", "Jacarés",
            "Japins", "Jurus", "Lobos", "Lontras", "Macacos", "Onças", "Pardais",
            "Pavões", "Pica-Paus", "Pombas", "Quatis", "Raposas", "Sabias", "Saracuras",
            "Tamanduás", "Tartarugas", "Tucanos", "Urubus"
        ]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Animais))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro
    elif 86 <= Probabilidade <= 90:
        """
        Objetos/ Ocupações	            5%
        """
        Objetos_Ocupacoes = [
            "da Pedra", "das Pedras", "da Colina", "das Colinas", "da Fonte", "das Fontes",
            "do Sino", "dos Sinos", "da Serra", "das Serras", "do Lago", "dos Lagos", "da Ponte", "das Pontes",
            "do Moinho", "dos Moinhos", "da Torre", "das Torres", "do Castelo", "dos Castelos", "da Chave",
            "das Chaves", "do Martelo", "dos Martelos", "da Lança", "das Lanças", "da Forja", "das Forjas",
            "da Ferradura", "das Ferraduras", "da Âncora", "das Âncoras", "da Lamparina", "das Lamparinas",
            "da Estrela", "das Estrelas", "da Concha", "das Conchas", "dos Ferreiros", "dos Carpinteiros",
            "dos Padeiros", "dos Ceramistas", "dos Ourives", "dos Porteiros", "dos Agricultores", "dos Oleiros",
            "dos Tecelões", "dos Tanoeiros", "dos Ciclistas", "dos Navegadores", "dos Marinheiros",
            "dos Pescadores", "dos Guias", "dos Artistas", "dos Músicos", "dos Poetas", "dos Escribas", "dos Astrônomos"
        ]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Objetos_Ocupacoes))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro
    elif 91 <= Probabilidade <= 95:
        """
        Temáticos (cores, minerais, elementos)	    5%
        """
        Tematicos = [
            "Vermelho", "Azul", "Amarelo", "Verde", "Branco", "Preto",
            "Cinza", "Violeta", "Laranja", "Rosa",
            "Ouro", "Prata", "Bronze", "Cobre", "Granito", "Mármore",
            "Ferro", "Aço", "Quartzo", "Cristal",
            "Hidrogênio", "Hélio", "Carbono", "Oxigênio", "Nitrogênio"
        ]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Tematicos))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro
    elif 96 <= Probabilidade <= 100:
        """
        Conceituais	                                5%
        """
        Conceituais = [
            "Paz", "Esperança", "União", "Igualdade", "Justiça", "Liberdade",
            "Fraternidade", "Progresso", "Vitória", "Independência", "Renovação",
            "Sabedoria", "Harmonia", "Fortaleza", "Coragem", "Gratidão",
            "Caridade", "Benevolência", "Firmeza", "Amizade", "Lealdade",
            "Tranquilidade", "Clareza", "Honra", "Glória", "Virtude",
            "Concordia", "Bonança", "Prosperidade", "Dignidade",
            "Esperança Nova", "Novo Amanhecer", "Alvorada", "Aurora",
            "Horizonte", "Luz", "Brilho", "Estrela", "Sol", "Lua"
        ]
        Nome_de_bairro.append(choice(TipodeConjunto))
        Nome_de_bairro.append(choice(Conceituais))
        Nome_de_bairro = " ".join(Nome_de_bairro)
        return Nome_de_bairro


def NumerodaCasa():
    Numero = []
    Numero.append(str(randint(1, 2200)))
    Prob_Letra = randint(1, 100)
    if Prob_Letra == 1:
        Letras = ["C", "D"]
        Numero.append(choice(Letras))
    elif 2 <= Prob_Letra <= 10:
        Letras = ["A", "B"]
        Numero.append(choice(Letras))
    Numero = "".join(Numero)
    return Numero


def NomedeCidade():
    """
        Precisamos criar uma estrutura melhor além de uma simples lista
    """
    CidadesBrasileiras = [
        "São Paulo", "Rio de Janeiro", "Brasília", "Fortaleza", "Salvador",
        "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia",
        "Porto Alegre", "Belém", "Guarulhos", "Campinas", "São Luís",
        "São Gonçalo", "Maceió", "Duque de Caxias", "Natal", "Teresina",
        "São Bernardo do Campo", "Nova Iguaçu", "João Pessoa", "Jaboatão dos Guararapes",
        "Sorocaba", "Ribeirão Preto", "Uberlândia", "Contagem", "Feira de Santana",
        "Campo Grande", "Camaçari", "Santo André", "Diadema", "Juiz de Fora",
        "Osasco", "São José dos Campos", "Londrina", "Niterói", "Natal",
        "Uberaba", "Blumenau", "Santo Amaro", "Joinville", "Santa Maria",
        "Ananindeua", "Petrolina", "Canoas", "Pelotas", "Vitoria",
        "Caruaru", "Ponta Grossa", "Piracicaba", "Caxias do Sul",
        "Vitória da Conquista", "Jundiaí", "Santos", "Franca", "Itu",
        "Suzano", "São José do Rio Preto", "Taboão da Serra", "Várzea Grande",
        "Gravataí", "Criciúma", "Duque de Caxias", "Parnaíba", "Itajaí",
        "Sinop", "Maringá", "Pindamonhangaba", "Aparecida de Goiânia",
        "Piracicaba", "Guarapuava", "Cabo de Santo Agostinho", "Paracatu",
        "Lauro de Freitas", "Colombo", "Canoas", "Ibiporã", "Jacareí",
        "Poços de Caldas", "Aracaju"
    ]
    Nome = []
    Nome.append(choice(CidadesBrasileiras))
    Nome = "".join(Nome)
    return Nome


def NomedoEstado(a=True):
    if a == False:
        EstadosSiglas = [
            "AC", "AL", "AP", "AM", "BA",
            "CE", "DF", "ES", "GO", "MA",
            "MT", "MS", "MG", "PA", "PB",
            "PR", "PE", "PI", "RJ", "RN",
            "RS", "RO", "RR", "SC", "SP",
            "SE", "TO"
        ]
        return choice(EstadosSiglas)
    else:
        EstadosNomes = [
            "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia",
            "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
            "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba",
            "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
            "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo",
            "Sergipe", "Tocantins"
        ]
        return choice(EstadosNomes)


def Gera_CPF():
    #CRIA LOGO O MODULO DE CPF SEU PREGUIÇOSO !!!
    CPF = str()
    with open("CPF", "w+") as file:
        conteudo = file.read()
        print(conteudo)
    for c in range(11):
        CPF += str(randint(0,9))
    return CPF


def Gera_CEP():
    CEP = str()
    for c in range(5):
        CEP += str(randint(0, 9))
    CEP += "-"
    for d in range(3):
        CEP += str(randint(0, 9))
    return CEP


def Digitacao(Entrada, velociade_de_digitacao):
    print(Entrada)
    pyperclip.copy(Entrada)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    # pyperclip.copy("\n")
    # pyautogui.hotkey("ctrl", "v")
    time.sleep(velociade_de_digitacao)

def Gera_Idade():
    return str(randint(10,100))


def Cadastro_Victor_bank(repeticoes, velociade_de_digitacao):
    for i in range(repeticoes):
        Functions_geratriz = [NomeCompleto(), Gera_CPF(), NomedeRua(),NomedoBairro(),
                              NumerodaCasa(), NomedeCidade(), NomedoEstado(),
                              Gera_CEP()]
        for c in range(7):
            Digitacao(Functions_geratriz[c], velociade_de_digitacao)

        winsound.Beep(700, 100)
        print("*" * 100)
    winsound.Beep(100, 700)


def Gera_lista_ramdom():
    Lista = []
    for c in range(7):
        Lista.append(Functions_geratriz[c])
    return Lista


if __name__ == "__main__":
    Quantidade = int(input("Digite quantos cadastros faremos:   "))
    Time = int(input("Quanto tempo iremos esperar?:   "))
    for c in range(Time):
        print(f"Contagem {c+1}")
        time.sleep(1)
    Cadastro_Victor_bank(Quantidade,0.2)
