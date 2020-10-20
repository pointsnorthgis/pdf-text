'''
    Program for reading through PDF documents and returning
    a list of words.
'''
import os
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


class PdfText(object):
    def __init__(self, pdf_path=None, password=None):
        self.pdf_path = pdf_path
        self.pdf_password = password
        self.pdf_string = None
        self.pdf_words = []

    def get_pdf_string(self):
        string_io = self.parse_pdf()
        self.pdf_string = string_io.getvalue()
        return self.pdf_string

    def get_pdf_words(self):
        if self.pdf_string is None:
            self.get_pdf_string()
        self.pdf_words = self.pdf_string.split()
        return self.pdf_words

    def parse_pdf(self):
        output_string = StringIO()
        with open(self.pdf_path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                
            return output_string
