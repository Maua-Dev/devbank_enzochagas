from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.main import get_all_items, get_item, create_item, delete_item, update_item
from src.app.repo.item_repository_mock import ItemRepositoryMock
from src.app.entities.user import User
from src.app.main import get_user, get_all_users, see_user_balance, see_user_name, see_user_agency, see_user_account 
from src.app.repo.user_repository_mock import UsersRepositoryMock
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.main import get_all_transactions, get_transaction, withdraw_money_transaction, deposit_money_transaction, current_balance_after_transaction

class Test_Main:
    def test_get_all_items(self):
        repo = ItemRepositoryMock()
        response = get_all_items()
        assert all([item_expect.to_dict() == item for item_expect, item in zip(repo.items.values(), response.get("items"))]) 
        
    def test_get_item(self):
        repo = ItemRepositoryMock()
        item_id = 1
        response = get_item(item_id=item_id)
        assert response == {
            'item_id' : item_id,
            'item': repo.items.get(item_id).to_dict()
        }
        
    def test_get_item_id_is_none(self):
        
        item_id = None
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
    
    def test_get_item_id_is_not_int(self):
        item_id = '1'
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
            
    def test_get_item_id_is_not_positive(self):
        item_id = -1
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
            
    def test_create_item(self):
        repo = ItemRepositoryMock()
        
        body = {
            'item_id': 0,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        response = create_item(request=body)
        assert response == {'item_id': 0,'item': {'admin_permission': False, 'item_type': 'TOY', 'name': 'test', 'price': 1.0}}
    
    def test_create_item_conflict(self):
        repo = ItemRepositoryMock()
        
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
    
    def test_create_item_missing_id(self):
        body = {
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
        
    def test_create_item_id_is_not_int(self):
        body = {
            'item_id': '0',
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
    
    def test_create_item_id_is_not_positive(self):
        body = {
            'item_id': -1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_missing_type(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_item_type_is_not_string(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 1,
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_item_type_is_not_valid(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'test',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_param_not_validated(self):
        body = {
            'item_id': 1,
            'name': '',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False,
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_delete_item(self):
        body = {
            "item_id": 1
        }
        response = delete_item(request=body)
        assert response == {'item_id': 1, 'item': {'name': 'Barbie', 'price': 48.9, 'item_type': 'TOY', 'admin_permission': False}}
        
    def test_delete_item_missing_id(self):
        with pytest.raises(HTTPException) as err:
            delete_item(request={})
            
    def test_delete_item_id_is_not_int(self):
        body = {
            "item_id": '1'
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_id_not_found(self):
        body = {
            "item_id": 100
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_id_not_positive(self):
        body = {
            "item_id": -100
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_without_admin_permission(self):
        body = {
            "item_id": 4
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_update_item(self):
        body = {
            "item_id": 2,
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        response = update_item(request=body)
        assert response == {'item_id': 2, 'item': {'name': 'test', 'price': 1.0, 'item_type': 'TOY', 'admin_permission': False}}
        
    def test_update_item_missing_id(self):
        body = {
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
    
    def test_update_item_id_is_not_int(self):
        body = {
            "item_id": "1",
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_not_positive(self):
        body = {
            "item_id": -1,
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_not_found(self):
        body = {
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_without_admin_permission(self):
        body = {
            "item_id": 4,
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
    
    def test_update_item_type_not_string(self):
        body = {
            "name": "test",
            "price": 1.0,
            "item_type": 1,
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_type_not_valid(self):
        
        body = {
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_get_all_users(self):
        repo = UsersRepositoryMock()
        response = get_all_users()
        assert all([user_expect.to_dict() == user for user_expect, user in zip(repo.users.values(), response.get("users"))])
    
    def test_get_user(self):
        repo = UsersRepositoryMock()
        user_id = 1
        response = get_user(user_id=user_id)
        assert response == {
            'user_id' : user_id,
            'user': repo.users.get(user_id).to_dict()
        }
        
    def test_get_user_id_is_none(self):
        user_id = None
        with pytest.raises(HTTPException) as err:
            get_user(user_id=user_id)
            
    def test_get_user_id_is_not_int(self):
        user_id = '1'
        with pytest.raises(HTTPException) as err:
            get_user(user_id=user_id)
            
    def test_get_user_id_is_not_positive(self):
        user_id = -1
        with pytest.raises(HTTPException) as err:
            get_user(user_id=user_id)
            
    def test_see_user_balance(self):
        repo_user = UsersRepositoryMock()
        user_id = 1
        response = see_user_balance(user_id)
        assert response == {
            'user_id' : user_id,
            'user_balance': repo_user.users.get(user_id).current_balance
        }
    
    def test_see_user_balance_id_is_none(self):
        user_id = None
        with pytest.raises(HTTPException) as err:
            see_user_balance(user_id)
            
    def test_see_user_balance_id_is_not_int(self):
        user_id = '1'
        with pytest.raises(HTTPException) as err:
            see_user_balance(user_id)
            
    def test_see_user_agency(self):
        repo_user = UsersRepositoryMock()
        user_id = 1
        response = see_user_agency(user_id)
        assert response == {
            'user_id' : user_id,
            'user_agency': repo_user.users.get(user_id).agency
        }
        
    def test_see_user_agency_id_is_none(self):
        user_id = None
        with pytest.raises(HTTPException) as err:
            see_user_agency(user_id)
            
    def test_see_user_agency_id_is_not_int(self):
        user_id = '1'
        with pytest.raises(HTTPException) as err:
            see_user_agency(user_id)
            
    def test_see_user_account(self):
        repo_user = UsersRepositoryMock()
        user_id = 1
        response = see_user_account(user_id)
        assert response == {
            'user_id' : user_id,
            'user_account': repo_user.users.get(user_id).account
        }
        
    def test_see_user_account_id_is_none(self):
        user_id = None
        with pytest.raises(HTTPException) as err:
            see_user_account(user_id)
            
    def test_see_user_account_id_is_not_int(self):
        user_id = '1'
        with pytest.raises(HTTPException) as err:
            see_user_account(user_id)
            
    
    def test_see_user_name(self):
        repo_user = UsersRepositoryMock()
        user_id = 1
        response = see_user_name(user_id)
        assert response == {
            'user_id' : user_id,
            'user_name': repo_user.users.get(user_id).name
        }
        
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMock()
        response = get_all_transactions()
        assert all([transaction_expect.to_dict() == transaction for transaction_expect, transaction in zip(repo.transaction.values(), response.get("transactions"))])
        
    def test_get_transaction(self):
        repo = TransactionRepositoryMock()
        transaction_id = 1
        response = get_transaction(transaction_id=transaction_id)
        assert response == {
            'transaction_id' : transaction_id,
            'transaction': repo.transaction.get(transaction_id).to_dict()
        }
        
    def test_get_transaction_id_is_none(self):
        transaction_id = None
        with pytest.raises(HTTPException) as err:
            get_transaction(transaction_id=transaction_id)
            
    def test_get_transaction_id_is_not_int(self):
        transaction_id = 'Vitor Soller se ver me avise kkkkk'
        with pytest.raises(HTTPException) as err:
            get_transaction(transaction_id=transaction_id)
            
    def test_get_transaction_id_is_not_positive(self):
        transaction_id = -1
        with pytest.raises(HTTPException) as err:
            get_transaction(transaction_id=transaction_id)   
            
    def test_withdraw_money_transaction(self):
        repo = TransactionRepositoryMock()
        
        body = {
            'transaction_id': 0,
            'type_transaction': 'WITHDRAWAL',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        response = withdraw_money_transaction(request=body)
        assert response == {'transaction_id': 0, 'transaction': {'type_transaction': 'WITHDRAWAL', 'value_transaction': 100.0, 'current_balance': 1000.0, 'time_stamp': 1672531199}}
        
    def test_withdraw_money_transaction_conflict(self):
        repo = TransactionRepositoryMock()
        
        body = {
            'transaction_id': 1,
            'type_transaction': 'WITHDRAWAL',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            withdraw_money_transaction(request=body)
            
    def test_withdraw_money_transaction_missing_id(self):
        body = {
            'type_transaction': 'WITHDRAWAL',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            withdraw_money_transaction(request=body)
            
    def test_deposit_money_transaction(self):
        repo = TransactionRepositoryMock()
        
        body = {
            'transaction_id': 4,
            'type_transaction': 'DEPOSIT',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        response = deposit_money_transaction(request=body)
        assert response == {'transaction_id': 4, 'transaction': {'type_transaction': 'DEPOSIT', 'value_transaction': 100.0, 'current_balance': 1000.0, 'time_stamp': 1672531199}}
        
    def test_deposit_money_transaction_conflict(self):  
        repo = TransactionRepositoryMock()
        
        body = {
            'transaction_id': 1,
            'type_transaction': 'DEPOSIT',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            deposit_money_transaction(request=body)
            
    def test_deposit_money_transaction_missing_id(self):
        body = {
            'type_transaction': 'DEPOSIT',
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            deposit_money_transaction(request=body)
            
    def test_current_balance_after_transaction(self):
        repo = TransactionRepositoryMock()
        
        body = {
            'transaction_id': 1,  
            'transaction_type': 'DEPOSIT',         
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        response = current_balance_after_transaction(request=body)
        assert response == {'transaction_id': 1, 'current_balance': 1100.0}
        
    def test_current_balance_after_transaction_missing_id(self):
        body = {
            'transaction_type': 'DEPOSIT',         
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            current_balance_after_transaction(request=body)
            
    def test_current_balance_after_transaction_id_is_not_int(self):
        body = {
            'transaction_id': '1',
            'transaction_type': 'DEPOSIT',         
            'value_transaction': 100.0,
            'current_balance': 1000.0,
            'time_stamp': 1672531199
        }
        with pytest.raises(HTTPException) as err:
            current_balance_after_transaction(request=body)
            
            