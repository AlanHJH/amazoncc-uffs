class Produto:
    descricao = None
    preco = None
    quantidade = None
    def __init__(self, descricao="", preco=0, quantidade=0):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade


    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade        

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_preco(self, preco):
        self.preco = preco

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
    
    