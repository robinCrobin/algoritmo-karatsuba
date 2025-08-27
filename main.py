def karatsuba(x: int, y: int) -> int: # Nó A
    if x < 10 or y < 10: # Nó B
        return x * y # Nó C 
    
    m = max(len(str(x)), len(str(y))) // 2 # Nó D
    divisor = 10 ** m # Nó E
    
    a, b = divmod(x, divisor) # Nó F
    c, d = divmod(y, divisor) # Nó G
    
    ac = karatsuba(a, c) # Nó H
    bd = karatsuba(b, d) # Nó H
    ad_bc = karatsuba(a + b, c + d)# Nó H
    ad_bc = ad_bc - ac - bd # Nó I
    
    return ac * (divisor ** 2) + ad_bc * divisor + bd # Nó J

def main():
    print("ALGORITMO DE KARATSUBA")
    print("=" * 40)
    
    casos_teste = [
        # Casos base (pelo menos um número com 1 dígito)
        (5, 7),           # ambos 1 dígito
        (9, 123),         # primeiro 1 dígito
        (456, 8),         # segundo 1 dígito
        
        # Casos recursivos
        (12, 34),         
        (123, 456),       
        (1234, 5678),    
        (123456789, 987654321),
        (10, 20)
    ]
    
    for x, y in casos_teste:
        resultado = karatsuba(x, y)
        print(f"{x} × {y} = {resultado}")

if __name__ == "__main__":
    main()