from art import *

class Tela:
    def print_menu_list(self, itens):
        for posicao in range(len(itens)):
            print(" " * 5  + str(posicao) + itens[posicao])

class TelaDeCadastro(Tela):
    def __init__(self):
        print("\n"*3)
        tprint(" Amazon UFFS") # 5 de altura
        self.print_menu_list(["Cadastrar", "Login", "Sair"])
        print("\n"*13)
        input("Digite uma opção > ")
        