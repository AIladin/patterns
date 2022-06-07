from builder import StringBuilder


def main():
    builder = StringBuilder()
    result = (
        builder.append_substring("Лабораторна ")
        .append_substring(" 3. ")
        .append_substring("Будівельник.")
        .insert_substring("робота", 12)
        .get_result()
    )
    print(result)


if __name__ == "__main__":
    main()
