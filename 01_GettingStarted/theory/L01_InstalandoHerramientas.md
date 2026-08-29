# L01 · Instalando tus herramientas

> **Módulo 01 — Getting Started**

---

## El centro de mando: La Terminal

Si alguna vez has visto una película de hackers, probablemente los viste escribiendo rápidamente en una pantalla negra con letras blancas o verdes. Eso es la **Terminal** (o línea de comandos).

En el día a día usamos el ratón para abrir carpetas y hacer doble clic en los programas. La terminal hace exactamente lo mismo, pero en lugar de hacer clics, **escribes comandos de texto**. Para programar en C++, necesitas sentirte cómodo con la terminal porque es ahí donde le darás instrucciones directas al compilador.

### Comandos de supervivencia esenciales

Independientemente de si usas Windows, Mac o Linux, estos tres conceptos te llevarán a donde necesitas ir:

1. **¿Dónde estoy?**
   - En Windows: escribe `cd` y presiona Enter.
   - En Mac/Linux: escribe `pwd` y presiona Enter.
   - *El sistema te responderá con la ruta de la carpeta donde estás ubicado en este momento.*

2. **¿Qué hay en esta carpeta?**
   - En Windows PowerShell o Mac/Linux: escribe `ls` y presiona Enter.
   - En Windows (CMD clásico): escribe `dir` y presiona Enter.
   - *Verás una lista de todos los archivos y subcarpetas.*

3. **Quiero entrar a otra carpeta**
   - Comando: `cd nombre_de_la_carpeta` (cd significa "change directory" o cambiar directorio).
   - *Ejemplo: `cd LearningCpp`*
   - Para ir "hacia atrás" (salir de la carpeta actual): escribe `cd ..`

---

## Verificando a tu traductor: El Compilador

En la lección anterior aprendiste que necesitas un compilador para traducir tu código a ceros y unos. En este curso usaremos **GCC** (específicamente su comando `g++`), que es uno de los compiladores de C++ más utilizados en el mundo profesional.

> 🛠️ **Nota de Instalación:** Si aún no has instalado `g++`, dirígete a las guías de instalación para Windows, Mac o Linux en internet o consulta el canal de Discord.

Vamos a hacer una prueba rápida para ver si tu computadora ya reconoce al compilador. Abre tu terminal y escribe exactamente esto:

```bash
g++ --version
```

Si todo está correcto, la terminal te responderá con un bloque de texto indicando la versión instalada (por ejemplo, `g++ (GCC) 13.2.0` o similar). 

Si la terminal te dice algo como *"g++ no se reconoce como un comando interno o externo"*, significa que el compilador no está instalado, o que tu sistema operativo no sabe en qué carpeta encontrarlo (un problema común llamado "variables de entorno PATH"). No puedes programar en C++ hasta que ese comando funcione.

---

## ✦ Resumen

- La **terminal** es tu interfaz para darle órdenes escritas a la computadora.
- Usa `ls` (o `dir`) para ver los archivos, y `cd nombre_carpeta` para moverte.
- El comando `g++` es el programa que llamaremos desde la terminal para compilar nuestro código.
- Verificar la instalación con `g++ --version` es el primer paso antes de intentar escribir código.

---

## ✦ Preguntas de autochequeo

> [!WARNING]
> **Regla de oro:** Estas preguntas se pueden responder *solo* con lo que leíste en esta lección. No busques en internet — si no puedes responderlas de memoria, relee la sección correspondiente.

<details>
<summary><b>1. Si estás en la terminal y escribes el comando <code>ls</code> (o <code>dir</code>), ¿qué información te mostrará la computadora?</b></summary>

> Te mostrará una lista de todos los archivos y subcarpetas que existen dentro de la carpeta donde estás ubicado actualmente.
</details>

<details>
<summary><b>2. Si quieres salir de la carpeta actual y volver a la carpeta "madre" anterior, ¿qué comando exacto debes escribir?</b></summary>

> Debes escribir `cd ..`
</details>

<details>
<summary><b>3. ¿Para qué sirve ejecutar el comando <code>g++ --version</code> antes de empezar a programar?</b></summary>

> Sirve para comprobar si tu computadora tiene el compilador GCC instalado correctamente y si lo reconoce como un comando válido. Si no lo haces, no sabrás si estás listo para compilar tu código.
</details>

---

| ⬅️ [Anterior: ¿Qué es programar?](L00_QueEsProgramar.md) | 📖 [Menú del Módulo](../README.md) | ➡️ [Siguiente: Tu primer programa](L02_TuPrimerPrograma.md) |
|---|---|---|

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>