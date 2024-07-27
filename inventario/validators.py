from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s must be a par number', 
            params={'value': value}
        )
