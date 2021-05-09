from entidades.usuario import Usuario

class Programa:
    usuarios = []
    usuario_logado = None
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = None
    
    def add_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    