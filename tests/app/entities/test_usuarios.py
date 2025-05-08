import pytest
from src.app.entities.usuarios import Usuarios
from src.app.errors.entity_errors import ParamNotValidated


class Test_usuarios: 
    def Teste_Usuario(self):
      usuario = Usuarios("teste", 0000, 111111, 1000.00) 
      assert usuario.nome=="teste"
      assert usuario.conta == 0000
      assert usuario.agencia == 111111
      assert usuario.current_balance == 1000

    def teste_usuario_name_is_none(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(conta=2222, agencia=123456, current_balance=1000)

    def teste_usuario_conta_is_none(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", agencia=123456, current_balance=1000)

    def teste_usuario_agencia_is_none(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", conta=1234, current_balance=1000)

    def teste_usuario_current_balance_is_none(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", conta=1234, agencia=123456)

    def teste_usuario_name_is_not_string(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome=1234, conta=1234, agencia=123456, current_balance=1000)

    def teste_usuario_conta_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", conta="1234", agencia=123456, current_balance=1000)

    def teste_usuario_agencia_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", conta=1234, agencia="abc", current_balance=1000)

    def teste_usuario_current_balance_is_not_float(self):
       with pytest.raises(ParamNotValidated):
          Usuarios(nome="enzo", conta=1234, agencia=123456, current_balance="1000.00")

    def teste_usuario_name_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            Usuarios(nome="e", conta=1234, agencia=123456, current_balance=1000)
   
    def teste_usuario_agencia_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            Usuarios(nome="enzo", conta=1234, agencia=123, current_balance=1000)  

    def teste_usuario_conta_is_too_short(self): 
          with pytest.raises(ParamNotValidated):
               Usuarios(nome="enzo", conta=12, agencia=123456, current_balance=1000)    
       
    def teste_usuario_current_balance_is_negative(self):
         with pytest.raises(ParamNotValidated):
            Usuarios(nome="enzo", conta=1234, agencia=123456, current_balance=-1000)
    


