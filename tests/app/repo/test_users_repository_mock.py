import pytest
from src.app.entities.user import Users
from src.app.repo.users_repository_mock import UsersRepositoryMock

class Test_UsersRepositoryMock:
    
    def test_get_all_users(self):
        repo = UsersRepositoryMock()
        assert all([user_expect == user for user_expect, user in zip(repo.users.values(), repo.get_all_users())])
        
    def test_get_user(self):
        repo = UsersRepositoryMock()
        user = repo.get_user(user_id=1)
        assert user == repo.users.get(1)
        
    # def test_create_user(self):
    #     repo = UsersRepositoryMock()
    #     len_before = len(repo.users)
    #     user = Users(nome="test", agencia=1234, conta=567899, current_balance=1000.00)
    #     repo.create_user(user=user, user_id=0)
        
    def test_see_user_balance(self):
        repo = UsersRepositoryMock()
        user = repo.get_user(user_id=1)
        balance = repo.see_user_balance(user=user)
        assert balance == user.current_balance
        
    def test_see_user_name(self):
        repo = UsersRepositoryMock()
        user = repo.get_user(user_id=1)
        name = repo.see_user_name(user=user)
        assert name == user.nome
        
    def test_see_user_agencia(self):
        repo = UsersRepositoryMock()
        user = repo.get_user(user_id=1)
        agencia = repo.see_user_agencia(user=user)
        assert agencia == user.agencia
        
    
    

