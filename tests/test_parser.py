import unittest
import io
import os
from src.main import PdfText

class TestParser(unittest.TestCase):

    def setUp(self):
        pdf_parser = PdfText()

    def test_obj_init(self):
        pdf_parser = PdfText()
        self.assertIsInstance(pdf_parser, PdfText)
        self.assertEqual(pdf_parser.pdf_string, None)
        self.assertEqual(pdf_parser.pdf_words, None)

    def test_pdf_text(self):
        pdf_parser = PdfText()
        pdf_path = './test_data/howto-argparse.pdf'
        pdf_parser.pdf_path = pdf_path
        self.assertIsInstance(
            pdf_parser.parse_pdf(), io.StringIO
            )
        self.assertIsInstance(pdf_parser.get_pdf_string(), str)
        self.assertIsInstance(pdf_parser.pdf_string, str)
        self.assertTrue(len(pdf_parser.pdf_string) > 0)
        self.assertIsInstance(pdf_parser.get_pdf_words(), list)
        self.assertIsInstance(pdf_parser.pdf_words, list)
        self.assertGreater(len(pdf_parser.pdf_words), 0)

    def test_pdf_image(self):
        pdf_parser = PdfText()
        pdf_path = './test_data/test_pdf_image.pdf'
        pdf_parser.pdf_path = pdf_path
        pdf_parser.get_pdf_string()
        pdf_parser.get_pdf_words()
        self.assertIsInstance(
            pdf_parser.parse_pdf(), io.StringIO
            )
        self.assertIsInstance(pdf_parser.get_pdf_string(), str)
        self.assertIsInstance(pdf_parser.pdf_string, str)
        self.assertTrue(len(pdf_parser.pdf_string) > 0)
        self.assertIsInstance(pdf_parser.get_pdf_words(), list)
        self.assertIsInstance(pdf_parser.pdf_words, list)
        self.assertGreater(len(pdf_parser.pdf_words), 0)


    def test_pdf_to_text(self):
        pdf_parser = PdfText()
        pdf_path = './test_data/howto-argparse.pdf'
        pdf_parser.pdf_path = pdf_path
        pdf_parser.parse_pdf()
        txt_path = pdf_parser.write_to_text()
        self.assertTrue(os.path.isfile(txt_path))
        if os.path.isfile(txt_path):
            os.remove(txt_path)

if __name__ == '__main__':
    unittest.main()