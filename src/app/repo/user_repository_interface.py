from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from ..entities.user import User


class IUserRepository(ABC):
    
    
    def get_all_users(self) -> List[User]:
        '''
        Returns all the users in the database 
        '''
        pass
    
    def get_user(self, user_id: int) -> Optional[User]:
        '''
        Returns the user with the given id.
        If the user does not exist, returns None
        '''
        pass
    
    def see_user_balance(self, user: User) -> float:
        '''
        Returns the balance of the user
        '''
        pass
    
    def see_user_name(self, user: User) -> str:
        '''
        Returns the name of the user
        '''
        pass
    
    def see_user_agency(self, user: User) -> int:
        '''
        Returns the agency of the user
        '''
        pass
    
    def see_user_account(self, user: User) -> int:
        '''
        Returns the account of the user
        '''
        pass
    
    