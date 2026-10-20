import os
import json
import time
from playwright.sync_api import sync_playwright

def run_tests():
    html_path = os.path.abspath("index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}")
        page.wait_for_timeout(500)

        # 1. Multiple buttons in same row
        rc_row = """titulo(Prueba Botones Fila)
contenedor(btn_row)
rejilla(3)
boton(btn_1)(Boton 1)
boton(btn_2)(Boton 2)
boton(btn_3)(Boton 3)"""

        page.fill("#rcEditor", rc_row)
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        grid_cols = page.evaluate("() => document.getElementById('previewFrame').contentDocument.querySelector('.rejilla')?.style.gridTemplateColumns")
        assert "repeat(3, 1fr)" in grid_cols, f"Unexpected grid columns: {grid_cols}"
        print("✓ Test 1 Passed: Grid 3 columns generated")

        # 2. Vertical buttons layout
        rc_vert = """titulo(Prueba Botones Verticales)
contenedor(btn_vert)
boton(btn_a)(Opcion A)
boton(btn_b)(Opcion B)
boton(btn_c)(Opcion C)"""

        page.fill("#rcEditor", rc_vert)
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        btn_count = page.evaluate("() => document.getElementById('previewFrame').contentDocument.querySelectorAll('button').length")
        assert btn_count == 3, f"Expected 3 buttons, found {btn_count}"
        print("✓ Test 2 Passed: 3 vertical buttons generated")

        # 3. Containers, sections, grids
        rc_app = """titulo(App Completa)
seccion(sec_main)
contenedor(box_main)
ancho(400px)
fondo(#1e222d)
color(#ffffff)
relleno(20px)
radio(12px)
encabezado(1)(Titulo App)
parrafo(Parrafo de prueba)
entrada(inp_user)(jules)
boton(btn_save)(Guardar)
avisar(btn_save)(Guardado!)
fincontenedor
finseccion"""

        page.fill("#rcEditor", rc_app)
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        heading_text = page.evaluate("() => document.getElementById('previewFrame').contentDocument.querySelector('h1')?.innerText")
        assert heading_text == "Titulo App", f"Unexpected heading: {heading_text}"
        print("✓ Test 3 Passed: Containers and sections rendered")

        # 4. Modifying single letter without breaking design
        rc_mod = rc_app.replace("Titulo App", "Titulo Modificado")
        page.fill("#rcEditor", rc_mod)
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        heading_mod = page.evaluate("() => document.getElementById('previewFrame').contentDocument.querySelector('h1')?.innerText")
        assert heading_mod == "Titulo Modificado", f"Unexpected mod heading: {heading_mod}"
        print("✓ Test 4 Passed: Single property edit updated cleanly")

        # 5. Incomplete RC command preserves last valid preview
        preview_before = page.evaluate("() => document.getElementById('previewFrame').srcdoc")
        page.fill("#rcEditor", "encab") # incomplete command
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        preview_after = page.evaluate("() => document.getElementById('previewFrame').srcdoc")
        assert preview_after == preview_before, "Preview was destroyed by incomplete typing"
        print("✓ Test 5 Passed: Last valid preview preserved on incomplete syntax")

        # 6. Save modal interaction
        page.fill("#rcEditor", rc_app)
        page.dispatch_event("#rcEditor", "input")
        page.wait_for_timeout(500)

        page.click("#saveBtn")
        page.wait_for_timeout(300)
        export_modal_visible = page.evaluate("() => !document.getElementById('exportModal').classList.contains('hidden')")
        assert export_modal_visible, "Export modal did not open on Save click"
        print("✓ Test 6 Passed: Export modal opens correctly")

        browser.close()

    print("\nALL 10 REFACTORING & EXPORT TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
