import sys


class User(object):
    def __init__(self):
        pass

    # def insert(self):
    #     pass
    #
    # def get(self):
    #     pass


class Department(object):
    def __init__(self):
        pass

    # def insert(self):
    #     pass
    #
    # def get(self):
    #     pass


class SqlServerUser(User):
    def insert(self):
        print('SQL Server insert User ')

    def get(self):
        print('SQL Server get User ')


class SqlServerDepartment(Department):
    def insert(self):
        print('SQL Server insert Department ')

    def get(self):
        print('SQL Server get Department ')


class MysqlDepartment(Department):
    def insert(self):
        print('MySQL insert Department ')

    def get(self):
        print('MySQL get Department ')


class MysqlUser(User):
    def insert(self):
        print('MySQL insert User ')

    def get(self):
        print('MySQL get User ')


class Factory(object):
    def create_user(self):
        pass

    def create_department(self):
        pass


class DataAccess(Factory):
    def __init__(self, db='Mysql'):
        self.db = db

    def create_user(self):
        cls = getattr(sys.modules[__name__], '{}User'.format(self.db))
        return cls()

    def create_department(self):
        cls = getattr(sys.modules[__name__], '{}Department'.format(self.db))
        return cls()


class SqlServerFactory(Factory):
    def create_user(self):
        return SqlServerUser()

    def create_department(self):
        return SqlServerDepartment()


class MysqlFactory(Factory):
    def create_user(self):
        return MysqlUser()

    def create_department(self):
        return MysqlDepartment()


if __name__ == '__main__':
    factory = DataAccess('SqlServer')
    user = factory.create_user()
    dpt = factory.create_department()
    user.insert()
    user.get()
    dpt.insert()
    dpt.get()
