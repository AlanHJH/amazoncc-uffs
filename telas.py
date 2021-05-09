from art import *
from entidades.usuario import Usuario

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
    
    def print_campo(self, campo, valor):
        self.linha -= 1
        print(str(campo) + ": " + str(valor))


class TelaPricnipal(Tela):
    programa = None
    def __init__(self, programa):
        self.programa = programa
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
            if opcao == 0:
                TelaCadastro(self.programa)

class TelaCadastro(Tela):
    nome = None
    email = None
    cpf = None
    senha = None
    programa = None
    def __init__(self, programa):
        self.programa = programa
        self.print_screen()

    def get_quntidade_campos_preenchido(self):
        campos_preenchidos = 0
        if self.nome != None:
            campos_preenchidos += 1
        if self.email != None:
            campos_preenchidos += 1
        if self.cpf != None:
            campos_preenchidos += 1
        if self.senha != None:
            campos_preenchidos += 1
        return campos_preenchidos

    def print_screen(self, msg=""):
        self.linha = self.linhas
        self.print_ascii_texto("  Cadastro")

        self.print_linhas(4)
        self.print_texto(msg, (self.colunas // 2) - (len(msg) // 2))

        campos_preenchidos = self.get_quntidade_campos_preenchido()
        self.print_linhas(self.linha - campos_preenchidos - 1)

        if self.nome != None:
            self.print_campo(" Nome", self.nome)
        if self.email != None:
            self.print_campo(" E-mail", self.email)
        if self.cpf != None:
            self.print_campo(" Cpf", self.cpf)
        if self.senha != None:
            self.print_campo(" Senha", "*" * len(str(self.senha)))

        self.pedir_proximo_campo()

    def pedir_proximo_campo(self):
        posible_options = ["n","s","sim","não","nao"]
        if self.nome == None:
            self.nome = str(input(" Digite o seu nome: "))
            self.print_screen()
        if self.email == None:
            self.email = str(input(" Digite o seu e-mail: "))
            self.print_screen()
        if self.cpf == None:
            self.cpf = str(input(" Digite o seu cpf: "))
            self.print_screen()
        if self.senha == None:
            self.senha = str(input(" Digite o seu senha: "))
            self.print_screen()
        
        con = str(input(" Deseja confirmar o seu cadastro?   (s) sim (n) não : "))
        con.lower()
        if con not in posible_options:
            self.print_screen("Erro: Opção invalida!")
        else:
            if (con == 's') or (con == 'sim'):
                usuario = Usuario(self.nome, self.cpf,self.senha,self.email)
                self.programa.add_usuario(usuario)
                TelaPricnipal(self.programa)
            else:
                TelaPricnipal(self.programa)