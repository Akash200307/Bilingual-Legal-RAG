from bs4 import element
from unstructured.partition.pdf import partition_pdf
from llama_index.readers.file import UnstructuredReader


def partitioning(file_path):
    try:
        reader=UnstructuredReader()
        print("Started processing ......")
        elements=partition_pdf(
            filename=file_path,
            strategy="hi_res",
            infer_table_structure=True,
            extract_images_in_pdf=False,
            ocr_languages="eng"
        )
    except FileNotFoundError:
        return "File not found error"
    return elements



