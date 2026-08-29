/**
 * ============================================================================
 * MODULES EXPLORER & DETAIL MODAL - LEARNINGCPP
 * ============================================================================
 */

import { PHASES, MODULES } from './data/curriculum.js';

export class ModulesExplorer {
  constructor(containerId, modalId) {
    this.container = document.getElementById(containerId);
    this.modal = document.getElementById(modalId);
    this.activePhase = 'all';
    this.searchQuery = '';
    
    if (this.container) {
      this.init();
    }
  }

  init() {
    this.renderTabs();
    this.renderModules();
    this.bindEvents();
  }

  renderTabs() {
    const tabsContainer = document.getElementById('phase-tabs-container');
    if (!tabsContainer) return;

    tabsContainer.innerHTML = PHASES.map(p => `
      <button class="tab-btn ${p.id === this.activePhase ? 'active' : ''}" data-phase="${p.id}">
        ${p.name} <span style="opacity: 0.7; font-size: 0.75em; margin-left: 4px;">(${p.count})</span>
      </button>
    `).join('');
  }

  renderModules() {
    const filtered = MODULES.filter(m => {
      const matchesPhase = this.activePhase === 'all' || m.phase === this.activePhase;
      const query = this.searchQuery.toLowerCase();
      const matchesQuery = !query || 
        m.title.toLowerCase().includes(query) ||
        m.tagline.toLowerCase().includes(query) ||
        m.description.toLowerCase().includes(query) ||
        m.lessons.some(l => l.title.toLowerCase().includes(query) || l.desc.toLowerCase().includes(query));
      return matchesPhase && matchesQuery;
    });

    if (filtered.length === 0) {
      this.container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: var(--space-12); background: var(--bg-card); border-radius: var(--radius-xl); border: 1px dashed var(--border-strong);">
          <div style="font-size: 2.5rem; margin-bottom: var(--space-3);">🔍</div>
          <h3>No se encontraron módulos</h3>
          <p class="text-muted" style="margin-top: var(--space-2);">Intenta buscar con otros términos (ej: 'punteros', 'vector', 'templates', 'casting').</p>
        </div>
      `;
      return;
    }

    this.container.innerHTML = filtered.map(m => `
      <div class="module-card fade-in-up" data-module-id="${m.id}">
        <div>
          <div class="module-header">
            <span class="module-number">MÓDULO ${m.id}</span>
            <span class="badge ${m.status === 'completed' ? 'badge-emerald' : 'badge-amber'}">
              ${m.status === 'completed' ? '✔ ' + m.statusLabel : '🔄 ' + m.statusLabel}
            </span>
          </div>
          <h3 class="module-title">${m.icon} ${m.title}</h3>
          <p class="module-desc">${m.tagline}</p>
        </div>

        <div>
          <div style="font-size: var(--font-size-xs); color: var(--brand-primary); margin-bottom: var(--space-3); font-weight: var(--font-weight-medium);">
            🏆 Proyecto: <strong>${m.project}</strong>
          </div>
          <div class="module-footer">
            <span>📚 ${m.lessonsCount} Lecciones</span>
            <span style="display: flex; align-items: center; gap: 4px; color: var(--brand-primary); font-weight: var(--font-weight-semibold);">
              Ver detalles &rarr;
            </span>
          </div>
        </div>
      </div>
    `).join('');
  }

  bindEvents() {
    // Phase tabs
    const tabsContainer = document.getElementById('phase-tabs-container');
    if (tabsContainer) {
      tabsContainer.addEventListener('click', (e) => {
        const btn = e.target.closest('.tab-btn');
        if (!btn) return;
        this.activePhase = btn.dataset.phase;
        this.renderTabs();
        this.renderModules();
      });
    }

    // Search input
    const searchInput = document.getElementById('modules-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.trim();
        this.renderModules();
      });
    }

    // Module Card Click -> Open Detail Modal
    this.container.addEventListener('click', (e) => {
      const card = e.target.closest('.module-card');
      if (!card) return;
      const modId = card.dataset.moduleId;
      const mod = MODULES.find(m => m.id === modId);
      if (mod) {
        this.openModal(mod);
      }
    });

    // Close Modal Button
    if (this.modal) {
      this.modal.addEventListener('click', (e) => {
        if (e.target === this.modal || e.target.closest('.modal-close-btn')) {
          this.closeModal();
        }
      });

      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && this.modal.classList.contains('open')) {
          this.closeModal();
        }
      });
    }
  }

  openModal(mod) {
    if (!this.modal) return;
    const modalTitle = this.modal.querySelector('#modal-module-title');
    const modalContent = this.modal.querySelector('#modal-module-body');

    modalTitle.innerHTML = `
      <div style="display: flex; align-items: center; gap: var(--space-3);">
        <span style="font-size: 1.8rem;">${mod.icon}</span>
        <div>
          <div style="font-size: var(--font-size-xs); color: var(--brand-primary); font-family: var(--font-family-mono);">
            MÓDULO ${mod.id} · ${mod.phaseName}
          </div>
          <h2 style="font-size: var(--font-size-2xl);">${mod.title}</h2>
        </div>
      </div>
    `;

    modalContent.innerHTML = `
      <div style="margin-bottom: var(--space-6);">
        <p style="color: var(--text-secondary); font-size: var(--font-size-base); line-height: 1.6;">
          ${mod.description}
        </p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4); margin-bottom: var(--space-6);">
        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
          <div style="font-size: var(--font-size-xs); color: var(--text-muted); text-transform: uppercase;">Proyecto Integrador</div>
          <div style="font-weight: var(--font-weight-bold); font-size: var(--font-size-sm); margin-top: 4px; color: var(--brand-primary);">
            🏆 ${mod.project}
          </div>
        </div>
        <div style="background: var(--bg-surface); padding: var(--space-4); border-radius: var(--radius-lg); border: 1px solid var(--border-subtle);">
          <div style="font-size: var(--font-size-xs); color: var(--text-muted); text-transform: uppercase;">Estado de Desarrollo</div>
          <div style="font-weight: var(--font-weight-bold); font-size: var(--font-size-sm); margin-top: 4px;">
            ${mod.status === 'completed' ? '🟢 Listo para estudiar' : '🟡 En construcción'}
          </div>
        </div>
      </div>

      <h4 style="font-size: var(--font-size-base); margin-bottom: var(--space-3); color: var(--text-primary);">
        📖 Lecciones del Módulo (${mod.lessons.length}):
      </h4>
      <div style="display: flex; flex-direction: column; gap: var(--space-2); margin-bottom: var(--space-6);">
        ${mod.lessons.map(l => `
          <div style="display: flex; gap: var(--space-3); padding: var(--space-3); background: var(--bg-surface); border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <span style="font-family: var(--font-family-mono); font-size: 0.8em; color: var(--brand-primary); font-weight: bold; padding: 2px 6px; background: var(--bg-muted); border-radius: 4px; height: fit-content;">
              ${l.id}
            </span>
            <div>
              <div style="font-weight: var(--font-weight-semibold); font-size: var(--font-size-sm);">${l.title}</div>
              <div style="font-size: var(--font-size-xs); color: var(--text-muted);">${l.desc}</div>
            </div>
          </div>
        `).join('')}
      </div>

      ${mod.bugDemos && mod.bugDemos.length > 0 ? `
        <h4 style="font-size: var(--font-size-base); margin-bottom: var(--space-3); color: var(--status-danger);">
          🐞 Demos de Bugs Intencionales (Break-First):
        </h4>
        <div style="display: flex; flex-wrap: wrap; gap: var(--space-2); margin-bottom: var(--space-6);">
          ${mod.bugDemos.map(b => `
            <span class="badge badge-amber" style="font-family: var(--font-family-mono); font-size: 0.75rem;">
              🐛 ${b}
            </span>
          `).join('')}
        </div>
      ` : ''}

      <div style="padding: var(--space-4); background: rgba(56, 189, 248, 0.08); border-radius: var(--radius-lg); border-left: 3px solid var(--brand-primary);">
        <strong style="font-size: var(--font-size-xs); color: var(--brand-primary); text-transform: uppercase;">Decisión Arquitectónica Clave:</strong>
        <p style="font-size: var(--font-size-sm); color: var(--text-secondary); margin-top: 4px;">${mod.keyDecision}</p>
      </div>
    `;

    this.modal.classList.add('open');
  }

  closeModal() {
    if (!this.modal) return;
    this.modal.classList.remove('open');
  }
}
