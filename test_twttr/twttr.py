def main():
    s=input()
    return shorten(s)


def shorten(word):
    s=''
    for i in word:
        if i not in 'aieouAEIOU':
            s+=i
    return s


if __name__ == "__main__":
    main()
