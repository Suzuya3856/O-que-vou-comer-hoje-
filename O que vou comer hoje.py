import os
from lugares.Lugares import Lugares

#função para definir o título do programa
def Título():
    print("""
░█████╗░░█████╗░███╗░░░███╗██╗██████╗░░█████╗░  ██████╗░░█████╗░  ██╗░░░██╗███████╗███████╗
██╔══██╗██╔══██╗████╗░████║██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░██║██╔════╝╚════██║
██║░░╚═╝██║░░██║██╔████╔██║██║██║░░██║███████║  ██║░░██║███████║  ╚██╗░██╔╝█████╗░░░░███╔═╝
██║░░██╗██║░░██║██║╚██╔╝██║██║██║░░██║██╔══██║  ██║░░██║██╔══██║  ░╚████╔╝░██╔══╝░░██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║██████╔╝██║░░██║  ██████╔╝██║░░██║  ░░╚██╔╝░░███████╗███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚══════╝
""")

#função para gerar o subtítulo de cada tela
def subtítulo(subtitulo):
    os.system("cls")
    linha = "*" * (len(subtitulo))
    print(linha)
    print(f"{subtitulo}")
    print(linha)
    print()

#função para voltar ao menu de adicionar opções
def voltar_adicionar():
    input("Aperte qualquer tecla para retornar")
    adicionar_opcao()

#função para voltar ao menu inicial
def voltar():
    input("\nPress any key to return")
    main()

#função para encerrar o programa
def sair():
    subtítulo("PROGRAMA ENCERRADO")

#função para definir as opções do menu
def o_que_fazer():
    print("\t\t\t1. Adicionar nova opção\n")
    print("\t\t\t2. Ver opções\n")
    print("\t\t\t3. Sortear o que vai ser da vez\n")
    print("\t\t\t4. Vazar")
    
#função que realiza o adicionar restaurantes
def adicionar_opcao():
    subtítulo("ADICIONANDO LUGAR")
    lugar1 = Lugares("","","")
    lugar1.nome = input("\nQual o nome do lugar?\n\n")
    lugar1.prato = input("\nO que ce come lá?\n\n")
    try:
        lugar1.preço = int(input("\nQuanto é?\n\n"))
    except ValueError:
        print("Preço inválido!")
        Lugares.lugares.remove(lugar1)
        voltar_adicionar()
    print("Beleza, tá na lista!")
    voltar()

#função que exibe as opções disponíveis
def mostrar_opcao():
    subtítulo("OPÇÕES QUE VOCÊ TEM")
    Lugares.mostrar_lugares()
    voltar()

#função que sorteia aleatoriamente uma das opções    
def sortear():
    subtítulo("O QUE VAI SER?")
    Lugares.sortear()
    voltar()

#função que leva o usuário ao menu escolhido
def o_que_ce_escolheu():
    try:
        escolha = int(input("\n\nO que ce quer fazer? "))
    except ValueError:
        print("Opção inválida!")
        voltar()
    if escolha == 1:
        adicionar_opcao()
    elif escolha == 2:
        mostrar_opcao()
    elif escolha == 3:
        sortear()
    elif escolha == 4:
        sair()
    else:
        voltar()

#função principal que executa as outras
def main():
    os.system("cls")
    Título()
    o_que_fazer()
    o_que_ce_escolheu()

#condição que verifica a ativação da função main    
if (__name__ 
        == "__main__"):
    main()