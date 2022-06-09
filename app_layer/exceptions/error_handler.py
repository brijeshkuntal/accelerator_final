class EmployeeError(Exception):
    """
    Handling employee level exception
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'EmployeeError, {0} '.format(self.message)
        else:
            return 'EmployeeError has been raised'


class EmployeeNotFoundException(Exception):
    """
    Raised when Employee does not Exists
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Employee with ID {0} - not Exist.'.format(self.message)
        else:
            return 'Employee not Found.'


class UserError(Exception):
    """
    Handling user level exception
    """

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'UserError, {0} '.format(self.message)
        else:
            return 'UserError has been raised'


