# pdf-text
## Program for extracting text from pdf


Dependencies
--------
[pytesseract](https://pypi.org/project/pytesseract/) is an Optical Character Recognition (OCR) library that will extract text from images. This library requires the [Python Image Library (PIL)](https://pillow.readthedocs.io/en/stable/) to be installed on the system as well as [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract), which powers the character recognition.pip

### Install PIL (Linux)
`
~$> sudo apt-get install python3-pil
$ (env)> pip install pillow
`

### Install tesseract (Linux)
`
~$> sudo apt-get install tesseract-ocr
$ (env)> pip install tesseract
`


[pdfminer.six](https://github.com/pdfminer/pdfminer.six) will extract text from a pdf containing text that is not in image format.



Other options for extracting text from PDFs are:
--------

[pdfplumber](https://github.com/jsvine/pdfplumber)

[textract](https://textract.readthedocs.io/en/stable/python_package.html)
