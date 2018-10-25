import testdata

# Models declared

# REFER: https://pypi.org/project/python-testdata/
class Devices(testdata.DictFactory):
    id = testdata.CountingFactory(10)
    name = testdata.FakeDataFactory('name')
    displayname = testdata.RandomLengthStringFactory()
    description = testdata.RandomLengthStringFactory()


