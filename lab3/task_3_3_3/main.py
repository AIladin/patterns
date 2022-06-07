from clonable_builder import ClonableStringBuilder


def main():
    builder = ClonableStringBuilder()
    builder.append_substring("Лабораторна poбота 3. ").append_substring("Задача ")

    builder_2 = builder.clone()

    builder.append_substring("3.3.2.")
    builder_2.append_substring("3.3.3.")
    print(builder.get_result())
    print(builder_2.get_result())


if __name__ == "__main__":
    main()
