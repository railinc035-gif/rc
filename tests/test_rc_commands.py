import os
import unittest
from playwright.sync_api import sync_playwright

class TestRcCommands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.abspath("index.html")

    def test_75_commands_spec_exists(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            spec_count = page.evaluate("() => Object.keys(window.RC_COMMANDS_SPEC).length")
            self.assertEqual(spec_count, 75, f"Expected 75 commands in RC_COMMANDS_SPEC, found {spec_count}")
            browser.close()

    def test_parameter_parsing_and_brackets(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            res = page.evaluate('() => window.parseRcLine("encabezado[h_main](2)(Bienvenido a RC)")')
            self.assertEqual(res['cmd'], 'encabezado')
            self.assertEqual(res['bracketId'], 'h_main')
            self.assertEqual(res['args'], ['2', 'Bienvenido a RC'])
            browser.close()

    def test_nested_containers_and_closing(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            rc_code = """
seccion(sec_app)
contenedor(box_main)
encabezado(1)(Titulo)
fincontenedor
finseccion
"""
            html_out = page.evaluate('(code) => window.rcToHtml(code)', rc_code)
            self.assertIn('<section id="sec_app">', html_out)
            self.assertIn('<div id="box_main">', html_out)
            self.assertIn('<h1>Titulo</h1>', html_out)
            browser.close()

    def test_circular_inclusion_detection(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            # Define circular module files in JS context
            page.evaluate('''() => {
                window.rcToHtml("incluir(m1.rc)", new Set(["m1.rc"]));
            }''')

            rc_circular = "incluir(m1.rc)"
            html_out = page.evaluate('(code) => window.rcToHtml(code, new Set(["m1.rc"]))', rc_circular)
            self.assertIn("Inclusión circular detectada", html_out)
            browser.close()

    def test_unknown_command_warning(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{self.html_path}")

            rc_code = "comando_inexistente(123)"
            html_out = page.evaluate('(code) => window.rcToHtml(code)', rc_code)
            self.assertIn("Comando desconocido 'comando_inexistente'", html_out)
            browser.close()

if __name__ == "__main__":
    unittest.main()
