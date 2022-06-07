# Умова
14.2.1. Реалізуйте програму для (симуляції)
відкриття файлів різних типів. Реалізацію здійсніть використовуючи шаблон
проектування Ланцюжок обов’язків. 
# Результат
```
PNG_Handler is queued after JPG_Handler
DOCX_Handler is queued after PNG_Handler
DOC_Handler is queued after DOCX_Handler
XLS_Handler is queued after DOC_Handler
XLSX_Handler is queued after XLS_Handler
PPTX_Handler is queued after XLSX_Handler
PDF_Handler is queued after PPTX_Handler
JPG_Handler is opening image.jpg.
JPG_Handler not supported extension .png passing to next handler.
PNG_Handler is opening image.png.
JPG_Handler not supported extension .docx passing to next handler.
PNG_Handler not supported extension .docx passing to next handler.
DOCX_Handler is opening document.docx.
JPG_Handler not supported extension .doc passing to next handler.
PNG_Handler not supported extension .doc passing to next handler.
DOCX_Handler not supported extension .doc passing to next handler.
DOC_Handler is opening document.doc.
JPG_Handler not supported extension .xls passing to next handler.
PNG_Handler not supported extension .xls passing to next handler.
DOCX_Handler not supported extension .xls passing to next handler.
DOC_Handler not supported extension .xls passing to next handler.
XLS_Handler is opening table.xls.
JPG_Handler not supported extension .xlsx passing to next handler.
PNG_Handler not supported extension .xlsx passing to next handler.
DOCX_Handler not supported extension .xlsx passing to next handler.
DOC_Handler not supported extension .xlsx passing to next handler.
XLS_Handler not supported extension .xlsx passing to next handler.
XLSX_Handler is opening table.xlsx.
JPG_Handler not supported extension .pptx passing to next handler.
PNG_Handler not supported extension .pptx passing to next handler.
DOCX_Handler not supported extension .pptx passing to next handler.
DOC_Handler not supported extension .pptx passing to next handler.
XLS_Handler not supported extension .pptx passing to next handler.
XLSX_Handler not supported extension .pptx passing to next handler.
PPTX_Handler is opening presentation.pptx.
JPG_Handler not supported extension .pdf passing to next handler.
PNG_Handler not supported extension .pdf passing to next handler.
DOCX_Handler not supported extension .pdf passing to next handler.
DOC_Handler not supported extension .pdf passing to next handler.
XLS_Handler not supported extension .pdf passing to next handler.
XLSX_Handler not supported extension .pdf passing to next handler.
PPTX_Handler not supported extension .pdf passing to next handler.
PDF_Handler is opening document.pdf.
```
