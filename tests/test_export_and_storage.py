import os
import unittest
from playwright.sync_api import sync_playwright

class TestExportAndStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_standalone_html_export(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            sample_rc = """titulo(App Exportada)
seccion(sec_export)
encabezado(1)(App Standalone)
boton(btn_alert)(Aviso)
finseccion
avisar(btn_alert)(Hola)
"""
            page.fill("#rcEditor", sample_rc)
            page.wait_for_timeout(300)

            exported_html = page.evaluate("(code) => window.rcToHtml(code)", sample_rc)
            self.assertIn('<title>App Exportada</title>', exported_html)
            self.assertIn('<section id="sec_export">', exported_html)
            self.assertIn('addEventListener(\'click\', () => alert(\'Hola\'))', exported_html)

            browser.close()

if __name__ == "__main__":
    unittest.main()
