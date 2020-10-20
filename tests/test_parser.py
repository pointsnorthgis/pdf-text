import unittest
import io
from src.main import PdfText

class TestParser(unittest.TestCase):

    def setUp(self):
        self.pdf_parser = PdfText()

    def test_obj_init(self):
        self.assertIsInstance(self.pdf_parser, PdfText)
        self.assertEqual(self.pdf_parser.pdf_string, None)
        self.assertEqual(self.pdf_parser.pdf_words, None)

    def test_pdf_text(self):
        pdf_path = './test_data/howto-argparse.pdf'
        self.pdf_parser.pdf_path = pdf_path
        self.assertIsInstance(
            self.pdf_parser.parse_pdf(), io.StringIO
            )
        self.assertIsInstance(self.pdf_parser.get_pdf_string(), str)
        self.assertIsInstance(self.pdf_parser.pdf_string, str)
        self.assertTrue(len(self.pdf_parser.pdf_string) > 0)
        self.assertIsInstance(self.pdf_parser.get_pdf_words(), list)
        self.assertIsInstance(self.pdf_parser.pdf_words, list)
        self.assertTrue(len(self.pdf_parser.pdf_words) > 0)

    def test_pdf_image(self):
        pdf_path = './test_data/test_pdf_image.pdf'
        self.pdf_parser.pdf_path = pdf_path
        self.assertIsInstance(
            self.pdf_parser.parse_pdf(), io.StringIO
            )
        self.assertIsInstance(self.pdf_parser.get_pdf_string(), str)
        self.assertIsInstance(self.pdf_parser.pdf_string, str)
        self.assertIsInstance(self.pdf_parser.get_pdf_words(), list)
        self.assertIsInstance(self.pdf_parser.pdf_words, list)


if __name__ == '__main__':
    unittest.main()