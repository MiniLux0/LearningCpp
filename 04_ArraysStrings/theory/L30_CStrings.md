# L30 — C-Strings: Arreglos de Caracteres, Delimitador Nulo y Librerías C Standard

> **Concepto central:** Una C-string no es un tipo de dato nativo especial, sino un **arreglo contiguo de `char`** cuyo final está marcado por el caracter especial **nulo `'\0'` (ASCII 0)**.

---

## Objetivos de aprendizaje

- [ ] Entender el rol indispensable del caracter nulo `'\0'` en el manejo de cadenas estilo C
- [ ] Manipular caracteres individuales con las funciones de clasificación y conversión de `<cctype>`
- [ ] Utilizar las funciones fundamentales de `<cstring>` (`strlen`, `strcpy`, `strcat`, `strcmp`, `strchr`)
- [ ] Leer entradas completas con espacios mediante `cin.getline()`
- [ ] Implementar algoritmos clásicos sobre cadenas: limpieza/normalización, palíndromos y conteo de palabras

---

## 1. La idea central: El caracter nulo `'\0'`

En C/C++, la memoria no guarda el tamaño de una C-string. En su lugar, las funciones leen caracter por caracter hasta encontrar el **caracter nulo `'\0'`**.

```
C-String "Hola" en memoria (requiere 5 bytes):
+---+---+---+---+------+
| 'H' | 'o' | 'l' | 'a' | '\0' |
+---+---+---+---+------+
  0   1   2   3    4    ← índice
```

### Inicialización explícita vs Literal de cadena

```cpp
// 1. Inicialización manual elemento por elemento (requiere '\0' explícito)
char manual[] = {'H', 'o', 'l', 'a', '\0'}; // tamaño = 5

// 2. Literal de cadena (el compilador agrega '\0' automáticamente)
char saludo[20] = "Hola"; // Ocupa 5 bytes útiles, resto ceros

// 3. Tamaño deducido
char autoLen[] = "Hola"; // El compilador asigna tamaño = 5 bytes ('H','o','l','a','\0')
```

> ⚠️ **Peligro:** Si declaras `char arr[4] = {'H', 'o', 'l', 'a'};` sin `'\0'`, las funciones como `cout << arr` o `strlen(arr)` continuarán leyendo la memoria contigua hasta encontrar casualmente un byte `0`, provocando **lecturas basura o segmentation fault**.

---

## 2. Clasificación y Conversión de Caracteres (`<cctype>`)

La librería `<cctype>` provee funciones para analizar caracteres individuales.

### Funciones de inspección (Devuelven un `bool` / `int` distinto de cero si se cumple)
- `isalpha(c)` — ¿Es una letra ('A'-'Z', 'a'-'z')?
- `isdigit(c)` — ¿Es un dígito decimal ('0'-'9')?
- `isalnum(c)` — ¿Es alfanumérico (letra o dígito)?
- `isupper(c)` / `islower(c)` — ¿Es mayúscula / minúscula?
- `ispunct(c)` — ¿Es un signo de puntuación (ej. `!`, `,`, `.`)?
- `isspace(c)` — ¿Es un espacio en blanco (`' '`, `'\t'`, `'\n'`)?

### Funciones de conversión
- `tolower(c)` — Convierte a minúscula (si es mayúscula).
- `toupper(c)` — Convierte a mayúscula (si es minúscula).

```cpp
#include <cctype>

char c = 'A';
if (isupper(static_cast<unsigned char>(c))) {
    char minusc = static_cast<char>(tolower(static_cast<unsigned char>(c))); // 'a'
}
```

> **Buena práctica:** Castear el argumento a `unsigned char` al llamar a las funciones de `<cctype>` para evitar comportamientos indefinidos si el `char` tiene valores negativos.

---

## 3. Manipulación de C-Strings (`<cstring>`)

La librería `<cstring>` proporciona utilidades clásicas para trabajar con arreglos de `char` terminados en `'\0'`.

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `strlen(s)` | Devuelve la longitud de `s` (sin contar `'\0'`) | `strlen("Hola")` $\rightarrow$ `4` |
| `strcpy(dest, src)` | Copia la cadena `src` en `dest` (incluye `'\0'`) | `strcpy(buf, "Hola");` |
| `strcat(dest, src)` | Concatena `src` al final de `dest` | `strcat(buf, " Mundo");` |
| `strcmp(s1, s2)` | Compara `s1` y `s2` lexicográficamente | `0` (iguales), `<0` (`s1<s2`), `>0` (`s1>s2`) |
| `strchr(s, c)` | Busca el caracter `c` en `s`. Retorna `char*` | `strchr("Hola", 'l')` $\rightarrow$ puntero a `'l'` |

