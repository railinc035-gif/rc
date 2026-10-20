import os
import unittest
from playwright.sync_api import sync_playwright

class TestButtonEvents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_interactive_buttons(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            rc_code = """titulo(Prueba Botones)
entrada(in_x)(50)
entrada(in_y)(10)
etiqueta(out_lbl)(0)

boton(b_sum)(Sumar)
sumar(b_sum)(in_x)(in_y)(out_lbl)

boton(b_sub)(Restar)
restar(b_sub)(in_x)(in_y)(out_lbl)

boton(b_clr)(Limpiar)
limpiar(b_clr)(in_x)
"""

            page.fill("#rcEditor", rc_code)
            page.wait_for_timeout(300)

            frame = page.frame_locator("#previewFrame")

            # Click sumar
            frame.locator("#b_sum").click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator("#out_lbl").inner_text(), "60")

            # Click restar
            frame.locator("#b_sub").click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator("#out_lbl").inner_text(), "40")

            # Click limpiar
            frame.locator("#b_clr").click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator("#in_x").input_value(), "")

            browser.close()

if __name__ == "__main__":
    unittest.main()
