# Solicitar datos al usuario y hacer una validación, también se quitan los espacios en blanco
nombre = input("Introduce tu nombre: ").strip()
while not nombre:
    nombre = input("El nombre no puede estar vacío. Introduce tu nombre: ").strip()

apellido1 = input("Introduce tu primer apellido: ").strip()
while not apellido1:
    apellido1 = input("El primer apellido no puede estar vacío. Introduce tu primer apellido: ").strip()

apellido2 = input("Introduce tu segundo apellido: ").strip()
while not apellido2:
    apellido2 = input("El segundo apellido no puede estar vacío. Introduce tu segundo apellido: ").strip()

# Validar edad (número entero)
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Por favor, introduce un número entero válido.")

# Validar peso (número flotante)
while True:
    try:
        peso = float(input("Introduce tu peso en kg: "))
        break
    except ValueError:
        print("Por favor, introduce un número válido para el peso.")

# Validar estatura (número flotante)
while True:
    try:
        estatura = float(input("Introduce tu estatura en centímetros: ")) / 100  # Convertir a metros
        break
    except ValueError:
        print("Por favor, introduce un número válido para la estatura.")

# Calcular masa corporal
masaCorporal = peso / estatura**2

# Mostrar resultado
print(f"Estimado(a) {nombre} {apellido1} {apellido2}, su masa corporal es: {masaCorporal:.2f}. "
      f"Al tener {edad} años, pesar {peso} kg y medir {estatura * 100} cm.")
