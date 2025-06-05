import random

usuario = 'desativo'

listaGeneros = [["ação"], ["aventura"], ["comédia"], ["drama"], ["ficção científica"], ["terror"], ["romance"], ["suspense"], ["fantasia"], ["musical"], ["documentário"], ["policial"]]

# Criar as horas da lista
for i in range(len(listaGeneros)): # esse menos um é para não contar o primerio
    for j in range(len(listaGeneros)):
        horas = random.randint(0, 5)
        listaGeneros[i].append(horas) # esse mais um é para ele pular o primerio
    
# Perguntando dados
login = input("Digite o seu nome: ")

introducao = input(f"Bem-vindo {login}, Gostaria de receber seus dados de uso (tempo assistindo) na plataforama?(s/n) ")

if introducao == "s":
    usuario = 'ativo'
else:
    print("Obrigado por logar!")

while usuario == 'ativo':
    
    escolhaGenero = int(input("\n \n Escolha o genero que você que ver o tempo mensal: \n 1 = ação \n 2 = aventura \n 3 = comédia \n 4 = drama \n 5 = ficção \n 6 = terror \n 7 = romance \n 8 = suspense \n 9 = fantasia \n 10 = musical \n 11 = documentário \n 12 = policial \n \n Número do gênero: "))
    
    if 0 < escolhaGenero < 13:
        print("\n", listaGeneros[escolhaGenero - 1]) # esse menos um é para o número escolhido pelo usuario (que começa em 1) bata com o da lista (que começa em zero)
    else:
        print("\n Não tem esse número nas opções")
        
    reiniciar = input("\n Deseja pesquisar novamente?(s/n) ")

    if reiniciar == "s":
        usuario = "ativo"
    elif reiniciar == "n":
        print("Obrigado por acessar a plataforma, até mais!")
        usuario = "desativo"


loop = True
while loop == True:

    # Gêneros assistidos
    listaGeneros = ["ação", "aventura", "comédia", "drama", "ficção científica",
                    "terror", "romance", "suspense", "fantasia", "musical", "documentário", "policial"]

    # Mêses do ano
    listaMeses = ["jan", "fev", "mar", "abr", "mai",
                  "jun", "jul", "ago", "set", "out", "nov", "dez"]

    # Horas assistidas por mês
    # listaHorasFilme  # Ta ali em cima

    # FUNÇÃO DESCOBRIR GÊNERO PREFERIDO

    # def generoFav():

    # FUNÇÃO CALCULAR TEMPO

    # def calcTempo(listaHorasMes):

    # Mensagem de bem vindo e escolha da função
    print("Bem vindo ao nosso programa de streaming\n")
    print("\ndigite o numero para a função escolhida")

    print("\n(1) | Total de horas assistidas ")
    print("(2) | Qual é o meu genero preferido ")

    escolha = int(input("\nDigite aqui: "))

'''
    Criação da matriz 
    NÃO ALTERAR
'''
# ;favInput