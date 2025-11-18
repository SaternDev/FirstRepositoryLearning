# Escribe un programa que cada vez que se ejecute pida por teclado una cantidad de 
# segundos entre 0 y 10000 y que escriba su valor en horas, minutos y segundos.

segAsk = int(input('Dime una cantidad de segundos entre 0  y 10000: '))

valorHoras = segAsk // 3600
print(valorHoras)
valorMinutos = (segAsk % 3600) // 60
print(valorMinutos)
valorSeg = (segAsk % 3600) % 60
print(valorSeg)