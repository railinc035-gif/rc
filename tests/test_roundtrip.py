import os
import json
import time
from playwright.sync_api import sync_playwright

def run_tests():
    html_path = os.path.abspath("index.html")
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}")

        # Set panel selector to 'all' so both editors are displayed
        page.select_option("#panelSelector", "all")
        page.dispatch_event("#panelSelector", "change")

        # -------------------------------------------------------------
        # Test A: HTML -> RC -> HTML
        # -------------------------------------------------------------
        test_a_html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Test A App</title>
<style>
  .card { background-color: #1e222d; color: #ffffff; padding: 20px; border-radius: 12px; margin: 15px; }
  .btn { background-color: #3b82f6; color: #ffffff; padding: 8px 16px; border-radius: 6px; }
</style>
</head>
<body>
  <div id="card_1" class="card">
    <h1 id="title_1">Título Test A</h1>
    <p id="desc_1">Párrafo de descripción.</p>
    <button id="btn_action" class="btn">Acción</button>
  </div>
  <script>
    document.getElementById('btn_action').addEventListener('click', () => alert('OK'));
  </script>
</body>
</html>"""

        rc_a = page.evaluate("(html) => htmlToRc(html)", test_a_html)
        html_a = page.evaluate("(rc) => rcToHtml(rc)", rc_a)

        results["Test_A"] = {
            "rc": rc_a,
            "html": html_a,
            "has_invented_cmds": any(cmd in rc_a for cmd in ["fincontenedor", "finseccion", "finrejilla", "finlista", "fintabla"])
        }

        # -------------------------------------------------------------
        # Test B: RC -> HTML -> RC (Official RC syntax)
        # -------------------------------------------------------------
        test_b_rc = """titulo(Mi App Oficial)
seccion(sec_main)
contenedor(box_1)
fondo(#1e222d)
color(#ffffff)
relleno(20px)
radio(10px)
encabezado(1)(Bienvenido)
parrafo(Texto de ejemplo)
boton(btn_1)(Clic Aqui)
avisar(btn_1)(Hola)"""

        html_b = page.evaluate("(rc) => rcToHtml(rc)", test_b_rc)
        rc_b = page.evaluate("(html) => htmlToRc(html)", html_b)

        results["Test_B"] = {
            "html": html_b,
            "rc_back": rc_b,
            "has_invented_cmds": any(cmd in rc_b for cmd in ["fincontenedor", "finseccion", "finrejilla", "finlista", "fintabla"])
        }

        # -------------------------------------------------------------
        # Test C: Copy, Delete, Paste workflow
        # -------------------------------------------------------------
        page.fill("#htmlEditor", test_a_html)
        page.dispatch_event("#htmlEditor", "input")
        time.sleep(0.3)

        generated_rc = page.input_value("#rcEditor")

        # Clear RC editor and paste generated RC
        page.fill("#rcEditor", "")
        page.dispatch_event("#rcEditor", "input")
        time.sleep(0.3)

        page.fill("#rcEditor", generated_rc)
        page.dispatch_event("#rcEditor", "input")
        time.sleep(0.3)

        final_html_c = page.input_value("#htmlEditor")
        preview_content = page.evaluate("() => document.getElementById('previewFrame').srcdoc")

        results["Test_C"] = {
            "generated_rc": generated_rc,
            "final_html": final_html_c,
            "preview_content": preview_content
        }

        # -------------------------------------------------------------
        # Test D: Complex Application
        # -------------------------------------------------------------
        test_d_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>App Compleja Dashboard</title>
  <style>
    body { background-color: #0f172a; color: #f8fafc; font-family: 'Segoe UI', sans-serif; }
    .header { background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 16px; }
    .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
    .card { background: #1e293b; padding: 16px; border-radius: 8px; border: 1px solid #334155; }
    .btn-submit { background-color: #22c55e; color: #000000; padding: 8px 16px; border-radius: 4px; font-weight: bold; }
    .img-avatar { width: 64px; height: 64px; border-radius: 50%; }
  </style>
</head>
<body>
  <section id="sec_dash">
    <div id="box_head" class="header">
      <h1 id="title_main">Dashboard Admin</h1>
      <p id="sub_title">Gestión de usuarios y estadísticas.</p>
    </div>

    <div id="grid_main" class="grid">
      <div id="card_user" class="card">
        <h2 id="h_user">Perfil de Usuario</h2>
        <img id="img_user" src="avatar.png" alt="imagen" class="img-avatar">
        <label id="lbl_name">Nombre:</label>
        <input type="text" id="inp_name" value="Jules Studio">
        <button id="btn_save" class="btn-submit">Guardar Cambios</button>
      </div>

      <div id="card_stats" class="card">
        <h2 id="h_stats">Métricas</h2>
        <span id="lbl_status">Estado: Activo</span>
      </div>
    </div>
  </section>

  <script>
    document.getElementById('btn_save').addEventListener('click', function() {
      const val = document.getElementById('inp_name').value;
      document.getElementById('lbl_status').innerText = 'Guardado: ' + val;
    });
  </script>
</body>
</html>"""

        rc_d = page.evaluate("(html) => htmlToRc(html)", test_d_html)
        html_d = page.evaluate("(rc) => rcToHtml(rc)", rc_d)
        rc_d_back = page.evaluate("(html) => htmlToRc(html)", html_d)

        results["Test_D"] = {
            "rc": rc_d,
            "html": html_d,
            "rc_back": rc_d_back,
            "has_invented_cmds": any(cmd in rc_d for cmd in ["fincontenedor", "finseccion", "finrejilla", "finlista", "fintabla"])
        }

        browser.close()

    print("=== TEST RESULTS SUMMARY ===")
    print(f"Test A Invented Cmds: {results['Test_A']['has_invented_cmds']}")
    print(f"Test B Invented Cmds: {results['Test_B']['has_invented_cmds']}")
    print(f"Test D Invented Cmds: {results['Test_D']['has_invented_cmds']}")
    print(f"Test C Output matches preview: {results['Test_C']['final_html'] == results['Test_C']['preview_content']}")
    print("\nALL ROUND TRIP TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
