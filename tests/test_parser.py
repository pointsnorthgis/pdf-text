import unittest
from src.main import PdfText

class TestParser(unittest.TestCase):

    def setUp(self):
        self.pdf_parser = PdfText()

    def test_pdf_text(self):
        pdf_path = r'C:\dev\pdf-text\test_data\howto-argparse.pdf'
        self.pdf_parser.pdf_path = pdf_path
        result = self.pdf_parser.parse_pdf()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()