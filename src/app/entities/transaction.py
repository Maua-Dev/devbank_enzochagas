from typing import Tuple
from src.app.errors.entity_errors import ParamNotValidated

class Transaction:
    type = str 
    value = float
    current_balance = float
    time_stamp = float 
    
    def __init__(self, type:str = None, value:float = None, current_balance:float = None, time_stamp:float = None):
        validate_type = self.validate_type(type)
        if validate_type[0] is False:
            raise ParamNotValidated("type", validate_type[1])
        self.type = type
        
        validate_value = self.validate_value(value)
        if validate_value[0] is False:
            raise ParamNotValidated("value", validate_value[1])
        self.value = value
        
        vaidate_current_balance = self.validate_current_balance(current_balance)
        if vaidate_current_balance[0] is False:
            raise ParamNotValidated("current_balance", vaidate_current_balance[1])
        self.current_balance = current_balance
        
        validate_time_stamp = self.validate_time_stamp(time_stamp)
        if validate_time_stamp[0] is False:
            raise ParamNotValidated("time_stamp", validate_time_stamp[1])
        self.time_stamp = time_stamp
        
        
    @staticmethod
    def validate_type(type:str) -> Tuple[bool,str]:
        if type is None:
            return (False, "Type is required")
        if type not in ["deposit", "withdrawal"]:
            return (False, "Type must be either 'deposit' or 'withdrawal'")
        return (True, "")
    
    