import os
from pymongo import MongoClient
from random import randint
from pprint import pprint
from models import Users, Roles
import testdata

#Step 2: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)

# Issue the serverStatus command and print the results
db = client.tododb

def add_users():
    for user in Users().generate(10): # let say we only want 10 users
        db.users.insert_one(user)
        print(user)
    print('finished creating users')
    

def add_roles():
    for role in Roles().generate(4): # let say we only want 4 roles
        db.roles.insert_one(role)
        print(role)
    print('finished creating roles')
    


if __name__ == '__main__':
    add_users()
    add_roles()
