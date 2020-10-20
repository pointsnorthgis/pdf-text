# pdf-text
Program for extracting text from pdf


Dependencies
--------
## [pytesseract](https://pypi.org/project/pytesseract/) 
An Optical Character Recognition (OCR) library that will extract text from images. This library requires the [Python Image Library (PIL)](https://pillow.readthedocs.io/en/stable/) to be installed on the system as well as [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which powers the character recognition. [pdf2image](https://github.com/Belval/pdf2image) converts PDFs to images that OCR can work on.

### Install PIL (Linux)
`~$> sudo apt-get install python3-pil`

`$ (env)> pip install pillow`

### Install tesseract (Linux)
`~$> sudo apt-get install tesseract-ocr`

`$ (env)> pip install tesseract`


## [pdfminer.six](https://github.com/pdfminer/pdfminer.six) 
This library can extract text from a pdf containing text that is not in image format.
`$ (env)> pip install pdfminer.six`


Other options for extracting text from PDFs are:
--------

[pdfplumber](https://github.com/jsvine/pdfplumber)

[textract](https://textract.readthedocs.io/en/stable/python_package.html)
