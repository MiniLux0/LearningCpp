/**
 * ============================================================================
 * INTERACTIVE TERMINAL SIMULATOR - LEARNINGCPP
 * ============================================================================
 */

export class TerminalSimulator {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.history = [];
    this.historyIndex = -1;
    this.currentCode = `#include <iostream>

int main() {
    int oro_del_jugador{100};
    std::cout << "Bienvenido a LearningCpp!\\n";
    std::cout << "Oro inicial en Stack: " << oro_del_jugador << "\\n";
    return 0;
}`;
    this.isCompiled = false;
    this.init();
  }

  init() {
    this.render();
    this.bindEvents();
    this.printInitialBanner();
  }

  render() {
    this.container.innerHTML = `
      <div class="terminal-header">
        <div class="terminal-dots">
          <span class="dot dot-red"></span>
          <span class="dot dot-yellow"></span>
          <span class="dot dot-green"></span>
        </div>
        <div class="terminal-title">bash — LearningCpp Shell v2.0 (g++ 13.2 C++17/20)</div>
        <div style="font-size: 0.75rem; color: var(--text-muted);">x86_64</div>
      </div>
      <div class="terminal-body" id="term-output"></div>
      <div class="terminal-interactive-bar">
        <span class="terminal-prompt">user@learningcpp:~$</span>
        <input type="text" id="term-input" autocomplete="off" spellcheck="false" 
          placeholder="Prueba: 'compile', 'run', 'help', o 'modules'..." 
          style="flex: 1; background: transparent; border: none; color: #fff; font-family: var(--font-family-mono); font-size: 0.85rem; outline: none;" />
        <button id="term-send-btn" class="btn btn-primary" style="padding: 0.25rem 0.75rem; font-size: 0.75rem;">Ejecutar</button>
      </div>
    `;
  }

  bindEvents() {
    const input = this.container.querySelector('#term-input');
    const sendBtn = this.container.querySelector('#term-send-btn');

    const handleCommand = () => {
      const val = input.value.trim();
      if (!val) return;
      this.history.push(val);
      this.historyIndex = this.history.length;
      this.execute(val);
      input.value = '';
    };

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        handleCommand();
      } else if (e.key === 'ArrowUp') {
        if (this.historyIndex > 0) {
          this.historyIndex--;
          input.value = this.history[this.historyIndex];
        }
      } else if (e.key === 'ArrowDown') {
        if (this.historyIndex < this.history.length - 1) {
          this.historyIndex++;
          input.value = this.history[this.historyIndex];
        } else {
          this.historyIndex = this.history.length;
          input.value = '';
        }
      }
    });

    sendBtn.addEventListener('click', handleCommand);
  }

  printInitialBanner() {
    this.printLine('user@learningcpp:~$ ', 'cat welcome.txt', 'prompt-cmd');
    this.printLine('', '🚀 Entorno interactivo de compilación C++17/20 listo.', 'terminal-out-info');
    this.printLine('', 'Escribe "compile" para compilar tu primer programa o "help" para ver comandos.', 'terminal-out-info');
  }

  printLine(prefix, text, className = '') {
    const output = this.container.querySelector('#term-output');
    if (!output) return;

    const line = document.createElement('div');
    line.className = 'terminal-line';
    
    if (prefix) {
      const promptSpan = document.createElement('span');
      promptSpan.className = 'terminal-prompt';
      promptSpan.textContent = prefix;
      line.appendChild(promptSpan);
    }

    const textSpan = document.createElement('span');
    if (className) textSpan.className = className;
    textSpan.textContent = text;
    line.appendChild(textSpan);

    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
  }

  execute(cmd) {
    this.printLine('user@learningcpp:~$ ', cmd, 'cmd-text');
    const lower = cmd.toLowerCase().trim();

    if (lower === 'clear' || lower === 'cls') {
      const output = this.container.querySelector('#term-output');
      if (output) output.innerHTML = '';
      return;
    }

    if (lower === 'help') {
      this.printLine('', 'Comandos disponibles:', 'terminal-out-info');
      this.printLine('', '  compile | g++     - Compila el programa actual con C++17 y warnings (-Wall -Wextra)', 'terminal-out-info');
      this.printLine('', '  run | ./app       - Ejecuta el binario compilado', 'terminal-out-info');
      this.printLine('', '  cat main.cpp      - Muestra el código fuente actual', 'terminal-out-info');
      this.printLine('', '  modules           - Lista los 15 módulos del plan de estudios', 'terminal-out-info');
      this.printLine('', '  test bug          - Simula la detonación de un Undefined Behavior', 'terminal-out-info');
      this.printLine('', '  clear             - Limpia la pantalla de la terminal', 'terminal-out-info');
      return;
    }

    if (lower.startsWith('g++') || lower === 'compile') {
      this.printLine('', '[INFO] g++ -std=c++17 -Wall -Wextra -O2 main.cpp -o app', 'terminal-out-info');
      setTimeout(() => {
        this.printLine('', '✔ Compilación exitosa con C++17 (0 errores, 0 warnings). Binario generado: app.exe', 'terminal-out-success');
        this.isCompiled = true;
      }, 200);
      return;
    }

    if (lower === './app' || lower === 'run' || lower === '.\\app.exe') {
      if (!this.isCompiled) {
        this.printLine('', 'bash: ./app: No such file or directory. Debes compilar primero con "compile".', 'terminal-out-error');
        return;
      }
      this.printLine('', '--- EJECUTANDO ./app ---', 'terminal-out-info');
      this.printLine('', 'Bienvenido a LearningCpp!', 'terminal-out-success');
      this.printLine('', 'Oro inicial en Stack: 100', 'terminal-out-success');
      this.printLine('', '[Proceso finalizado con código de salida: 0 (0x0)]', 'terminal-out-info');
      return;
    }

    if (lower === 'cat main.cpp' || lower === 'cat') {
      this.printLine('', this.currentCode, 'terminal-out-info');
      return;
    }

    if (lower === 'modules') {
      this.printLine('', '=== PLAN DE ESTUDIOS LEARNINGCPP (15 MÓDULOS) ===', 'terminal-out-info');
      this.printLine('', 'Fase 1: M01 (Getting Started) | M02 (Fundamental Types) | M03 (Scope & Control Flow)', 'terminal-out-success');
      this.printLine('', 'Fase 2: M04 (Functions) | M05 (Constants & Strings)', 'terminal-out-success');
      this.printLine('', 'Fase 3: M06 (Arrays & Vectors) | M07 (Compound Types)', 'terminal-out-warn');
      this.printLine('', 'Fase 4: M08 (References & Addresses) | M09 (Dynamic Memory & RAII)', 'terminal-out-warn');
      this.printLine('', 'Fase 5: M10 (Classes) | M11 (Inheritance) | M12 (Polymorphism)', 'terminal-out-warn');
      this.printLine('', 'Fase 6: M13 (Error Handling) | M14 (Templates) | M15 (STL Algorithms & Capstone)', 'terminal-out-warn');
      return;
    }

    if (lower === 'test bug') {
      this.printLine('', '[ALERTA] Detonando D03_IntegerDivisionBug.cpp...', 'terminal-out-warn');
      this.printLine('', 'Calculando division entera: 7 / 2 = 3 (PERDIDA DE PRECISION CRITICA)', 'terminal-out-error');
      this.printLine('', 'Solucion moderna aplicada: static_cast<double>(7) / 2 = 3.5', 'terminal-out-success');
      return;
    }

    // Default fallback
    this.printLine('', `bash: ${cmd}: orden no encontrada. Escribe "help" para ver la lista de comandos.`, 'terminal-out-error');
  }
}
