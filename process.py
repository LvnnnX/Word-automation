from library import *
PATH = Path(__file__).parent

def get_docs(docs):
    docs = DocxTemplate(PATH / docs)
    return docs

