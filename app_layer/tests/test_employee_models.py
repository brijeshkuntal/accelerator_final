from django.test import TestCase
from app_layer.models import Employee


class EmployeeTestCase(TestCase):
    employee_data_list = [{
        "empName": "Testing 1",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }, {
        "empName": "Testing 2",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }, {
        "empName": "Testing 3",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }, {
        "empName": "Testing 4",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }, {
        "empName": "Testing 5",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }, {
        "empName": "Testing 6",
        "empDOJ": "2021-01-22",
        "empDescription": "Testing",
        "empCategory": "Employee",
        "empCity": "Jaipur",
        "empOfficeVenue": "Jaipur"
    }
    ]

    @classmethod
    def setUpTestData(cls):
        employee_obj_list = []
        for employee_data in cls.employee_data_list:
            employee_obj_list.append(Employee(empName=employee_data['empName'],
                                              empDOJ=employee_data['empDOJ'],
                                              empDescription=employee_data['empDescription'],
                                              empCategory=employee_data['empCategory'],
                                              empCity=employee_data['empCity'],
                                              empOfficeVenue=employee_data['empOfficeVenue']))
        Employee.objects.bulk_create(employee_obj_list)

    def tearDown(self):
        Employee.objects.all().delete()

    # Test case 1
    def test_data_length(self):
        self.assertEqual(len(Employee.objects.all()), 6)

    # Test case 2
    def test_check_date(self):
        self.assertEqual(str(Employee.objects.all()[0].empDOJ), '2021-01-22')

    # Test case 3
    def test_check_name(self):
        self.assertQuerysetEqual(Employee.objects.filter(empName='Testing 7'),[])

    # Test case 4
    def test_check_instance(self):
        self.assertEqual(self.employee_data_list[0]["empName"], Employee.objects.all()[0].empName)

    # Test case 5
    def test_check_length(self):
        self.assertEqual(len(Employee.objects.all()), len(self.employee_data_list))

    # Test case 6
    def test_instance_after_delete(self):
        self.tearDown()
        self.assertQuerysetEqual(Employee.objects.all(),[])

