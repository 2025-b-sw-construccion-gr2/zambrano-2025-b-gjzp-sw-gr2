import math

def calculadora():
    print("--- Calculadora Pro v1.0 ---")
    print("Operaciones: +, -, *, /, ^ (potencia), r (raíz)")
    
    try:
        n1 = float(input("Ingrese el primer número: "))
        op = input("Ingrese la operación: ").lower()
        
        if op == 'r':
            if n1 < 0:
                print("Error: No se puede calcular raíz de un negativo.")
            else:
                print(f"Resultado: {math.sqrt(n1)}")
            return

        n2 = float(input("Ingrese el segundo número: "))

        if op == '+':
            print(f"Resultado: {n1 + n2}")
        elif op == '-':
            print(f"Resultado: {n1 - n2}")
        elif op == '*':
            print(f"Resultado: {n1 * n2}")
        elif op == '/':
            if n2 == 0:
                print("Error: División por cero no permitida.")
            else:
                print(f"Resultado: {n1 / n2}")
        elif op == '^':
            print(f"Resultado: {pow(n1, n2)}")
        else:
            print("Operación no válida.")
            
    except ValueError:
        print("Error: Por favor, ingrese solo números válidos.")

calculadora()