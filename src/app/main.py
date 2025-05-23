from fastapi import FastAPI, HTTPException

from mangum import Mangum

from .environments import Environments

from .repo.item_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item

from .entities.user import User

from .repo.user_repository_mock import UsersRepositoryMock

from .entities.transaction import Transaction

from .repo.transaction_repository_mock import TransactionRepositoryMock

from .enums.transaction_type_enum import TransactionTypeEnum



app = FastAPI()

repo_item = Environments.get_item_repo()()



@app.get("/items/get_all_items")
def get_all_items():
    items = repo_item.get_all_items()
    return {
        "items": [item.to_dict() for item in items]
    }

@app.get("/items/{item_id}")
def get_item(item_id: int):
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo_item.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    return {
        "item_id": item_id,
        "item": item.to_dict()    
    }

@app.post("/items/create_item", status_code=201)
def create_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo_item.get_item(item_id)
    if item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    
    name = request.get("name")
    price = request.get("price")
    item_type = request.get("item_type")
    if item_type is None:
        raise HTTPException(status_code=400, detail="Item type is required")
    if type(item_type) != str:
        raise HTTPException(status_code=400, detail="Item type must be a string")
    if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
        raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
    admin_permission = request.get("admin_permission")
    
    try:
        item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    item_response = repo_item.create_item(item, item_id)
    return {
        "item_id": item_id,
        "item": item_response.to_dict()    
    }
    
@app.delete("/items/delete_item")
def delete_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo_item.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    item_deleted = repo_item.delete_item(item_id)
    
    return {
        "item_id": item_id,
        "item": item_deleted.to_dict()    
    }
    
@app.put("/items/update_item")
def update_item(request: dict):
    item_id = request.get("item_id")
    
    validation_item_id = Item.validate_item_id(item_id=item_id)
    if not validation_item_id[0]:
        raise HTTPException(status_code=400, detail=validation_item_id[1])
    
    item = repo_item.get_item(item_id)
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    if item.admin_permission == True:
        raise HTTPException(status_code=403, detail="Item Not found")
    
    name = request.get("name")
    price = request.get("price")
    admin_permission = request.get("admin_permission")
    
    item_type_value = request.get("item_type")
    if item_type_value != None:
        if type(item_type_value) != str:
            raise HTTPException(status_code=400, detail="Item type must be a string")
        if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
            raise HTTPException(status_code=400, detail="Item type is not a valid one")
        item_type = ItemTypeEnum[item_type_value]
    else:
        item_type = None
        
    item_updated = repo_item.update_item(item_id, name, price, item_type, admin_permission)
    
    return {
        "item_id": item_id,
        "item": item_updated.to_dict()    
    }
    
repo_user = Environments.get_user_repo()()

@app.get("/users/get_all_users")
def get_all_users():
    users = repo_user.get_all_users()
    return {
            "users": [user.to_dict() for user in users]
        } 
    
    
      
@app.get("/users/get_user/{user_id}")
def get_user(user_id: int):
    validation_user_id = User.validate_user_id(user_id=user_id)
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return {
        "user_id": user_id,
        "user": user.to_dict()    
    }


    
    
@app.get("/user/see_user_balance/{user_id}")
def see_user_balance(user_id: int):
    validation_user_id = User.validate_user_id(user_id=user_id)
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return {
        "user_id": user_id,
        "user_balance": repo_user.see_user_balance(user)    
    }
    
@app.get("/user/see_user_name/{user_id}")
def see_user_name(user_id: int):    
    validation_user_id = User.validate_user_id(user_id=user_id)
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return {
        "user_id": user_id,
        "user_name": repo_user.see_user_name(user)    
    }
    
@app.get("/user/see_user_agency")  
def see_user_agency(user_id: int):
    validation_user_id = User.validate_user_id(user_id=user_id)
    
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return {
        "user_id": user_id,
        "user_agency": repo_user.see_user_agency(user)    
    }
