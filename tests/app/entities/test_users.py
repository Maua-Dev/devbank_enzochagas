import pytest
from src.app.entities.user import Users
from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated


class Test_usuarios: 
    def Teste_Usuario(self):
      users = Users("teste", 0000, 111111, 1000.00) 
      assert users.nome=="teste"
      assert users.conta == 0000
      assert users.agencia == 111111
      assert users.current_balance == 1000

    def test_users_name_is_none(self):
       with pytest.raises(ParamNotValidated):
          Users(conta=2222, agencia=123456, current_balance=1000)

    def teste_users_conta_is_none(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", agencia=123456, current_balance=1000)

    def teste_users_agencia_is_none(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", conta=1234, current_balance=1000)

    def teste_users_current_balance_is_none(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", conta=1234, agencia=123456)

    def teste_users_name_is_not_string(self):
       with pytest.raises(ParamNotValidated):
          Users(nome=1234, conta=1234, agencia=123456, current_balance=1000)

    def teste_users_conta_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", conta="1234", agencia=123456, current_balance=1000)

    def teste_users_agencia_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", conta=1234, agencia="abc", current_balance=1000)

    def teste_users_current_balance_is_not_float(self):
       with pytest.raises(ParamNotValidated):
          Users(nome="enzo", conta=1234, agencia=123456, current_balance="1000.00")

    def teste_users_name_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            Users(nome="e", conta=1234, agencia=123456, current_balance=1000)
   
    def teste_users_agencia_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            Users(nome="enzo", conta=1234, agencia=123, current_balance=1000)  

    def teste_users_conta_is_too_short(self): 
          with pytest.raises(ParamNotValidated):
               Users(nome="enzo", conta=12, agencia=123456, current_balance=1000)    
       
    def teste_users_current_balance_is_negative(self):
         with pytest.raises(ParamNotValidated):
            Users(nome="enzo", conta=1234, agencia=123456, current_balance=-1000)
    