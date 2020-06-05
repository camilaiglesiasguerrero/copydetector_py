# Copy detector

Compara archivos .c en diferentes directorios y genera un archivo CSV indicando los archivos similares.

  - Generación de archivo CSV de salida.
  - Comparación de contenido quitando caracteres como {,},\n,\t
  - Ignora palabras reservadas del lenguaje como break, include, etc.

### Instalación

Copy detector requiere [Python 3](https://www.python.org/download/releases/3.0/) para funcionar.

Clonar el repositorio y ejecutar el script indicando la carpeta a analizar.

```sh
$ cd copydetector_py
$ python3 main.py /path/to/directory
```

### Licencia

    Copy detector
    Copyright (C) <2020>  <Ernesto Gigliotti>
    Copyright (C) <2020>  <Camila Iglesias>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.