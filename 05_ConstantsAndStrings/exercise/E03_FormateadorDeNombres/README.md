# E03: Formateador de Nombres

## Contexto
Estás programando la base de datos de un MMORPG de fantasía. Cuando un jugador crea su cuenta, el sistema debe generar una "Etiqueta de Chat" uniendo un prefijo de clan (ej. `"[Novato] "`), su nombre, y un sufijo de nivel (ej. `" (Lv.1)"`).

## Tu Misión
Abre el archivo `E03_FormateadorDeNombres.cpp`. 
1. Asegúrate de incluir la librería correcta que le da el poder al programa para entender y manipular `std::string`.
2. Repara la línea que genera la etiqueta de chat. El error ocurre porque el compilador intenta evaluar `"Etiqueta: " + "[Novato] "` de izquierda a derecha. Ambos son literales estáticos (C-strings) y carecen de métodos de concatenación.
3. Puedes repararlo encerrando la primera palabra en un tipo `std::string` explícitamente (ej: `std::string{"Etiqueta: "}`) para forzar que toda la cadena inicie como una estructura de datos dinámica.
