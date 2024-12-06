def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d1=''
    l=len(d)
    for i in range(1,l):
        d1=d1+d[i]
    return float(d1)


def percent_to_float(p):
    p1=''
    l=len(p)
    for i in range (l-1):
        p1=p1+p[i]
    return (float(p1))/100



main()
