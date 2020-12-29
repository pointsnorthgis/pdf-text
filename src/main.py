'''
    Program for reading through PDF documents and returning
    a list of words.
'''
import os
from io import StringIO
import argparse

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import pdf2image

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
        if pdf_string == '\x0c':
            pdf_string = ''
        if len(pdf_string) > 0:
            self.pdf_string = pdf_string
            return self.pdf_string

        # see if pdf is image with text
        else:
            # run OCR to get text
            self.pdf_is_image = True
            self.ocr_pdf()
            return self.pdf_string

    def get_pdf_words(self):
        '''Create an array with all the words in the pdf'''
        unique_words = []
        if self.pdf_string is None:
            self.get_pdf_string()
        for word in self.pdf_string.split():
            if word not in unique_words:
                unique_words.append(word)
        self.pdf_words = unique_words
        return self.pdf_words

    def write_to_text(self, save_path=None):
        '''Create a text file from the pdf string'''
        if not save_path:
            save_path = os.path.splitext(self.pdf_path)[0] + '.txt'
        
        with open(save_path, "w") as txt_file:
            self.get_pdf_string()
            txt_file.write(self.pdf_string)

        return save_path

    def ocr_pdf(self):
        '''
        Use optical character recognition to extract text from pdf
        Step 1. Open PDF
        Step 2. Turn PDF page into image
        Step 3. Extract text from image creating string object
        Step 4. Repeat process for each PDF page building on string object
        '''
        pages = pdf2image.convert_from_path(self.pdf_path, 500)
        pdf_text = ''
        for image in pages:
            image = image.filter(ImageFilter.MedianFilter())
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2)
            image = image.convert('1')
            text = pytesseract.image_to_string(image)
            pdf_text = pdf_text + text
        self.pdf_string = pdf_text
        return self.pdf_string

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
        del in_file


if __name__ == "__main__":
    '''Commandline function for turning a pdf into a text file'''
    parser = argparse.ArgumentParser(description='Extract text from pdf.')
    parser.add_argument(
        '--pdf', type=str, nargs=1, required=True,
        help='''
        Use the --pdf flag to enter a PDF file to split into multiple pages 
        or enter multiple pdf documents to merge into a single pdf.
        '''
        )
    parser.add_argument(
        '--output', type=str, nargs=1, required=True,
        help='''
        Text file output location and name
        '''
        )
    args = parser.parse_args()
    pdf = args.pdf
    if pdf:
        for pdf_file in pdf:
            if os.path.splitext(pdf_file)[1].lower() != '.pdf':
                raise Exception("Only include PDF Files")
            if not os.path.isfile(pdf_file):
                raise Exception("Ensure PDF files exist")
    
    if len(args.output) > 1:
        raise Exception("Enter only one output text file")
    else:
        out_file = args.output[0]
        if os.path.splitext(out_file) != '.txt':
            raise Exception("Output file must be .txt format")

    pdf2txt = PdfText(pdf_path=pdf[0])
    pdf2txt.get_pdf_string()
    print("Complete")
    pass