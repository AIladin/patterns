import listener
from publisher import Publisher


def main():
    wc_listener = listener.WordCounterListener()
    line_length_listener = listener.MaxLengthListener()
    word_length_listener = listener.MaxWordLengthListener()
    listeners = [
        line_length_listener,
        word_length_listener,
        wc_listener,
    ]
    publisher = Publisher("input01.txt")

    for listener_obj in listeners:
        publisher.subscribe(listener_obj)

    with publisher:
        while publisher.update():
            pass
    print()
    print(f"Total words: {wc_listener.word_count}")
    print(
        f"Longest line: {line_length_listener.line}, {line_length_listener.max_length} chars."
    )
    print(
        f"Longest word: {word_length_listener.longest_word}, {len(word_length_listener.longest_word)}."
    )
    print(f"Source line: {word_length_listener.source_line}")


if __name__ == "__main__":
    main()
