import os
import unittest
from playwright.sync_api import sync_playwright

class TestRoundtripB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_rc_to_html_to_rc(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            original_rc = """titulo(Mi Titulo)
contenedor(box1)
encabezado(1)(Bienvenido)
texto(Texto de prueba)
boton(btn1)(Aceptar)
fincontenedor
"""

            # 1. RC -> HTML
            html_out = page.evaluate("(rc) => window.rcToHtml(rc)", original_rc)
            self.assertIn('<div id="box1">', html_out)
            self.assertIn('<h1>Bienvenido</h1>', html_out)
            self.assertIn('<button id="btn1">Aceptar</button>', html_out)

            # 2. HTML -> RC
            rc_back = page.evaluate("(html) => window.htmlToRc(html)", html_out)
            self.assertIn("contenedor(box1)", rc_back)
            self.assertIn("encabezado(1)(Bienvenido)", rc_back)
            self.assertIn("boton(btn1)(Aceptar)", rc_back)

            browser.close()

if __name__ == "__main__":
    unittest.main()
