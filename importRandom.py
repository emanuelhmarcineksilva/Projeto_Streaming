import random

listaGeneros = ["ação", "aventura", "comédia", "drama", "ficção", "terror",
                "romance", "suspense", "fantasia", "musical", "documentário", "anime"]

listaMeses = ["jan", "fev", "mar", "abr", "mai", "jun",
              "jul", "ago", "set", "out", "nov", "dez"]

space = "______________________________________________"

linhas = 12
colunas = 12

login = "logado"

def horas_genero():
        horas_por_genero = [0] * colunas
        for j in range(colunas):
            for i in range(linhas):
                horas_por_genero[j] += m[i][j]
        return horas_por_genero

def genero_favorito(horas_por_genero):
    #print(horas_por_genero)
    maior = horas_por_genero[0]
    indice = 0
    for i in range(1, colunas):
        if horas_por_genero[i] > maior:
            maior = horas_por_genero[i]
            indice = i
            genero_favorito = listaGeneros[indice]
    print("Seu gênero favorito de filmes é",
            genero_favorito, "com", maior, "horas assistidas")

def total_horas():
    total = 0
    for i in range(linhas):
        for j in range(colunas):
            total += m[i][j]
    print(total)

m = [0] * linhas
for i in range(linhas):
    m[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        m[i][j] = random.randint(1, 6)

'''
# printa a matriz
for i in range(linhas):
    lin = listaMeses[i]
    for j in range(colunas):
        lin += ' ' + str(m[i][j])
'''


# Mensagens iniciais:
print(space, "\nOlá, Bem vindo a nossa plataforma de streaming!!")

nome = str(input("\nDigite seu nome: "))
quantidadeHoras = int(input("Digite a média de horas que você assiste diariamente: "))
valorAssinatura = float(input("Digite o valor mensal da sua assinatura: "))



while login == "logado":


    # MENU DE OPERAÇÕES:
    print(space, "\nMenu de operações:", f"\n\nO que deseja fazer {nome}?",
          "\n\n 1 - Ver tabela de horas asisstidas por mês",
          "\n 2 - Ver meu gênero favorito",
          "\n 3 - Logar com outra conta",
          "\n 0 - Sair")

    decisao = int(input("\n Escolha uma opção: "))



    if decisao == 1:
        print(horas_genero())

    if decisao == 2:
        totais = horas_genero()
        genero_favorito(totais)

    elif decisao == 3:
        print("Olá, Bem vindo a nossa plataforma de streaming!!")

        nome = str(input("\nDigite seu nome: "))
        quantidadeHoras = int(input("Digite a média de horas que você assiste diariamente: "))
        valorAssinatura = float(input("Digite o valor mensal da sua assinatura: "))

    elif decisao == 0:
        login = "deslogado"

    '''
    totais = horas_genero()
    genero_favorito(totais)
    '''
    
