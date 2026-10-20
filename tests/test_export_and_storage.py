import os
import json
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

            rc_code = """
titulo(App Exportada)
seccion(sec_export)
encabezado(1)(App Standalone)
boton(btn_alert)(Aviso)
avisar(btn_alert)(Hola)
finseccion
"""
            exported_html = page.evaluate('(code) => window.rcToHtml(code)', rc_code)
            self.assertIn("<!DOCTYPE html>", exported_html)
            self.assertIn("<title>App Exportada</title>", exported_html)
            self.assertIn("<h1>App Standalone</h1>", exported_html)
            self.assertIn("addEventListener('click', () => alert(\"Hola\"))", exported_html)
            browser.close()

    def test_legacy_local_storage_migration(self):
        legacy_data = {
            'files': [
                ['proyecto.rc', {'type': 'rc', 'content': 'titulo(Proyecto Migrado)\nparrafo(Exito)'}],
                ['index.html', {'type': 'html', 'content': ''}]
            ],
            'active': {'rc': 'proyecto.rc', 'html': 'index.html'},
            'panelMode': 'rc-html'
        }

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            page.evaluate('legacy => localStorage.setItem("rc_studio_state", legacy)', json.dumps(legacy_data))
            page.reload()
            page.wait_for_timeout(500)

            rc_val = page.evaluate('() => document.getElementById("rcEditor").value')
            self.assertIn("Proyecto Migrado", rc_val)
            browser.close()

if __name__ == "__main__":
    unittest.main()
