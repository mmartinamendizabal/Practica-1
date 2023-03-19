from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","/","*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
#Variables para contabilizar las respuestas
correct=0
incorrect=0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    #Verifico que la división no sea por 0
    while ((operator=="/")and(number_2==0)):
        number_2 = randrange(10)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado y lo convertimos a integer para operar con él
    result = int(input("resultado: "))
    if (operator=="+"):
        control=number_1+number_2
    elif (operator=="-"):
        control=number_1-number_2
    elif (operator=="*"):
        control=number_1*number_2
    elif (operator=="/"):
        control=number_1/number_2
    if (control==result):
        print("Correcto!")
        correct+=1
    else:
        print("Incorrecto :(")
        incorrect+=1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tuviste {correct} respuestas correctas y {incorrect} respuestas incorrectas.")