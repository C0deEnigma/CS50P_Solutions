import validators
s=input('What\'s your email adress? ')
if validators.email(s):
    print('Valid')
else:
    print('Invalid')

