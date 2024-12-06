c=input('camelCase: ')
p=''
for i in c:
    if i.isupper()==True:
        p=p+'_'+i.lower()
    else:
        p=p+i
print('snake_case: ',p)
