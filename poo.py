
class Estudante:

    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        return (self.nota1 + self.nota2) / 2
    def situacao(self):
        if situacao.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Recuperação"

        return "Reprovado"

    def descrever(self):
        return(f"{self.nome:<16}{slf.nota1:<7}{self.nota2:<7}"f"{self.media():<8.1f}{self.sitoacao():<14}")

estudantes = []

def cadastrar():
    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    estudantes.append(Estudante(nome, nota1, nota2))
    print("Estudante cadastrado. ")

def listar():
    if len(nomes) == 0: #len() retorna o tamanho da lista/
        print("Nenhum estudante cadastrado.")
        return

    print(f"\n{'NOME':<20}{'N1:':<5}{'N2:':<5}{'MEDIA':<8}{'SITUAÇÂO': <14}")

    for estudante in estudantes:
        print(estudante.descrever())

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

