

class UserType(object):
    def __init__(self, name, created_date, updated_date):
        self.name = name
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return '{} is added successfully'.format(self.name)