@app.get("/user/see_user_account")
def see_user_account(user_id: int):
    validation_user_id = User.validate_user_id(user_id=user_id)
    if not validation_user_id[0]:
        raise HTTPException(status_code=400, detail=validation_user_id[1])
    
    user = repo_user.get_user(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return {
        "user_id": user_id,
        "user_account": repo_user.see_user_account(user)    
    }
    

repo_transaction = Environments.get_transaction_repo()() 


   
@app.get("/transactions/get_all_transactions")
def get_all_transactions():
    transactions = repo_transaction.get_all_transactions()
    return {
        "transactions": [transaction.to_dict() for transaction in transactions]
    }
    
@app.get("/transactions/get_transaction/{transaction_id}")
def get_transaction(transaction_id: int):
    validation_transaction_id = Transaction.validate_transaction_id(transaction_id=transaction_id)
    if not validation_transaction_id[0]:
        raise HTTPException(status_code=400, detail=validation_transaction_id[1])
    
    transaction = repo_transaction.get_transaction(transaction_id)
    
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction Not found")
    
    return {
        "transaction_id": transaction_id,
        "transaction": transaction.to_dict()    
    }
    
@app.post("/transactions/withdraw_money_transaction", status_code=201)
def withdraw_money_transaction(request: dict):
    transaction_id = request.get("transaction_id")
    
    validation_transaction_id = Transaction.validate_transaction_id(transaction_id=transaction_id)
    if not validation_transaction_id[0]:
        raise HTTPException(status_code=400, detail=validation_transaction_id[1])
    
    transaction = repo_transaction.get_transaction(transaction_id)
    if transaction is not None:
        raise HTTPException(status_code=409, detail="Transaction already exists")
    
    if transaction_id is None:
        raise HTTPException(status_code=400, detail="Transaction ID is required")
    
    type_transaction = request.get("type_transaction")
    value_transaction = request.get("value_transaction")
    current_balance = request.get("current_balance")
    time_stamp = request.get("time_stamp")
    
    try:
        transaction = Transaction(type_transaction=TransactionTypeEnum[type_transaction], value_transaction=value_transaction, current_balance=current_balance, time_stamp=time_stamp)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    transaction_response = repo_transaction.withdraw_money_transaction(transaction, transaction_id)
    return {
        "transaction_id": transaction_id,
        "transaction": transaction_response.to_dict()    
    }

@app.post("/transactions/deposit_money_transaction", status_code=201)
def deposit_money_transaction(request: dict):
    transaction_id = request.get("transaction_id")
    
    validation_transaction_id = Transaction.validate_transaction_id(transaction_id=transaction_id)
    if not validation_transaction_id[0]:
        raise HTTPException(status_code=400, detail=validation_transaction_id[1])
    
    transaction = repo_transaction.get_transaction(transaction_id)
    if transaction is not None:
        raise HTTPException(status_code=409, detail="Transaction already exists")
    
    type_transaction = request.get("type_transaction")
    value_transaction = request.get("value_transaction")
    current_balance = request.get("current_balance")
    time_stamp = request.get("time_stamp")
    
    try:
        transaction = Transaction(type_transaction=TransactionTypeEnum[type_transaction], value_transaction=value_transaction, current_balance=current_balance, time_stamp=time_stamp)
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    transaction_response = repo_transaction.deposit_money_transaction(transaction, transaction_id)
    return {
        "transaction_id": transaction_id,
        "transaction": transaction_response.to_dict()    
    }
    
@app.post("/transactions/current_balance_after_transaction")
def current_balance_after_transaction(request: dict):
    transaction_id = request.get("transaction_id")
    
    validation_transaction_id = Transaction.validate_transaction_id(transaction_id=transaction_id)
    if not validation_transaction_id[0]:
        raise HTTPException(status_code=400, detail=validation_transaction_id[1])
    
    transaction = repo_transaction.get_transaction(transaction_id)
    
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction Not found")
    
    return {
        "transaction_id": transaction_id,
        "current_balance": repo_transaction.current_balance_after_transaction(transaction)    
    }
   

handler = Mangum(app, lifespan="off")

    
