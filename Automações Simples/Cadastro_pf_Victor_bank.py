import pyautogui
import time
from random import randint, choice
def NomeCompleto():
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

    Probabilidade = randint(1,100)
    Tamanho = 0
    Partes = []
    # 5% Tem mais de 3 Nomes, 20% tem 3 Nomes, 25% tem 2 nomes, 50% tem 1 nome

    if 1 <= Probabilidade <= 5:
        Tamanho = randint(4,7)
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

print(NomeCompleto())

