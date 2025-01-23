# Pedir un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Calcular la suma de números desde 1 hasta el número ingresado (n⋅(n+1))/2.
suma = (numero * (numero + 1)) // 2

# Mostrar el resultado
print(f"La suma de los números desde 1 hasta {numero} es {suma}.")