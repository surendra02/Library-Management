# This file is resposible to some fields validations from form.
import re
def check_mobile(mobile):
    """check if mobile lenth is 10 and have only digit retur True!"""
    if len(mobile)==10:
        if mobile.isdigit():
            return True
        else:
            return False
    else:
        return False

def check_name(name):
    """if student name does not contains any digit True otherwise return false!"""
    a=re.findall("\d",name)
    if not a:
        return True
    else:
        return False
def check_email(email):
    """if email match this patern return True otherwise False!"""
    pattern = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if re.search(pattern,email):
        return True
    else:
        return False