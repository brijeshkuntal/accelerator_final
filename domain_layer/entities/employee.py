import graphene
import datetime


class EmployeeEntity:
    """Employee Entity """
    empID: graphene.Int = int()
    empName: graphene.String = str()
    empDOJ: graphene.Date = datetime.date.today()
    empDescription: graphene.String = str()
    empCategory: graphene.String = str()
    empCity: graphene.String = str()
    empOfficeVenue: graphene.String = str()
