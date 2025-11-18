# Escribe un programa que pida una frase por teclado. Realiza las siguientes tareas: 
# 1. Imprime el número de caracteres del texto. 
# 2. Imprime si el texto contiene la vocal ‘a’ (devolviendo True o False) 
# 3. Imprime el texto sin espacios al principio y al final. 
# 4. Muestra los últimos 5 caracteres (utiliza el troceado de cadenas). 

fraseInicio = input('Dime una frase: ')

#1
print(f'La lonjitud de la cadena es: {len(fraseInicio)}')

#2
print('a' in fraseInicio)

#3
fraseArreglada = fraseInicio.strip()
print(fraseArreglada)

#4
print(fraseArreglada[-5:])