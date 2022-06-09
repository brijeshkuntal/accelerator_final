from graphene_django.utils.testing import GraphQLTestCase, graphql_query
import json


class EmployeeFeatureTestCase(GraphQLTestCase):
    @classmethod
    def setUpTestData(cls):
        response = graphql_query(
            query='''
            mutation($email:String!, $username:String!, $password:String!, $displayName:String!)
                {
                register(email:$email, username:$username, password: $password, displayName:$displayName)
                    {
                        success, token, refreshToken, user{username,displayName,email}
                    }
                }
            ''',
            op_name=None,
            variables={
                "email": "test@test.com",
                "password": "Testing@54321",
                "username": "TestUser",
                "displayName": "Test User"
            }
        )
        content = json.loads(response.content)
        cls.token = content['data']['register']['token']

        # adding data in for employee table
        graphql_query(
            """
            mutation firstmutation($empName:String!, $empCity:String!,  $empOfficeVenue:String!,
            $empDOJ:Date, $empDescription:String!,$empCategory:String!)
            {
             createEmployee(empName: $empName,empCity: $empCity, empOfficeVenue: $empOfficeVenue,
                empDOJ:$empDOJ, empDescription:$empDescription,
                empCategory:$empCategory)
                {
              employee {
                empName: empName
                empCity: empCity
                empOfficeVenue: empOfficeVenue
                empDOJ: empDOJ
                empDescription:empDescription
                empCategory:empCategory
                empID
              }
            }
            }
            """,
            op_name=None,
            variables={"empName": "a", "empCity": "k", "empOfficeVenue": "k", "empDOJ": "2022-03-07",
                       "empDescription": "j", "empCategory": "culture"},
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + cls.token
            }
        )

    # Test Case 1
    def test_create_user(self):
        response = self.query(
            """
            mutation firstmutation($empName:String!, $empCity:String!,  $empOfficeVenue:String!,
            $empDOJ:Date, $empDescription:String!,$empCategory:String!)
            {
             createEmployee(empName: $empName,empCity: $empCity, empOfficeVenue: $empOfficeVenue,
                empDOJ:$empDOJ, empDescription:$empDescription,
                empCategory:$empCategory)
                {
              employee {
                empName: empName
                empCity: empCity
                empOfficeVenue: empOfficeVenue
                empDOJ: empDOJ
                empDescription:empDescription
                empCategory:empCategory
                empID
              }
            }
            }
            """,
            op_name=None,
            variables={"empName": "a", "empCity": "k", "empOfficeVenue": "k", "empDOJ": "2022-03-07",
                       "empDescription": "j", "empCategory": "culture"},
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + self.token
            }
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertCountEqual(content['data']['createEmployee'], ['employee'])

    # Test Case 2
    def test_update_user(self):
        response = self.query(
        """
            mutation firstmutation($empID:Int!,$empName:String!)
            {
             updateEmployee(empID:$empID,empName: $empName)
                {
              employee {
                empName
                empOfficeVenue
                empID
              }
            }
            }
        """,
            op_name=None,
            variables={"empID":1,"empName": "newA"},
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + self.token
            }
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertCountEqual(content['data']['updateEmployee'], {'employee': {'empName': 'newA', 'empOfficeVenue': 'k', 'empID': '1'}})

    # Test Case 3
    def test_delete_user(self):
        response = self.query(
            """
                mutation firstmutation($empID:Int!)
                {
                 deleteEmployee(empID:$empID)
                    {
                  employee {
                          empID
                  }
                }
                }
            """,
            op_name=None,
            variables={"empID": 1},
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + self.token
            }
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertCountEqual(content['data']['deleteEmployee'],{'employee': None})

    # Test Case 4
    def test_check_get_all_employees(self):
        response = self.query(
            '''
             query{
              allEmployees{
                empID
                empName
                empCity
                empOfficeVenue
              }
            }
            ''',
            op_name=None,
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + self.token
            }
        )
        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertCountEqual(content['data']['allEmployees'],
                              [{'empID': '1', 'empName': 'a', 'empCity': 'k', 'empOfficeVenue': 'k'}])

    # Test Case 5
    def test_check_get_employee(self):
        response = self.query(
            '''
            query MyQuery {
                employees(empID: 1) {
                    empName
                    empID
                }
            }
            ''',
            op_name=None,
            headers={
                "HTTP_AUTHORIZATION": "Bearer " + self.token
            }
        )
        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertCountEqual(content['data']['employees'],
                              [{'empID': '1', 'empName': 'a'}])
