class UpdateEmployeeCommand:
    def __init__(self, request, emp):
        self.request = request
        self.emp = emp