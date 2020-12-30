# pdf-text
Program for extracting text from pdf

Dependencies
--------
## [pytesseract](https://pypi.org/project/pytesseract/) 
An Optical Character Recognition (OCR) library that will extract text from images. This library requires the 
[Python Image Library (PIL)](https://pillow.readthedocs.io/en/stable/) to be installed on the system as well as 
[Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which powers the character recognition. 
[pdf2image](https://github.com/Belval/pdf2image) converts PDFs to images that OCR can work on.

### Install PIL (Linux)
`~$> sudo apt-get install python3-pil`

`$ (env)> pip install pillow`

### Install tesseract (Linux)
`~$> sudo apt-get install tesseract-ocr`

`$ (env)> pip install tesseract`

## pdf2image
[pdf2image](https://pdf2image.readthedocs.io/en/latest/installation.html) is a library that turn pages of a 
"scanned" PDF file into image files. These image files are required for perfoming OCR.

### Install pdf2image and dependancies
[Poppler](https://pypi.org/project/python-poppler/) is a requirement of pdf2image and must be installed as a 
python package and on the operating system along with cmake and libpoppler-cpp-dev.

Install Ubuntu 20.04 packages

```
~$> sudo apt-get install cmake
~$> sudo apt-get install -y libpoppler-cpp-dev
~$> sudo apt-get install poppler-utils
```

Install python package

`$ (env)> pip install python-poppler`


## [pdfminer.six](https://github.com/pdfminer/pdfminer.six) 
This library can extract text from a pdf containing text that is not in image format.
`$ (env)> pip install pdfminer.six`


Other options for extracting text from PDFs are:
--------

[pdfplumber](https://github.com/jsvine/pdfplumber)

[textract](https://textract.readthedocs.io/en/stable/python_package.html)


Usage
--------
### How to run PDF-TEXT using commandline
1. Install above dependancies
2. Using python run:
    `$ (env)> python --pdf /path/to/pdf/pdf_file.pdf --output /path/to/pdf/out_text.txt`