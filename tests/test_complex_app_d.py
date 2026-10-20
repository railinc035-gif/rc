import os
import unittest
from playwright.sync_api import sync_playwright

class TestComplexAppD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_complex_app_fidelity(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            complex_rc = """titulo(Aplicacion Compleja)
seccion(sec_main)
contenedor(header_box)
encabezado(1)(Dashboard)
fincontenedor

rejilla(2)
contenedor(col1)
parrafo(Columna 1)
entrada(inp1)(100)
fincontenedor

contenedor(col2)
parrafo(Columna 2)
entrada(inp2)(200)
fincontenedor
finrejilla

etiqueta(lbl_res)(0)
boton(btn_calc)(Calcular)
sumar(btn_calc)(inp1)(inp2)(lbl_res)
finseccion
"""

            page.fill("#rcEditor", complex_rc)
            page.wait_for_timeout(300)

            frame = page.frame_locator("#previewFrame")
            self.assertEqual(frame.locator("h1").inner_text(), "Dashboard")

            frame.locator("#btn_calc").click()
            page.wait_for_timeout(200)

            self.assertEqual(frame.locator("#lbl_res").inner_text(), "300")

            browser.close()

if __name__ == "__main__":
    unittest.main()
