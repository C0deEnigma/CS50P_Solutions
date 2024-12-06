def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    if not is_valid(plate):
        print("Invalid")


def is_valid(s):
    l=len(s)
    #Alphanumeric condn
    if not(s.isalnum()):
        return False
    #length range
    if l>6 or l<2:
        return False
    #first two chars letter
    for i in [0,1]:
        if not(s[i].isalpha()):
            return False
    p=-1
    for i in range(l):
        if s[i].isdigit():
            p=i
            #0 can't be first no
            if s[p]=='0':
                return False
            #last chars should be no
            for j in range(p,l):
                if not(s[j].isdigit()):
                    return False
            break
    #if no no is found it's valid
    if p==-1:
        return True
    return True

main()
