from classes.validator import Validator

username = 'Re&val'
validator = Validator()
if validator.username_is_valid(username):
    print('Username is valid')
else:
    print('Username is invalid')