import decorators
from printable_string import PrintableStrings


def main():
    hello = PrintableStrings("")
    hello = decorators.PostCommaDecorator(hello)
    hello = decorators.PostWordDecorator(hello, "World")
    hello = decorators.PostExclaimDecorator(hello)
    hello = decorators.PostEndlDeccorator(hello)
    hello = decorators.PreWordDecorator(hello, "Hello")
    hello.print()


if __name__ == "__main__":
    main()
