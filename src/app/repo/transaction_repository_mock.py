from ..enums.transaction_type_enum import TransactionType
from ..entities.transaction import Transaction

from typing import Dict, Optional, List 


class TransactionRepositoryMock:
    transaction: Dict[int, Transaction]
    
    def __init__(self):
        self.transaction = {
            1: Transaction(type=TransactionType.DEPOSIT, value=100.0, current_balance=1000.0, time_stamp=1672531199),
            2: Transaction(type=TransactionType.WITHDRAWAL, value=50.0, current_balance=950.0, time_stamp=1672531200),
        }
        
        #o monte de numeros do timestamp representa a quantidade de segundos que se passaram desde 
        # 1 de janeiro de 1970 até a efetualização da transação. 
        
    def get_all_transactions(self) -> List[Transaction]:
        return self.transaction.values()
    
    #Método para buscar uma trasnação por um id 
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transaction.get(transaction_id, None)
    
    def create_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        self.transaction[transaction_id] = transaction
        return transaction
    
    def delete_transaction(self, transaction_id: int) -> Transaction:
        transaction = self.transaction.pop(transaction_id, None)
        return transaction
    
    def update_transaction(self, transaction_id:int, type:TransactionType=None, value:float=None, current_balance:float=None, time_stamp:float=None) -> Transaction:
        transaction = self.transaction.get(transaction_id, None)
        if transaction is None:
            return None
        
        if type is not None:
            transaction.type = type
        if value is not None:
            transaction.value = value
        if current_balance is not None:
            transaction.current_balance = current_balance
        if time_stamp is not None:
            transaction.time_stamp = time_stamp
        self.transaction[transaction_id] = transaction
        
        return transaction  