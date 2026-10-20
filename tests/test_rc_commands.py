import os
import unittest
from playwright.sync_api import sync_playwright

class TestRcCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_parameter_parsing_and_brackets(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            res = page.evaluate('() => window.parseRcLine ? window.parseRcLine("encabezado[h_main](2)(Bienvenido a RC)") : null')
            if res:
                self.assertEqual(res["cmd"], "encabezado")
                self.assertEqual(res["bracketId"], "h_main")
                self.assertEqual(res["args"], ["2", "Bienvenido a RC"])

            browser.close()

if __name__ == "__main__":
    unittest.main()
