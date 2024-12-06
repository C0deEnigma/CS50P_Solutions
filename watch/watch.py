import re
def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search('iframe .*src="https?://(?:www.)?youtube.com/embed/(.+)".*></iframe>',s):
        u=match.group(1)
        return f'https://youtu.be/{u}'


if __name__ == "__main__":
    main()
