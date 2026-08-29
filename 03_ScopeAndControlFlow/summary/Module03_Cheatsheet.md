# Módulo 03 — Arquitectura de Flujo y Scope: Cheatsheet

Referencia rápida de las estructuras de control lógico, iteración y manejo de memoria local del Módulo 03.

---

## Resumen por lección

### L01 — Control de flujo binario (`if` / `else`)
- El bloque `if` representa la desviación condicional básica en la arquitectura del flujo. 
- La condición se enmarca entre paréntesis `()` y se resuelve estrictamente en una expresión `bool`.
- El bloque de ejecución se aísla mediante llaves `{ }`.
- El bloque `else` funge como *fallback* (plan de contingencia) si la evaluación falla.

### L02 — Evaluación Secuencial Excluyente (`else if`)
- Utilizado para estructurar ramas múltiples mutuamente excluyentes.
- **Evaluación de Cortocircuito:** Al cumplirse una condición superior, se ejecuta su bloque y el compilador omite procesar el resto de la estructura.
- **Código Inalcanzable (Unreachable Code):** Defecto lógico generado por un orden secuencial erróneo (evaluar casos generales antes que los específicos deja ramas completamente aisladas de la ejecución).

### L03 — Bloques y Aislamiento de Memoria (Scope)
- **Local Scope (Alcance Local):** Las llaves `{ }` demarcan fronteras estrictas de memoria. Toda variable alojada internamente es destruida incondicionalmente y liberada de la memoria RAM al alcanzar la llave de cierre `}`.
- **Jerarquía de Visibilidad:** Un Scope interior (hijo) tiene acceso de lectura/escritura a las variables del Scope exterior (padre). El Scope padre es ciego al contenido de sus hijos.
- **Variable Shadowing (Ocultamiento):** Si se redeclara un identificador dentro de un Scope interior (`int oro = 10;`) teniendo un homónimo superior, el compilador reservará una nueva dirección superpuesta que bloqueará el acceso a la variable original, corrompiendo la mutación de estado esperada.

### L04 — Selección Directa Enrutada (`switch`)
- Estructura de control optimizada para verificaciones de **igualdad exacta** (no soporta evaluaciones relacionales lógicas).
- **El defecto del Fallthrough:** Si se omite la instrucción de escape `break;`, el flujo ignorará las fronteras semánticas, cayendo en cascada y procesando las ramas de código inferiores.
- **Vulnerabilidad de Scope Compartido:** Todo el bloque `switch` comparte un único Scope Local. Para inicializar una variable dentro de una etiqueta `case`, la arquitectura exige encapsular el caso entre llaves `{ }` para crear un aislamiento de memoria seguro.

### L05 — Iteración Condicional (`while` y `do-while`)
- **`while` (Pre-comprobación):** Evalúa la condición antes de ceder acceso al bloque. Si falla desde el contacto inicial, las instrucciones jamás se ejecutan.
- **Bucle Infinito (Infinite Loop):** Falla crítica ocurrida al omitir la mutación de la variable de control dentro del bloque, congelando el flujo y causando saturación de CPU.
- **`do-while` (Post-comprobación):** Ejecuta el bloque primero de forma obligatoria, garantizando al menos una pasada, y evalúa la condición de continuidad al final.

### L06 — Iteración Determinista (`for`)
- Estructura predilecta cuando la cantidad total de iteraciones es previamente calculable.
- Encapsula la gestión completa de la iteración: **Inicialización** (ejecución única, Scope aislado), **Condición** (evaluación antes de cada ciclo) y **Mutación** (incremento o alteración al final de la pasada).
- **Buffer Overflow (Off-By-One Bug):** Defecto originado por confundir operadores inclusivos (`<=`) con exclusivos (`<`), provocando una iteración extra o faltante que suele vulnerar los límites de estructuras indexadas en base-0.

### L07 — Alteración Manual de Iteración (`break` y `continue`)
- **`break` (Terminación Prematura):** Destruye el bucle al instante y redirige el flujo de control al exterior.
- **`continue` (Salto de Iteración):** Aborta la ejecución de la iteración actual y forza el retorno inmediato a la evaluación condicional para iniciar el siguiente ciclo.
- *Riesgo en While:* Utilizar un `continue` antes de la mutación de estado provocará un bucle infinito silencioso.

### L08 — Proyecto Arquitectónico: Cajero Automático
- Desarrollo integral que consolida el uso de iteraciones perpetuas, enrutamiento transaccional mediante `switch`, y protección estructural de variables en Scopes exteriores.

---

## Patrones clave del Módulo 03

```cpp
#include <iostream>

int main() {
    int balanceOperativo{500};
    
    // 1. Efecto Cascada seguro (prioridad descendente)
    if (balanceOperativo >= 1000) {
        std::cout << "Privilegios VIP concedidos.\n";
    } else if (balanceOperativo >= 500) {
        std::cout << "Privilegios Estándar.\n";
    } else {
        std::cout << "Transaccion denegada.\n";
    }

    // 2. Iteracion Perpetua Controlada con Switch
    while (true) {
        std::cout << "Ejecutar comando (1-2, 3 para abortar): ";
        int instruccion{0};
        std::cin >> instruccion;
        
        switch (instruccion) {
            case 1:
                std::cout << "Consultando base de datos...\n";
                break; // Escape (Evita Fallthrough)
            case 2: {
                // Scope Local aislado para prevenir conflictos de compilador
                int factorCrecimiento{50}; 
                balanceOperativo = balanceOperativo + factorCrecimiento; // Mutacion pura (Sin Shadowing)
                break;
            }
            case 3:
                std::cout << "Cerrando sesion.\n";
                return 0; // Terminacion inmediata de rutina main
            default:
                std::cout << "Input anomalo detectado.\n";
                break;
        }
    }
    
    return 0;
}
```

---

## Checklist antes de pasar al Módulo 04

- [ ] Comprendo la evaluación mutuamente excluyente de un bloque `if/else if` y su susceptibilidad al "Unreachable Code".
- [ ] Entiendo que la estructura `switch` requiere de `break` para garantizar aislamiento, y que solo evalúa igualdades absolutas.
- [ ] Dominó el concepto de Local Scope (`{ }`) y su mecanismo de asignación/liberación de memoria tras la llave de cierre `}`.
- [ ] Identifico el "Variable Shadowing" y evito redeclarar identificadores para garantizar mutaciones correctas al Scope padre.
- [ ] Prevengo un Bucle Infinito (*Infinite Loop*) asegurando la mutación de estado dentro del bloque `while`.
- [ ] Diferencio conceptualmente la pre-comprobación del `while` de la post-comprobación obligatoria del `do-while`.
- [ ] Identifico la arquitectura de ciclo de vida en un `for` y reconozco los riesgos de indexación del defecto "Off-By-One".
- [ ] Diferencio funcionalmente la terminación prematura de `break` frente al salto iterativo de `continue`.

---

<div align="center">
  <sub>Maintained by <strong>MiniLux0</strong> · 2026</sub>
</div>
