import unittest
from translator import frenchToEnglish, englishToFrench

class EnglishToFrenchTest(unittest.TestCase):
    """Testing english to french function"""
    def test1(self):
        """Testing for empty parameter"""
        self.assertEqual('"' + "Bonjour" + '"', englishToFrench(""))

    def test2(self):
        """Testing Hello. Should return Bonjour"""
        self.assertEqual('"' + "Bonjour" + '"', englishToFrench("Hello"))

class FrenchToEnglishTest(unittest.TestCase):
    """Testing french to englsih function"""
    def test1(self):
        """Testing for empty parameter"""
        self.assertEqual('"' + "My name is" + '"', frenchToEnglish(""))
    def test2(self):
        """Testing Bonjour. Should return Hello"""
        self.assertEqual('"' + "Hello" + '"', frenchToEnglish("Bonjour"))

unittest.main()
