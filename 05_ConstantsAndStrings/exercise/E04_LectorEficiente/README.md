# E04: Lector Eficiente

## Contexto
Trabajas en el motor de búsqueda de una colosal enciclopedia galáctica. El programa necesita escanear y mostrar fragmentos de artículos de millones de páginas continuamente.

El antiguo desarrollador configuró la función central de escaneo para que reciba el texto por defecto utilizando un pesado y masivo `std::string`. Esto está provocando que el servidor clone (copie físicamente en RAM) artículos de miles de páginas cada vez que un usuario hace una búsqueda, provocando que la memoria se sature y los servidores se apaguen en segundos.

## Tu Misión
Abre el archivo `E04_LectorEficiente.cpp`.
1. Incluye la librería moderna necesaria para crear "vistas ligeras" de texto.
2. Modifica la firma (los parámetros) de la función `analizarArticulo` para que utilice "Referencias Ligeras" ultraligeros en lugar de clonar un pesado objeto dinámico de texto `std::string`.
3. Modifica la variable estática dentro del `main` para que también sea una vista ligera y no asigne memoria innecesaria.
