from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated


class Users:
    nome = str; 
    agencia = int; 
    conta = int; 
    current_balance = 1000.00

    def __init__(self, nome:str = None, agencia:int = None, conta:int = None, current_balance:float = None):
        validation_nome = self.validate_nome(nome)
        if validation_nome[0] is False:
            raise ParamNotValidated("nome", validation_nome[1])
        self.nome = nome

        validation_agencia = self.validate_agencia(agencia)
        if validation_agencia[0] is False:
            raise ParamNotValidated("agencia", validation_agencia[1])
        self.agencia = agencia

        validation_conta = self.validate_conta(conta)
        if validation_conta[0] is False:
            raise ParamNotValidated("conta", validation_conta[1])
        self.conta = conta

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_nome(nome: str) -> Tuple[bool, str]:
        if nome is None:
            return (False, "Name is required")
        if type(nome) != str:
            return (False, "Name musst be a string")
        if len(nome) < 2:
            return (False, "Nome must be at least 2 characters long")
        return (True, "")

    @staticmethod
    def validate_agencia(agencia:int) -> Tuple[bool,str]: #isso se refere ao "Falso e msg de erro

        if agencia is None:
            return (False, "Agency is required")
        if type(agencia) != int:
            return (False, "Agency must be an integer")
        if agencia < 0:
            return (False, "Agency must be a positive number")
        if len(str(agencia))<4:
            return(False, "Agency must be at least 4 digits long")
        return (True, "")

    @staticmethod
    def validate_conta(conta:int)-> Tuple[bool,str]:
        if conta is None:
            return (False, "Account is required")
        if not isinstance(conta, int):  # Verifica o tipo primeiro
            return (False, "Account must be an integer")
        if conta<0:
            return(False, "Accont must be a positive number")
        if len(str(conta))<6:
            return(False, "Account must be 6 digits long") 
        if len(str(conta))>6:
            return(False, "Account must be 6 digits long")
        return (True, "")
    
    
    @staticmethod
    def validate_current_balance(current_balance:float) -> Tuple[bool,str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a positive number")
        return (True, "")