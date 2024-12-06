def main():
    t1=input('What time is it? ')
    t=convert(t1)
    if t>=7 and t<=8 :
        print('breakfast time')
    elif t>=12 and t<=13 :
        print('lunch time')
    elif t>=18 and t<=19 :
        print('dinner time')
    else:
        print('',end='')

def convert(time):
    h,m=time.split(':')
    return(int(h)+int(m)/60)
if __name__ == "__main__":
    main()