```cpp
#include <cstring>

char dest[50];
strcpy(dest, "Hola");       // dest = "Hola\0"
strcat(dest, " Mundo");     // dest = "Hola Mundo\0"

int cmp = strcmp(dest, "Hola Mundo"); // cmp == 0 (iguales)
```

> ⚠️ **Buffer Overflow:** `strcpy` y `strcat` **no verifican** si el arreglo de destino `dest` tiene capacidad suficiente. Asegúrate de que `dest` sea lo suficientemente grande para almacenar la cadena resultante más el caracter `'\0'`.

---

## 4. Lectura de C-Strings con Espacios (`cin.getline`)

El operador `cin >> buffer` **se detiene al encontrar el primer espacio o salto de línea**. Para leer líneas completas (nombres completos, frases):

```cpp
char nombre[50];
cout << "Ingresa tu nombre completo: ";
cin.getline(nombre, 50); // Lee hasta 49 caracteres o hasta encontrar '\n'
```

---

## 5. Algoritmos Clásicos con C-Strings

### Algoritmo 1: Normalización / Limpieza (Dos Punteros Read/Write)
Convierte a minúsculas y elimina signos de puntuación y espacios in-place.

```cpp
void limpiarNormalizar(char str[]) {
    // 1. Convertir a minúsculas
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(static_cast<unsigned char>(str[i]));
    }

    // 2. Filtrar caracteres no alfanuméricos
    int write = 0;
    for (int read = 0; str[read] != '\0'; read++) {
        if (isalnum(static_cast<unsigned char>(str[read]))) {
            str[write++] = str[read];
        }
    }
    str[write] = '\0'; // Mantener el contrato del caracter nulo
}
```

---

### Algoritmo 2: Verificación de Palíndromo (Punteros Opuestos)

```cpp
bool esPalindromo(const char str[]) {
    int len = strlen(str);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        if (str[i] != str[j]) return false;
    }
    return true;
}
```

---

### Algoritmo 3: Conteo de Palabras (Máquina de Estados de 1 Flag)

```cpp
int contarPalabras(const char texto[]) {
    int palabras = 0;
    bool enPalabra = false;
    
    for (int i = 0; texto[i] != '\0'; i++) {
        if (isspace(static_cast<unsigned char>(texto[i]))) {
            enPalabra = false;
        } else if (!enPalabra) {
            enPalabra = true;
            palabras++;
        }
    }
    return palabras;
}
```

---

## 6. Preguntas de Chequeo

<details>
<summary><strong>1. ¿Qué sucede si imprimes una C-string que no contiene <code>'\0'</code>?</strong></summary>

`cout << str` continuará leyendo la memoria contigua imprimiendo basura hasta que encuentre casualmente un byte con valor `0`, o causará un fallo de segmentación (Segmentation Fault / Access Violation).
</details>

<details>
<summary><strong>2. ¿Qué valor retorna <code>strcmp("Ana", "Beatriz")</code>?</strong></summary>

Retorna un valor negativo ($<0$), ya que `'A'` tiene un valor ASCII menor que `'B'`, lo que indica que `"Ana"` precede alfabéticamente a `"Beatriz"`.
</details>

---

## 7. Ejercicio Propuesto

> **Invertir una C-String in-place:**
> Escribe la función `void invertir(char s[])` que invierta los caracteres de la cadena `s` sin crear un arreglo auxiliar.

```cpp
void invertir(char s[]) {
    int len = strlen(s);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}
```

---

## Archivos relacionados

- [`L30_CStrings.cpp`](../code/L30_CStrings.cpp) — Código ejecutable con `<cctype>`, `<cstring>`, `cin.getline()`, normalización y palíndromos

## Navegación

| ← Anterior | 🏠 Section Home |
|------------|-----------------|
| [L29 — Multidimensional Arrays](L29_MultidimensionalArrays.md) | [Arrays & Strings](../) |
