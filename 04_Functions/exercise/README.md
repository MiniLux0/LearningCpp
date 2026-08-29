# 🏋️ Ejercicios Prácticos — Módulo 04

Esta carpeta contiene los retos diseñados para consolidar los conceptos arquitectónicos de **Funciones**, dominando la modularidad, el aislamiento de memoria (Scope local), la clonación de datos (Pass-by-value), el proceso de *Refactoring* y el ensamblaje de la librería estocástica `<random>`.

## 📁 Lista de Retos

- 📁 **`E01_ConstructorDeSaludos/`**: Aprende a extraer rutinas delegadas que inyecten parámetros formales, evitando la repetición y el acoplamiento monolítico (DRY).
- 📁 **`E02_CalculadoraDeArea/`**: El sistema inyecta datos basura a la renderización 3D por una falla de firma estricta. Cierra los caminos lógicos para prevenir el *Undefined Behavior*.
- 📁 **`E03_PanelDeBienvenida/`**: Refactoriza un error fatal de compilación provocado por intentar interceptar e inicializar memoria a partir de una rutina de Efecto Secundario (`void`).
- 📁 **`E04_ConversorDeTemperaturas/`**: Las transformaciones matemáticas se están perdiendo en la memoria debido al aislamiento de Scope (*Pass-by-value*). Restaura el flujo inyectando el dato con `return`.
- 📁 **`E05_CamaraDeAislamiento/`**: Resuelve un error de visibilidad (*not declared in this scope*) donde el flujo orquestador intenta leer memoria que ya ha sido destruida en una rutina delegada local.
- 📁 **`E06_RefactorizacionDelMenu/`**: Aplica el proceso de *Extracción de Rutinas* para modularizar un bloque monolítico acoplado, delegando las responsabilidades de renderizado e I/O.
- 📁 **`E07_GeneradorDeSemillas/`**: El PRNG colapsó estadísticamente arrojando secuencias clonadas. Domina `<random>` e implementa el modificador `static` para preservar el estado del motor en memoria.
- 📁 **`E08_AdivinaElNumero/`**: Mini-proyecto integrador (Sistema Interactivo). Diseña el *Game Loop* combinando bucles iterativos, condicionales, y motores PRNG orquestados desde un Scope principal modular.

## 🛠️ Cómo hacer los ejercicios

1. Entra a la carpeta del reto de tu interés.
2. Todo reto tiene un contexto o "lore", así que **siempre lee el `README.md`** que está dentro de la carpeta antes de tocar el código.
3. Abre el archivo principal `.cpp` y sigue las instrucciones que están detalladas en los comentarios (busca los `TODO`).
4. Compila el archivo a mano usando la terminal (ej: `g++ E01_Nombre.cpp -o app`).
5. Si no sabes cómo continuar o el compilador arroja errores, entra a la subcarpeta `solution/` y revisa el código resuelto.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
