from art import *

class Tela:
    linha = 24
    linhas = 24
    colunas = 80
    def __init__(self):
        self.linhas = 24
        self.colunas = 80
        self.linha = 24

    def print_menu_list(self, itens, spacing_left):
        self.linha -= len(itens)
        for posicao in range(len(itens)):
            print(" " * spacing_left + str(posicao) + " - " + itens[posicao])
    
    def print_ascii_texto(self, texto):
        self.linha -= 7
        tprint(texto)

    def print_linhas(self, numero_linhas):
        self.linha -= numero_linhas
        for posicao in range(numero_linhas):
            print("")

    def print_texto(self, texto, spacing_left):
        self.linha -= 1
        print(" " * spacing_left + texto)


class TelaPricnipal(Tela):
    def __init__(self):
        self.print_screen("Usuario não encontrado, por favor se logar ou criar conta.")
        self.pedir_opcao_menu()

    def print_screen(self, msg=""):
        self.linha = self.linhas
        self.print_ascii_texto("  Amazon UFFS")
        self.print_menu_list(["Cadastrar", "Login", "Sair"], 35)
        self.print_linhas(5)
        self.print_texto(msg, (self.colunas // 2) - (len(msg) // 2))
        self.print_linhas(self.linha - 1)

    def pedir_opcao_menu(self):
        opcao = int(input(" Digite a opção desejada: "))
        if (opcao < 0) or (opcao > 2):
            self.print_screen("Opção invalida")
            self.pedir_opcao_menu()
        else:
            print(opcao)

