from datetime import date

from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _


def validate_name(value):
    """
    Validator for validating name field .
    1) Input value should not be less than 5 characters
    2) Input value's first character must be a alphabet character
    """
    if len(value) < 5:
        raise ValidationError(

            _('%(value)s length is too short'),

            params={'value': value},

        )

    if not value[0].isalpha():
        raise ValidationError(

            _('%(value)s First character must be letter'),

            params={'value': value},

        )


def validate_date(value):
    """
    Validator for validating date field .
    Input value should not be of Date type
    """
    if not isinstance(value, date):
        raise ValidationError(

            _('%(value)s Given value is not a date type object'),

            params={'value': value},

        )


def validate_empDescription(value):
    """
    Validator for validating Description field .
    Input value should is mandatory field
    """
    if not value:
        raise ValidationError("Please provide description.")
