# 🏋️ Ejercicios Prácticos — Módulo 06

Esta carpeta contiene los retos diseñados para consolidar el dominio de arreglos, vectores dinámicos, acceso seguro con `.at()`, contención de excepciones con `try/catch`, recorridos con `range-based for` y arquitectura multi-archivo en C++ Moderno.

## 📁 Lista de Retos

- 📂 **`E03_InventarioDinamico/`**: Configura el sistema de almacenamiento de una nave exploradora inicializando vectores con llaves `{}` y constructores por conteo `()` de forma precisa.
- 📂 **`E04_ElIndicePerdido/`**: Repara un sistema de telemetría de radar espacial eliminando accesos ciegos con `[]` y sustituyéndolos por el acceso seguro con `.at()`.
- 📂 **`E05_AtrapandoLaBomba/`**: Protege el cajero automático del banco intergaláctico envolviendo consultas de cuentas en bloques `try/catch` para capturar `std::out_of_range`.
- 📂 **`E06_IteracionSegura/`**: Elimina vulnerabilidades *Off-By-One* en el procesador de señales sísmicas migrando bucles tradicionales hacia `range-based for`.
- 📂 **`E07_CreciendoVectores/`**: Optimiza el motor de abordaje de una estación orbital pre-reservando memoria con `.reserve()` e insertando pasajeros dinámicamente con `.push_back()`.
- 📂 **`E08_RefactorizacionHeader/`**: Refactoriza una biblioteca matemática monolítica separándola limpiamente en `VectorUtils.h` (interfaz) y `VectorUtils.cpp` (implementación).
- 📂 **`E09_RegistroDeCalificaciones/`**: Mini-proyecto integrador. Construye el sistema de gestión académica interactivo con validación de rangos, listados, consultas seguras y estadísticas globales.

## 🛠️ Cómo hacer los ejercicios

1. Entra a la carpeta del reto de tu interés.
2. Todo reto tiene un contexto o "lore", así que **siempre lee el `README.md`** que está dentro de la carpeta antes de tocar el código.
3. Abre el archivo principal `.cpp` y sigue las instrucciones que están detalladas en los comentarios (busca los `TODO`).
4. Compila el archivo a mano usando la terminal (ej: `g++ -std=c++17 E03_InventarioDinamico.cpp -o app`).
5. Si no sabes cómo continuar o el compilador arroja errores, entra a la subcarpeta `solution/` y revisa el código resuelto.

---

<div align="center">
  <sub>Maintained by <strong>Jesus Vera V. (MiniLux0)</strong> · 2026</sub>
</div>
