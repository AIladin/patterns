from handler import file_handler


def init_handlers() -> file_handler.FileHandler:
    root_handler = file_handler.JPG_Handler()

    root_handler.set_next(file_handler.JPG_Handler()).set_next(
        file_handler.PNG_Handler()
    ).set_next(file_handler.DOCX_Handler()).set_next(
        file_handler.DOCX_Handler()
    ).set_next(
        file_handler.XLS_Handler()
    ).set_next(
        file_handler.XLSX_Handler()
    ).set_next(
        file_handler.PPTX_Handler()
    ).set_next(
        file_handler.PDF_Handler()
    )
    return root_handler


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
