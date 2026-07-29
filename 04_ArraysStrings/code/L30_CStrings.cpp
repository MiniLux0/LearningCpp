#include <iostream>
#include <cctype>   // isalpha, isupper, ispunct, tolower, toupper
#include <cstring>  // strcpy, strcat, strlen, strcmp, strchr
using namespace std;

void limpiarNormalizar(char str[]) {
    // 1. Convertir a minusculas
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = tolower(static_cast<unsigned char>(str[i]));
    }

    // 2. Eliminar puntuacion y espacios (compactar)
    int write = 0;
    for (int read = 0; str[read] != '\0'; read++) {
        if (isalnum(static_cast<unsigned char>(str[read]))) {
            str[write++] = str[read];
        }
    }
    str[write] = '\0';
}

bool esPalindromo(const char str[]) {
    int len = strlen(str);
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        if (str[i] != str[j]) return false;
    }
    return true;
}

int main() {
    cout << "=== L30: C-Strings ===" << endl;

    // 1. C-string = array de char terminado en '\0'
    char saludo[20] = "Hola";
    cout << "char saludo[20] = \"Hola\": " << saludo << endl;
    cout << "strlen(saludo) = " << strlen(saludo) << endl;

    // 2. Inicializacion explicita con \0
    char manual[] = {'H', 'o', 'l', 'a', '\0'};
    cout << "\nInicializacion manual: " << manual << endl;

    // 3. cctype - isalpha, isupper, ispunct, tolower
    cout << "\n=== cctype ===" << endl;
    char prueba = 'A';
    cout << "isalpha('A') = " << isalpha(prueba) << endl;
    cout << "isupper('A') = " << isupper(prueba) << endl;
    cout << "islower('a') = " << islower('a') << endl;
    cout << "isdigit('5') = " << isdigit('5') << endl;
    cout << "ispunct('!') = " << ispunct('!') << endl;
    cout << "tolower('A') = " << char(tolower('A')) << endl;
    cout << "toupper('a') = " << char(toupper('a')) << endl;

    // 4. cstring - strcpy, strcat, strlen, strcmp, strchr
    cout << "\n=== cstring ===" << endl;
    char dest[50];
    strcpy(dest, "Hola");
    cout << "strcpy(dest, \"Hola\"): " << dest << endl;

    strcat(dest, " Mundo");
    cout << "strcat(dest, \" Mundo\"): " << dest << endl;

    cout << "strlen(dest) = " << strlen(dest) << endl;

    char s1[] = "Hola";
    char s2[] = "Hola";
    char s3[] = "Mundo";
    cout << "strcmp(s1, s2) = " << strcmp(s1, s2) << " (0 = iguales)" << endl;
    cout << "strcmp(s1, s3) = " << strcmp(s1, s3) << " (<0 s1 < s3)" << endl;

    char *ptr = strchr(dest, 'M');
    if (ptr) cout << "strchr(dest, 'M') = " << ptr << endl;

    // 5. Lectura de strings con espacios (cin.getline)
    char nombre[50];
    cout << "\nIngresa tu nombre completo: ";
    cin.getline(nombre, 50);
    cout << "Hola, " << nombre << "!" << endl;

    // 6. Ejercicio: limpiar/normalizar string (palindromo)
    cout << "\n=== Ejercicio: Normalizar y verificar palindromo ===" << endl;
    char frase[100] = "Anita lava la tina";
    cout << "Original: \"" << frase << "\"" << endl;
    limpiarNormalizar(frase);
    cout << "Normalizado: \"" << frase << "\"" << endl;
    cout << "Es palindromo? " << (esPalindromo(frase) ? "SI" : "NO") << endl;

    // 7. Ejemplo mas: contar palabras
    char texto[200] = "  Hola   mundo   C++  ";
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
    cout << "\nTexto: \"" << texto << "\"" << endl;
    cout << "Palabras: " << palabras << endl;

    return 0;
}