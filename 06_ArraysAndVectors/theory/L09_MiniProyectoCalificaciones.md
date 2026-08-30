# L09: Mini-proyecto Integrador: Sistema de Registro de Calificaciones

Imagina el libro de registro oficial de un docente universitario: a medida que los estudiantes rinden exámenes, el profesor anota cada nota en las páginas del libro, calcula el promedio del grupo, identifica la calificación más alta y más baja, y si algún estudiante consulta su nota por número de lista, el profesor verifica cuidadosamente el índice en el libro para no equivocarse de alumno. Desvanecemos la metáfora del libro de actas para integrar todos los conceptos de ingeniería dominados en este módulo: **Colecciones dinámicas `std::vector<double>`**, **Entrada interactiva con validación**, **Recorridos idiomáticos `range-based for`**, **Acceso seguro con `.at()`** y **Contención de excepciones con `try / catch`**.

---

## 1. Visión General del Proyecto

El **Sistema de Registro de Calificaciones** es una aplicación de consola modular diseñada para almacenar, consultar y auditar un conjunto dinámico de calificaciones académicas ingresadas por el usuario.

```text
======================================================
     SISTEMA DE GESTION DE CALIFICACIONES ACADEMICAS
======================================================
1. Registrar nueva calificacion
2. Listar todas las calificaciones registradas
3. Consultar calificacion por posicion de indice
4. Calcular estadisticas (Promedio, Maxima, Minima)
5. Salir
======================================================
```

---

## 2. Requisitos Técnicos y Arquitectura de Diseño

El sistema consolida los siguientes estándares y herramientas:

1. **Gestión Dinámica de Memoria (`std::vector<double>`):** La cantidad de notas no está limitada; el vector crece a demanda mediante `.push_back()`.
2. **Validación de Rangos Académicos:** Toda nota ingresada debe encontrarse estrictamente en el rango válido `[0.0, 20.0]`.
3. **Manejo Seguro de Contenedor Vacío:** Operaciones estadísticas (promedio, máximo, mínimo) deben verificar previamente `.empty()` para prevenir divisiones entre cero o accesos inválidos.
4. **Acceso Seguro y Resiliencia con `try/catch`:** La consulta por índice debe ejecutarse con `.at(indice)` dentro de un bloque `try`, capturando `const std::out_of_range&` para garantizar que índices inválidos jamás aborten el programa.
5. **Recorrido Limpio:** El listado general y el cálculo de promedio deben implementarse utilizando `range-based for`.

---

## 3. Diagrama de Flujo del Sistema

```text
INICIO
  │
  ├── Bucle Principal while(activo)
  │     ├── Mostrar Menú de Opciones
  │     ├── Leer opción del usuario con std::cin
  │     │
  │     ├── [Opción 1]: push_back() con validación de rango [0.0 - 20.0]
  │     ├── [Opción 2]: Listado con range-based for
  │     ├── [Opción 3]: Consulta con .at(i) envuelto en try/catch
  │     ├── [Opción 4]: Estadísticas (Promedio / Máx / Mín) verificando .empty()
  │     └── [Opción 5]: Salir del sistema
  │
FIN
```

---

> 🧪 **Laboratorio:** Revisa la implementación de referencia completa y ejecútala en tu terminal. Abre [`../lab/L09_MiniProyecto.cpp`](../lab/L09_MiniProyecto.cpp).
>
> 🏋️ **Ejercicio:** Construye tu propia versión del sistema de registro completando los módulos pendientes y superando las pruebas. Atrévete con el reto en [`../exercise/E09_RegistroDeCalificaciones/E09_RegistroDeCalificaciones.cpp`](../exercise/E09_RegistroDeCalificaciones/E09_RegistroDeCalificaciones.cpp).

---

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques respuestas en librerías avanzadas ni conceptos no vistos.

<details>
<summary><b>1. ¿Por qué es fundamental comprobar <code>notas.empty()</code> antes de calcular el promedio?</b></summary>

> Porque si el vector está vacío, `notas.size()` retorna 0, y calcular `suma / notas.size()` causaría una división entre cero, generando un resultado inválido (`NaN` o inf).
</details>

<details>
<summary><b>2. ¿Cómo protege el bloque <code>try/catch</code> la consulta de calificaciones por índice?</b></summary>

> Si el usuario solicita un índice inexistente (ej. índice 99 en una lista de 3 notas), `.at(99)` lanza `std::out_of_range`, la cual es capturada por el `catch`, mostrando un mensaje de advertencia en lugar de abortar abruptamente el programa.
</details>

---

| ⬅️ [Anterior: L08 — Arquitectura Multi-Archivo](L08_ArquitecturaMultiArchivo.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Resumen del Módulo](../summary/Module06_Cheatsheet.md) |
|:---|:---:|---:|

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
