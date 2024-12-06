a=input('Input:')
s=''
for i in a:
    if i not in 'aieouAEIOU':
        s+=i
print('Output:',s)
