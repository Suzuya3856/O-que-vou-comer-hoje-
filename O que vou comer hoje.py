import os
from lugares.Lugares import Lugares
def Título():
    print("""
░█████╗░░█████╗░███╗░░░███╗██╗██████╗░░█████╗░  ██████╗░░█████╗░  ██╗░░░██╗███████╗███████╗
██╔══██╗██╔══██╗████╗░████║██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░██║██╔════╝╚════██║
██║░░╚═╝██║░░██║██╔████╔██║██║██║░░██║███████║  ██║░░██║███████║  ╚██╗░██╔╝█████╗░░░░███╔═╝
██║░░██╗██║░░██║██║╚██╔╝██║██║██║░░██║██╔══██║  ██║░░██║██╔══██║  ░╚████╔╝░██╔══╝░░██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║██████╔╝██║░░██║  ██████╔╝██║░░██║  ░░╚██╔╝░░███████╗███████╗
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚══════╝
""")
def subtítulo(subtitulo):
    os.system("cls")
    linha = "*" * (len(subtitulo))
    print(linha)
    print(f"{subtitulo}")
    print(linha)
    print()
def voltar_adicionar():
    input("Aperte qualquer tecla para retornar")
    adicionar_opcao()
def voltar():
    input("\nPress any key to return")
    main()
def sair():
    subtítulo("PROGRAMA ENCERRADO")

def o_que_fazer():
    print("\t\t\t1. Adicionar nova opção\n")
    print("\t\t\t2. Ver opções\n")
    print("\t\t\t3. Sortear o que vai ser da vez\n")
    print("\t\t\t4. Vazar")
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
def mostrar_opcao():
    subtítulo("OPÇÕES QUE VOCÊ TEM")
    Lugares.mostrar_lugares()
    voltar()
def sortear():
    subtítulo("O QUE VAI SER?")
    Lugares.sortear()
    voltar()
    
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
def main():
    os.system("cls")
    Título()
    o_que_fazer()
    o_que_ce_escolheu()
    
if __name__ == "__main__":
    main()