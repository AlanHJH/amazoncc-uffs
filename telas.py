from art import *
from entidades.usuario import Usuario
from cpf import valida_cpf, get_numbers

lower = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
upper = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'

class Tela:
    linha = 24
    linhas = 24
    colunas = 80
    def __init__(self):
        self.linhas = 24
        self.colunas = 80
        self.linha = 24

    def print_menu_list(self, itens, spacing_left, starting = 0):
        self.linha -= len(itens)
        for posicao in range(len(itens)):
            num_item = starting + posicao
            spacing_number = ""
            if num_item < 10:
                spacing_number = " "
            print(" " * spacing_left + str(num_item) + spacing_number + " - " + itens[posicao])

    def print_menu_listas(self, itens, itens2 , spacing_left):
        quantidade_coluna = 10
        self.linha -= len(itens)
        for posicao in range(len(itens)):
            
            coluna_esquerda = ""
            coluna_direita = ""

            if posicao < len(itens):
                coluna_esquerda = " " * spacing_left + str(posicao) + " - " + itens[posicao]

            if posicao < len(itens2):
                espacamento_esquerda = 40 - len(coluna_esquerda) - 1 
                coluna_direita = "  " * espacamento_esquerda + " " + str(posicao + quantidade_coluna) + "-" + itens2[posicao]

            print(coluna_esquerda + coluna_direita)
    
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
        msg = ""
        if self.programa.usuario_logado != None:
            msg = "Ola, " + self.programa.usuario_logado.nome
        else:
            msg = "Usuario não encontrado, por favor se logar ou criar conta."
        self.print_screen(msg)
        self.pedir_opcao_menu()

    def print_screen(self, msg=""):
        self.linha = self.linhas
        self.print_ascii_texto("  Amazon UFFS")
        self.print_menu_list(["Cadastrar", "Login", "Ver Carrinho","Ver Produtos","Clientes", "Limpar Saldo", "Sair"], 35)
        self.print_linhas(5)
        self.print_texto(msg, (self.colunas // 2) - (len(msg) // 2))
        self.print_linhas(self.linha - 1)

    def pedir_opcao_menu(self):
        opcao = str(input(" Digite a opção desejada: "))
        opcao = get_numbers(opcao)

        if len(opcao) > 0:
            opcao = int(opcao)
        else: 
            opcao = -1

        if (opcao < 0) or (opcao > 6):
            self.print_screen("Opção invalida")
            self.pedir_opcao_menu()
        else:
            if opcao == 0:
                TelaCadastro(self.programa)
            if opcao == 1:
                TelaLogin(self.programa)
            if opcao == 2:
                if self.programa.usuario_logado == None:
                    self.print_screen("Para acessar esta opção é necessário que você esteja logado!")
                    self.pedir_opcao_menu()
                else:
                    TelaCarrinho(self.programa)
            if opcao == 3:
                if self.programa.usuario_logado == None:
                    self.print_screen("Para acessar esta opção é necessário que você esteja logado!")
                    self.pedir_opcao_menu()
                else:
                    TelaProdutos(self.programa)
            if opcao == 4:
                if self.programa.usuario_logado == None:
                    self.print_screen("Para acessar esta opção é necessário que você esteja logado!")
                    self.pedir_opcao_menu()
                else:
                    TelaClientes(self.programa)
            if opcao == 5:
                if self.programa.usuario_logado == None:
                    self.print_screen("Para acessar esta opção é necessário que você esteja logado!")
                    self.pedir_opcao_menu()
                else:
                    self.programa.limpa_saldo()
                    self.print_screen("Saldo Liberado")
                    self.pedir_opcao_menu()
            if opcao == 6:
                self.programa.end_program()

class TelaCadastro(Tela):
    nome = None
    email = None
    cpf = None
    senha = None
    programa = None
    def __init__(self, programa):
        self.programa = programa
        self.print_screen("Para sair digite 's'")

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
    
    def valida_nome(self):
        erro = ""

        if self.nome == 's':
            TelaPricnipal(self.programa)
        
        if self.programa.is_nome_unique(self.nome) == False:
            erro = "ERRO: Nome ja esta sendo utilizado"
        
        if self.nome == "":
            erro = "ERRO: Nome é campo obrigatório"
        
        if len(erro) > 0:
            self.nome = None

        return erro
    
    def valida_email(self):
        erro = ""

        if self.email == 's':
            TelaPricnipal(self.programa)
        
        if self.programa.is_email_unique(self.email) == False:
            erro = "ERRO: E-mail ja esta sendo utilizado"
        
        if self.email == "":
            erro = "ERRO: E-mail é campo obrigatório"
        
        if len(erro) > 0:
            self.email = None

        return erro
    
    def valida_cpf(self):
        erro = ""

        if self.cpf == 's':
            TelaPricnipal(self.programa)
        
        if valida_cpf(self.cpf) == False:
            erro = "ERRO: CPF Inválido!"

        if self.programa.is_cpf_unique(self.cpf) == False:
            erro = "ERRO: CPF ja esta sendo utilizado"

        if len(erro) > 0:
            self.cpf = None

        return erro

    def valida_senha(self):
        erro = ""

        if self.senha == 's':
            TelaPricnipal(self.programa)

        if len(erro) > 0:
            self.senha = None

        return erro

    def pedir_proximo_campo(self):
        posible_options = ["n","s","sim","não","nao"]
        if self.nome == None:
            self.nome = str(input(" Digite o seu nome: "))
            msg = self.valida_nome()
            self.print_screen(msg)
        if self.email == None:
            self.email = str(input(" Digite o seu e-mail: "))
            msg = self.valida_email()
            self.print_screen(msg)
        if self.cpf == None:
            self.cpf = str(input(" Digite o seu cpf: "))
            msg = self.valida_cpf()
            self.print_screen(msg)
        if self.senha == None:
            self.senha = str(input(" Digite o seu senha: "))
            msg = self.valida_senha()
            self.print_screen(msg)
        
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

class TelaLogin(Tela):
    cpf = None
    senha = None
    def __init__(self, programa):
        self.programa = programa
        self.print_screen()

    def get_quntidade_campos_preenchido(self):
        campos_preenchidos = 0
        if self.cpf != None:
            campos_preenchidos += 1
        if self.senha != None:
            campos_preenchidos += 1
        return campos_preenchidos

    def print_screen(self, msg="Caso queira sair digite 's' e aperte ENTER"):
        self.linha = self.linhas
        self.print_ascii_texto("  Login")

        self.print_linhas(4)
        self.print_texto(msg, (self.colunas // 2) - (len(msg) // 2))

        campos_preenchidos = self.get_quntidade_campos_preenchido()
        self.print_linhas(self.linha - campos_preenchidos - 1)

        if self.cpf != None:
            self.print_campo(" CPF", self.cpf)
        if self.senha != None:
            self.print_campo(" Senha", self.senha)

        self.pedir_proximo_campo()

    def pedir_proximo_campo(self):
        if self.cpf == None:
            self.cpf = str(input(" CPF: "))
            if self.cpf == 's' or self.cpf == 'S':
                TelaPricnipal(self.programa)
            else:
                self.print_screen()
        if self.senha == None:
            self.senha = str(input(" Senha: "))
            if self.senha == 's' or self.senha == 'S':
                TelaPricnipal(self.programa)
            else:
                self.print_screen()

        usuario = self.programa.user_exists(self.cpf, self.senha)
        
        if usuario == None:
            self.cpf = None
            self.senha = None
            self.print_screen("Combinação usuário e senha não encontrado")
        else:
            self.programa.set_usuario_logado(usuario)
            TelaPricnipal(self.programa)

        
class TelaProdutos(Tela):
    programa = None
    pagina_atual = 0
    def __init__(self, programa):
        self.programa = programa
        self.pagina_atual = 0
        self.print_screen()
        self.get_pagina()
    
    def get_produtos(self):
        return self.programa.get_prdutos( 0)

    def print_screen(self, msg=""):
        self.linha = self.linhas
        self.print_ascii_texto(" Produtos")
        self.print_menu_list(self.programa.get_prdutos( self.pagina_atual),2,self.pagina_atual * 14)
        self.print_linhas(self.linha - 2)
        self.print_texto("Pagina atual: " + str(self.pagina_atual)  + " - Digite 's' para sair e 'c' para comprar | " + msg, 0)
    
    def get_compra(self):
        codigo = str(input("Qual produto deseja comprar: "))    

        codigo = get_numbers(codigo)

        if len(codigo) > 0:
            codigo = int(codigo)
        else: 
            codigo = -1

        if codigo > len(self.programa.produtos) or codigo < 0:
            self.print_screen("Código Inválido!")
            self.get_compra()
        else:
            self.print_screen()
            quantidade = str(input("Quantidade: "))

            if quantidade == "" or quantidade == None:
                quantidade = 0
            else:
                quantidade = float(quantidade)

            saldo_item = self.programa.produtos[codigo].preco *quantidade
            possivel_total = self.programa.get_saldo_carrinho() + saldo_item

            while possivel_total > 1000:
                self.print_screen("Qtd Muito Alta!")
                quantidade = str(input("Quantidade: "))

                if quantidade == "" or quantidade == None:
                    quantidade = 0
                else:
                    quantidade = float(quantidade)

                saldo_item = self.programa.produtos[codigo].preco *quantidade
                possivel_total = self.programa.get_saldo_carrinho() + saldo_item

            self.programa.adicionar_no_carrinho(codigo, quantidade)
            self.print_screen()
            self.get_pagina()

    def get_pagina(self):
        pg = str(input("Qual pagina deseja visualizar: "))

        if pg == None or pg == "":
            self.print_screen("Código Inválido!")
            self.get_pagina()

        if pg == 's':
            TelaPricnipal(self.programa) 
        elif pg == 'c':
            self.print_screen()
            self.get_compra()
        else:
            is_number = True

            for i in pg:
                if i  in lower + upper:
                    is_number = False

            if is_number:
                self.pagina_atual = int(pg)
                self.print_screen()
                self.get_pagina()
            else:
                self.print_screen("Caracter inválido!")
                self.get_pagina()

class TelaCarrinho(Tela):
    programa = None
    pagina_atual = 0
    def __init__(self, programa):
        self.programa = programa
        self.pagina_atual = 0
        self.print_screen()
        self.get_pagina()
    
    def get_produtos(self):
        return self.programa.get_prdutos( 0)

    def print_screen(self, msg=""):
        self.linha = self.linhas
        self.print_ascii_texto(" Carrinho")
        self.print_texto("Código|Quantidade|Descrição|Preço", 2)
        self.print_menu_list(self.programa.get_prdutos_carrinho( self.pagina_atual),2,self.pagina_atual * 13)
        self.print_linhas(self.linha - 3)
        self.print_texto("Saldo Atual: " + str(self.programa.get_saldo_carrinho()),0)
        self.print_texto("Pagina atual: " + str(self.pagina_atual)  + " - Digite 's' para sair e 'r' para remover | " + msg, 0)
        
    def get_remove(self):
        opcoes_validas = "s0123456789"
        codigo = str(input("Digite o código que você deseja remover: "))

        if codigo == None or codigo == "":
            self.print_screen("Código Inválido!")
            self.get_remove()

        if codigo == 's':
            TelaPricnipal(self.programa) 
        else:
            if str(codigo) not in opcoes_validas:
                self.print_screen("Código Inválido!")
                self.get_remove()
            else:   
                codigo = int(codigo)     
                if codigo < 0 or codigo >= len(self.programa.carrinho[self.programa.usuario_logado.cpf]) or len(self.programa.carrinho[self.programa.usuario_logado.cpf]) == 0:
                    self.print_screen("Código Inválido!")
                    self.get_remove()
                else:
                    self.programa.remove_item_carrinho(codigo)
                    self.print_screen()
                    self.get_pagina()

    def get_pagina(self):
        pg = str(input("Qual pagina deseja visualizar: "))

        if pg ==  None or pg == '':
            self.print_screen()
            self.get_pagina()

        if pg == 's':
            TelaPricnipal(self.programa) 
        elif pg == 'r':
            self.print_screen()
            self.get_remove()
        else:
            is_number = True

            for i in pg:
                if i  in lower + upper:
                    is_number = False

            if is_number:
                self.pagina_atual = int(pg)
                self.print_screen()
                self.get_pagina()
            else:
                self.print_screen("Caracter inválido!")
                self.get_pagina()

class TelaClientes(Tela):
    programa = None
    cpf = None
    nome = None
    email = None
    def __init__(self, programa):
        self.programa = programa
        self.cpf = None
        self.nome = None
        self.email = None
        self.print_screen()
        self.get_cpf()
    
    def get_produtos(self):
        return self.programa.get_prdutos( 0)

    def print_screen(self, msg="Nenhum usuário encontrado!"):
        self.linha = self.linhas
        self.print_ascii_texto(" Usuarios")
        self.print_linhas(4)

        if self.cpf == None:
            self.print_texto(msg, (self.colunas // 2) - (len(msg) // 2))
        else:
            self.print_texto("Nome: " + self.nome, 2)
            self.print_texto("E-mail: " + self.email, 2)
        self.print_linhas(self.linha - 2)
        self.print_texto("Para sair digite 's'",0)
        

    def get_cpf(self):
        self.cpf = str(input("Digite o cpf do usuário que deseja consultar:"))
        if self.cpf == 's':
            TelaPricnipal(self.programa)
        else:
            usuario_pesquisa = self.programa.get_usuario_by_cpf(self.cpf)
            if usuario_pesquisa != None:
                self.cpf = usuario_pesquisa.cpf
                self.email = usuario_pesquisa.email
                self.nome = usuario_pesquisa.nome
            else:
                self.cpf = None
            self.print_screen()
            self.get_cpf()
        