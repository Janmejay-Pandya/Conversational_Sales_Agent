from . import mongo

def customers():
    return mongo.db["customers"]

def products():
    return mongo.db["products"]

def inventory():
    return mongo.db["inventory"]

def promotions():
    return mongo.db["promotions"]

def sessions():
    return mongo.db["sessions"]

def orders():
    return mongo.db["orders"]

def stores():
    return mongo.db["stores"]
