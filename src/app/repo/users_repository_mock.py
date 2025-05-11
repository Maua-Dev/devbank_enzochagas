from ..entities.user import User
from ..errors.entity_errors import ParamNotValidated
class UsersRepositoryMock:

    def __init__(self):
    
        
        self.users = {
        1: User(name="Lucas", agency=1234, account=536277, current_balance=1000.00),
        2: User(name="Ana", agency=5678, account=123456, current_balance=2000.00),
        3: User(name="Carlos", agency=2890, account=234567, current_balance=1500.00),
        4: User(name="Maria", agency=1234, account=345679, current_balance=2500.00),
    }
        
    def get_all_users(self):
        return self.users.values()
    
    def get_user(self, user_id: int):
        return self.users.get(user_id, None)        
    
    # def create_user(self, user: Users, user_id: int):
    #     self.users[user_id] = user
    #     return user
    
    def see_user_balance(self, user: User):
        return user.current_balance    
    
    def see_user_name(self, user: User):
        return user.name
    
    def see_user_agency(self, user: User):
        return user.agency  
    
    def see_user_account(self, user: User):
        return user.account