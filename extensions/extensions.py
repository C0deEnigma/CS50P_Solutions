F=input('File name:')
f=''
l=len(F)
for i in range(5,0,-1):
    f=f+F[-i].lower()
if '.gif' in f:
    print('image/gif')
elif '.jpg' in f:
    print('image/jpeg')
elif '.jpeg' in f:
    print('image/jpeg')
elif '.png' in f:
    print('image/png')
elif '.txt' in f:
    print('text/plain')
elif '.zip' in f:
    print('application/zip')
elif '.pdf' in f:
    print('application/pdf')
else:
    print('application/octet-stream')
