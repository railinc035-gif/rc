import os
import unittest
from playwright.sync_api import sync_playwright

class TestRoundtripA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_html_to_rc_to_html(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            original_html = """
            <div id="panel_test" style="background-color: #1a202c; color: #ffffff; padding: 20px; border-radius: 8px;">
              <h1>App de Prueba A</h1>
              <p>Texto informativo</p>
              <button id="btn_click">Hacer clic</button>
            </div>
            """

            # 1. HTML -> RC
            rc_out = page.evaluate("(html) => window.htmlToRc(html)", original_html)
            self.assertIn("contenedor(panel_test)", rc_out)
            self.assertIn("boton(btn_click)(Hacer clic)", rc_out)

            # 2. RC -> HTML
            html_back = page.evaluate("(rc) => window.rcToHtml(rc)", rc_out)
            self.assertIn('id="panel_test"', html_back)
            self.assertIn('App de Prueba A', html_back)
            self.assertIn('id="btn_click"', html_back)

            browser.close()

if __name__ == "__main__":
    unittest.main()
