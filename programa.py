from entidades.usuario import Usuario

class Programa:
    usuarios = []
    usuario_logado = None
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = None
    
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


