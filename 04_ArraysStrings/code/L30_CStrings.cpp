#include <iostream>
#include <cctype>   // isalpha, isdigit, isalnum, isupper, islower, ispunct, tolower, toupper
#include <cstring>  // strlen, strcpy, strcat, strcmp, strchr
#include <cstdlib>  // atoi, atof, atol
#include <cstdio>   // sprintf
using namespace std;

// ============================================================================
// L30 — C-STRINGS: CHARACTER ARRAYS, NULL TERMINATOR, AND C LIBRARIES
// ============================================================================

// Algorithm 1: In-place cleaning and normalization (Two Read/Write pointers)
void limpiarNormalizar(char str[]) {
    // 1. Convert to lowercase
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = static_cast<char>(tolower(static_cast<unsigned char>(str[i])));
    }

    // 2. Filter non-alphanumeric characters
    int write = 0;
    for (int read = 0; str[read] != '\0'; read++) {
        if (isalnum(static_cast<unsigned char>(str[read]))) {
            str[write++] = str[read];
        }
    }
    str[write] = '\0'; // Maintain the null character '\0' contract
}

// Algorithm 2: Palindrome verification (Opposite pointers)
bool esPalindromo(const char str[]) {
    int len = static_cast<int>(strlen(str));
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        if (str[i] != str[j]) return false;
    }
    return true;
}

// Algorithm 3: Word count (1-flag state machine)
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

// Proposed Exercise: In-place C-String reversal
void invertir(char s[]) {
    int len = static_cast<int>(strlen(s));
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}

int main() {
    cout << "=== L30: C-Strings ===" << endl;

    // 1. Null character '\0' and Initialization
    cout << "\n--- 1. C-String and Initialization ---" << endl;
    char manual[] = {'H', 'e', 'l', 'l', 'o', '\0'}; // 6 bytes
    char saludo[20] = "Hello";                   // Literal (automatically adds '\0')

    cout << "Manual initialization: " << manual << " (strlen = " << strlen(manual) << ")" << endl;
    cout << "Literal char saludo[20]: " << saludo << " (strlen = " << strlen(saludo) << ")" << endl;

    // 2. <cctype> Functions
    // PEDAGOGICAL NOTE:
    // For beginners, using toupper(c) or tolower(c) directly is enough.
    // We use static_cast<unsigned char>(c) as an advanced best practice to avoid
    // negative values with special characters/accents in compilers with 'signed char'.
    cout << "\n--- 2. <cctype> Library ---" << endl;
    char c = 'A';
    cout << "isalpha('A') = " << (isalpha(static_cast<unsigned char>(c)) ? "true" : "false") << endl;
    cout << "isdigit('9') = " << (isdigit(static_cast<unsigned char>('9')) ? "true" : "false") << endl;
    cout << "ispunct('!') = " << (ispunct(static_cast<unsigned char>('!')) ? "true" : "false") << endl;
    cout << "tolower('A') = " << static_cast<char>(tolower(static_cast<unsigned char>('A'))) << endl;
    cout << "toupper('a') = " << static_cast<char>(toupper(static_cast<unsigned char>('a'))) << endl;

    // 3. <cstring> Functions
    cout << "\n--- 3. <cstring> Library ---" << endl;
    char dest[50];
    strcpy(dest, "Hello");
    cout << "strcpy(dest, \"Hello\"): " << dest << endl;

    strcat(dest, " World");
    cout << "strcat(dest, \" World\"): " << dest << endl;
    cout << "strlen(dest) = " << strlen(dest) << endl;

    char s1[] = "Ana";
    char s2[] = "Beatriz";
    cout << "strcmp(\"Ana\", \"Beatriz\") = " << strcmp(s1, s2) << " (< 0 indicates 'Ana' comes first)" << endl;

    const char *pos = strchr(dest, 'W');
    if (pos) {
        cout << "strchr(dest, 'W') found substring starting from 'W': \"" << pos << "\"" << endl;
    }

    // 4. Text <-> Number Conversions (<cstdlib>, <cstdio>)
    cout << "\n--- 4. Text <-> Number Conversions (<cstdlib>, <cstdio>) ---" << endl;
    char textoNum[] = "125.75";
    double precio = atof(textoNum);
    cout << "atof(\"125.75\") + 10 = " << precio + 10.0 << endl;

    int numInt = atoi("42");
    cout << "atoi(\"42\") * 2 = " << numInt * 2 << endl;

    char bufferFormatted[32];
    int edad = 21;
    sprintf(bufferFormatted, "I am %d years old", edad);
    cout << "sprintf(buffer, \"I am %d years old\", 21): \"" << bufferFormatted << "\"" << endl;

    // 5. Algorithm: Normalization and Palindrome
    cout << "\n--- 5. Normalization and Palindrome ---" << endl;
    char frase[100] = "Anita lava la tina!"; // "Anita washes the tub" - a Spanish palindrome
    cout << "Original phrase: \"" << frase << "\"" << endl;

    limpiarNormalizar(frase);
    cout << "Cleaned/normalized phrase: \"" << frase << "\"" << endl;
    cout << "Is it a palindrome?: " << (esPalindromo(frase) ? "YES" : "NO") << endl;

    // 6. Algorithm: Word Count
    cout << "\n--- 6. Word Count ---" << endl;
    char texto[200] = "  Hello   world   C++  learning   is  great! ";
    cout << "Text: \"" << texto << "\"" << endl;
    cout << "Total words: " << contarPalabras(texto) << endl;

    // 7. Proposed Exercise: In-place string reversal
    cout << "\n--- 7. Proposed Exercise: In-Place Reversal ---" << endl;
    char palabra[50] = "Estructura";
    cout << "Before reversal: \"" << palabra << "\"" << endl;
    invertir(palabra);
    cout << "After reversal: \"" << palabra << "\"" << endl;

    return 0;
}