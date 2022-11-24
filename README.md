# Copy detector

Compara archivos .c en diferentes directorios y genera un archivo CSV indicando los archivos similares.

  - Generación de archivo CSV de salida.
  - Comparación de contenido quitando caracteres como {,},\n,\t
  - Ignora palabras reservadas del lenguaje como break, include, etc.

### Instalación

Requisitos para Copy detector funcione [Clic en el icono]

<table>
  <tbody>
    <tr>
      <td>
        <a href="https://www.python.org" target="_blank">
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
        </a> 
      </td>
      <td>
        Python 3
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://pandas.pydata.org/" target="_blank"> 
            <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original-wordmark.svg?raw=true" alt="Pandas" width="40" height="40" /> 
        </a>
      </td>
      <td>
        Pandas
      </td>
    </tr>
  </tbody>
</table>
</br>

* Instalar requisitos contenidos en el archivo _requirements.txt_

```sh
pip install -r requirements.txt
```

* O sino instalar Pandas de la siguiente manera:
```sh
pip install pandas
```

* Clonar el repositorio y ejecutar el script indicando la carpeta a analizar.

```sh
$ cd copydetector_py
$ python3 main.py /path/to/directory
```

### Licencia

    Copy detector
    Copyright (C) <2020>  <Ernesto Gigliotti>
    Copyright (C) <2020>  <Camila Iglesias>
    Copyright (C) <2022>  <Facundo Falcone> - Improvements

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