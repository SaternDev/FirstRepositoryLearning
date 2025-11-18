# Escribe un programa que cada vez que se ejecute pida por teclado dos números, uno 
# de ellos que represente el peso de una persona (entre 50 y 100 kilos) y el otro la altura 
# (entre 1.50 y 2.00 metros) y que escriba el IMC (Índice de Masa Corporal) 
# correspondiente, redondeado con un decimal. Se recuerda que el IMC se calcula con 
# la fórmula IMC = peso / altura2.  

pesoPers = float(input('Dime el peso de la persona en  kg entre 50 y 100Kg: '))
alturaPers = float(input('Dime la altura de la persona en m entre 1.50 y 2.00: '))

imc = round(pesoPers / alturaPers ** 2, 1)

print(f'Este es tu IMC: {imc}')