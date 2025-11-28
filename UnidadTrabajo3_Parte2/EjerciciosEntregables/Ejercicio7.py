# Pide al usuario un nombre de archivo hasta que exista en el directorio actual.

# Cuando exista, muestra su tamaño en bytes y termina el programa.

# Librerías: from pathlib import Path

from pathlib import Path

archivo = Path(input('Dime el nombre de un archivo: '))


while not Path(archivo).exists:
    print('El archivo no existe, dime un archivo que si exista')
    archivo = Path(input('Dime el nombre de un archivo: '))