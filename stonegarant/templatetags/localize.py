# -*- coding: utf-8 -*-
from django import template

register = template.Library()

def num_memorials(value):
    number = int(value)
    loc_string = "ПАМЯТНИКОВ"
    modulo = number % 10

    if modulo == 1:
        loc_string = "ПАМЯТНИК"
    elif modulo in [2,3,4]:
        loc_string = "ПАМЯТНИКA"

    return u"%d %s" % (number, loc_string)

register.filter('num_memorials', num_memorials)