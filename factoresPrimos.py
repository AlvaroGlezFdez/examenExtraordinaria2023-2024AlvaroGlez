
factores = []

def es_primo(num): # con esta funcion verificas que el numero que se ha introducido es primo
   
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def calcular_factores_primos(n): # Funcion de calcular factores primos que toma como argumento un número
    
    # Dividir el número por 2 mientras sea divisible
    while n % 2 == 0:
        factores.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n //= i
    # Si el número es mayor que 2, entonces es un numero (factor) primo
    if n > 2:
        factores.append(n)
    return factores

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero mayor que 1: "))
            if numero > 1:
                break
            else:
                print("El número debe ser mayor que 1.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    
    factores = calcular_factores_primos(numero)
    print(f"Factores primos de {numero}: {factores}")

if __name__ == "__main__":  # Llamamos a la funcion principal que solicita y comprueba las condiciones iniciales del número y llama a la funcion de clacular los factores orimos
    main()









