/**
 * ============================================================================
 * INTERACTIVE "BREAK-FIRST, FIX-LATER" PLAYGROUND - LEARNINGCPP
 * ============================================================================
 */

export const BUGS_DATA = [
  {
    id: "division",
    title: "1. La Trampa de la División Entera (7 / 2 = 3)",
    topic: "Tipos Fundamentales & Casting",
    module: "M02 (Fundamental Types - L03/L05)",
    brokenSnippet: `// ❌ FALLO CLÁSICO: División entera truncada
#include <iostream>

int main() {
    int total_cuenta{70};
    int amigos{20};
    
    // El hardware ejecuta división entera truncando los decimales
    double por_persona = total_cuenta / amigos; // 70 / 20 = 3.0 (ERROR LÓGICO)
    
    std::cout << "Monto por persona: $" << por_persona << '\\n'; 
    // Muestra $3 en lugar de $3.5 (Faltan $10 en total)
    return 0;
}`,
    fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Casting explícito en compilación
#include <iostream>

int main() {
    int total_cuenta{70};
    int amigos{20};
    
    // static_cast promueve explícitamente a double antes de la división
    double por_persona{ static_cast<double>(total_cuenta) / amigos };
    
    std::cout << "Monto exacto: $" << por_persona << '\\n'; 
    // Muestra $3.5 de forma exacta sin pérdidas
    return 0;
}`,
    explanation: "En C++, cuando ambos operandos son enteros, el operador `/` descarta silenciosamente los decimales. Con `static_cast<double>()` forzamos la división en punto flotante sin recurrir a C-casts inseguros."
  },
  {
    id: "passbyvalue",
    title: "2. Pass-by-value: La Trampa del Clon Aislado",
    topic: "Funciones & Memoria en Stack",
    module: "M04 (Functions - L04) & M08",
    brokenSnippet: `// ❌ FALLO CLÁSICO: Mutar una copia aislada
#include <iostream>

void duplicarOro(int cantidad) {
    // Esta variable es un CLON en una nueva dirección del Stack
    cantidad = cantidad * 2; 
}

int main() {
    int oro{100};
    duplicarOro(oro);
    
    // El oro original jamás cambió en el main
    std::cout << "Oro: " << oro << '\\n'; // Imprime 100
    return 0;
}`,
    fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Paso por referencia (Zero-Copy)
#include <iostream>

// El operador '&' enlaza directamente con la dirección de memoria original
void duplicarOro(int& cantidad) {
    cantidad = cantidad * 2; // Muta directamente la variable original
}

int main() {
    int oro{100};
    duplicarOro(oro);
    
    std::cout << "Oro mutado: " << oro << '\\n'; // Imprime 200
    return 0;
}`,
    explanation: "Por defecto, C++ clona cada argumento en el Stack (Pass-by-value). Con referencias `&` creamos un alias directo a la memoria física original, eliminando copias pesadas."
  },
  {
    id: "uninitialized",
    title: "3. La Variable sin Inicializar (Basura en RAM)",
    topic: "Inicialización Uniforme {}",
    module: "M01 (Getting Started - L05)",
    brokenSnippet: `// ❌ FALLO CLÁSICO: Basura residual en el Stack
#include <iostream>

int main() {
    int vidas_jugador; // ¡Memoria sin inicializar!
    
    // Lee lo que sea que estuviese antes en esa dirección física
    std::cout << "Vidas: " << vidas_jugador << '\\n'; 
    // Salida impredecible (Undefined Behavior): ej. 4201952 o crasheo
    return 0;
}`,
    fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Inicialización uniforme {}
#include <iostream>

int main() {
    // Las llaves garantizan inicialización inmediata por defecto (0)
    int vidas_jugador{3}; 
    
    std::cout << "Vidas garantizadas: " << vidas_jugador << '\\n'; 
    // Siempre imprime 3 limpiamente
    return 0;
}`,
    explanation: "Declarar variables primitivas sin inicializar es una de las causas #1 de bugs de seguridad. C++17/20 impone la inicialización uniforme con llaves `{}`."
  },
  {
    id: "slicing",
    title: "4. Object Slicing: Destrucción de Datos en Polimorfismo",
    topic: "Herencia & Polimorfismo",
    module: "M11 (Inheritance - L06) & M12",
    brokenSnippet: `// ❌ FALLO CLÁSICO: Almacenar derivadas por valor
#include <iostream>
#include <vector>

class Base { public: virtual void atacar() { std::cout << "Base\\n"; } };
class Jefe : public Base { public: int vidaExtra{500}; void atacar() override { std::cout << "Jefe\\n"; } };

int main() {
    std::vector<Base> enemigos;
    enemigos.push_back(Jefe{}); // 💥 SLICING: 'vidaExtra' es recortada y destruida
    enemigos[0].atacar(); // Llama a Base::atacar en vez de Jefe::atacar
}
`,
    fixedSnippet: `// ✅ SOLUCIÓN MODERNA: Punteros inteligentes polimórficos
#include <iostream>
#include <vector>
#include <memory>

class Base { public: virtual void atacar() const = 0; virtual ~Base() = default; };
class Jefe : public Base { public: void atacar() const override { std::cout << "Ataque de Jefe!\\n"; } };

int main() {
    std::vector<std::unique_ptr<Base>> enemigos;
    enemigos.push_back(std::make_unique<Jefe>());
    
    enemigos[0]->atacar(); // Despacho dinámico VTable perfecto
}
`,
    explanation: "Guardar objetos derivados por valor en contenedores base recorta (*slices*) los campos especializados. La solución idiomática es `std::vector<std::unique_ptr<Base>>` con destructores virtuales."
  }
];

export class CodePlayground {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;
    this.currentBugIndex = 0;
    this.init();
  }

  init() {
    this.render();
    this.bindEvents();
  }

  render() {
    const bug = BUGS_DATA[this.currentBugIndex];
    this.container.innerHTML = `
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: var(--space-4); margin-bottom: var(--space-6);">
        <div>
          <span class="badge badge-amber" style="margin-bottom: var(--space-2);">${bug.module}</span>
          <h3 style="font-size: var(--font-size-2xl);">${bug.title}</h3>
        </div>
        <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
          ${BUGS_DATA.map((b, idx) => `
            <button class="btn btn-secondary bug-tab-btn ${idx === this.currentBugIndex ? 'active' : ''}" data-index="${idx}" style="font-size: 0.75rem; padding: 0.4rem 0.8rem; ${idx === this.currentBugIndex ? 'background: var(--brand-primary); color: #000;' : ''}">
              Bug #${idx + 1}
            </button>
          `).join('')}
        </div>
      </div>

      <div class="diff-container">
        <div class="diff-box">
          <div class="diff-header broken">
            <span>🐞 1. Break-First (El Dolor del Fallo)</span>
            <span>ERROR EN RUNTIME / LÓGICO</span>
          </div>
          <pre><code class="language-cpp">${this.escapeHtml(bug.brokenSnippet)}</code></pre>
        </div>

        <div class="diff-box">
          <div class="diff-header fixed">
            <span>✨ 2. Fix-Later (La Solución Moderna C++17/20)</span>
            <span>IDIOMÁTICO & SEGURO</span>
          </div>
          <pre><code class="language-cpp">${this.escapeHtml(bug.fixedSnippet)}</code></pre>
        </div>
      </div>

      <div style="margin-top: var(--space-6); padding: var(--space-5); background: var(--bg-card); border-radius: var(--radius-lg); border-left: 4px solid var(--brand-primary);">
        <h4 style="font-size: var(--font-size-base); margin-bottom: var(--space-2); color: var(--brand-primary);">🧠 Modelo Mental & Hardware:</h4>
        <p style="font-size: var(--font-size-sm); color: var(--text-secondary); line-height: 1.6;">${bug.explanation}</p>
      </div>
    `;
  }

  escapeHtml(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  bindEvents() {
    this.container.querySelectorAll('.bug-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const idx = parseInt(btn.dataset.index, 10);
        this.currentBugIndex = idx;
        this.render();
        this.bindEvents();
      });
    });
  }
}
