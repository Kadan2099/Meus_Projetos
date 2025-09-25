import pyautogui
import time
import random

# Ativando a segurança: mover o mouse para o canto superior esquerdo encerra o programa
pyautogui.FAILSAFE = True

# Texto dividido em frases
Massa = [
    ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Karina", "Lucas", "Mariana", "Nicolas", "Olívia", "Paulo", "Quésia", "Rafael", "Sofia", "Thiago",
    "Ursula", "Victor", "Wagner", "Ximena", "Yara", "Zeca", "Amanda", "Bianca", "Caio", "Diego",
    "Elaine", "Fabiana", "Gustavo", "Hugo", "Isabela", "João", "Kelly", "Leonardo", "Marta", "Natália",
    "Otávio", "Patrícia", "Quirino", "Renata", "Samuel", "Tatiane", "Ulisses", "Valéria", "William", "Xavier",
    "Yasmin", "Zuleica", "Alberto", "Beatriz", "Cristiano", "Denise", "Emerson", "Flávia", "Giovana", "Henrique",
    "Ingrid", "José", "Kátia", "Larissa", "Mateus", "Nicole", "Orlando", "Priscila", "Queila", "Roberto",
    "Simone", "Talita", "Ubirajara", "Vânia", "Wellington", "Xisto", "Yuri", "Zilda", "Arthur", "Bruna",
    "Cecília", "Davi", "Estela", "Felipe", "Giovana", "Heitor", "Isabel", "Jonas", "Kamila", "Luana",
    "Marcelo", "Noemi", "Pedro", "Quintino", "Rogério", "Sandra", "Tereza", "Vicente", "Wesley", "Zion"
    ], #Nome

    [38, 57, 23, 57, 46, 61, 24, 37, 46, 67, 34, 34, 33, 69, 60, 28, 62, 72, 34, 70, 65, 55, 69, 27, 21, 23, 35, 32, 68,
     20, 23, 44, 72, 74, 67, 47, 42, 23, 19, 61, 65, 75, 73, 61, 39, 25, 35, 67, 33, 27, 73, 55, 57, 70, 29, 71, 69, 51,
     50, 44, 66, 44, 38, 67, 35, 57, 41, 57, 61, 51, 72, 71, 71, 49, 29, 18, 75, 26, 38, 26, 20, 37, 38, 41, 58, 45, 45,
     30, 42, 21, 73, 46, 53, 71, 34, 26, 30, 66, 33, 39]
    , #Idade

    ["Analista Jr", "Analista Pleno", "Analista Sénior", "Estagiário",
     "Coordenador", "Gerente", "Supervisor", "Operador", "Técnico"], #Cargo
]

def Nome():
    return Massa[0][random.randint(0,(len(Massa[0])-1))]

def Idade():
    return Massa[1][random.randint(0,(len(Massa[1])-1))]

def Cargo():
    return Massa[2][random.randint(0,(len(Massa[2])-1))]

def Salario():
    return float(random.randint(1412,10000)+ random.randint(0,100)/100)

Cadastros = int(input("Digite quantos cadastros vamos fazer:   "))

time.sleep(5)
pyautogui.write(str(Cadastros) + "\n")
time.sleep(1)
for frase in range(Cadastros):
    Name = str(Nome()) + "\n"
    Age = str(Idade()) + "\n"
    Job = str(Cargo()) + "\n"
    Pay = str(Salario()) + "\n"
    pyautogui.write(Name)
    pyautogui.write(Age)
    pyautogui.write(Job)
    pyautogui.write(Pay)
    print(Name[:-1])
    print(Age[:-1])
    print(Job[:-1])
    print(Pay[:-1])
    print("\n")
    time.sleep(3)
