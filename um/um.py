import re


def main():
    print(count(input("Text: ")))


def count(s):
    s1=re.sub(r'(\w+um)|(um\w+)','',s.lower())
    c=0
    for i in s1.split():
        if 'um' in i:
            c+=1
    return c


if __name__ == "__main__":
    main()
