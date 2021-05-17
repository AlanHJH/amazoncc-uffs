from typing import SupportsAbs
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
            Produto("Pasta de dente", 22.50),
            Produto("Vacina COVID-19", 199.99),
            Produto("Microfone Fifine", 229.50),
            Produto("Cuia de mate", 13.5),
            Produto("Ovo", 0.25),
            Produto("Gado Nelori", 500),
            Produto("Kit Smirnoff", 125.3),
            Produto("Bone do sindicato", 5.5),
            Produto("Cortina Vermelha", 22.2),
            Produto("Arpirador de po", 22.2),
            Produto("Banana", 21.2),
            Produto("Maracuja", 21.2),
            Produto("Santinho de Politico", 0.5),
        ]
        self.carrinho = {}
        self.usuario_logado = None

    def add_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.carrinho[usuario.cpf] = []

    def user_exists(self, cpf, senha):
        usurio_resposta = None
        for usuario in self.usuarios:
            if usuario.cpf == cpf and usuario.senha == senha:
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
            secao_preco = str("%.2f" % round(item.preco, 2))[
                0:caracteres_por_item]
            quantidade_ponto = len(secao_descricao) + len(secao_preco)
            lista_final.append(
                secao_descricao + "." * (caracteres_por_item - quantidade_ponto) + secao_preco)

        return lista_final

    def get_prdutos_carrinho(self, pagina):
        caracteres_por_item = 70
        itens_na_tela = 13
        inicio = itens_na_tela * pagina
        itens_coluna_um = self.carrinho[self.usuario_logado.cpf][inicio: inicio + 13]

        lista_final = []

        for item in itens_coluna_um:
            secao_descricao = str(item.quantidade) + \
                " - " + item.descricao[0:40]
            secao_preco = str("%.2f" % round(item.preco, 2))[
                0:caracteres_por_item]
            quantidade_ponto = len(secao_descricao) + len(secao_preco)
            lista_final.append(
                secao_descricao + "." * (caracteres_por_item - quantidade_ponto) + secao_preco)

        return lista_final

    def get_usuario_by_cpf(self, cpf):
        usuario_resposta = None
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                usuario_resposta = usuario
        return usuario_resposta

    def adicionar_no_carrinho(self, codigo, quantidade):
        produto = self.produtos[codigo]
        self.carrinho[self.usuario_logado.cpf].append(Produto(
            descricao=produto.get_descricao(),
            preco=produto.get_preco(),
            quantidade=quantidade
        ))

    def remove_item_carrinho(self, codigo):
        del self.carrinho[self.usuario_logado.cpf][codigo]

    def is_email_unique(self, email):
        unique = True
        for usuario in self.usuarios:
            if usuario.email == email:
                unique = False
        return unique

    def is_cpf_unique(self, cpf):
        unique = True
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                unique = False
        return unique

    def is_nome_unique(self, nome):
        unique = True
        for usuario in self.usuarios:
            if usuario.nome == nome:
                unique = False
        return unique

    def get_saldo_carrinho(self):
        soma = 0

        for produto in self.carrinho[self.usuario_logado.cpf]:
            soma += produto.quantidade * produto.preco

        return soma

    def limpa_saldo(self):
        self.carrinho[self.usuario_logado.cpf] = []
