import os
import unittest
from playwright.sync_api import sync_playwright

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_calculator_digit_and_clear(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            calc_rc = """titulo(Calculadora)
contenedor(c)
entrada(inp_disp)()
boton(btn_1)(1)
boton(btn_5)(5)
boton(btn_clr)(C)
fincontenedor
incrementar(btn_1)(inp_disp)(1)
incrementar(btn_5)(inp_disp)(5)
limpiar(btn_clr)(inp_disp)
"""
            page.fill("#rcEditor", calc_rc)
            page.wait_for_timeout(300)

            frame = page.frame_locator('#previewFrame')

            frame.locator('#btn_1').click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator('#inp_disp').input_value(), '1')

            frame.locator('#btn_5').click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator('#inp_disp').input_value(), '15')

            frame.locator('#btn_clr').click()
            page.wait_for_timeout(100)
            self.assertEqual(frame.locator('#inp_disp').input_value(), '')

            browser.close()

if __name__ == "__main__":
    unittest.main()
