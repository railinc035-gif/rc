import os
import unittest
from playwright.sync_api import sync_playwright

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_calculator_digit_accumulation(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")
            page.evaluate('() => localStorage.clear()')
            page.reload()
            page.wait_for_timeout(600)

            frame = page.frame_locator('#previewFrame')

            frame.locator('#btn_1').click()
            page.wait_for_timeout(100)
            frame.locator('#btn_2').click()
            page.wait_for_timeout(100)
            frame.locator('#btn_3').click()
            page.wait_for_timeout(100)

            val = frame.locator('#inp_disp').input_value()
            self.assertEqual(val, '123')
            browser.close()

    def test_calculator_clear_button(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")
            page.evaluate('() => localStorage.clear()')
            page.reload()
            page.wait_for_timeout(600)

            frame = page.frame_locator('#previewFrame')

            frame.locator('#btn_5').click()
            page.wait_for_timeout(100)
            frame.locator('#btn_clr').click()
            page.wait_for_timeout(100)

            val = frame.locator('#inp_disp').input_value()
            self.assertEqual(val, '')
            browser.close()

    def test_calculator_zero_division(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")
            page.evaluate('() => localStorage.clear()')
            page.reload()
            page.wait_for_timeout(600)

            frame = page.frame_locator('#previewFrame')

            frame.locator('#btn_8').click()
            page.wait_for_timeout(100)
            frame.locator('#btn_div').click()
            page.wait_for_timeout(100)

            val = frame.locator('#inp_disp').input_value()
            self.assertIn('Error: División por cero', val)
            browser.close()

if __name__ == "__main__":
    unittest.main()
