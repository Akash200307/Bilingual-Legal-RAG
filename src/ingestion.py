from pathlib import  Path

import chromadb
from llama_index.core import  SimpleDirectoryReader
from llama_index.readers.file import  PyMuPDFReader
from llama_index.core.node_parser import SentenceSplitter


BASE_DIR=Path.cwd().parent
pdfs=BASE_DIR/"data"/"pdfs"/"1975"

def load_documents(pdf_dir,num_files_limit:int):

    reader=SimpleDirectoryReader(
        input_dir=pdf_dir,
        num_files_limit=num_files_limit,
        file_extractor={".PDF":PyMuPDFReader()},
        recursive=True
    )

    docs=reader.load_data()
    return docs
def chunking(doc,chunk_size=512,chunk_overlap=100):
    splitter=SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=""
    )
    nodes=splitter.get_nodes_from_documents(doc)
    print(f"Total chunks created are {len(nodes)}")
    return nodes































