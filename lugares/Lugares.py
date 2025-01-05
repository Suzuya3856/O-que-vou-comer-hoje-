import random
class Lugares():
    lugares = []
    def __init__(self, nome, prato, preço):
        self.nome = nome
        self.prato = prato
        self.preço = preço
        Lugares.lugares.append(self)
    
    @classmethod
    def sortear(cls):
        sorteado = random.choice(Lugares.lugares)  
        print(f"É fi, a escolha da vez foi {sorteado.prato}, espero que se tenha {sorteado.preço} reais,\nporque o que for decidido aqui é lei.") 
    def mostrar_lugares():
        print(f"\n{"Onde é".ljust(25)} | {"Prato".ljust(25)} | {"Preço".ljust(25)}")
        for lugar in Lugares.lugares:
            print(f"{lugar.nome.ljust(25)} | {lugar.prato.ljust(25)} | {str(lugar.preço).ljust(25)}")
        

dino = Lugares("Dino's Lanches", "Dog Completo", 21)
jl = Lugares("JL Lanches", "X-Marmita",38)
lets = Lugares("Let's Eat","Barbacoa Burrito",50)
bens = Lugares("Ben's Chicken","2 lanche de frango",37)