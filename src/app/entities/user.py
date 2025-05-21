from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated


class User:
    name = str; 
    agency = int; 
    account = int; 
    current_balance = 1000.00

    def __init__(self, name:str = None, agency:int = None, account:int = None, current_balance:float = None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("nome", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agencia", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 2:
            return (False, "Name must be at least 2 characters long")
        return (True, "")

    @staticmethod
    def validate_agency(agency:int) -> Tuple[bool,str]: #isso se refere ao "Falso e msg de erro

        if agency is None:
            return (False, "Agency is required")
        if type(agency) != int:
            return (False, "Agency must be an integer")
        if agency < 0:
            return (False, "Agency must be a positive number")
        if len(str(agency))<4:
            return(False, "Agency must be at least 4 digits long")
        return (True, "")

    @staticmethod
    def validate_account(account:int)-> Tuple[bool,str]:
        if account is None:
            return (False, "Account is required")
        if not isinstance(account, int):  # Verifica o tipo primeiro
            return (False, "Account must be an integer")
        if account<0:
            return(False, "Accont must be a positive number")
        if len(str(account))<6:
            return(False, "Account must be 6 digits long") 
        if len(str(account))>6:
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
    
    
    @staticmethod
    def validate_user_id(user_id:int) -> Tuple[bool,str]:
        if user_id is None:
            return (False, "User ID is required")
        if type(user_id) != int:
            return (False, "User ID must be an integer")
        if user_id < 0:
            return (False, "User ID must be a positive number")
        return (True, "")
    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
        
    def __eq__(self, value):
        return self.name == value.name and self.agency == value.agency and self.account == value.account and self.current_balance == value.current_balance
    
    def __repr__(self):
        return f"User(name={self.name}, agency={self.agency}, account={self.account}, current_balance={self.current_balance})"