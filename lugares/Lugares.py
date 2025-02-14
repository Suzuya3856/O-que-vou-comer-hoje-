import random


# criando a classe
class Lugares:
    lugares = []

    # método decorator
    def __init__(self, nome, prato, preço):
        self.nome = nome
        self.prato = prato
        self.preço = preço
        Lugares.lugares.append(self)

    # convertendo para string os valores do objeto
    def __str__(self):
        return f"{self.nome}, {self.prato},{self.preço}"

    # método que realiza o sorteio dos objetos
    @classmethod
    def sortear(cls):
        sorteado = random.choice(Lugares.lugares)
        print(
            f"É fi, a escolha da vez foi {sorteado.prato}, espero que se tenha {sorteado.preço} reais,\nporque o que for decidido aqui é lei."
        )

    # método que exibe uma tabela com os valores dos objetos
    @staticmethod
    def mostrar_lugares():
        print(f"{"Onde é".ljust(15)} | {"Comida".ljust(15)} | {"Preço"}\n")
        for lugar in Lugares.lugares:
            print(f"{lugar.nome.ljust(20)} | {lugar.prato.ljust(20)} | {lugar.preço}")


