from django.template import Library
from django.core.exceptions import ObjectDoesNotExist

register = Library()

@register.filter
def where_date(flights,searchdate):
    return filter(lambda flight:flight.date==searchdate,flights)