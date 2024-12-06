import re
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$',ip):
        a=int(match.group(1))
        b=int(match.group(2))
        c=int(match.group(3))
        d=int(match.group(4))
        if a>255:
            return False
        elif b>255:
            return False
        elif c>255:
            return False
        elif d>255:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()
