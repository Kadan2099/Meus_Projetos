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

Lista = [PrimeiroNome,SegundoNome,SegundoNome,SegundoNome,SegundoNome,SegundoNome,SegundoNome,Sobrenome]
Tamanho = 0
def Calculon(List):
    max = len(List[0])
    contador = 0
    for c in List:
        if len(c) > max:
            max = len(c)
            contador += 1
            print(f"Item {c} tamanho {len(c)} atual contagem de caracteres de nome maior sendo = {max}")

    return max

for b in Lista:
    Tamanho += Calculon(b)
    print(f"Tamanho de nome igual {Tamanho}")
    print("@" * 100)

print(Tamanho)

while True:
    word = input("Digite a string que deseja medir cuidado com espaços: ")
    print(f"Tamanho de string definido como: {len(word)}")