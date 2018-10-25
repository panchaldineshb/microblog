import testdata

# Models declared

# REFER: https://pypi.org/project/python-testdata/
class Users(testdata.DictFactory):
    '''
    Users
    '''
    id = testdata.CountingFactory(10)
    firstname = testdata.FakeDataFactory('firstName')
    lastname = testdata.FakeDataFactory('lastName')
    address = testdata.FakeDataFactory('address')
    gender = testdata.RandomSelection(['female', 'male'])
    age = testdata.RandomInteger(10, 30) 

