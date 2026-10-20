import re

with open("index.html", "r") as f:
    content = f.read()

script_pos = content.find("<script>")
html_head = content[:script_pos]

new_script = """<script>
(() => {
  // ==========================================
  // ESPECIFICACIÓN CENTRAL DE 75 COMANDOS RC
  // ==========================================
  const RC_COMMANDS_SPEC = {
    // Categoría I: Estructura y Contenido (Comandos 1 - 30)
    incluir: { cat: 1, name: 'incluir', params: ['archivo'], minArgs: 1, type: 'include', desc: 'Incluye otro archivo RC del proyecto' },
    titulo: { cat: 1, name: 'titulo', params: ['texto'], minArgs: 1, type: 'head', desc: 'Define el título de la página/aplicación' },
    seccion: { cat: 1, name: 'seccion', params: ['nombre'], minArgs: 0, type: 'container', tag: 'section', desc: 'Crea un contenedor tipo sección' },
    contenedor: { cat: 1, name: 'contenedor', params: ['id'], minArgs: 0, type: 'container', tag: 'div', desc: 'Crea un contenedor multipropósito' },
    rejilla: { cat: 1, name: 'rejilla', params: ['columnas'], minArgs: 1, type: 'container', tag: 'div', isGrid: true, desc: 'Crea una cuadrícula CSS Grid de N columnas' },
    linea: { cat: 1, name: 'linea', params: [], minArgs: 0, type: 'element', tag: 'hr', selfClosing: true, desc: 'Inserta una línea divisoria horizontal (<hr>)' },
    texto: { cat: 1, name: 'texto', params: ['mensaje'], minArgs: 1, type: 'element', tag: 'p', desc: 'Inserta un mensaje de texto libre' },
    encabezado: { cat: 1, name: 'encabezado', params: ['nivel', 'mensaje'], minArgs: 2, type: 'element', tag: 'h', desc: 'Inserta un encabezado jerárquico del 1 al 6' },
    parrafo: { cat: 1, name: 'parrafo', params: ['mensaje'], minArgs: 1, type: 'element', tag: 'p', desc: 'Inserta un párrafo de texto (<p>)' },
    negrita: { cat: 1, name: 'negrita', params: ['texto'], minArgs: 1, type: 'element', tag: 'b', desc: 'Aplica formato de texto en negrita (<b>)' },
    cursiva: { cat: 1, name: 'cursiva', params: ['texto'], minArgs: 1, type: 'element', tag: 'i', desc: 'Aplica formato de texto en cursiva (<i>)' },
    subrayado: { cat: 1, name: 'subrayado', params: ['texto'], minArgs: 1, type: 'element', tag: 'u', desc: 'Aplica formato de texto subrayado (<u>)' },
    etiqueta: { cat: 1, name: 'etiqueta', params: ['id', 'texto'], minArgs: 1, type: 'element', tag: 'span', desc: 'Crea una etiqueta identificable por ID' },
    bloque: { cat: 1, name: 'bloque', params: ['texto'], minArgs: 1, type: 'element', tag: 'div', desc: 'Inserta un bloque contenedor de texto' },
    cita: { cat: 1, name: 'cita', params: ['texto'], minArgs: 1, type: 'element', tag: 'blockquote', desc: 'Inserta una cita destacada (<blockquote>)' },
    codigo: { cat: 1, name: 'codigo', params: ['texto'], minArgs: 1, type: 'element', tag: 'code', desc: 'Inserta un fragmento de código (<code>)' },
    enlace: { cat: 1, name: 'enlace', params: ['url', 'texto'], minArgs: 2, type: 'element', tag: 'a', desc: 'Crea un hipervínculo (<a href="...">)' },
    imagen: { cat: 1, name: 'imagen', params: ['url'], minArgs: 1, type: 'element', tag: 'img', selfClosing: true, desc: 'Inserta una imagen (<img src="...">)' },
    listadesordenada: { cat: 1, name: 'listadesordenada', params: [], minArgs: 0, type: 'container', tag: 'ul', desc: 'Inicia una lista no ordenada (<ul>)' },
    listaordenada: { cat: 1, name: 'listaordenada', params: [], minArgs: 0, type: 'container', tag: 'ol', desc: 'Inicia una lista numerada (<ol>)' },
    elementolista: { cat: 1, name: 'elementolista', params: ['texto'], minArgs: 1, type: 'element', tag: 'li', desc: 'Inserta un elemento de lista (<li>)' },
    tabla: { cat: 1, name: 'tabla', params: [], minArgs: 0, type: 'container', tag: 'table', desc: 'Inicia una tabla de datos (<table>)' },
    filatabla: { cat: 1, name: 'filatabla', params: [], minArgs: 0, type: 'container', tag: 'tr', desc: 'Inicia una fila de tabla (<tr>)' },
    encabezadotabla: { cat: 1, name: 'encabezadotabla', params: ['texto'], minArgs: 1, type: 'element', tag: 'th', desc: 'Inserta una celda de encabezado (<th>)' },
    celdatabla: { cat: 1, name: 'celdatabla', params: ['texto'], minArgs: 1, type: 'element', tag: 'td', desc: 'Inserta una celda de datos (<td>)' },
    boton: { cat: 1, name: 'boton', params: ['id', 'texto'], minArgs: 1, type: 'element', tag: 'button', desc: 'Crea un botón interactivo' },
    etiquetacampo: { cat: 1, name: 'etiquetacampo', params: ['texto'], minArgs: 1, type: 'element', tag: 'label', desc: 'Crea una etiqueta de formulario (<label>)' },
    cargando: { cat: 1, name: 'cargando', params: [], minArgs: 0, type: 'element', tag: 'div', className: 'cargando', desc: 'Inserta un indicador visual de carga' },
    lienzo: { cat: 1, name: 'lienzo', params: ['id'], minArgs: 1, type: 'element', tag: 'canvas', desc: 'Crea un área de dibujo HTML5 Canvas' },
    areatexto: { cat: 1, name: 'areatexto', params: ['id', 'texto'], minArgs: 1, type: 'element', tag: 'textarea', desc: 'Crea un área de texto multilínea (<textarea>)' },

    // Categoría II: Estilo y Diseño Visual (Comandos 31 - 50)
    fondo: { cat: 2, name: 'fondo', params: ['color'], minArgs: 1, type: 'style', prop: 'background-color', desc: 'Establece el color de fondo del elemento' },
    color: { cat: 2, name: 'color', params: ['color'], minArgs: 1, type: 'style', prop: 'color', desc: 'Establece el color del texto' },
    letra: { cat: 2, name: 'letra', params: ['fuente'], minArgs: 1, type: 'style', prop: 'font-family', desc: 'Establece la familia tipográfica / fuente' },
    tamano: { cat: 2, name: 'tamano', params: ['px'], minArgs: 1, type: 'style', prop: 'font-size', desc: 'Establece el tamaño de letra en píxeles' },
    ancho: { cat: 2, name: 'ancho', params: ['px'], minArgs: 1, type: 'style', prop: 'width', desc: 'Establece el ancho del elemento' },
    alto: { cat: 2, name: 'alto', params: ['px'], minArgs: 1, type: 'style', prop: 'height', desc: 'Establece el alto del elemento' },
    gap: { cat: 2, name: 'gap', params: ['px'], minArgs: 1, type: 'style', prop: 'gap', desc: 'Establece el espaciado interno en rejillas' },
    margen: { cat: 2, name: 'margen', params: ['px'], minArgs: 1, type: 'style', prop: 'margin', desc: 'Establece el margen exterior' },
    relleno: { cat: 2, name: 'relleno', params: ['px'], minArgs: 1, type: 'style', prop: 'padding', desc: 'Establece el relleno interior (padding)' },
    radio: { cat: 2, name: 'radio', params: ['px'], minArgs: 1, type: 'style', prop: 'border-radius', desc: 'Establece el radio de bordes redondeados' },
    centrar: { cat: 2, name: 'centrar', params: [], minArgs: 0, type: 'style', action: 'center', desc: 'Alinea o centra horizontalmente' },
    alinearizquierda: { cat: 2, name: 'alinearizquierda', params: [], minArgs: 0, type: 'style', action: 'left', desc: 'Alinea el texto a la izquierda' },
    alinearderecha: { cat: 2, name: 'alinearderecha', params: [], minArgs: 0, type: 'style', action: 'right', desc: 'Alinea el texto a la derecha' },
    borde: { cat: 2, name: 'borde', params: ['color'], minArgs: 1, type: 'style', prop: 'border', desc: 'Establece el borde del elemento' },
    sombra: { cat: 2, name: 'sombra', params: ['nivel'], minArgs: 1, type: 'style', action: 'shadow', desc: 'Aplica sombra con nivel de elevación' },
    transparencia: { cat: 2, name: 'transparencia', params: ['nivel'], minArgs: 1, type: 'style', action: 'opacity', desc: 'Establece nivel de opacidad/transparencia (1 a 10)' },
    ocultar: { cat: 2, name: 'ocultar', params: ['id'], minArgs: 1, type: 'script', action: 'hide', desc: 'Oculta el elemento especificado por ID' },
    mostrar: { cat: 2, name: 'mostrar', params: ['id'], minArgs: 1, type: 'script', action: 'show', desc: 'Muestra el elemento especificado por ID' },
    flotante: { cat: 2, name: 'flotante', params: ['posicion'], minArgs: 1, type: 'style', action: 'displayOrFloat', desc: 'Establece posicionamiento (relative, absolute, fixed, flex, grid)' },
    desplazamiento: { cat: 2, name: 'desplazamiento', params: [], minArgs: 0, type: 'style', prop: 'overflow', val: 'auto', desc: 'Habilita barras de desplazamiento (overflow auto)' },

    // Categoría III: Campos, Eventos y Lógica (Comandos 51 - 75)
    entrada: { cat: 3, name: 'entrada', params: ['id', 'valor'], minArgs: 1, type: 'input', inputType: 'text', desc: 'Crea un campo de texto (<input type="text">)' },
    camponumero: { cat: 3, name: 'camponumero', params: ['id', 'valor'], minArgs: 1, type: 'input', inputType: 'number', desc: 'Crea un campo numérico (<input type="number">)' },
    campocorreo: { cat: 3, name: 'campocorreo', params: ['id', 'valor'], minArgs: 1, type: 'input', inputType: 'email', desc: 'Crea un campo de correo (<input type="email">)' },
    campocontrasena: { cat: 3, name: 'campocontrasena', params: ['id'], minArgs: 1, type: 'input', inputType: 'password', desc: 'Crea un campo de contraseña (<input type="password">)' },
    campofecha: { cat: 3, name: 'campofecha', params: ['id'], minArgs: 1, type: 'input', inputType: 'date', desc: 'Crea un selector de fecha (<input type="date">)' },
    campochequeo: { cat: 3, name: 'campochequeo', params: ['id', 'texto'], minArgs: 2, type: 'checkbox', desc: 'Crea una casilla de verificación (checkbox)' },
    desplegable: { cat: 3, name: 'desplegable', params: ['id'], minArgs: 1, type: 'element', tag: 'select', desc: 'Crea un menú desplegable (<select>)' },
    avisar: { cat: 3, name: 'avisar', params: ['idbtn', 'mensaje'], minArgs: 2, type: 'event', desc: 'Muestra alerta al presionar un botón' },
    ira: { cat: 3, name: 'ira', params: ['idbtn', 'url'], minArgs: 2, type: 'event', desc: 'Navega a una URL al presionar un botón' },
    ocultarboton: { cat: 3, name: 'ocultarboton', params: ['idbtn', 'idtarget'], minArgs: 2, type: 'event', desc: 'Oculta el elemento objetivo al hacer clic' },
    mostrarboton: { cat: 3, name: 'mostrarboton', params: ['idbtn', 'idtarget'], minArgs: 2, type: 'event', desc: 'Muestra el elemento objetivo al hacer clic' },
    alternar: { cat: 3, name: 'alternar', params: ['idbtn', 'idtarget'], minArgs: 2, type: 'event', desc: 'Alterna visibilidad del elemento objetivo al hacer clic' },
    limpiar: { cat: 3, name: 'limpiar', params: ['idbtn', 'idin'], minArgs: 2, type: 'event', desc: 'Limpia el campo de entrada al hacer clic' },
    limpiarlienzo: { cat: 3, name: 'limpiarlienzo', params: ['idbtn', 'idlienzo'], minArgs: 2, type: 'event', desc: 'Limpia el lienzo canvas al hacer clic' },
    deshabilitar: { cat: 3, name: 'deshabilitar', params: ['id'], minArgs: 1, type: 'script', desc: 'Deshabilita un campo o botón' },
    habilitar: { cat: 3, name: 'habilitar', params: ['id'], minArgs: 1, type: 'script', desc: 'Habilita un campo o botón' },
    copiartexto: { cat: 3, name: 'copiartexto', params: ['idbtn', 'idtarget'], minArgs: 2, type: 'event', desc: 'Copia el contenido del elemento al portapapeles' },
    sumar: { cat: 3, name: 'sumar', params: ['idbtn', 'in1', 'in2', 'lbl'], minArgs: 4, type: 'math', op: '+', desc: 'Suma valores de in1 e in2 y los muestra en lbl' },
    restar: { cat: 3, name: 'restar', params: ['idbtn', 'in1', 'in2', 'lbl'], minArgs: 4, type: 'math', op: '-', desc: 'Resta valores de in1 e in2 y los muestra en lbl' },
    multiplicar: { cat: 3, name: 'multiplicar', params: ['idbtn', 'in1', 'in2', 'lbl'], minArgs: 4, type: 'math', op: '*', desc: 'Multiplica valores de in1 e in2 y los muestra en lbl' },
    dividir: { cat: 3, name: 'dividir', params: ['idbtn', 'in1', 'in2', 'lbl'], minArgs: 4, type: 'math', op: '/', desc: 'Divide valores de in1 e in2 (maneja división por cero)' },
    incrementar: { cat: 3, name: 'incrementar', params: ['idbtn', 'idtarget', 'paso'], minArgs: 2, type: 'math', op: 'inc', desc: 'Incrementa valor en destino según el paso especificado' },
    decrementar: { cat: 3, name: 'decrementar', params: ['idbtn', 'idtarget', 'paso'], minArgs: 2, type: 'math', op: 'dec', desc: 'Decrementa valor en destino según el paso especificado' },
    guardarlocal: { cat: 3, name: 'guardarlocal', params: ['idbtn', 'clave', 'idin'], minArgs: 3, type: 'storage', action: 'save', desc: 'Guarda en localStorage el valor del campo al pulsar el botón' },
    cargarlocal: { cat: 3, name: 'cargarlocal', params: ['clave', 'lbl'], minArgs: 2, type: 'storage', action: 'load', desc: 'Lee el valor almacenado y lo muestra en la etiqueta de destino' }
  };

  const CLOSING_COMMANDS = new Set([
    'fin', 'finseccion', 'fincontenedor', 'finrejilla', 'finlista', 'fintabla', 'finfilatabla'
  ]);

  // Auxiliares de formato
  function cleanParam(val) {
    if (val === null || val === undefined) return '';
    return String(val)
      .replace(/[\\r\\n]+/g, ' ')
      .replace(/\\s+/g, ' ')
      .trim();
  }

  function formatColor(val) {
    if (!val) return '';
    val = val.trim();
    if (val.startsWith('#')) return val.toLowerCase();
    if (/^[0-9a-fA-F]{3}$|^[0-9a-fA-F]{6}$|^[0-9a-fA-F]{8}$/.test(val)) {
      return '#' + val.toLowerCase();
    }
    return val.toLowerCase();
  }

  function formatUnit(val) {
    if (!val) return '0px';
    val = String(val).trim();
    if (!val) return '0px';
    if (/^[0-9]+(?:\\.[0-9]+)?$/.test(val)) return val + 'px';
    return val;
  }

  function formatBorder(val) {
    if (!val) return '1px solid #ccc';
    val = val.trim();
    if (/\\b(solid|dashed|dotted|double|groove|ridge|inset|outset|none)\\b/i.test(val) || /^[0-9]+px/i.test(val)) {
      return val;
    }
    return `1px solid ${formatColor(val)}`;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function escapeJsString(str) {
    if (str === null || str === undefined) return "''";
    return JSON.stringify(String(str));
  }

  // ==========================================
  // PARSER DE LÍNEAS RC
  // ==========================================
  function parseRcLine(line, lineNum = 1) {
    line = line.trim();
    if (!line || line.startsWith('//')) return null;

    let bracketId = '';
    let workLine = line;

    // Sintaxis de corchetes: comando[id](args) o comando[id]
    const bracketMatch = workLine.match(/^([a-z0-9_]+)\\[([a-z0-9_]+)\\](.*)$/i);
    if (bracketMatch) {
      const baseCmd = bracketMatch[1].toLowerCase();
      bracketId = bracketMatch[2].toLowerCase();
      const restAfterBracket = bracketMatch[3].trim();
      workLine = baseCmd + restAfterBracket;
    }

    const parenIndex = workLine.indexOf('(');
    let cmd = workLine.toLowerCase();
    let args = [];

    if (parenIndex !== -1) {
      cmd = workLine.slice(0, parenIndex).trim().toLowerCase();
      const rest = workLine.slice(parenIndex);

      let depth = 0;
      let currentArg = '';
      let inArg = false;

      for (let i = 0; i < rest.length; i++) {
        const ch = rest[i];
        if (ch === '(') {
          if (depth === 0) {
            inArg = true;
            currentArg = '';
          } else {
            currentArg += ch;
          }
          depth++;
        } else if (ch === ')') {
          depth--;
          if (depth === 0) {
            inArg = false;
            args.push(currentArg.trim());
            currentArg = '';
          } else {
            currentArg += ch;
          }
        } else {
          if (inArg) currentArg += ch;
        }
      }
    }

    return { cmd, bracketId, args, rawLine: line, lineNum };
  }

  // ==========================================
  // COMPILADOR Y GENERADOR RC -> HTML/CSS/JS
  // ==========================================
  function rcToHtml(rcCode, visitedFiles = new Set()) {
    if (!rcCode || !rcCode.trim()) return '';

    const lines = rcCode.split('\\n');
    let title = 'Aplicación RC Studio';
    const scriptLines = [];
    const warnings = [];

    const nodesById = new Map();

    function createNode(tag, id = '', className = '', isContainer = false) {
      const node = {
        tag,
        id,
        className,
        isContainer,
        styles: [],
        children: [],
        attrs: {},
        innerText: '',
        rawHtml: ''
      };
      if (id) {
        nodesById.set(id, node);
      }
      return node;
    }

    const rootNode = createNode('body', 'body_root', '', true);
    const nodeStack = [rootNode];
    let lastCreatedNode = null;

    function currentContainer() {
      for (let i = nodeStack.length - 1; i >= 0; i--) {
        if (nodeStack[i].isContainer) return nodeStack[i];
      }
      return rootNode;
    }

    function currentTargetForStyle() {
      if (lastCreatedNode && lastCreatedNode.tag !== 'body') {
        return lastCreatedNode;
      }
      return currentContainer();
    }

    function addChild(node) {
      const targetContainer = currentContainer();
      targetContainer.children.push(node);
      lastCreatedNode = node;

      if (node.isContainer) {
        nodeStack.push(node);
      }
    }

    function closeContainerTag(expectedTags) {
      while (nodeStack.length > 1) {
        const top = nodeStack[nodeStack.length - 1];
        if (!expectedTags || expectedTags.includes(top.tag)) {
          nodeStack.pop();
          lastCreatedNode = null;
          break;
        }
        nodeStack.pop();
      }
    }

    lines.forEach((rawLine, idx) => {
      const lineNum = idx + 1;
      const line = rawLine.trim();
      if (!line) return;

      if (line.startsWith('//')) {
        const commentNode = createNode('comment');
        commentNode.rawHtml = `<!-- ${escapeHtml(line.slice(2).trim())} -->`;
        currentContainer().children.push(commentNode);
        lastCreatedNode = null;
        return;
      }

      const parsed = parseRcLine(line, lineNum);
      if (!parsed) return;

      const { cmd, bracketId, args } = parsed;
      const spec = RC_COMMANDS_SPEC[cmd];

      if (!spec && !CLOSING_COMMANDS.has(cmd)) {
        warnings.push(`Línea ${lineNum}: Comando desconocido '${escapeHtml(cmd)}'`);
        return;
      }

      const a1 = args[0] || '';
      const a2 = args[1] || '';
      const a3 = args[2] || '';
      const a4 = args[3] || '';

      const listCmds = ['elementolista'];
      const tableCmds = ['filatabla', 'encabezadotabla', 'celdatabla'];
      const elementCmds = [
        'seccion', 'contenedor', 'rejilla', 'boton', 'parrafo', 'texto',
        'encabezado', 'entrada', 'camponumero', 'campocorreo', 'campocontrasena',
        'campofecha', 'campochequeo', 'desplegable', 'areatexto', 'lienzo',
        'cargando', 'tabla', 'listadesordenada', 'listaordenada'
      ];

      if (elementCmds.includes(cmd)) {
        lastCreatedNode = null;
      }

      if (nodeStack.length > 1) {
        const top = nodeStack[nodeStack.length - 1];
        if ((top.tag === 'ul' || top.tag === 'ol') && !listCmds.includes(cmd)) {
          nodeStack.pop();
        } else if (top.tag === 'tr' && cmd === 'filatabla') {
          nodeStack.pop();
        } else if (top.tag === 'tr' && !tableCmds.includes(cmd)) {
          nodeStack.pop();
          if (nodeStack.length > 1 && nodeStack[nodeStack.length - 1].tag === 'table') {
            nodeStack.pop();
          }
        } else if (top.tag === 'table' && !tableCmds.includes(cmd)) {
          nodeStack.pop();
        }
      }

      // Procesar comando según su tipo
      if (CLOSING_COMMANDS.has(cmd)) {
        if (cmd === 'finseccion') closeContainerTag(['section']);
        else if (cmd === 'fincontenedor') closeContainerTag(['div']);
        else if (cmd === 'finrejilla') closeContainerTag(['div']);
        else if (cmd === 'finlista') closeContainerTag(['ul', 'ol']);
        else if (cmd === 'fintabla') closeContainerTag(['table']);
        else if (cmd === 'finfilatabla') closeContainerTag(['tr']);
        else closeContainerTag();
        return;
      }

      switch (cmd) {
        case 'incluir': {
          const targetFileName = cleanParam(a1);
          if (!targetFileName) break;

          if (visitedFiles.has(targetFileName)) {
            const errNode = createNode('comment');
            errNode.rawHtml = `<!-- Error: Inclusión circular detectada en '${escapeHtml(targetFileName)}' -->`;
            currentContainer().children.push(errNode);
            break;
          }

          if (typeof files !== 'undefined' && !files.has(targetFileName)) {
            const errNode = createNode('comment');
            errNode.rawHtml = `<!-- Error de inclusión: el archivo '${escapeHtml(targetFileName)}' no existe -->`;
            currentContainer().children.push(errNode);
            break;
          }

          if (typeof files !== 'undefined') {
            const targetFile = files.get(targetFileName);
            const newVisited = new Set(visitedFiles);
            newVisited.add(targetFileName);

            if (targetFileName.endsWith('.rc') || targetFile.type === 'rc') {
              const subHtml = rcToHtml(targetFile.content, newVisited);
              const incNode = createNode('comment');
              const bodyMatch = subHtml.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i);
              incNode.rawHtml = bodyMatch ? bodyMatch[1].trim() : subHtml;
              currentContainer().children.push(incNode);

              const scriptMatch = subHtml.match(/<script>([\\s\\S]*?)<\\/script>/i);
              if (scriptMatch) scriptLines.push(scriptMatch[1].trim());
            }
          }
          break;
        }

        case 'titulo':
          title = cleanParam(a1);
          break;

        case 'seccion': {
          closeContainerTag(['section']);
          const secId = bracketId || cleanParam(a1);
          const secNode = createNode('section', secId, '', true);
          addChild(secNode);
          break;
        }

        case 'contenedor': {
          const divId = bracketId || cleanParam(a1);
          const divNode = createNode('div', divId, '', true);
          addChild(divNode);
          break;
        }

        case 'rejilla': {
          const gridId = bracketId || cleanParam(a2 || '');
          const cols = parseInt(a1, 10) || 1;
          const gridNode = createNode('div', gridId, 'rejilla', true);
          gridNode.styles.push('display: grid;');
          gridNode.styles.push(`grid-template-columns: repeat(${cols}, 1fr);`);
          addChild(gridNode);
          break;
        }

        case 'linea':
          addChild(createNode('hr'));
          break;

        case 'texto':
        case 'parrafo': {
          const pNode = createNode('p', bracketId);
          pNode.innerText = cleanParam(a1);
          addChild(pNode);
          break;
        }

        case 'encabezado': {
          const level = Math.max(1, Math.min(6, parseInt(a1, 10) || 1));
          const hNode = createNode(`h${level}`, bracketId);
          hNode.innerText = cleanParam(a2);
          addChild(hNode);
          break;
        }

        case 'negrita': {
          const bNode = createNode('b', bracketId);
          bNode.innerText = cleanParam(a1);
          addChild(bNode);
          break;
        }

        case 'cursiva': {
          const iNode = createNode('i', bracketId);
          iNode.innerText = cleanParam(a1);
          addChild(iNode);
          break;
        }

        case 'subrayado': {
          const uNode = createNode('u', bracketId);
          uNode.innerText = cleanParam(a1);
          addChild(uNode);
          break;
        }

        case 'etiqueta': {
          const lblId = bracketId || cleanParam(a1);
          const lblText = cleanParam(bracketId ? a1 : (a2 || a1));
          const lblNode = createNode('span', lblId);
          lblNode.innerText = lblText;
          addChild(lblNode);
          break;
        }

        case 'bloque': {
          const blkNode = createNode('div', bracketId);
          blkNode.innerText = cleanParam(a1);
          addChild(blkNode);
          break;
        }

        case 'cita': {
          const qNode = createNode('blockquote', bracketId);
          qNode.innerText = cleanParam(a1);
          addChild(qNode);
          break;
        }

        case 'codigo': {
          const codeNode = createNode('code', bracketId);
          codeNode.innerText = cleanParam(a1);
          addChild(codeNode);
          break;
        }

        case 'enlace': {
          const aNode = createNode('a', bracketId);
          aNode.innerText = cleanParam(a2);
          aNode.href = cleanParam(a1);
          addChild(aNode);
          break;
        }

        case 'imagen': {
          const imgNode = createNode('img', bracketId);
          imgNode.src = cleanParam(a1);
          addChild(imgNode);
          break;
        }

        case 'listadesordenada':
          addChild(createNode('ul', bracketId, '', true));
          break;

        case 'listaordenada':
          addChild(createNode('ol', bracketId, '', true));
          break;

        case 'elementolista': {
          const liNode = createNode('li', bracketId);
          liNode.innerText = cleanParam(a1);
          addChild(liNode);
          break;
        }

        case 'tabla':
          addChild(createNode('table', bracketId, '', true));
          break;

        case 'filatabla':
          addChild(createNode('tr', bracketId, '', true));
          break;

        case 'encabezadotabla': {
          const thNode = createNode('th', bracketId);
          thNode.innerText = cleanParam(a1);
          addChild(thNode);
          break;
        }

        case 'celdatabla': {
          const tdNode = createNode('td', bracketId);
          tdNode.innerText = cleanParam(a1);
          addChild(tdNode);
          break;
        }

        case 'boton': {
          let btnId = bracketId;
          let btnText = '';
          if (bracketId) {
            btnText = cleanParam(a1);
          } else if (args.length >= 2) {
            btnId = cleanParam(a1);
            btnText = cleanParam(a2);
          } else {
            btnId = '';
            btnText = cleanParam(a1);
          }
          const btnNode = createNode('button', btnId);
          btnNode.innerText = btnText;
          addChild(btnNode);
          break;
        }

        case 'etiquetacampo': {
          const lblField = createNode('label', bracketId);
          lblField.innerText = cleanParam(a1);
          addChild(lblField);
          break;
        }

        case 'cargando': {
          const loadNode = createNode('div', bracketId, 'cargando');
          loadNode.innerText = 'Cargando...';
          addChild(loadNode);
          break;
        }

        case 'lienzo':
          addChild(createNode('canvas', bracketId || cleanParam(a1)));
          break;

        case 'areatexto': {
          const areaId = bracketId || cleanParam(a1);
          const areaNode = createNode('textarea', areaId);
          areaNode.innerText = cleanParam(a2);
          addChild(areaNode);
          break;
        }

        case 'entrada': {
          const inTxtId = bracketId || cleanParam(a1);
          const inTxt = createNode('input', inTxtId);
          inTxt.inputType = 'text';
          inTxt.val = cleanParam(a2);
          addChild(inTxt);
          break;
        }

        case 'camponumero': {
          const inNumId = bracketId || cleanParam(a1);
          const inNum = createNode('input', inNumId);
          inNum.inputType = 'number';
          inNum.val = cleanParam(a2);
          addChild(inNum);
          break;
        }

        case 'campocorreo': {
          const inMailId = bracketId || cleanParam(a1);
          const inMail = createNode('input', inMailId);
          inMail.inputType = 'email';
          inMail.val = cleanParam(a2);
          addChild(inMail);
          break;
        }

        case 'campocontrasena': {
          const inPassId = bracketId || cleanParam(a1);
          const inPass = createNode('input', inPassId);
          inPass.inputType = 'password';
          addChild(inPass);
          break;
        }

        case 'campofecha': {
          const inDateId = bracketId || cleanParam(a1);
          const inDate = createNode('input', inDateId);
          inDate.inputType = 'date';
          addChild(inDate);
          break;
        }

        case 'campochequeo': {
          const chkId = bracketId || cleanParam(a1);
          const chkNode = createNode('label', chkId);
          chkNode.rawHtml = `<label><input type="checkbox" id="${chkId}"> ${escapeHtml(cleanParam(a2))}</label>`;
          addChild(chkNode);
          break;
        }

        case 'desplegable': {
          const selId = bracketId || cleanParam(a1);
          addChild(createNode('select', selId));
          break;
        }

        case 'fondo':
          currentTargetForStyle().styles.push(`background-color: ${formatColor(a1)};`);
          break;

        case 'color':
          currentTargetForStyle().styles.push(`color: ${formatColor(a1)};`);
          break;

        case 'letra':
          currentTargetForStyle().styles.push(`font-family: ${a1.includes(',') ? a1 : a1 + ', sans-serif'};`);
          break;

        case 'tamano':
          currentTargetForStyle().styles.push(`font-size: ${formatUnit(a1)};`);
          break;

        case 'ancho':
          currentTargetForStyle().styles.push(`width: ${formatUnit(a1)};`);
          break;

        case 'alto':
          currentTargetForStyle().styles.push(`height: ${formatUnit(a1)};`);
          break;

        case 'gap':
          currentTargetForStyle().styles.push(`gap: ${formatUnit(a1)};`);
          break;

        case 'margen':
          currentTargetForStyle().styles.push(`margin: ${formatUnit(a1)};`);
          break;

        case 'relleno':
          currentTargetForStyle().styles.push(`padding: ${formatUnit(a1)};`);
          break;

        case 'radio':
          currentTargetForStyle().styles.push(`border-radius: ${formatUnit(a1)};`);
          break;

        case 'centrar': {
          const targetCentrar = currentTargetForStyle();
          if (targetCentrar.isContainer) {
            targetCentrar.styles.push(`margin-left: auto; margin-right: auto; text-align: center; justify-content: center; align-items: center;`);
          } else {
            targetCentrar.styles.push(`display: block; margin-left: auto; margin-right: auto; text-align: center;`);
          }
          break;
        }

        case 'alinearizquierda': {
          const targetIzq = currentTargetForStyle();
          if (targetIzq.isContainer) {
            targetIzq.styles.push(`text-align: left; justify-content: flex-start; align-items: flex-start;`);
          } else {
            targetIzq.styles.push(`text-align: left;`);
          }
          break;
        }

        case 'alinearderecha': {
          const targetDer = currentTargetForStyle();
          if (targetDer.isContainer) {
            targetDer.styles.push(`text-align: right; justify-content: flex-end; align-items: flex-end;`);
          } else {
            targetDer.styles.push(`text-align: right;`);
          }
          break;
        }

        case 'borde':
          currentTargetForStyle().styles.push(`border: ${formatBorder(a1)};`);
          break;

        case 'sombra': {
          const shadowLvl = parseInt(a1, 10) || 1;
          currentTargetForStyle().styles.push(`box-shadow: 0 ${shadowLvl * 2}px ${shadowLvl * 4}px rgba(0,0,0,0.2);`);
          break;
        }

        case 'transparencia': {
          const op = (parseFloat(a1) || 10) / 10;
          currentTargetForStyle().styles.push(`opacity: ${op};`);
          break;
        }

        case 'flotante': {
          const flotVal = cleanParam(a1).toLowerCase();
          if (['flex', 'inline-flex', 'grid', 'inline-grid', 'block', 'inline-block', 'none'].includes(flotVal)) {
            currentTargetForStyle().styles.push(`display: ${flotVal};`);
          } else if (flotVal === 'column' || flotVal === 'column-reverse' || flotVal === 'row' || flotVal === 'row-reverse') {
            currentTargetForStyle().styles.push(`flex-direction: ${flotVal};`);
          } else if (flotVal === 'izquierda' || flotVal === 'left') {
            currentTargetForStyle().styles.push(`float: left;`);
          } else if (flotVal === 'derecha' || flotVal === 'right') {
            currentTargetForStyle().styles.push(`float: right;`);
          } else {
            currentTargetForStyle().styles.push(`position: ${flotVal};`);
          }
          break;
        }

        case 'desplazamiento':
          currentTargetForStyle().styles.push(`overflow: auto;`);
          break;

        case 'ocultar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.style.setProperty('display', 'none');`);
          break;

        case 'mostrar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.style.setProperty('display', 'block');`);
          break;

        case 'avisar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => alert(${escapeJsString(a2)}));`);
          break;

        case 'ira':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => window.location.href = ${escapeJsString(a2)});`);
          break;

        case 'ocultarboton':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const el = document.getElementById(${escapeJsString(a2)}); if(el) el.style.display = 'none'; });`);
          break;

        case 'mostrarboton':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const el = document.getElementById(${escapeJsString(a2)}); if(el) el.style.display = 'block'; });`);
          break;

        case 'alternar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const el = document.getElementById(${escapeJsString(a2)}); if(el) el.style.display = (el.style.display === 'none' ? 'block' : 'none'); });`);
          break;

        case 'limpiar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const el = document.getElementById(${escapeJsString(a2)}); if(el) { if('value' in el) el.value = ''; else el.innerText = ''; } });`);
          break;

        case 'limpiarlienzo':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const c = document.getElementById(${escapeJsString(a2)}); if(c && c.getContext) c.getContext('2d').clearRect(0, 0, c.width, c.height); });`);
          break;

        case 'deshabilitar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.setAttribute('disabled', 'true');`);
          break;

        case 'habilitar':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.removeAttribute('disabled');`);
          break;

        case 'copiartexto':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => { const el = document.getElementById(${escapeJsString(a2)}); if(el) navigator.clipboard.writeText(el.value || el.innerText); });`);
          break;

        case 'sumar':
        case 'restar':
        case 'multiplicar':
        case 'dividir': {
          const opChar = spec.op;
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => {
            const el1 = document.getElementById(${escapeJsString(a2)});
            const el2 = document.getElementById(${escapeJsString(a3)});
            const lbl = document.getElementById(${escapeJsString(a4)});
            if(!el1 || !el2 || !lbl) return;
            const v1 = parseFloat(el1.value !== undefined ? el1.value : el1.innerText) || 0;
            const v2 = parseFloat(el2.value !== undefined ? el2.value : el2.innerText) || 0;
            let res = 0;
            if('${opChar}' === '+') res = v1 + v2;
            else if('${opChar}' === '-') res = v1 - v2;
            else if('${opChar}' === '*') res = v1 * v2;
            else if('${opChar}' === '/') {
              if(v2 === 0) {
                if('value' in lbl) lbl.value = 'Error: División por cero'; else lbl.innerText = 'Error: División por cero';
                return;
              }
              res = v1 / v2;
            }
            res = Number(res.toFixed(8)) / 1;
            if('value' in lbl && lbl.tagName !== 'SPAN' && lbl.tagName !== 'P' && lbl.tagName !== 'DIV') lbl.value = res.toString();
            else lbl.innerText = res.toString();
          });`);
          break;
        }

        case 'incrementar':
        case 'decrementar': {
          const isInc = cmd === 'incrementar';
          const stepVal = a3 || '1';
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => {
            const el = document.getElementById(${escapeJsString(a2)});
            if(!el) return;
            const stepStr = ${escapeJsString(stepVal)};
            if('value' in el && el.tagName !== 'SPAN' && el.tagName !== 'P' && el.tagName !== 'DIV') {
              if (el.value === '' || el.value === 'Error: División por cero') el.value = stepStr;
              else el.value = el.value + stepStr;
            } else {
              if (el.innerText === '' || el.innerText === 'Error: División por cero') el.innerText = stepStr;
              else el.innerText = el.innerText + stepStr;
            }
          });`);
          break;
        }

        case 'guardarlocal':
          scriptLines.push(`document.getElementById(${escapeJsString(a1)})?.addEventListener('click', () => {
            const el = document.getElementById(${escapeJsString(a3)});
            if(el) localStorage.setItem(${escapeJsString(a2)}, el.value !== undefined ? el.value : el.innerText);
          });`);
          break;

        case 'cargarlocal':
          scriptLines.push(`{
            const val = localStorage.getItem(${escapeJsString(a1)}) || '';
            const lbl = document.getElementById(${escapeJsString(a2)});
            if(lbl) { if('value' in lbl && lbl.tagName !== 'SPAN' && lbl.tagName !== 'P') lbl.value = val; else lbl.innerText = val; }
          }`);
          break;
      }
    });

    function renderNode(node, depth = 1) {
      const indent = ' '.repeat(depth * 2);
      if (node.rawHtml) return `${indent}${node.rawHtml}`;

      let attrs = '';
      if (node.id) attrs += ` id="${escapeHtml(node.id)}"`;
      if (node.className) attrs += ` class="${escapeHtml(node.className)}"`;
      if (node.inputType) attrs += ` type="${escapeHtml(node.inputType)}"`;
      if (node.val !== undefined && node.val !== '') attrs += ` value="${escapeHtml(node.val)}"`;
      if (node.href) attrs += ` href="${escapeHtml(node.href)}"`;
      if (node.src) attrs += ` src="${escapeHtml(node.src)}" alt="imagen"`;

      if (node.attrs) {
        for (const [k, v] of Object.entries(node.attrs)) {
          if (!['id', 'class', 'type', 'value', 'href', 'src', 'style'].includes(k.toLowerCase())) {
            attrs += ` ${escapeHtml(k)}="${escapeHtml(v)}"`;
          }
        }
      }

      if (node.styles.length > 0) attrs += ` style="${node.styles.join(' ')}"`;

      const selfClosing = ['hr', 'img', 'input'];
      if (selfClosing.includes(node.tag)) {
        return `${indent}<${node.tag}${attrs}>`;
      }

      const textContent = escapeHtml(node.innerText || '');
      if (!node.children || node.children.length === 0) {
        return `${indent}<${node.tag}${attrs}>${textContent}</${node.tag}>`;
      }

      const childrenHtml = node.children.map(c => renderNode(c, depth + 1)).join('\\n');
      return `${indent}<${node.tag}${attrs}>\\n${textContent ? indent + '  ' + textContent + '\\n' : ''}${childrenHtml}\\n${indent}</${node.tag}>`;
    }

    const bodyChildren = rootNode.children.map(c => renderNode(c, 1)).join('\\n');

    let warningBlock = '';
    if (warnings.length > 0) {
      warningBlock = `  <div style="background: #2a1b1b; color: #ff8080; border: 1px solid #662222; padding: 10px; margin: 10px 0; border-radius: 6px; font-family: monospace; font-size: 12px;">\\n` +
        warnings.map(w => `    <div>⚠️ ${w}</div>`).join('\\n') + `\\n  </div>\\n`;
    }

    let scriptBlock = '';
    if (scriptLines.length > 0) {
      scriptBlock = `\\n  <script>\\n    ${scriptLines.join('\\n    ')}\\n  <\\/script>`;
    }

    return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>${escapeHtml(title)}</title>
  <style>
    body { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 16px; box-sizing: border-box; background: #0e1015; color: #ffffff; }
    *, *:before, *:after { box-sizing: inherit; }
    button { cursor: pointer; padding: 10px 14px; font-size: 15px; border-radius: 8px; border: 1px solid #3d4454; background: #272c38; color: #ffffff; display: inline-block; vertical-align: middle; box-sizing: border-box; transition: background 0.15s ease; margin: 4px; }
    button:hover { background: #383f50; }
    button:active { background: #1e222c; }
    input[type="text"], input[type="number"], input[type="email"], input[type="password"], input[type="date"], textarea, select { width: 100%; padding: 10px; font-size: 15px; border-radius: 8px; border: 1px solid #3d4454; background: #151821; color: #ffffff; outline: none; box-sizing: border-box; margin: 4px 0; }
    .rejilla { display: grid; width: 100%; gap: 10px; box-sizing: border-box; }
    .cargando { display: inline-block; padding: 10px 20px; background: #222733; color: #68b5ff; border-radius: 6px; border: 1px dashed #68b5ff; }
  </style>
</head>
<body>
${warningBlock}${bodyChildren}${scriptBlock}
</body>
</html>
`;
  }

  // ==========================================
  // CALCULADORA OFICIAL DE EJEMPLO EN RC
  // ==========================================
  const initialCalculatorRc = `// calculadora profesional en rapid code (rc)
titulo(calculadora rc studio)

seccion(sec_calc)
contenedor(calc_card)
ancho(340px)
fondo(#181a20)
color(#ffffff)
relleno(20px)
radio(16px)
borde(1px solid #2d3240)
sombra(4)
centrar

encabezado(2)(calculadora rc)
color(#68b5ff)
tamano(20px)

contenedor(pantalla_box)
fondo(#0d0f14)
relleno(12px)
radio(10px)
margen(12px)
borde(1px solid #252a36)

entrada(inp_disp)()
tamano(24px)
color(#50fa7b)
alinearderecha
fincontenedor

rejilla(4)
gap(8px)
margen(10px)

// Fila 1
boton(btn_7)(7)
boton(btn_8)(8)
boton(btn_9)(9)
boton(btn_div)(/)

// Fila 2
boton(btn_4)(4)
boton(btn_5)(5)
boton(btn_6)(6)
boton(btn_mul)(*)

// Fila 3
boton(btn_1)(1)
boton(btn_2)(2)
boton(btn_3)(3)
boton(btn_res)(-)

// Fila 4
boton(btn_clr)(C)
boton(btn_0)(0)
boton(btn_eq)(=)
boton(btn_sum)(+)

// Campos de memoria para operandos
entrada(inp_a)(0)
ocultar(inp_a)
entrada(inp_b)(0)
ocultar(inp_b)

finrejilla
fincontenedor
finseccion

// Lógica de dígitos
incrementar(btn_7)(inp_disp)(7)
incrementar(btn_8)(inp_disp)(8)
incrementar(btn_9)(inp_disp)(9)

incrementar(btn_4)(inp_disp)(4)
incrementar(btn_5)(inp_disp)(5)
incrementar(btn_6)(inp_disp)(6)

incrementar(btn_1)(inp_disp)(1)
incrementar(btn_2)(inp_disp)(2)
incrementar(btn_3)(inp_disp)(3)
incrementar(btn_0)(inp_disp)(0)

// Operaciones aritméticas oficiales RC
sumar(btn_sum)(inp_disp)(inp_a)(inp_disp)
restar(btn_res)(inp_disp)(inp_a)(inp_disp)
multiplicar(btn_mul)(inp_disp)(inp_a)(inp_disp)
dividir(btn_div)(inp_disp)(inp_a)(inp_disp)

limpiar(btn_clr)(inp_disp)`;

  const STORAGE_KEY = "rc_studio_state";
  const files = new Map();
  let activeFile = "main.rc";
  const panelSel = document.getElementById("panelSelector");

  function saveState() {
    try {
      const state = {
        files: Array.from(files.entries()),
        activeFile: activeFile,
        panelMode: panelSel ? panelSel.value : "rc-preview"
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn("No se pudo guardar el estado en localStorage", e);
    }
  }

  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return false;
      const parsed = JSON.parse(raw);
      if (!parsed || !Array.isArray(parsed.files) || parsed.files.length === 0) return false;

      files.clear();
      for (const [name, fileObj] of parsed.files) {
        if (name && fileObj && fileObj.content !== undefined) {
          if (name.endsWith('.html') && fileObj.type !== 'rc') continue;
          const fileName = name.endsWith('.rc') ? name : name + '.rc';
          files.set(fileName, { type: 'rc', content: fileObj.content });
        }
      }

      if (files.size === 0) return false;

      if (parsed.activeFile && files.has(parsed.activeFile)) {
        activeFile = parsed.activeFile;
      } else if (parsed.active && parsed.active.rc && files.has(parsed.active.rc)) {
        activeFile = parsed.active.rc;
      } else {
        activeFile = [...files.keys()][0] || "main.rc";
      }

      if (parsed.panelMode && panelSel) {
        panelSel.value = (parsed.panelMode === 'rc-html' || parsed.panelMode === 'all') ? 'rc-preview' : parsed.panelMode;
      }

      return files.size > 0;
    } catch (e) {
      console.warn("Error al cargar estado desde localStorage", e);
      return false;
    }
  }

  function initDefaultFiles() {
    files.set("main.rc", { type: "rc", content: initialCalculatorRc });
    activeFile = "main.rc";
  }

  if (!loadState()) {
    initDefaultFiles();
  }

  const editorEl = document.getElementById("rcEditor");
  const gutterEl = document.getElementById("rcGutter");
  const tabsEl = document.getElementById("rcTabs");
  const listEl = document.getElementById("fileList");
  const explorerEl = document.getElementById("explorer");
  let toastTimer;
  let isTranslating = false;
  let translateTimer = null;
  let lastValidHtml = "";

  function updateLivePreview(htmlContent) {
    const frame = document.getElementById("previewFrame");
    if (frame) {
      frame.srcdoc = htmlContent || '';
    }
  }

  function applyPanelMode(mode) {
    const rcSec = document.getElementById("rcEditorSection");
    const prevSec = document.getElementById("previewPaneSection");

    if (rcSec) rcSec.style.display = (mode === "preview" ? "none" : "flex");
    if (prevSec) prevSec.style.display = (mode === "rc" ? "none" : "flex");
  }

  function highlightRc(code) {
    if (!code) return "";
    const lines = code.split("\\n");
    const standaloneCmds = new Set([
      "linea", "centrar", "alinearizquierda", "alinearderecha", "desplazamiento", "cargando",
      "listadesordenada", "listaordenada", "tabla", "filatabla", "fin", "finseccion",
      "fincontenedor", "finrejilla", "finlista", "fintabla", "finfilatabla"
    ]);

    return lines.map(line => {
      const trimmed = line.trim();
      if (trimmed.startsWith("//")) {
        return `<span class="hl-comment">${escapeHtml(line)}</span>`;
      }

      const tokenRegex = /(#[0-9a-fA-F]{3,8}\\b)|(\\b\\d+(?:px|rem|em|%)?\\b)|([\\u00C0-\\u024F\\u1E00-\\u1EFFa-zA-Z0-9_]+)(?=\\()|([\\u00C0-\\u024F\\u1E00-\\u1EFFa-zA-Z0-9_]+)|([\\(\\)\\[\\]=])|([^\\(\\)\\[\\]=#\\u00C0-\\u024F\\u1E00-\\u1EFFa-zA-Z0-9_]+)/g;

      let result = "";
      let match;
      while ((match = tokenRegex.exec(line)) !== null) {
        const [full, color, num, cmdWithParen, word, symbol, rest] = match;
        if (color) {
          result += `<span class="hl-color">${escapeHtml(color)}</span>`;
        } else if (num) {
          result += `<span class="hl-num">${escapeHtml(num)}</span>`;
        } else if (cmdWithParen) {
          result += `<span class="hl-cmd">${escapeHtml(cmdWithParen)}</span>`;
        } else if (word) {
          if (standaloneCmds.has(word.toLowerCase()) || RC_COMMANDS_SPEC[word.toLowerCase()]) {
            result += `<span class="hl-cmd">${escapeHtml(word)}</span>`;
          } else {
            result += escapeHtml(word);
          }
        } else if (symbol) {
          result += `<span class="hl-paren">${escapeHtml(symbol)}</span>`;
        } else if (rest) {
          result += escapeHtml(rest);
        } else {
          result += escapeHtml(full);
        }
      }

      return result || escapeHtml(line);
    }).join("\\n");
  }

  function updateHighlight() {
    const codeEl = document.getElementById("rcHighlightCode");
    const layer = document.getElementById("rcHighlight");
    if (!editorEl || !codeEl || !layer) return;

    const val = editorEl.value || "";
    codeEl.innerHTML = highlightRc(val) + (val.endsWith("\\n") ? "\\n " : "");
    layer.scrollTop = editorEl.scrollTop;
    layer.scrollLeft = editorEl.scrollLeft;
  }

  function updateLineNumbers() {
    if (!editorEl || !gutterEl) return;
    const lines = editorEl.value.split("\\n").length;
    let nums = "";
    for (let i = 1; i <= lines; i++) {
      nums += i + "\\n";
    }
    gutterEl.textContent = nums;
    gutterEl.scrollTop = editorEl.scrollTop;
  }

  function rootNodeHasContent(rcCode) {
    if (!rcCode || !rcCode.trim()) return false;
    const lines = rcCode.split('\\n');
    return lines.some(l => {
      const parsed = parseRcLine(l);
      return parsed && parsed.cmd && (RC_COMMANDS_SPEC[parsed.cmd] || CLOSING_COMMANDS.has(parsed.cmd));
    });
  }

  function autoTranslate() {
    if (isTranslating) return;
    isTranslating = true;
    try {
      if (activeFile && files.has(activeFile)) {
        const rcVal = editorEl.value;
        files.get(activeFile).content = rcVal;

        if (!rcVal.trim()) {
          lastValidHtml = "";
          updateLivePreview("");
          return;
        }

        const generatedHtml = rcToHtml(rcVal);
        if (generatedHtml && rootNodeHasContent(rcVal)) {
          lastValidHtml = generatedHtml;
        }
      }
    } catch (e) {
      console.warn("Error interpretando RC:", e);
    } finally {
      isTranslating = false;
      saveState();
      updateHighlight();
      if (lastValidHtml !== undefined) {
        updateLivePreview(lastValidHtml);
      }
    }
  }

  function debounceTranslate() {
    clearTimeout(translateTimer);
    translateTimer = setTimeout(autoTranslate, 180);
  }

  function notify(message) {
    const el = document.getElementById("toast");
    if (!el) return;
    el.textContent = message;
    el.style.display = "block";
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.style.display = "none", 2200);
  }

  function renderTabs() {
    if (!tabsEl) return;
    tabsEl.innerHTML = "";
    [...files.keys()].forEach(name => {
      const b = document.createElement("button");
      b.className = "tab" + (activeFile === name ? " active" : "");
      b.textContent = name;
      b.title = "Abrir " + name;
      b.onclick = () => openFile(name);
      tabsEl.appendChild(b);
    });
  }

  function renderExplorer() {
    if (!listEl) return;
    listEl.innerHTML = "";
    if (!files.size) {
      listEl.innerHTML = '<div class="empty">No hay archivos.</div>';
      return;
    }
    [...files.keys()].sort((a,b) => a.localeCompare(b)).forEach(name => {
      const row = document.createElement("div");
      row.className = "file-row" + (activeFile === name ? " active" : "");
      const label = document.createElement("span");
      label.className = "filename";
      label.textContent = name;
      label.title = "Abrir " + name;
      label.onclick = () => openFile(name);

      const ext = document.createElement("span");
      ext.className = "ext";
      ext.textContent = "⭐ .RC";

      const renameBtn = document.createElement("button");
      renameBtn.className = "mini";
      renameBtn.textContent = "✎";
      renameBtn.title = "Cambiar nombre";
      renameBtn.onclick = () => renameFile(name);

      const delBtn = document.createElement("button");
      delBtn.className = "mini";
      delBtn.textContent = "×";
      delBtn.title = "Eliminar archivo";
      delBtn.onclick = () => deleteFile(name);

      row.append(label, ext, renameBtn, delBtn);
      listEl.appendChild(row);
    });
  }

  function renderAll() {
    renderTabs();
    if (activeFile && files.has(activeFile)) {
      editorEl.value = files.get(activeFile).content;
      document.getElementById("rcStatusName").textContent = activeFile;
    } else {
      editorEl.value = "";
      document.getElementById("rcStatusName").textContent = "Sin archivo abierto";
    }
    updateCursor();
    updateLineNumbers();
    updateHighlight();
    renderExplorer();
    autoTranslate();
  }

  function openFile(name) {
    if (activeFile && files.has(activeFile)) {
      files.get(activeFile).content = editorEl.value;
    }
    activeFile = name;
    saveState();
    renderAll();
  }

  function uniqueName(base) {
    let name = base;
    if (!name.toLowerCase().endsWith('.rc')) name += '.rc';
    if (!files.has(name)) return name;
    let i = 2;
    while (files.has(name.slice(0, -3) + "-" + i + ".rc")) i++;
    return name.slice(0, -3) + "-" + i + ".rc";
  }

  function createFile() {
    if (activeFile && files.has(activeFile)) {
      files.get(activeFile).content = editorEl.value;
    }
    const requested = prompt("Nombre del nuevo archivo RC:", "modulo.rc");
    if (requested === null) return;
    let base = requested.trim().replace(/[\\\\/:*?"<>|]/g, "");
    if (!base) { notify("Escribe un nombre válido."); return; }
    const name = uniqueName(base);
    files.set(name, { type: "rc", content: `// nuevo archivo rc\\n\\n` });
    activeFile = name;
    saveState();
    renderAll();
    editorEl.focus();
    notify("Archivo creado: " + name);
  }

  function renameFile(oldName) {
    if (activeFile && files.has(activeFile)) {
      files.get(activeFile).content = editorEl.value;
    }
    const requested = prompt("Nuevo nombre del archivo RC:", oldName);
    if (requested === null) return;
    let base = requested.trim().replace(/[\\\\/:*?"<>|]/g, "");
    if (!base) { notify("Escribe un nombre válido."); return; }
    if (!base.toLowerCase().endsWith('.rc')) base += '.rc';
    if (base !== oldName && files.has(base)) { notify("Ya existe un archivo con ese nombre."); return; }
    const file = files.get(oldName);
    files.delete(oldName);
    files.set(base, file);
    if (activeFile === oldName) activeFile = base;
    saveState();
    renderAll();
    notify("Archivo renombrado.");
  }

  function deleteFile(name) {
    if (files.size <= 1) {
      notify("Debe existir al menos un archivo en el proyecto.");
      return;
    }
    if (!confirm(`¿Eliminar "${name}"?`)) return;
    files.delete(name);
    if (activeFile === name) activeFile = [...files.keys()][0];
    saveState();
    renderAll();
    notify("Archivo eliminado.");
  }

  function updateCursor() {
    const before = editorEl.value.slice(0, editorEl.selectionStart);
    const line = before.split("\\n").length;
    const col = before.length - before.lastIndexOf("\\n");
    document.getElementById("rcStatusLine").textContent = `Línea ${line}, Col ${col}`;
  }

  // Listeners del editor RC
  editorEl.addEventListener("input", () => {
    if (activeFile && files.has(activeFile)) {
      files.get(activeFile).content = editorEl.value;
    }
    updateCursor();
    updateLineNumbers();
    updateHighlight();
    debounceTranslate();
  });

  editorEl.addEventListener("scroll", () => {
    gutterEl.scrollTop = editorEl.scrollTop;
    const layer = document.getElementById("rcHighlight");
    if (layer) {
      layer.scrollTop = editorEl.scrollTop;
      layer.scrollLeft = editorEl.scrollLeft;
    }
  });

  editorEl.addEventListener("click", updateCursor);
  editorEl.addEventListener("keyup", updateCursor);
  editorEl.addEventListener("keydown", e => {
    if (e.key === "Tab") {
      e.preventDefault();
      const start = editorEl.selectionStart, end = editorEl.selectionEnd;
      editorEl.setRangeText("  ", start, end, "end");
      if (activeFile && files.has(activeFile)) {
        files.get(activeFile).content = editorEl.value;
      }
      updateCursor();
      updateLineNumbers();
      updateHighlight();
      debounceTranslate();
    }
  });

  document.getElementById("newRc").onclick = createFile;
  document.getElementById("toggleExplorer").onclick = () => {
    explorerEl.classList.toggle("hidden");
    document.getElementById("toggleExplorer").setAttribute("aria-expanded", String(!explorerEl.classList.contains("hidden")));
  };
  document.getElementById("closeExplorer").onclick = () => {
    explorerEl.classList.add("hidden");
    document.getElementById("toggleExplorer").setAttribute("aria-expanded", "false");
  };

  function downloadFile(filename, content, type = "text/plain;charset=utf-8") {
    const blob = new Blob([content], { type });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
    notify("Descargando " + filename);
  }

  function extractCssFromRc(rcCode) {
    const html = rcToHtml(rcCode);
    if (!html) return '/* No CSS generado */\\n';

    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    let cssText = '/* CSS generado automáticamente desde RC Studio */\\n\\n';

    doc.querySelectorAll('style').forEach(styleEl => {
      const content = styleEl.textContent.trim();
      if (content) {
        cssText += content + '\\n\\n';
      }
    });

    cssText += '/* Estilos de elementos */\\n';
    doc.querySelectorAll('[style]').forEach(el => {
      const styleAttr = el.getAttribute('style');
      if (!styleAttr || !styleAttr.trim()) return;

      let selector = '';
      if (el.getAttribute('id')) {
        selector = '#' + el.getAttribute('id');
      } else if (el.getAttribute('class')) {
        selector = '.' + el.getAttribute('class').split(/\\s+/).join('.');
      } else {
        selector = el.tagName.toLowerCase();
      }

      cssText += `${selector} {\\n  ${styleAttr.split(';').map(s => s.trim()).filter(Boolean).join(';\\n  ')};\\n}\\n\\n`;
    });

    return cssText;
  }

  const exportModal = document.getElementById("exportModal");
  const closeExportModal = document.getElementById("closeExportModal");

  function showExportModal() {
    if (exportModal) exportModal.classList.remove("hidden");
  }

  function hideExportModal() {
    if (exportModal) exportModal.classList.add("hidden");
  }

  document.getElementById("saveBtn").onclick = () => {
    if (activeFile && files.has(activeFile)) {
      files.get(activeFile).content = editorEl.value;
      saveState();
    }
    showExportModal();
  };

  if (closeExportModal) closeExportModal.onclick = hideExportModal;
  if (exportModal) {
    exportModal.onclick = (e) => {
      if (e.target === exportModal) hideExportModal();
    };
  }

  document.getElementById("exportRcBtn").onclick = () => {
    hideExportModal();
    const name = activeFile || "main.rc";
    const content = editorEl.value;
    downloadFile(name.endsWith('.rc') ? name : name + '.rc', content);
  };

  document.getElementById("exportHtmlBtn").onclick = () => {
    hideExportModal();
    const baseName = (activeFile || "app.rc").replace(/\\.rc$/i, '');
    const content = rcToHtml(editorEl.value);
    downloadFile(`${baseName}.html`, content, "text/html;charset=utf-8");
  };

  document.getElementById("exportCssBtn").onclick = () => {
    hideExportModal();
    const baseName = (activeFile || "app.rc").replace(/\\.rc$/i, '');
    const content = extractCssFromRc(editorEl.value);
    downloadFile(`${baseName}.css`, content, "text/css;charset=utf-8");
  };

  if (panelSel) {
    panelSel.addEventListener("change", e => {
      applyPanelMode(e.target.value);
      saveState();
    });
    applyPanelMode(panelSel.value);
  }

  // Modal Diccionario RC
  const dictModal = document.getElementById("dictModal");
  const dictBtn = document.getElementById("dictBtn");
  const closeDictModal = document.getElementById("closeDictModal");
  const dictSearch = document.getElementById("dictSearch");

  if (dictBtn && dictModal) {
    dictBtn.addEventListener("click", () => {
      dictModal.classList.remove("hidden");
      if (dictSearch) dictSearch.focus();
    });
  }

  function hideDictModal() {
    if (dictModal) dictModal.classList.add("hidden");
  }

  if (closeDictModal) closeDictModal.addEventListener("click", hideDictModal);
  if (dictModal) {
    dictModal.addEventListener("click", (e) => {
      if (e.target === dictModal) hideDictModal();
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      hideDictModal();
      hideExportModal();
    }
  });

  if (dictSearch) {
    dictSearch.addEventListener("input", (e) => {
      const q = e.target.value.trim().toLowerCase();
      const categories = document.querySelectorAll(".dict-category");
      categories.forEach(cat => {
        let visibleCount = 0;
        const items = cat.querySelectorAll(".cmd-item");
        items.forEach(item => {
          const text = item.textContent.toLowerCase();
          if (!q || text.includes(q)) {
            item.style.display = "flex";
            visibleCount++;
          } else {
            item.style.display = "none";
          }
        });
        cat.style.display = (visibleCount > 0 || !q) ? "block" : "none";
      });
    });
  }

  // Exportar funciones globalmente para pruebas
  window.rcToHtml = rcToHtml;
  window.parseRcLine = parseRcLine;
  window.RC_COMMANDS_SPEC = RC_COMMANDS_SPEC;

  renderAll();
})();
</script>
</body>
</html>
"""

full_content = html_head + new_script

with open("index.html", "w") as f:
    f.write(full_content)

print("Updated index.html successfully!")
