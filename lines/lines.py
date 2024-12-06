import sys
if len(sys.argv)!=2:
    if len(sys.argv)==1:
        sys.exit('Too few command-line arguments')
    else:
        sys.exit('Too many command-line arguments')
else:
    try:
        with open(sys.argv[1]) as file:
            if sys.argv[1].split('.')[1] != 'py':
                sys.exit('Not a Python file')
            data=file.readlines()
            s=0
            for line in data:
                if line.lstrip() == '' or line.lstrip()[0]=='#':
                    pass
                else:
                    s+=1
            print(s)
    except FileNotFoundError:
        sys.exit('File does not exist')
