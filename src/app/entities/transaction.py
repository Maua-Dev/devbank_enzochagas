from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum

class Transaction:
    type_transaction : TransactionTypeEnum 
    value_transaction : float
    current_balance : float
    time_stamp : float 
    
    def __init__(self, type_transaction: TransactionTypeEnum = None, value_transaction:float = None, current_balance:float = None, time_stamp:float = None):
        
        
            validate_type = self.validate_type(type_transaction)
            if validate_type[0] is False:
                raise ParamNotValidated("type_transaction", validate_type[1])
            self.type_transaction = type_transaction
            
            validate_value = self.validate_value(value_transaction)
            if validate_value[0] is False:
                raise ParamNotValidated("value_transaction", validate_value[1])
            self.value_transaction = value_transaction
            
            vaidate_current_balance = self.validate_current_balance(current_balance)
            if vaidate_current_balance[0] is False:
                raise ParamNotValidated("current_balance", vaidate_current_balance[1])
            self.current_balance = current_balance
            
            validate_time_stamp = self.validate_time_stamp(time_stamp)
            if validate_time_stamp[0] is False:
                raise ParamNotValidated("time_stamp", validate_time_stamp[1])
            self.time_stamp = time_stamp
            
     
     
     
     
        
    @staticmethod
    def validate_type(type_transaction: TransactionTypeEnum) -> Tuple[bool,str]:
        if type_transaction is None:
            return (False, "Type is required")
        if type(type_transaction) != TransactionTypeEnum:
            return (False, "Type must be a TransactionTypeEnum")
        return (True, "")
    @staticmethod 
    def validate_value( value_transaction:float) -> Tuple[bool,str]:
        if value_transaction is None:
            return (False, "Value is required")
        if not isinstance(value_transaction, float):
            return (False, "Value must be a float")
        if value_transaction <= 0:
            return (False, "Value must be a positive number")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance:float) -> Tuple[bool,str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if not isinstance(current_balance, float):
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a non-negative number")
        return (True, "")
    
    @staticmethod 
    def validate_time_stamp(time_stamp:int) -> Tuple[bool,str]:
        if time_stamp is None:
            return (False, "Time stamp is required")
        if not isinstance(time_stamp, int):
            return (False, "Time stamp must be a integer")
        return (True, "")
    
    @staticmethod
    def validate_transaction_id(transaction_id:int) -> Tuple[bool,str]:
        if transaction_id is None:
            return (False, "Transaction ID is required")
        if not isinstance(transaction_id, int):
            return (False, "Transaction ID must be an integer")
        if transaction_id < 0:
            return (False, "Transaction ID must be a positive number")
        return (True, "")
    
    
    def to_dict(self):
            return {
                'type_transaction': self.type_transaction.value,
                'value_transaction': self.value_transaction,
                'current_balance': self.current_balance,
                'time_stamp': self.time_stamp
            }
            
            
            
    def __str__(self):
        return f"Transaction(type_transaction={self.type_transaction}, value_transaction={self.value_transaction}, current_balance={self.current_balance}, time_stamp={self.time_stamp})"
    
    def __repr__(self):
        return f"Transaction(type_transaction={self.type_transaction}, value_transaction={self.value_transaction}, current_balance={self.current_balance}, time_stamp={self.time_stamp})"
    