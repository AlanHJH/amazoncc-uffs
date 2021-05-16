from entidades.usuario import Usuario
from entidades.produto import Produto
import sys

class Programa:
    usuarios = []
    produtos = []
    carrinho = []
    usuario_logado = None
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = None
        self.produtos = [
            Produto("1Pasta de dente", 22.50),
            Produto("2Tomate Kg", 5.5),
            Produto("3Pasta de dente", 22.50),
            Produto("4Tomate Kg", 5.5),
            Produto("5Pasta de dente", 22.50),
            Produto("6Tomate Kg", 5.5),
            Produto("7Pasta de dente", 22.50),
            Produto("8Tomate Kg", 5.5),
            Produto("9Pasta de dente", 22.50),
            Produto("10Tomate Kg", 5.5),
            Produto("11Pasta de dente", 22.50),
            Produto("12Tomate Kg", 5.5),
            Produto("13Pasta de dente", 22.50),
            Produto("14Tomate Kg", 5.5),
            Produto("15Pasta de dente", 22.50),
            Produto("16Tomate Kg", 5.5),
            Produto("17Pasta de dente", 22.50),
            Produto("18Tomate Kg", 5.5),
            Produto("19Pasta de dente", 22.50),
            Produto("20Tomate Kg", 5.5),
            Produto("21Tomate Kg", 5.5),
            Produto("22Tomate Kg", 5.5),
            Produto("23Tomate Kg", 5.5),
            Produto("24Tomate Kg", 5.5),
            Produto("25Tomate Kg", 5.5),
            Produto("26Tomate Kg", 5.5),
            Produto("27Tomate Kg", 5.5),
            Produto("28Tomate Kg", 5.5),
            Produto("29Tomate Kg", 5.5)
        ]
        self.carrinho = [
            Produto("1Pasta de dente", 22.50),
            Produto("2Tomate Kg", 5.5),
            Produto("3Pasta de dente", 22.50),
            Produto("4Tomate Kg", 5.5),
            Produto("5Pasta de dente", 22.50),
            Produto("6Tomate Kg", 5.5)
        ]
        self.usuario_logado = Usuario(
            nome="Alan Henrique Jahnel",
            cpf="11374288993",
            senha="123",
            email="alanjahnel123@gmail.com"
        )
    
    def add_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def user_exists(self, email, senha):
        usurio_resposta = None
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                usurio_resposta = usuario
        return usurio_resposta
    
    def set_usuario_logado(self, usuario):
        self.usuario_logado = usuario

    def get_usuario_logado(self):
        return self.usuario_logado
    
    def end_program(self):
        sys.exit()
    
    def get_prdutos(self, pagina):
        caracteres_por_item = 70
        itens_na_tela = 14
        inicio = itens_na_tela * pagina
        itens_coluna_um = self.produtos[inicio: inicio + 14]

        lista_final = []

        for item in itens_coluna_um:
            secao_descricao = item.descricao[0:40]
            secao_preco = str("%.2f" % round(item.preco,2))[0:caracteres_por_item]
            quantidade_ponto = len(secao_descricao) + len(secao_preco)
            lista_final.append(secao_descricao + "." * (caracteres_por_item - quantidade_ponto) + secao_preco)
        
        return lista_final
    
    def get_prdutos_carrinho(self, pagina):
        caracteres_por_item = 70
        itens_na_tela = 14
        inicio = itens_na_tela * pagina
        itens_coluna_um = self.carrinho[inicio: inicio + 14]

        lista_final = []

        for item in itens_coluna_um:
            secao_descricao = item.descricao[0:40]
            secao_preco = str("%.2f" % round(item.preco,2))[0:caracteres_por_item]
            quantidade_ponto = len(secao_descricao) + len(secao_preco)
            lista_final.append(secao_descricao + "." * (caracteres_por_item - quantidade_ponto) + secao_preco)
        
        return lista_final

    def get_usuario_by_cpf(self, cpf):
        usuario_resposta = None
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                usuario_resposta = usuario
        return usuario_resposta
