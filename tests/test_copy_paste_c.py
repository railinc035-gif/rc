import os
import unittest
from playwright.sync_api import sync_playwright

class TestCopyPasteC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_copy_clear_paste_flow(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            sample_rc = """titulo(Prueba C)
contenedor(card_c)
encabezado(2)(Titulo C)
boton(btn_c)(Ejecutar)
fincontenedor
"""

            # 1. Enter RC code into editor
            page.fill("#rcEditor", sample_rc)
            page.wait_for_timeout(300)

            frame = page.frame_locator("#previewFrame")
            self.assertEqual(frame.locator("h2").inner_text(), "Titulo C")

            # 2. Copy RC code
            copied_code = page.input_value("#rcEditor")

            # 3. Clear editor
            page.fill("#rcEditor", "")
            page.wait_for_timeout(300)

            # 4. Paste copied code back
            page.fill("#rcEditor", copied_code)
            page.wait_for_timeout(300)

            # 5. Verify live preview
            self.assertEqual(frame.locator("h2").inner_text(), "Titulo C")
            self.assertEqual(frame.locator("#btn_c").inner_text(), "Ejecutar")

            browser.close()

if __name__ == "__main__":
    unittest.main()
