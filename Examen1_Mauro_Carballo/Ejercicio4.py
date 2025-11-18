# Vamos a crear una contraseña segura a partir de un texto. Escribe un programa que 
# pida una contraseña por teclado. La contraseña debe ser una frase que solo contenga 
# letras minúsculas y espacios. Por ejemplo, “mi clave segura”. Realiza las siguientes 
# tareas: 
# 1. Convierte la cadena a formato título (la primera inicial de cada palabra en 
# mayúscula) 
# 2. Sustituye los espacios por guiones bajos (caracter _) y la ‘a’ por el número 4. 
# 3. Añade el carácter ‘$’ al inicio y al final 
# 4. Busca la posición del primer carácter ‘_’, extrae la subcadena desde el siguiente 
# carácter a ‘_’ hasta el final y añade esa subcadena al principio de la contraseña. 
# Imprime el resultado. En el ejemplo del ejercicio, el resultado sería: 
# Cl4ve_Segur4$$Mi_Cl4ve_Segur4$ 

passwordStart = input('Dime la contraseña solo con espacio y minusculas: ')

#1
passwordStart = passwordStart.title()

#2
passwordStart = passwordStart.replace(' ', '_')
passwordStart = passwordStart.replace('a', '4')

#3
passwordStart = '$' + passwordStart + '$'

#4
segPartPassword = passwordStart[passwordStart.find('_') + 1:]
finalPassword = segPartPassword + passwordStart

print(f'Tu contraseña final es: {finalPassword}')