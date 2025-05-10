from ..enums.transaction_type_enum import TransactionTypeEnum
from ..entities.transaction import Transaction

from typing import Dict, Optional, List 


class TransactionRepositoryMock:
    transaction: Dict[int, Transaction]
    
    def __init__(self):
        self.transaction = {
            1: Transaction(type_transaction=TransactionTypeEnum.DEPOSIT, value_transaction=100.0, current_balance=1000.0, time_stamp=1672531199),
            2: Transaction(type_transaction=TransactionTypeEnum.WITHDRAWAL, value_transaction=50.0, current_balance=950.0, time_stamp=1672531200),
        }
        
        #o monte de numeros do timestamp representa a quantidade de segundos que se passaram desde 
        # 1 de janeiro de 1970 até a efetualização da transação. 
        
    def get_all_transactions(self) -> List[Transaction]:
        return self.transaction.values()
    
    #Método para buscar uma trasnação por um id 
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        return self.transaction.get(transaction_id, None)
    
    
    def withdraw_money_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        self.transaction[transaction_id] = transaction
        return transaction
    
    def deposit_money_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        self.transaction[transaction_id] = transaction
        return transaction
    
    def current_balance_after_transaction(self, transaction: Transaction) -> float:
        if transaction.type_transaction == TransactionTypeEnum.WITHDRAWAL:
            transaction.current_balance -= transaction.value_transaction
        elif transaction.type_transaction == TransactionTypeEnum.DEPOSIT:
            transaction.current_balance += transaction.value_transaction
        else:
            raise ValueError("Invalid transaction type")
        return transaction.current_balance
     
     
    
    

    