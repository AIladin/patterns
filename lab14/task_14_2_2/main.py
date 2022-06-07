import operations


def main():
    handler = operations.AddHandler()

    handler.set_next(operations.DivHandler()).set_next(
        operations.MulHandler()
    ).set_next(operations.SubHandler())

    tasks = [
        (1, 1, "+"),
        (2, 2, "*"),
        (10.0, 20.5, "-"),
        (100, 10, "/"),
        (0, 0, "*"),
    ]
    for task in tasks:
        handler.handle(*task)


if __name__ == "__main__":
    main()
