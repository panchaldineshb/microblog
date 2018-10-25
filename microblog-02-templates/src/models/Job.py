import testdata

# Models declared

# REFER: https://pypi.org/project/python-testdata/
class Job(testdata.DictFactory):
    state = testdata.StatisticalValuesFactory([('pending', 90), ('error', 10)])
    assigned_user = testdata.ConditionalValueField('state', {'error': 'support'}, 'admin')
    description = testdata.RandomLengthStringFactory()

