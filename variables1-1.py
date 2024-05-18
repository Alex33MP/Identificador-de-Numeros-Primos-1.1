#IDENTIFICADOR DE NUMEROS PRIMOS 1.1

def es_primo(numero):# verifica si un número dado es primo o no. Comienza verificando si el número es menor que 2, en cuyo caso no es primo y devuelve False.
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1): #Se realiza un bucle for desde 2 hasta la raíz cuadrada del número más 1. Se utiliza int(numero ** 0.5) + 1 para asegurarse de que se incluya la raíz cuadrada en el rango.
        if numero % i == 0:#Si el número es divisible por alguno de los valores en el rango, entonces no es primo y se devuelve False.
            return False 
    return True #Si el bucle termina sin encontrar un divisor, entonces el número es primo y se devuelve True.

def numeros_primos_hasta(numero):
    numeros_primos = [] #La función numeros_primos_hasta(numero) encuentra todos los números primos hasta un número dado. Comienza con una lista vacía numeros_primos para almacenar los números primos encontrados.
    for num in range(2, numero + 1): #Se realiza un bucle for desde 2 hasta el número más 1.
        if es_primo(num): # Se llama a la función es_primo(numero) para verificar si cada número en el rango es primo.
            numeros_primos.append(num) #Si el número es primo, se agrega a la lista numeros_primos.
    return numeros_primos 