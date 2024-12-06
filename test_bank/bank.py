def main():
    g=input('')
    print(value(g))


def value(greeting):
    if 'hello' in ((greeting.split())[0]).lower():
        return 0
    elif greeting[0] in 'hH':
        return 20
    else:
        return 100


if __name__ == "__main__":
    print(main())
