from handler import file_handler


def init_handlers() -> file_handler.FileHandler:
    handlers = [
        file_handler.JPG_Handler(),
        file_handler.PNG_Handler(),
        file_handler.DOCX_Handler(),
        file_handler.DOC_Handler(),
        file_handler.XLS_Handler(),
        file_handler.XLSX_Handler(),
        file_handler.PPTX_Handler(),
        file_handler.PDF_Handler(),
    ]

    for prev_h, next_h in zip(handlers[:-1], handlers[1:]):
        prev_h.set_next(next_h)

    return handlers[0]


def main():
    files = [
        "image.jpg",
        "image.png",
        "document.docx",
        "document.doc",
        "table.xls",
        "table.xlsx",
        "presentation.pptx",
        "document.pdf",
    ]
    root_handler = init_handlers()
    for file in files:
        root_handler.open(file)


if __name__ == "__main__":
    main()
