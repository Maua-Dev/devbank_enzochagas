from ..entities.user import Users
from ..errors.entity_errors import ParamNotValidated
class UsuariosRepositoryMock:

    def __init__(self):
    
        
        self.users = {
        1: Users(nome="Lucas", agencia=1234, conta=536277, current_balance=1000.00),
        2: Users(nome="Ana", agencia=5678, conta=123456, current_balance=2000.00),
        3: Users(nome="C", agencia=910, conta=234567, current_balance=1500.00),
        4: Users(nome="Maria", agencia=-1234, conta=34567890, current_balance=-2500.00),
    }
        
    def get_all_users(self):
        return self.users.values()
    
    def get_user(self, user_id: int):
        return self.users.get(user_id, None)        
    
    def create_user(self, user: Users, user_id: int):
        self.users[user_id] = user
        return user
    
    def see_user_balance(self, user: Users):
        return user.current_balance    