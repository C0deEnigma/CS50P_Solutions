import re
s=input('What\'s your email adress? ')
if re.search(r'\w+@\w+\.(com|edu|org)',s):
    print('Valid')
else:
    print('Invalid')
