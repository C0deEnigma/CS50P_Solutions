l=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        d=input('Date: ')
        d=d.strip()
        if d.count('/')==2:
            f=d.split('/')
            month=f[0]
            date=f[1]
            year=f[2]
            if int(date)>31 or int(date)<1:
                continue
            if int(month)>12 or int(month)<1:
                    continue
        else:
            f=d.split()
            if f[0] in l:
                month=l.index(f[0])+1
                date=f[1].rstrip(',')
                year=f[2]
                if int(date)>31 or int(date)<1:
                    continue
                if int(month)>12 or int(month)<1:
                    continue
                if f[1][-1]!=',':
                    continue
            else:
                continue
    except ValueError:
        pass
    else:
        break
print(year+'-'+"{:02d}".format(int(month))+'-'+"{:02d}".format(int(date)))
