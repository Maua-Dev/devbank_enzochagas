from ..entities.usuarios import usuarios
from ..errors.entity_errors import ParamNotValidated
class UsuariosRepositoryMock:





    def __init__(self):
    
        
        self.usuarios = {
        1: usuarios(nome="Lucas", agencia=1234, conta=536277, current_balance=1000.00),
        2: usuarios(nome="Ana", agencia=5678, conta=123456, current_balance=2000.00),
        3: usuarios(nome="C", agencia=910, conta=234567, current_balance=1500.00),
        4: usuarios(nome="Maria", agencia=-1234, conta=34567890, current_balance=-2500.00),
    }
    def get_all_usuarios(self):
        return self.usuarios.values()
        
    def get_usuario(self, usuario_id:int):
        return self.usuarios.get(usuario_id, None)
        
    def create_usuario(self, usuario:usuarios, usuario_id:int): 
        self.usuarios[usuario_id] = usuario
        return usuario

    def delete_usuario(self, usuario_id:int) -> usuarios:
            usuario = self.usuarios.pop(usuario_id, None)
            return usuario
        
    def update_usuario(self, usuario_id:int, nome:str=None, agencia:int=None, conta:int=None, current_balance:float=None) -> usuarios:
        usuario = self.usuarios.get(usuario_id, None)
        if usuario is None:
            return None
            
        if nome is not None:
            usuario.nome = nome
        if agencia is not None:
            usuario.agencia = agencia
        if conta is not None:
            usuario.conta = conta
        if current_balance is not None:
            usuario.current_balance = current_balance
        self.usuarios[usuario_id] = usuario

        return usuario