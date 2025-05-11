import pytest
from src.app.entities.user import User
from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated


class Test_usuarios: 
    def Teste_Usuario(self):
      users = User("teste", 0000, 111111, 1000.00) 
      assert users.name=="teste"
      assert users.account == 0000
      assert users.agency == 111111
      assert users.current_balance == 1000

    def test_users_name_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(account=2222, agency=123456, current_balance=1000)

    def teste_users_conta_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", agency=123456, current_balance=1000)

    def teste_users_agencia_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", account=1234, current_balance=1000)

    def teste_users_current_balance_is_none(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", account=1234, agency=123456)

    def teste_users_name_is_not_string(self):
       with pytest.raises(ParamNotValidated):
          User(name=1234, account=1234, agency=123456, current_balance=1000)

    def teste_users_conta_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", account="1234", agency=123456, current_balance=1000)

    def teste_users_agencia_is_not_int(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", account=1234, agency="abc", current_balance=1000)

    def teste_users_current_balance_is_not_float(self):
       with pytest.raises(ParamNotValidated):
          User(name="enzo", account=1234, agency=123456, current_balance="1000.00")

    def teste_users_name_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            User(name="e", account=1234, agency=123456, current_balance=1000)
   
    def teste_users_agencia_is_too_short(self):
         with pytest.raises(ParamNotValidated):
            User(name="enzo", account=1234, agency=123, current_balance=1000)  

    def teste_users_conta_is_too_short(self): 
          with pytest.raises(ParamNotValidated):
               User(name="enzo", account=12, agency=123456, current_balance=1000)    
       
    def teste_users_current_balance_is_negative(self):
         with pytest.raises(ParamNotValidated):
            User(name="enzo", account=1234, agency=123456, current_balance=-1000)
    