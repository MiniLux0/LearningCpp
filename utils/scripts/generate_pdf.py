import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Syllabus Oficial — LearningCpp</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

  @page {
    size: A4;
    margin: 15mm 15mm 16mm 15mm;
    @top-right {
      content: "LearningCpp · C++ Moderno y Arquitectura de Sistemas";
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #64748b;
      font-weight: 500;
    }
    @bottom-right {
      content: "Página " counter(page) " de " counter(pages);
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #64748b;
      font-weight: 500;
    }
    @bottom-left {
      content: "LearningCpp · Syllabus Oficial (C++17 Base · Evolución C++20)";
      font-family: 'Inter', sans-serif;
      font-size: 7.5pt;
      color: #64748b;
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Inter', -apple-system, sans-serif;
    color: #0f172a;
    background-color: #ffffff;
    line-height: 1.42;
    font-size: 8.3pt;
    -webkit-font-smoothing: antialiased;
  }

  .page-break {
    page-break-after: always;
    break-after: page;
  }

  .avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Formal Institutional Masthead */
  .masthead {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 10px;
    margin-bottom: 12px;
  }

  .institution {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 7.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #2563eb;
    margin-bottom: 3px;
  }

  .course-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18pt;
    font-weight: 700;
    color: #09090b;
    line-height: 1.15;
    letter-spacing: -0.5px;
    margin-bottom: 3px;
  }

  .course-subtitle {
    font-size: 9pt;
    color: #475569;
    font-weight: 600;
    margin-bottom: 8px;
  }

  .masthead-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    font-size: 7.8pt;
    color: #334155;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
  }

  .masthead-meta span strong {
    color: #0f172a;
  }

  /* Typography */
  h2.section-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #0f172a;
    padding-bottom: 3px;
    margin-top: 12px;
    margin-bottom: 7px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  h3.sub-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 9pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 8px;
    margin-bottom: 3px;
  }

  p {
    margin-bottom: 5px;
    color: #334155;
    text-align: justify;
  }

  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.6pt;
    background: #f1f5f9;
    color: #0f172a;
    padding: 1px 3px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
  }

  /* Formal Data Tables */
  table.formal-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 8px;
    font-size: 7.8pt;
  }

  table.formal-table th {
    background: #f8fafc;
    color: #0f172a;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 7.2pt;
    letter-spacing: 0.5px;
    padding: 4px 7px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }

  table.formal-table td {
    padding: 4px 7px;
    border: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: middle;
  }

  table.formal-table tr:nth-child(even) td {
    background: #fafafa;
  }

  /* Learning Outcomes Grid */
  .ra-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 8px;
  }

  .ra-card {
    border: 1px solid #e2e8f0;
    border-left: 3px solid #2563eb;
    background: #fcfcfd;
    padding: 5px 8px;
    border-radius: 0 4px 4px 0;
  }

  .ra-card-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 7.8pt;
    color: #0f172a;
    margin-bottom: 2px;
  }

  .ra-card-desc {
    font-size: 7.3pt;
    color: #475569;
    line-height: 1.32;
    text-align: justify;
  }

  /* Workload & Rubrics Boxes */
  .workload-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin-bottom: 8px;
  }

  .workload-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 9px;
  }

  .workload-box h4 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 7.8pt;
    color: #0f172a;
    font-weight: 700;
    margin-bottom: 3px;
  }

  .workload-box p {
    font-size: 7.2pt;
    color: #475569;
    line-height: 1.3;
    margin-bottom: 0;
  }

  .rubrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
    margin-bottom: 8px;
  }

  .rubric-card {
    border: 1px solid #e2e8f0;
    background: #f8fafc;
    padding: 5px 8px;
    border-radius: 4px;
    border-top: 2px solid #2563eb;
  }

  .rubric-card h5 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 7.6pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
  }

  .rubric-card p {
    font-size: 7.1pt;
    color: #475569;
    line-height: 1.3;
    margin-bottom: 0;
  }

  /* Pillars Horizontal */
  .pillars-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
    margin-bottom: 8px;
  }

  .pillar-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-top: 2px solid #0f172a;
    padding: 5px 7px;
    border-radius: 0 0 4px 4px;
  }

  .pillar-box h4 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 7.5pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
  }

  .pillar-box p {
    font-size: 7pt;
    color: #475569;
    line-height: 1.25;
    margin-bottom: 0;
  }

  /* Phase Section Banner */
  .phase-header {
    background: #0f172a;
    color: #ffffff;
    padding: 4px 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-top: 10px;
    margin-bottom: 7px;
    border-radius: 3px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .phase-header span.tag {
    font-size: 6.8pt;
    font-weight: 500;
    color: #93c5fd;
    text-transform: uppercase;
  }

  /* Module Card */
  .module-card {
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    margin-bottom: 7px;
    background: #ffffff;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .module-header {
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
    padding: 5px 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .module-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    color: #0f172a;
  }

  .module-meta-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.8pt;
    font-weight: 600;
    padding: 1px 5px;
    border-radius: 3px;
    background: #e2e8f0;
    color: #334155;
  }

  .module-body {
    padding: 6px 8px;
  }

  .module-objective {
    font-size: 7.5pt;
    color: #334155;
    margin-bottom: 5px;
    line-height: 1.32;
  }

  .module-objective strong {
    color: #0f172a;
  }

  /* Lesson List Table */
  .lessons-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 4px;
    font-size: 7.3pt;
  }

  .lessons-table td {
    padding: 2.5px 5px;
    border-top: 1px solid #f1f5f9;
    vertical-align: top;
  }

  .lessons-table td.code-col {
    width: 28px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    color: #2563eb;
  }

  .lessons-table td.title-col {
    font-weight: 600;
    color: #1e293b;
    width: 175px;
  }

  .lessons-table td.desc-col {
    color: #64748b;
  }

  /* Module Footer Details */
  .module-footer-details {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5px;
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
    padding: 4px 7px;
    font-size: 7pt;
  }

  .module-footer-details span strong {
    color: #0f172a;
  }

  /* Commandment Box */
  .commandment-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 3px solid #0f172a;
    padding: 7px 10px;
    margin-top: 7px;
    margin-bottom: 8px;
  }

  .commandment-list {
    list-style: none;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 4px 10px;
    font-size: 7.2pt;
    color: #334155;
  }

  .commandment-list li strong {
    color: #0f172a;
  }

  /* Bibliography IEEE */
  .biblio-list {
    list-style: decimal;
    padding-left: 14px;
    font-size: 7.3pt;
    color: #334155;
    line-height: 1.35;
  }

  .biblio-list li {
    margin-bottom: 3px;
  }

  .footer-sig {
    margin-top: 10px;
    padding-top: 6px;
    border-top: 1px solid #cbd5e1;
    font-size: 7pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>
</head>
<body>

  <!-- ======================================================================
       PAGE 1: MASTHEAD, FICHA TÉCNICA, RA & METODOLOGÍA
       ====================================================================== -->
  <header class="masthead">
    <div class="institution">LEARNINGCPP · PROGRAMA DE INGENIERÍA Y ARQUITECTURA DE SOFTWARE</div>
    <h1 class="course-title">LearningCpp: C++ Moderno y Arquitectura de Sistemas</h1>
    <div class="course-subtitle">De Cero Absoluto a C++ Moderno — Fundamentos de Grado Profesional (C++17 Base · Evolución C++20)</div>
    <div class="masthead-meta">
      <span><strong>Estándar:</strong> C++17 Base (Evolución C++20)</span>
      <span><strong>Alcance:</strong> 15 Módulos · 6 Fases · 117 Lecciones</span>
      <span><strong>Dedicación:</strong> 16 Sem. Regular / 8 Sem. Intensiva</span>
      <span><strong>Autor:</strong> Jesus Vera V. (MiniLux0)</span>
    </div>
  </header>

  <h2 class="section-heading">1. Ficha Técnica y Fundamentación Académica</h2>
  <p>
    El programa <strong>LearningCpp</strong> constituye un itinerario formativo riguroso orientado a la enseñanza de C++ Moderno desde cero absoluto hasta los fundamentos de grado profesional de la ingeniería de software. El curso comprende el modelo físico de la memoria (Stack, Heap, direcciones y tabla virtual) blindando el software mediante gestión determinista de recursos (RAII con <code>std::unique_ptr</code>), inmutabilidad por defecto y computación declarativa con algoritmos STL.
  </p>

  <table class="formal-table">
    <thead>
      <tr>
        <th style="width: 25%;">Parámetro</th>
        <th>Especificación Técnica</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Toolchain Oficial</strong></td>
        <td><code>g++ >= 13.0</code> (MSYS2 UCRT64 / GNU Linux) o <code>Clang++ >= 16.0</code> (Apple Clang / LLVM).</td>
      </tr>
      <tr>
        <td><strong>Flags de Compilación</strong></td>
        <td><code>-std=c++17 -Wall -Wextra -Wpedantic -Wconversion -Wshadow -O2</code></td>
      </tr>
      <tr>
        <td><strong>Carga Horaria Sugerida</strong></td>
        <td><strong>Ruta Regular:</strong> 16 semanas (6-8 h/semana) · <strong>Ruta Bootcamp:</strong> 8 semanas (12-15 h/semana). Total: ~120 horas lectivas y prácticas.</td>
      </tr>
      <tr>
        <td><strong>Metodología Pedagógica</strong></td>
        <td><em>Break-First, Fix-Later</em>, Modelos Mentales de RAM, Principio de la Escalera, Scaffolding & Fading.</td>
      </tr>
      <tr>
        <td><strong>Evaluación & Entregables</strong></td>
        <td>15 Mini-Proyectos Modulares, 45 Demos de Bugs intencionales y 1 Proyecto Capstone Final Integrador.</td>
      </tr>
    </tbody>
  </table>

  <h2 class="section-heading">2. Resultados de Aprendizaje y Competencias (RA)</h2>
  <div class="ra-grid">
    <div class="ra-card">
      <div class="ra-card-title">RA1 · Modelo Físico de Memoria RAM</div>
      <div class="ra-card-desc">Diagnosticar la distribución física de bytes en memoria, ciclos de vida en el Stack frente al Heap y trazado exacto de direcciones hexadecimales (<code>0x...</code>).</div>
    </div>
    <div class="ra-card">
      <div class="ra-card-title">RA2 · Gestión Determinista de Recursos (RAII)</div>
      <div class="ra-card-desc">Dominar la propiedad de memoria en el Heap con <code>std::unique_ptr</code>, erradicando por completo fugas de memoria (Memory Leaks) y accesos Use-After-Free.</div>
    </div>
    <div class="ra-card">
      <div class="ra-card-title">RA3 · POO Segura y Polimorfismo Dinámico</div>
      <div class="ra-card-desc">Diseñar invariantes encapsuladas con constructores seguros, despacho dinámico mediante VTable, destructores virtuales obligatorios y blindaje contra Object Slicing.</div>
    </div>
    <div class="ra-card">
      <div class="ra-card-title">RA4 · Resiliencia y Tolerancia a Fallos</div>
      <div class="ra-card-desc">Implementar políticas de excepciones basadas en Stack Unwinding, optimización de relocalización con <code>noexcept</code> y ausencias esperadas con <code>std::optional</code>.</div>
    </div>
    <div class="ra-card">
      <div class="ra-card-title">RA5 · Metaprogramación y Programación Genérica</div>
      <div class="ra-card-desc">Construir plantillas monomórficas evaluadas en compilación con cero costo en runtime, buffers estáticos (NTTP) y funciones anónimas (Lambdas).</div>
    </div>
    <div class="ra-card">
      <div class="ra-card-title">RA6 · Computación Declarativa y Algoritmos STL</div>
      <div class="ra-card-desc">Utilizar algoritmos estándar de la STL (<code>&lt;algorithm&gt;</code>) para transformaciones, búsquedas y filtros, combinándolos con <code>range-for</code> idiomáticos para secuencias directas.</div>
    </div>
  </div>

  <h2 class="section-heading">3. Carga Horaria y Rúbricas de Dominio por Niveles</h2>
  <div class="workload-grid">
    <div class="workload-box">
      <h4>⏱️ Distribución de Horas por Fase</h4>
      <p>• Fase 1 (Fundamentos): ~15h · Fase 2 (Funciones): ~12h · Fase 3 (Colecciones): ~18h<br>• Fase 4 (Memoria Real): ~20h · Fase 5 (POO Moderna): ~25h · Fase 6 (Resiliencia & STL): ~30h</p>
    </div>
    <div class="workload-box">
      <h4>📈 Rutas de Aprendizaje</h4>
      <p>• <strong>Semestral:</strong> 16 semanas dedicando 6 a 8 horas semanales.<br>• <strong>Intensiva:</strong> 8 semanas con dedicación inmersiva de 12 a 15 horas semanales.</p>
    </div>
  </div>

  <div class="rubrics-grid">
    <div class="rubric-card">
      <h5>Nivel Aprendiz (Fases 1–2)</h5>
      <p>Streams seguros, prevención de narrowing con <code>{}</code>, casting seguro con <code>static_cast</code> y aislamiento de Stack frames.</p>
    </div>
    <div class="rubric-card">
      <h5>Nivel Intermedio (Fases 3–4)</h5>
      <p>Dominio de <code>std::vector</code> con <code>.at()</code>, paso <code>const &</code> Zero-Copy, Heap y ownership con <code>std::unique_ptr</code> (0 leaks).</p>
    </div>
    <div class="rubric-card">
      <h5>Nivel Avanzado (Fases 5–6)</h5>
      <p>Jerarquías polimórficas VTable, destructores virtuales, Stack Unwinding, templates <code>if constexpr</code> y pipelines STL.</p>
    </div>
  </div>

  <h2 class="section-heading">4. Los Cuatro Pilares Pedagógicos</h2>
  <div class="pillars-row">
    <div class="pillar-box">
      <h4>1. Escalera Progresiva</h4>
      <p>Cada lección se apoya estrictamente en lo visto antes. Cero saltos mágicos o cajas negras.</p>
    </div>
    <div class="pillar-box">
      <h4>2. Break-First, Fix-Later</h4>
      <p>Detonación de bugs reales (Undefined Behavior, Memory Leaks) antes de aprender la solución idiomática.</p>
    </div>
    <div class="pillar-box">
      <h4>3. Modelos de RAM</h4>
      <p>Diagramas visuales de hardware: Stack, Heap, punteros <code>0x...</code> y VTable de polimorfismo.</p>
    </div>
    <div class="pillar-box">
      <h4>4. Scaffolding & Fading</h4>
      <p>Analogías iniciales que desvanecen de inmediato hacia la terminología profesional de la industria.</p>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ======================================================================
       PAGE 2: MATRIZ GENERAL Y FASE 1
       ====================================================================== -->
  <h2 class="section-heading">5. Matriz General de Fases y Módulos</h2>
  <table class="formal-table">
    <thead>
      <tr>
        <th style="width: 14%;">Fase</th>
        <th style="width: 6%;">#</th>
        <th style="width: 25%;">Módulo</th>
        <th style="width: 8%;">Lecs.</th>
        <th>Eje Conceptual y Tecnológico</th>
        <th style="width: 22%;">Proyecto Entregable</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><strong>Fase 1:<br>Fundamentos</strong></td>
        <td><strong>01</strong></td>
        <td>Getting Started</td>
        <td>7</td>
        <td>Compilador <code>g++</code>, flujo I/O, namespaces y veto a malos hábitos.</td>
        <td>Terminal Interactiva</td>
      </tr>
      <tr>
        <td><strong>02</strong></td>
        <td>Fundamental Types</td>
        <td>7</td>
        <td>Tipado estático, <code>sizeof</code>, <code>{}</code> uniforme, <code>static_cast</code>.</td>
        <td>Split the Bill Calculator</td>
      </tr>
      <tr>
        <td><strong>03</strong></td>
        <td>Scope & Control Flow</td>
        <td>8</td>
        <td>Control de flujo, marcos de Stack, shadowing y prevención de UB.</td>
        <td>Taberna RPG / Cajero</td>
      </tr>
      <tr>
        <td rowspan="2"><strong>Fase 2:<br>Funciones</strong></td>
        <td><strong>04</strong></td>
        <td>Functions</td>
        <td>8</td>
        <td>Pass-by-value, aislamiento de pila, RNG moderno con <code>&lt;random&gt;</code>.</td>
        <td>Generador RPG con RNG</td>
      </tr>
      <tr>
        <td><strong>05</strong></td>
        <td>Constants & Strings</td>
        <td>6</td>
        <td><code>const</code>, <code>constexpr</code>, <code>std::string</code> y <code>std::string_view</code>.</td>
        <td>Generador de Claves</td>
      </tr>
      <tr>
        <td rowspan="2"><strong>Fase 3:<br>Colecciones</strong></td>
        <td><strong>06</strong></td>
        <td>Arrays & Vectors</td>
        <td>9</td>
        <td>Buffer Overflow de C, <code>std::vector</code>, <code>.at()</code>, multi-archivo.</td>
        <td>Registro de Calificaciones</td>
      </tr>
      <tr>
        <td><strong>07</strong></td>
        <td>Compound Types</td>
        <td>7</td>
        <td><code>struct</code>, <code>enum class</code>, Agregados C++17 y puente a C++20.</td>
        <td>Bestiario RPG V1</td>
      </tr>
      <tr>
        <td rowspan="2"><strong>Fase 4:<br>Memoria Real</strong></td>
        <td><strong>08</strong></td>
        <td>References & Addresses</td>
        <td>8</td>
        <td>Direcciones <code>&</code>, paso por <code>const &</code> (Zero-Copy), amnesia de <code>auto</code>.</td>
        <td>Bestiario V2 (Zero-Copy)</td>
      </tr>
      <tr>
        <td><strong>09</strong></td>
        <td>Dynamic Memory & RAII</td>
        <td>9</td>
        <td>Heap, punteros observadores, <code>std::unique_ptr</code>, <code>std::move</code>, RAII.</td>
        <td>Bestiario V3 (Heap RAII)</td>
      </tr>
      <tr>
        <td rowspan="3"><strong>Fase 5:<br>POO Moderna</strong></td>
        <td><strong>10</strong></td>
        <td>Classes & Encapsulation</td>
        <td>10</td>
        <td>Encapsulamiento <code>m_</code>, <code>const</code> methods, Member Init List, <code>operator&lt;&lt;</code>.</td>
        <td>Bestiario V4 (Multi-Archivo)</td>
      </tr>
      <tr>
        <td><strong>11</strong></td>
        <td>Inheritance</td>
        <td>7</td>
        <td>Relación IS-A, constructores, destrucción y trampa del Object Slicing.</td>
        <td>Jerarquía del Bestiario</td>
      </tr>
      <tr>
        <td><strong>12</strong></td>
        <td>Polymorphism</td>
        <td>8</td>
        <td>Despacho dinámico, <code>virtual</code>, VTable, destructor virtual, <code>override</code>.</td>
        <td>El Coliseo (Game Loop)</td>
      </tr>
      <tr>
        <td rowspan="3"><strong>Fase 6:<br>Resiliencia & STL</strong></td>
        <td><strong>13</strong></td>
        <td>Error Handling & Resilience</td>
        <td>7</td>
        <td>Stack Unwinding, jerarquía <code>std::exception</code>, <code>std::optional</code>, <code>noexcept</code>.</td>
        <td>Motor Resiliente</td>
      </tr>
      <tr>
        <td><strong>14</strong></td>
        <td>Templates & Lambdas</td>
        <td>8</td>
        <td>Polimorfismo estático, templates en <code>.hpp</code>, NTTP, lambdas modernas.</td>
        <td>Pipeline de Eventos</td>
      </tr>
      <tr>
        <td><strong>15</strong></td>
        <td>STL Algorithms & Capstone</td>
        <td>8</td>
        <td>Algoritmos STL, Erase-Remove Idiom, iteradores, asincronía y Capstone Final.</td>
        <td>EL MOTOR RPG DEFINITIVO</td>
      </tr>
    </tbody>
  </table>

  <!-- FASE 1 -->
  <div class="phase-header">
    <span>FASE 1: FUNDAMENTOS DE LA COMPUTACIÓN</span>
    <span class="tag">Módulos 01 a 03 · 22 Lecciones</span>
  </div>

  <!-- M01 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 01 — Getting Started & Pipeline del Compilador</span>
      <span class="module-meta-badge">7 Lecciones · 2 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Comprender la traducción de código a binario ejecutable, dominar la E/S en consola y erradicar vicios globales como <code>using namespace std;</code>.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L00</td><td class="title-col">¿Qué es programar?</td><td class="desc-col">Concepto de compilación y necesidad de código máquina binario.</td></tr>
        <tr><td class="code-col">L01</td><td class="title-col">Herramientas y Terminal</td><td class="desc-col">Verificación de compilador <code>g++</code> y comandos de navegación básica.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Primer programa (Hello World)</td><td class="desc-col">Anatomía de <code>int main()</code>, flujo <code>std::cout</code> y comando de compilación.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Namespaces y el ámbito std::</td><td class="desc-col">Prevención de colisión de identificadores y veto a <code>using namespace std;</code>.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Formato y salto de línea</td><td class="desc-col">Salto <code>'\n'</code> directo vs el sobrecosto de flush innecesario de <code>std::endl</code>.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Lectura y variables iniciales</td><td class="desc-col">Flujo <code>std::cin</code> e inicialización uniforme <code>int x{0};</code> contra basura en RAM.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Terminal Interactiva: lectura de líneas con <code>std::getline</code> y saneamiento.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D04_Uninitialized</code>, <code>D05_CinSpaces</code></span>
      <span><strong>Modelo RAM:</strong> Pipeline & Registros</span>
      <span><strong>Decisión:</strong> Veto a <code>using namespace std;</code></span>
    </div>
  </div>

  <!-- M02 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 02 — Fundamental Types & Sistema de Tipado</span>
      <span class="module-meta-badge">7 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Conocer la huella física en memoria de tipos primitivos y aplicar conversión explícita con <code>static_cast</code>.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Tipos primitivos y RAM</td><td class="desc-col"><code>int</code>, <code>double</code>, <code>char</code>, <code>bool</code> y tamaño en bytes con <code>sizeof</code>.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Inicialización Uniforme {}</td><td class="desc-col">Prevención de conversiones estrechas destructivas (Narrowing Conversions).</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Operadores aritméticos</td><td class="desc-col">Precedencia y corrección de la división entera truncada (7 / 2 = 3).</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Operadores lógicos y booleanos</td><td class="desc-col">Compuertas booleanas y prevención del error <code>if (x = 5)</code>.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Casting explícito (static_cast)</td><td class="desc-col">Transformación de tipos segura y verificada en tiempo de compilación.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Deducción de tipos con auto</td><td class="desc-col">Uso idiomático de <code>auto</code> sin perder claridad sobre el estado de la RAM.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">"Split the Bill": Calculadora de propinas y división exacta de gastos.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02_Narrowing</code>, <code>D03_IntDivision</code>, <code>D04_AssignInIf</code></span>
      <span><strong>Modelo RAM:</strong> Bytes en Stack (sizeof)</span>
      <span><strong>Decisión:</strong> Inicialización <code>{}</code> obligatoria</span>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- M03 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 03 — Scope & Control Flow (Control de Flujo)</span>
      <span class="module-meta-badge">8 Lecciones · 4 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Dominar bifurcaciones lógicas, iteraciones y la gestión de marcos de ámbito en el Stack.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Condicionales if / else</td><td class="desc-col">Bifurcaciones y prevención del punto y coma asesino <code>if(cond);</code>.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Cadenas else if</td><td class="desc-col">Evaluación por cortocircuito y prevención de código inalcanzable.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Bloques y Ámbito (Scope)</td><td class="desc-col">Ciclos de vida en Stack y prevención del bug de Variable Shadowing.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Conmutación con switch</td><td class="desc-col">Selección múltiple y prevención del error de Fallthrough involuntario.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Bucles while / do-while</td><td class="desc-col">Repetición condicional y prevención de bucles infinitos en consola.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Bucle contador for</td><td class="desc-col">Inicialización, condición, incremento y prevención de errores Off-By-One.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Break y Continue</td><td class="desc-col">Manipulación de saltos y limitaciones en bucles anidados.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">"Taberna RPG / Cajero": Menú interactivo con <code>while(true)</code> y <code>switch</code>.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_SemicolonIf</code>, <code>D03_Shadowing</code>, <code>D04_Fallthrough</code></span>
      <span><strong>Modelo RAM:</strong> Marcos de Ámbito {}</span>
      <span><strong>Decisión:</strong> Scope explícito con llaves</span>
    </div>
  </div>

  <!-- FASE 2 -->
  <div class="phase-header">
    <span>FASE 2: FUNCIONES Y TEXTOS</span>
    <span class="tag">Módulos 04 y 05 · 14 Lecciones</span>
  </div>

  <!-- M04 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 04 — Functions & Generación de Números Aleatorios</span>
      <span class="module-meta-badge">8 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Modularizar software en unidades funcionales atómicas y dominar el aislamiento de memoria en la pila.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Anatomía de una función</td><td class="desc-col">Firma, parámetros formales y separación de responsabilidades.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Retorno de valores</td><td class="desc-col">Obligatoriedad de <code>return</code> en todos los caminos lógicos contra UB.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Funciones void</td><td class="desc-col">Procedimientos sin retorno y comportamiento del compilador.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Parámetros por valor</td><td class="desc-col">La trampa del clon: demostración de copias aisladas en la pila.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Aislamiento en Stack</td><td class="desc-col">Independencia de memoria entre marcos de función y el <code>main</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Refactorización modular</td><td class="desc-col">Descomposición de funciones monolíticas en unidades reutilizables.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Aleatoriedad con &lt;random&gt;</td><td class="desc-col">Uso de <code>std::mt19937</code> y prohibición definitiva del arcaico <code>rand()</code>.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Generador de Atributos RPG: Tiradas probabilísticas y lógica modular.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02_MissingReturn</code>, <code>D04_PassByValue</code>, <code>D07_StaticRng</code></span>
      <span><strong>Modelo RAM:</strong> Call Stack Frames</span>
      <span><strong>Decisión:</strong> Veto a <code>rand()</code>; uso de <code>&lt;random&gt;</code></span>
    </div>
  </div>

  <!-- M05 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 05 — Constants, std::string & std::string_view</span>
      <span class="module-meta-badge">6 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Implementar inmutabilidad estricta y manipular cadenas sin sobrecosto de memoria.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Constantes con const</td><td class="desc-col">Inmutabilidad en tiempo de ejecución (Const Correctness).</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Evaluación con constexpr</td><td class="desc-col">Cálculos evaluados por el compilador con costo cero en runtime.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Cadenas std::string</td><td class="desc-col">Gestión de memoria dinámica interna y superación de <code>char[]</code>.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Vistas std::string_view</td><td class="desc-col">Paso de texto Zero-Copy y prevención de Dangling Views.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Saneamiento de buffers I/O</td><td class="desc-col">Limpieza de errores en flujos de entrada con <code>cin.clear()</code> y <code>cin.ignore()</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Generador de Contraseñas: Manipulación inmutable y validación estricta.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_Mutation</code>, <code>D04_DanglingStringView</code>, <code>D05_CinLoop</code></span>
      <span><strong>Modelo RAM:</strong> Buffer de cadenas & Vistas</span>
      <span><strong>Decisión:</strong> Separación <code>const</code> vs <code>constexpr</code></span>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- FASE 3 -->
  <div class="phase-header">
    <span>FASE 3: COLECCIONES Y ENTIDADES</span>
    <span class="tag">Módulos 06 y 07 · 16 Lecciones</span>
  </div>

  <!-- M06 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 06 — Arrays, std::vector & Arquitectura Multi-Archivo</span>
      <span class="module-meta-badge">9 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Gestionar colecciones dinámicas contiguas y estructurar proyectos profesionales en <code>.h</code> y <code>.cpp</code>.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Límites de variables sueltas</td><td class="desc-col">Colapso de software ante conjuntos extensos de datos homogéneos.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">C-Arrays y Buffer Overflow</td><td class="desc-col">Demostración física de corrupción de memoria adyacente en C clásico.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">std::vector moderno</td><td class="desc-col">Inicialización con llaves <code>{5}</code> (1 elemento) vs paréntesis <code>(5)</code> (5 casillas).</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Acceso seguro con .at()</td><td class="desc-col">Verificación de límites obligatoria frente a la trampa de <code>[]</code>.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Captura de std::out_of_range</td><td class="desc-col">Manejo táctico de excepciones con bloques <code>try / catch</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Range-based for</td><td class="desc-col">Iteración idiomática segura sin manipulación de índices manuales.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Métodos de std::vector</td><td class="desc-col"><code>push_back</code>, <code>size</code>, <code>empty</code>, <code>reserve</code> y realocación en Heap.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Arquitectura Multi-Archivo</td><td class="desc-col">Separación en <code>.h</code> y <code>.cpp</code> con directivas <code>#pragma once</code>.</td></tr>
        <tr><td class="code-col">L09</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Registro de Calificaciones: Sistema multi-archivo con notas dinámicas.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02_BufferOverflow</code>, <code>D03_BraceInit</code>, <code>D04_SilentBounds</code></span>
      <span><strong>Modelo RAM:</strong> Memoria Contigua en Heap</span>
      <span><strong>Decisión:</strong> Uso estricto de <code>.at()</code> formativo</span>
    </div>
  </div>

  <!-- M07 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 07 — Compound Types (struct & enum class)</span>
      <span class="module-meta-badge">7 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Modelar entidades compuestas y máquinas de estado con tipado estático fuerte y constructores seguros.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Colapso de firmas extensas</td><td class="desc-col">Por qué pasar 6 parámetros individuales destruye el diseño modular.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Estructuras con struct</td><td class="desc-col">Agrupación heterogénea y el operador de acceso punto (<code>.</code>).</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Agregados y Constructores C++17</td><td class="desc-col">Inicialización uniforme <code>{}</code> y puente a Designated Initializers de C++20.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Peligro de Números Mágicos</td><td class="desc-col">Fragilidad y vulnerabilidad de modelar estados con enteros.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Estados con enum class</td><td class="desc-col">Enumeraciones fuertemente tipadas con ámbito para eliminar bugs.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Colecciones de Entidades</td><td class="desc-col">Composición armónica de <code>std::vector&lt;struct&gt;</code> en memoria contigua.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Bestiario RPG V1: Base de datos en memoria con monstruos y combate.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02_MissingSemicolon</code>, <code>D03_AggregateOrder</code>, <code>D04_MagicNum</code></span>
      <span><strong>Modelo RAM:</strong> Struct Alignment & Padding</span>
      <span><strong>Decisión:</strong> Veto a <code>enum</code> de C; usar <code>enum class</code></span>
    </div>
  </div>

  <!-- FASE 4 -->
  <div class="phase-header">
    <span>FASE 4: ARQUITECTURA DE MEMORIA REAL</span>
    <span class="tag">Módulos 08 y 09 · 17 Lecciones</span>
  </div>

  <!-- M08 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 08 — References, Addresses & Zero-Copy</span>
      <span class="module-meta-badge">8 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Inspeccionar direcciones de hardware y aplicar la Regla de Oro del paso por referencia constante.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Costo de la copia profunda</td><td class="desc-col">Medición de degradación de rendimiento por clonación en memoria.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Direcciones en RAM (&)</td><td class="desc-col">Inspección de punteros físicos hexadecimales (<code>0x...</code>).</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Pass-by-Reference (&)</td><td class="desc-col">Creación de alias directos a la variable original para mutación eficiente.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Mutación accidental</td><td class="desc-col">Riesgo de corromper datos cuando solo se deseaba lectura.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">La Regla de Oro: const &</td><td class="desc-col">Tipos primitivos por valor, tipos pesados por <code>const &</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Amnesia de auto</td><td class="desc-col">Por qué <code>auto x = ref</code> descarta la referencia forzando <code>const auto&</code>.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Dangling References</td><td class="desc-col">Retorno mortal de referencias a variables locales del Stack.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Bestiario V2 (Zero-Copy): Refactorización integral con paso por <code>const &</code>.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_HeavyClone</code>, <code>D04_AccidentalMutation</code>, <code>D07_DanglingRef</code></span>
      <span><strong>Modelo RAM:</strong> Direcciones Hexadecimales &</span>
      <span><strong>Decisión:</strong> Regla de Oro: Primitivos valor, pesados <code>const &</code></span>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- M09 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 09 — Dynamic Memory, Smart Pointers & RAII</span>
      <span class="module-meta-badge">9 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Comprender la asignación en el Heap y aplicar la gestión automática determinista de recursos con RAII.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Stack vs Heap</td><td class="desc-col">Tamaño de segmentos de memoria y necesidad de memoria dinámica.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Punteros crudos (T*)</td><td class="desc-col">Variables de dirección, operador <code>*</code>, flecha <code>-&gt;</code> y uso como observadores.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Puntero nulo y Segfault</td><td class="desc-col">Comprobación previa defensiva y prevención de accesos inválidos.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Asignación manual con new</td><td class="desc-col">Solicitud de memoria y por qué <code>new[]</code> está prohibido en C++ moderno.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Memory Leaks</td><td class="desc-col">La pérdida silenciosa de recursos de RAM por omisión de <code>delete</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Dangling Pointers</td><td class="desc-col">Uso de punteros tras liberación (Use-After-Free).</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">RAII y std::unique_ptr</td><td class="desc-col">Gestión determinista atando el Heap al Stack con <code>std::make_unique&lt;T&gt;()</code>.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Semántica de Movimiento</td><td class="desc-col">Transferencia de propiedad con <code>std::move</code> y type aliases con <code>using</code>.</td></tr>
        <tr><td class="code-col">L09</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Bestiario V3 (Heap RAII): Entidades dinámicas gobernadas por <code>unique_ptr</code>.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D03_NullCrash</code>, <code>D05_MemoryLeak</code>, <code>D06_DanglingPointer</code></span>
      <span><strong>Modelo RAM:</strong> Stack-to-Heap Ownership Pointer</span>
      <span><strong>Decisión:</strong> Veto a <code>new[]/delete[]</code>; adopción estricta de RAII</span>
    </div>
  </div>

  <!-- FASE 5 -->
  <div class="phase-header">
    <span>FASE 5: PROGRAMACIÓN ORIENTADA A OBJETOS MODERNA</span>
    <span class="tag">Módulos 10 a 12 · 25 Lecciones</span>
  </div>

  <!-- M10 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 10 — Classes, Encapsulation & Sobrecarga de Operadores</span>
      <span class="module-meta-badge">10 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Blindar invariantes de software mediante encapsulamiento estricto y sobrecarga idiomática.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">El Estado Inconsistente</td><td class="desc-col">Por qué los <code>struct</code> públicos permiten corromper invariantes lógicas.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">El cerrojo de class</td><td class="desc-col">Privacidad por defecto, modificadores <code>private/public</code> y convención <code>m_</code>.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Métodos const correctness</td><td class="desc-col">Permitir invocaciones desde referencias constantes (<code>const &</code>).</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Getters y Setters seguros</td><td class="desc-col">Retorno por <code>const &</code> y validación rigurosa de rangos en mutaciones.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Member Initializer List</td><td class="desc-col">Inicialización en nacimiento, orden <code>-Wreorder</code> y calificador <code>explicit</code>.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Tell, Don't Ask</td><td class="desc-col">Evitar que los getters excesivos destruyan el diseño OO.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Sobrecarga operator&lt;&lt;</td><td class="desc-col">Integración natural con streams e igualdad con <code>operator==</code>.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Clases Multi-Archivo</td><td class="desc-col">Declaración en <code>.h</code> e implementación con <code>Clase::</code> en <code>.cpp</code>.</td></tr>
        <tr><td class="code-col">L09</td><td class="title-col">Destructores y RAII</td><td class="desc-col">Limpieza determinista de recursos al expirar el ciclo del objeto.</td></tr>
        <tr><td class="code-col">L10</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Bestiario V4: Clases POO robustas con operadores sobrecargados.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_InconsistentState</code>, <code>D03_ConstMember</code>, <code>D05_InitOrder</code></span>
      <span><strong>Modelo RAM:</strong> Layout de Objetos en Memoria</span>
      <span><strong>Decisión:</strong> Atributos privados con <code>m_</code> y Member Init List</span>
    </div>
  </div>

  <!-- M11 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 11 — Inheritance & Prevención de Object Slicing</span>
      <span class="module-meta-badge">7 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Reutilizar lógica mediante jerarquías IS-A y prevenir la destrucción de datos por Object Slicing.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Anti-patrón Copiar/Pegar</td><td class="desc-col">Costo de duplicar lógica en entidades hermanas y necesidad de jerarquías.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Herencia Simple (: public)</td><td class="desc-col">Relación IS-A y prevención de herencia privada accidental.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Modificador protected</td><td class="desc-col">Atributos protegidos con métodos de acceso controlados.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Cadenas de constructores</td><td class="desc-col">Delegación obligatoria hacia el constructor base.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Ciclo de vida en jerarquías</td><td class="desc-col">Construcción Padre->Hijo y destrucción inversa Hijo->Padre.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">La trampa de Object Slicing</td><td class="desc-col">Destrucción de datos al guardar derivadas por valor en <code>vector&lt;Base&gt;</code>.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Jerarquía del Bestiario: Árbol de 3 niveles (Entidad -> Monstruo -> Jefe).</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02b_PrivateInherit</code>, <code>D04_ConstructorChain</code>, <code>D06_ObjectSlicing</code></span>
      <span><strong>Modelo RAM:</strong> Object Slicing en Pila</span>
      <span><strong>Decisión:</strong> Herencia simple; veto a herencia múltiple con estado</span>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- M12 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 12 — Polymorphism, VTable & Despacho Dinámico</span>
      <span class="module-meta-badge">8 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Implementar despacho dinámico en runtime con tablas virtuales y contratos de interfaz.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Early Binding (Enlace Estático)</td><td class="desc-col">Por qué el compilador enlaza al tipo del puntero y no al objeto real.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Métodos virtual y la VTable</td><td class="desc-col">Despacho dinámico a través del puntero de tabla virtual <code>__vptr</code>.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">override y final</td><td class="desc-col">Detección de errores de firma con <code>override</code> y sellado de clases con <code>final</code>.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">El Destructor Virtual</td><td class="desc-col">Fuga de memoria letal al destruir polimórficamente sin <code>virtual ~Base()</code>.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Interfaces Puras (= 0)</td><td class="desc-col">Contratos abstractos puros y herencia múltiple de interfaces.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Colecciones Polimórficas</td><td class="desc-col"><code>vector&lt;unique_ptr&lt;Base&gt;&gt;</code> y downcasting seguro con <code>dynamic_cast</code>.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Impresión Polimórfica</td><td class="desc-col"><code>operator&lt;&lt;</code> delegando en método virtual puro <code>imprimir() const</code>.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">El Coliseo: Game Loop de combate polimórfico sin bifurcaciones <code>if/else</code>.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_StaticBinding</code>, <code>D03_SilentTypo</code>, <code>D04_VirtualDestructorLeak</code></span>
      <span><strong>Modelo RAM:</strong> VTable & __vptr</span>
      <span><strong>Decisión:</strong> Destructor virtual obligatorio en clases base</span>
    </div>
  </div>

  <!-- FASE 6 -->
  <div class="phase-header">
    <span>FASE 6: RESILIENCIA, ESPECIALIZACIÓN Y CAPSTONE FINAL</span>
    <span class="tag">Módulos 13 a 15 · 23 Lecciones</span>
  </div>

  <!-- M13 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 13 — Error Handling, Stack Unwinding & std::optional</span>
      <span class="module-meta-badge">7 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Construir software tolerante a fallos con Stack Unwinding, excepciones de dominio y <code>std::optional</code>.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Fragilidad de Códigos de Retorno</td><td class="desc-col">Por qué retornar enteros causa errores ignorados que corrompen el sistema.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Stack Unwinding & RAII</td><td class="desc-col">Destrucción automática de objetos RAII durante el vuelo de una excepción.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Jerarquía std::exception</td><td class="desc-col">Captura obligatoria por referencia constante (<code>catch (const std::exception& e)</code>).</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Excepciones en Constructores</td><td class="desc-col">Abortar la instanciación de objetos zombi en estado inválido.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Alternativa ligera std::optional</td><td class="desc-col">Manejo idiomático de ausencias esperadas con <code>std::nullopt</code> (C++17).</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Garantía de noexcept</td><td class="desc-col">Optimización crítica de relocalización de memoria en <code>std::vector</code>.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Motor de Mazmorras: Carga de mapas con recuperación ante corrupción.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_IgnoredReturn</code>, <code>D02_RawLeakOnThrow</code>, <code>D06_VectorCopyFallback</code></span>
      <span><strong>Modelo RAM:</strong> Stack Unwinding & Exception Frame</span>
      <span><strong>Decisión:</strong> Captura por <code>const std::exception&</code>; usar <code>std::optional</code></span>
    </div>
  </div>

  <!-- M14 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 14 — Templates & Metaprogramación Genérica</span>
      <span class="module-meta-badge">8 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Escribir código genérico monomórfico evaluado en compilación y dominar funciones anónimas Lambdas.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Fábrica de Código (Templates)</td><td class="desc-col">Polimorfismo estático vs dinámico: cero sobrecarga en runtime (Inlining).</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Plantillas de funciones</td><td class="desc-col">Deducción de tipos automática y plantillas multiparámetro.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">La trampa del Linker</td><td class="desc-col">Por qué las plantillas deben residir obligatoriamente en cabeceras (<code>.hpp</code>).</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Plantillas de clases y CTAD</td><td class="desc-col">Contenedores genéricos con deducción automática de tipos en C++17.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Parámetros No-Tipo (NTTP)</td><td class="desc-col">Buffers estáticos contiguos en Stack sin tocar el Heap (<code>std::size_t N</code>).</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Lambdas Modernas [](){}</td><td class="desc-col">Funciones anónimas instantáneas como predicados de primer nivel.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Capturas en Lambdas</td><td class="desc-col">Copia <code>[=]</code> vs referencia <code>[&]</code> y prevención de Dangling Captures.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">Mini-Proyecto Integrador</td><td class="desc-col">Pipeline Genérico de Eventos: Bus desacoplado con templates y lambdas.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D02_TemplateDeduction</code>, <code>D03_LinkerBug</code>, <code>D07_DanglingLambda</code></span>
      <span><strong>Modelo RAM:</strong> Monomorfización en Compilación</span>
      <span><strong>Decisión:</strong> Templates obligatoriamente en <code>.hpp</code></span>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- M15 -->
  <div class="module-card">
    <div class="module-header">
      <span class="module-title">Módulo 15 — STL Algorithms, Pipelines & Capstone Final</span>
      <span class="module-meta-badge">8 Lecciones · 3 Bug Demos</span>
    </div>
    <div class="module-body">
      <div class="module-objective"><strong>Objetivo:</strong> Dominar algoritmos estándar declarativos, Erase-Remove Idiom, iteradores y culminar el Capstone integral del curso.</div>
      <table class="lessons-table">
        <tr><td class="code-col">L01</td><td class="title-col">Algoritmos STL vs Bucles</td><td class="desc-col">Expresividad con <code>std::all_of</code>, <code>any_of</code> y <code>count_if</code> vs <code>range-for</code>.</td></tr>
        <tr><td class="code-col">L02</td><td class="title-col">Invalidación de Iteradores</td><td class="desc-col">Prevención de Segfaults mediante el Erase-Remove Idiom y puente a C++20.</td></tr>
        <tr><td class="code-col">L03</td><td class="title-col">Búsqueda y Predicados</td><td class="desc-col"><code>std::find_if</code> y <code>std::min_element</code> retornando <code>std::optional</code>.</td></tr>
        <tr><td class="code-col">L04</td><td class="title-col">Transformación y Reducción</td><td class="desc-col">Mapeo funcional con <code>std::transform</code> y reducción con <code>std::accumulate</code>.</td></tr>
        <tr><td class="code-col">L05</td><td class="title-col">Ordenamiento Avanzado</td><td class="desc-col"><code>std::sort</code> con lambdas y comparadores multicriterio personalizados.</td></tr>
        <tr><td class="code-col">L06</td><td class="title-col">Evolución C++20 Ranges</td><td class="desc-col">Evaluación perezosa con tuberías <code>|</code> sin vectores intermedios temporales.</td></tr>
        <tr><td class="code-col">L07</td><td class="title-col">Concurrencia Básica</td><td class="desc-col">Tareas en segundo plano con <code>std::async</code> y <code>std::future</code>.</td></tr>
        <tr><td class="code-col">L08</td><td class="title-col">CAPSTONE FINAL DEL CURSO</td><td class="desc-col">"El Motor RPG Definitivo": Consolidación armónica total de los 15 módulos.</td></tr>
      </table>
    </div>
    <div class="module-footer-details">
      <span><strong>Bug Demos:</strong> <code>D01_RawLoopOffByOne</code>, <code>D02_IteratorInvalidation</code>, <code>D07_DataRace</code></span>
      <span><strong>Modelo RAM:</strong> Pipelines de Algoritmos Declarativos</span>
      <span><strong>Decisión:</strong> Claridad ante todo: STL para procesar; range-for directo</span>
    </div>
  </div>

  <h2 class="section-heading">6. Mandamientos de Codificación y Estándares de Ingeniería</h2>
  <div class="commandment-box">
    <ul class="commandment-list">
      <li><strong>1. Veto a "using namespace std;":</strong> Usar prefijo explícito <code>std::</code>.</li>
      <li><strong>2. Veto a "std::endl":</strong> Usar carácter <code>'\n'</code> directo contra cuellos de botella I/O.</li>
      <li><strong>3. Inicialización Uniforme {}:</strong> Prohibido declarar variables sueltas sin inicializar.</li>
      <li><strong>4. Veto a new[] / delete[]:</strong> Gestión de memoria exclusiva con <code>std::unique_ptr</code>.</li>
      <li><strong>5. Const Correctness:</strong> Inmutabilidad por defecto en variables y métodos.</li>
      <li><strong>6. Veto a rand() / srand():</strong> Aleatoriedad exclusiva con la librería <code>&lt;random&gt;</code>.</li>
      <li><strong>7. Acceso Verificado .at():</strong> Evitar corchetes <code>[]</code> ciegos en etapas formativas.</li>
      <li><strong>8. Destructor Virtual Obligatorio:</strong> <code>virtual ~Base() = default;</code> en clases base.</li>
      <li><strong>9. Claridad ante todo:</strong> Algoritmos STL para procesar; range-for para secuencias directas.</li>
    </ul>
  </div>

  <h2 class="section-heading">7. Bibliografía Oficial de Referencia</h2>
  <ol class="biblio-list">
    <li><strong>Bjarne Stroustrup</strong>, <em>A Tour of C++</em>, 3rd ed. (C++20), Addison-Wesley Professional, 2022.</li>
    <li><strong>Scott Meyers</strong>, <em>Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14</em>, O'Reilly Media, 2014.</li>
    <li><strong>Jason Turner</strong>, <em>C++ Best Practices: 45ish Ways to Write Better Modern C++</em>, 2nd ed., Leanpub, 2022.</li>
    <li><strong>Bjarne Stroustrup & Herb Sutter</strong>, <em>C++ Core Guidelines</em>, Standard C++ Foundation (isocpp.github.io/CppCoreGuidelines), 2026.</li>
    <li><strong>ISO/IEC JTC1/SC22/WG21</strong>, <em>Programming Languages — C++ (ISO/IEC 14882:2020)</em>, International Organization for Standardization, 2020.</li>
  </ol>

  <div class="footer-sig">
    <span><strong>LearningCpp</strong> · Especificación Académica Oficial · Autor: Jesus Vera V. (MiniLux0)</span>
    <span>Licencia de Código Abierto (MIT) · 2026</span>
  </div>

</body>
</html>
"""

html_path = os.path.abspath("utils/scripts/temp_syllabus.html")
pdf_path = os.path.abspath("LearningCpp_Syllabus_Oficial.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]

print(f"Compilando PDF profesional de alto impacto en: {pdf_path}")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(html_path):
    os.remove(html_path)

if os.path.exists(pdf_path):
    print(f"¡Éxito! Archivo PDF generado con tamaño: {os.path.getsize(pdf_path)} bytes")
