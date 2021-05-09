class Usuario:
    nome = ""
    cpf = None
    senha = ""
    email = ""
    def __init__(self, nome="", cpf=0, senha="", email=""):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.email = email

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_email(self):
        return self.email

    def set_senha(self, senha):
        self.senha = senha

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf 

    def set_email(self, email):
        self.email = email


