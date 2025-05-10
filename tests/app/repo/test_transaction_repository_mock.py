import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock

class Test_TransactionRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        assert all([transaction_expect == transaction for transaction_expect, transaction in zip(repo.transaction.values(), repo.get_all_transactions())])
        
    def test_get_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = repo.get_transaction(transaction_id=1)
        assert transaction == repo.transaction.get(1)
        
    def test_withdraw_money_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(type_transaction=TransactionTypeEnum.WITHDRAWAL, value_transaction=50.0, current_balance=950.0, time_stamp=1672531200)
        transaction_id = 3
        repo.withdraw_money_transaction(transaction=transaction, transaction_id=transaction_id)
        assert repo.transaction.get(transaction_id) == transaction    

    def test_deposit_money_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(type_transaction=TransactionTypeEnum.DEPOSIT, value_transaction=100.0, current_balance=1100.0, time_stamp=1672531201)
        transaction_id = 4
        repo.deposit_money_transaction(transaction=transaction, transaction_id=transaction_id)
        assert repo.transaction.get(transaction_id) == transaction
        
    def test_current_balance_after_transaction(self):
        repo = TransactionRepositoryMock()
        transaction = Transaction(type_transaction=TransactionTypeEnum.WITHDRAWAL, value_transaction=50.0, current_balance=950.0, time_stamp=1672531200)
        new_balance = repo.current_balance_after_transaction(transaction)
        assert new_balance == 900.0