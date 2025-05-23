import pytest 
from ....src.app.entities.transaction import Transaction
from ....src.app.errors.entity_errors import ParamNotValidated
from ....src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_Transaction: 
    def test_transaction(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 1000.0, 1672531201)
        assert transaction.type_transaction == TransactionTypeEnum.DEPOSIT
        assert transaction.value_transaction == 100.0   
        assert transaction.current_balance == 1000.0
        assert transaction.time_stamp == 1672531201
        
    def test_transaction_dict(self):
        transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 1000.0, 1672531201)
        assert transaction.to_dict() == {'type_transaction': 'DEPOSIT', 'value_transaction': 100.0, 'current_balance': 1000.0, 'time_stamp': 1672531201}
    # A funçao to_dict() retorna um dicionário com os atributos da classe 
    
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(None, 100.0, 1000, 123456789)
            
    def test_transaction_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, None, 1000.0, 1672531201)
            
    def test_transaction_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, None, 1672531201)
            
    def test_transaction_time_stamp_is_none(self):
        with pytest.raises(ParamNotValidated): 
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 1000.0, None)
            
    def transaction_type_is_not_withdraw_or_deposit(self):
        with pytest.raises(ParamNotValidated):
            tarnsaction = Transaction("banana", 100.0, 1000.0, 1672531201)
            
    def test_transaction_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, "banana", 1000.0, 1672531201)
            
    def test_transaction_value_is_not_positive(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, -100.0, 1000.0, 1672531201)
            
    def test_transaction_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, "banana", 1672531201)
            
    def test_transaction_current_balance_is_not_positive(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, -1000.0, 1672531201)
            
    def test_transaction_time_stamp_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            transaction = Transaction(TransactionTypeEnum.DEPOSIT, 100.0, 1000.0, "banana")
            
        