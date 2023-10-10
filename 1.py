import random

# Listas de nomes e sobrenomes
nomes = ["Cecilia", "Joana", "Mariana", "Pericles", "Luísa", "Rafael", "Laura", "Carlos", "Evaristo", "Lucas",
         "Lívia", "Barbara", "Juliana", "Ronaldo", "Marciano", "Fiona", "Caciano", "Daniela", "Patrícia"]
sobrenomes = ["Kaminski", "Kramer", "Oliveira", "Silva", "Ferreira", "Rodrigues", "Sanches", "Lima", "Souza", "Costa",
              "Carvalho", "Chemeres", "Ribeiro", "Araújo", "Martins", "Cavalcanti", "Freitas", "Correia", "Vieira"]

def gera_dados_aleatorios(N):
    with open("dados_pessoais.txt", "w") as arquivo:
        for _ in range(N):
            nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
            idade = random.randint(18, 60)
            altura = round(random.uniform(1.50, 2.00), 2)
            arquivo.write(f"{nome_completo}, {idade} anos, {altura} m\n")

N = int(input("Digite o número de registros a serem gerados: "))
gera_dados_aleatorios(N)