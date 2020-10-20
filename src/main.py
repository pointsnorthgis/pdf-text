'''
    Program for reading through PDF documents and returning
    a list of words.
'''
import os
from io import StringIO

from PIL import Image
import pytesseract

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
        self.pdf_words = None
        self.pdf_is_image = False

    def get_pdf_string(self):
        string_io = self.parse_pdf()
        pdf_string = string_io.getvalue()
        if len(pdf_string) > 0:
            self.pdf_string = pdf_string
            return self.pdf_string

        # see if pdf is image with text
        else:
            return None

    def get_pdf_words(self):
        if self.pdf_string is None:
            self.get_pdf_string()
        self.pdf_words = self.pdf_string.split()
        return self.pdf_words

    def parse_pdf(self):
        '''
        Open a PDF document and extract text from all pages
        '''
        output_string = StringIO()
        with open(self.pdf_path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(
                rsrcmgr, output_string, laparams=LAParams()
                )
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                
            return output_string

    def parse_pdf_image(self):
        '''
        Open a PDF that contains text embedded in 
        images and extract text using OCR
        '''
        return
