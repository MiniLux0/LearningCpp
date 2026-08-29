/**
 * ============================================================================
 * INTERACTIVE HARDWARE & RAM VISUALIZER (STACK VS HEAP SIMULATOR)
 * Bespoke Handcrafted Component for LearningCpp
 * ============================================================================
 */

export class RamVisualizer {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.stackFrames = [
      { name: "main() Frame", address: "0x7ffee14b8a00", type: "Stack Frame", size: "32 bytes", color: "#3b82f6" }
    ];
    this.stackVariables = [
      { name: "int vidas_jugador{3}", address: "0x7ffee14b8a08", value: "3", size: "4 bytes", type: "int" }
    ];
    this.heapBlocks = [];

    this.init();
  }

  init() {
    this.render();
    this.bindEvents();
  }

  render() {
    this.container.innerHTML = `
      <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-xl); overflow: hidden;">
        
        <!-- Controls Bar -->
        <div style="padding: var(--space-4) var(--space-6); background: #161b22; border-bottom: 1px solid var(--border-subtle); display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: var(--space-3);">
          <div>
            <span style="font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400); text-transform: uppercase; letter-spacing: 0.05em;">Simulador de Memoria Física (x86_64 RAM)</span>
            <h4 style="font-size: var(--font-size-base); margin-top: 2px;">Inspección en Tiempo Real: Stack vs Heap & Ciclo RAII</h4>
          </div>
          <div style="display: flex; gap: var(--space-2); flex-wrap: wrap;">
            <button id="ram-btn-push-stack" class="btn btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.75rem;">
              + Push Variable en Stack
            </button>
            <button id="ram-btn-alloc-heap" class="btn btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.75rem;">
              + make_unique&lt;T&gt; (Heap)
            </button>
            <button id="ram-btn-scope-exit" class="btn btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.75rem; color: var(--color-warning);">
              ⚡ Salir de Ámbito {} (RAII Destructor)
            </button>
            <button id="ram-btn-reset" class="btn btn-secondary" style="font-size: 0.75rem; padding: 0.35rem 0.75rem;">
              ↺ Reset
            </button>
          </div>
        </div>

        <!-- Visual Memory Layout (Stack vs Heap Side-by-Side) -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1px; background: var(--border-subtle); min-height: 260px;">
          
          <!-- Stack Memory (Grows Downward) -->
          <div style="background: var(--bg-surface); padding: var(--space-5);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <span style="font-weight: 600; font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #3b82f6;"></span>
                STACK (Pila de Ejecución)
              </span>
              <span style="font-family: var(--font-family-mono); font-size: 0.7rem; color: var(--zinc-500);">LIFO · Memoria Automática</span>
            </div>

            <div id="ram-stack-list" style="display: flex; flex-direction: column; gap: var(--space-2);">
              ${this.stackVariables.map(v => `
                <div class="fade-in-up" style="background: rgba(59, 130, 246, 0.08); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: var(--radius-md); padding: var(--space-3); font-family: var(--font-family-mono); font-size: 0.75rem;">
                  <div style="display: flex; justify-content: space-between; color: #93c5fd; font-weight: 600;">
                    <span>${v.name}</span>
                    <span>${v.address}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between; color: var(--zinc-400); margin-top: 4px;">
                    <span>Valor: <strong style="color: #fff;">${v.value}</strong></span>
                    <span>${v.size}</span>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Heap Memory (Dynamic Allocation) -->
          <div style="background: var(--bg-surface); padding: var(--space-5);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3);">
              <span style="font-weight: 600; font-size: 0.85rem; display: flex; align-items: center; gap: 6px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #10b981;"></span>
                HEAP (Memoria Dinámica)
              </span>
              <span style="font-family: var(--font-family-mono); font-size: 0.7rem; color: var(--zinc-500);">RAII Smart Pointers</span>
            </div>

            <div id="ram-heap-list" style="display: flex; flex-direction: column; gap: var(--space-2);">
              ${this.heapBlocks.length === 0 ? `
                <div style="border: 1px dashed var(--border-strong); border-radius: var(--radius-md); padding: var(--space-6); text-align: center; color: var(--zinc-500); font-size: 0.75rem; font-family: var(--font-family-mono);">
                  [ Heap Vacío — Cero fugas de memoria ]<br>
                  Haz clic en "+ make_unique" para solicitar memoria dinámica
                </div>
              ` : this.heapBlocks.map(b => `
                <div class="fade-in-up" style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: var(--space-3); font-family: var(--font-family-mono); font-size: 0.75rem;">
                  <div style="display: flex; justify-content: space-between; color: #6ee7b7; font-weight: 600;">
                    <span>${b.name}</span>
                    <span>${b.address}</span>
                  </div>
                  <div style="display: flex; justify-content: space-between; color: var(--zinc-400); margin-top: 4px;">
                    <span>Propietario RAII: <strong style="color: #93c5fd;">${b.owner}</strong></span>
                    <span>${b.size}</span>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

        </div>

        <!-- Log / Explanation Footer -->
        <div id="ram-log-bar" style="padding: var(--space-3) var(--space-6); background: #11161d; border-top: 1px solid var(--border-subtle); font-family: var(--font-family-mono); font-size: 0.75rem; color: var(--zinc-400);">
          <span style="color: var(--brand-primary); font-weight: 600;">[SYS_LOG]</span> Estado actual: 1 variable en Stack (0x7ffee14b8a08), 0 bloques dinámicos en Heap.
        </div>
      </div>
    `;
  }

  bindEvents() {
    const btnPush = this.container.querySelector('#ram-btn-push-stack');
    const btnAlloc = this.container.querySelector('#ram-btn-alloc-heap');
    const btnScope = this.container.querySelector('#ram-btn-scope-exit');
    const btnReset = this.container.querySelector('#ram-btn-reset');

    if (btnPush) {
      btnPush.addEventListener('click', () => {
        const id = this.stackVariables.length + 1;
        const hex = (0x7ffee14b8a08 + id * 8).toString(16);
        this.stackVariables.push({
          name: `double ataque{${(id * 14.5).toFixed(1)}}`,
          address: `0x${hex}`,
          value: `${(id * 14.5).toFixed(1)}`,
          size: "8 bytes",
          type: "double"
        });
        this.render();
        this.bindEvents();
        this.updateLog(`Push en Stack: variable 'ataque' alojada en 0x${hex} (+8 bytes).`);
      });
    }

    if (btnAlloc) {
      btnAlloc.addEventListener('click', () => {
        const id = this.heapBlocks.length + 1;
        const heapHex = (0x600003a201b0 + id * 32).toString(16);
        const stackHex = (0x7ffee14b8a50 + id * 8).toString(16);

        // Add RAII owner in stack
        this.stackVariables.push({
          name: `std::unique_ptr<Monstruo> p${id}`,
          address: `0x${stackHex}`,
          value: `-> 0x${heapHex}`,
          size: "8 bytes (ptr)",
          type: "smart_ptr",
          isDynamicOwner: true,
          heapTargetId: id
        });

        // Add Heap block
        this.heapBlocks.push({
          id: id,
          name: `Monstruo { hp: ${100 * id}, nivel: ${id} }`,
          address: `0x${heapHex}`,
          owner: `p${id} (Stack)`,
          size: "32 bytes"
        });

        this.render();
        this.bindEvents();
        this.updateLog(`Asignación dinámica: std::make_unique<Monstruo>() asignó 32 bytes en Heap (0x${heapHex}) gobernados por p${id} en Stack.`);
      });
    }

    if (btnScope) {
      btnScope.addEventListener('click', () => {
        if (this.stackVariables.length <= 1 && this.heapBlocks.length === 0) {
          this.updateLog("No hay variables temporales de ámbito que liberar.");
          return;
        }

        // RAII Destruction
        const freedHeap = this.heapBlocks.length;
        this.heapBlocks = [];
        this.stackVariables = [this.stackVariables[0]]; // keep main frame

        this.render();
        this.bindEvents();
        this.updateLog(`⚡ Cierre de bloque {}: El Stack Unwinding destruyó las variables locales y RAII liberó automáticamente ${freedHeap} bloque(s) en el Heap sin fugas (delete implícito).`);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => {
        this.stackVariables = [
          { name: "int vidas_jugador{3}", address: "0x7ffee14b8a08", value: "3", size: "4 bytes", type: "int" }
        ];
        this.heapBlocks = [];
        this.render();
        this.bindEvents();
        this.updateLog("Memoria reinicializada al estado base.");
      });
    }
  }

  updateLog(msg) {
    const logBar = this.container.querySelector('#ram-log-bar');
    if (logBar) {
      logBar.innerHTML = `<span style="color: var(--brand-primary); font-weight: 600;">[SYS_LOG]</span> ${msg}`;
    }
  }
}
