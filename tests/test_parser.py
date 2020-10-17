import unittest
import io
from src.main import PdfText

class TestParser(unittest.TestCase):

    def setUp(self):
        self.pdf_parser = PdfText()

    def test_pdf_text(self):
        pdf_path = r'C:\dev\pdf-text\test_data\howto-argparse.pdf'
        self.pdf_parser.pdf_path = pdf_path
        self.assertIsInstance(
            self.pdf_parser.parse_pdf(), io.StringIO
            )
        self.pdf_parser.get_pdf_string()
        self.assertIsInstance(self.pdf_parser.pdf_string, str)
        self.pdf_parser.get_pdf_words()
        self.assertIsInstance(self.pdf_parser.pdf_words, list)


if __name__ == '__main__':
    unittest.main()