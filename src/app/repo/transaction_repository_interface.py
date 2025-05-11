from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from ..entities.transaction import Transaction
from enums.transaction_type_enum import TransactionTypeEnum

class ITransactionRepository(ABC):
    
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        '''
        Returns all the transactions in the database 
        '''
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[Transaction]:
        '''
        Returns the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        pass
    
    def withdraw_money_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        '''
        Withdraws money from the user account
        '''
        pass
    
    def deposit_money_transaction(self, transaction: Transaction, transaction_id: int) -> Transaction:
        '''
        Deposit money from the user account
        
        '''
        
    def current_balance_after_transaction(self, transaction: Transaction) -> float:
        '''
        Returns the current balance after the transaction
        '''
        pass