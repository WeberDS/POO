nomes = []
notas1 = []
notas2 = []

def cadastrar (): 
    nome = input("Digite o nome do aluno: ")
    notas1 = float(input("Digite a primeira nota: "))
    notas2 = float(input("Digite a segunda nota: "))
    
    nomes.append(nome)
    notas1.append(notas1)
    notas2.append(notas2) 
    print("Cadastro realizado!") 

def calcular_media(indice):
    return (notas1[indice] + notas2[indice]) / 2

def situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    
    return "Reprovado"

def listar ():
    if len(nomes) == 0:
        print("Nenhum aluno cadastrado.")   # len() retorna ao tamanho da lista, se for 0 significa que não há alunos cadastrados
        return
    print (f"\n{'Nome':<16}{'N1':<7}{'N2':<7}{'MÉDIA':8}{'SITUAÇÃO':<14}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}{calcular_media(i) :<8.1f} {situacao(calcular_media(i)):<14}")

def menu ():
    while True:
        print("\n1 - Cadastrar estudante:")
        print("2 - Listar alunos")
        print("0 - Sair")
        
        opcao = input("Escolha opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
menu()

