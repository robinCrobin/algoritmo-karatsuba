def karatsuba(x: int, y: int) -> int:
    """
    Implementação do algoritmo de Karatsuba para multiplicação rápida.
    
    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro
    
    Returns:
        int: Produto de x e y
    """
    # Caso base: se algum dos números tem apenas 1 dígito
    if x < 10 or y < 10:
        return x * y
    
    # Calcula o número de dígitos do maior número
    n = max(len(str(x)), len(str(y)))
    
    # Se n é ímpar, adiciona 1 para facilitar a divisão
    m = n // 2
    
    # Divide os números em duas partes
    divisor = 10 ** m
    
    a = x // divisor  # Parte alta de x
    b = x % divisor   # Parte baixa de x
    c = y // divisor  # Parte alta de y
    d = y % divisor   # Parte baixa de y
    
    # Três multiplicações recursivas (ao invés de quatro)
    ac = karatsuba(a, c)          # a * c
    bd = karatsuba(b, d)          # b * d
    ad_bc = karatsuba(a + b, c + d) - ac - bd  # (a+b)(c+d) - ac - bd = ad + bc
    
    # Combina os resultados usando a fórmula de Karatsuba
    # xy = ac * 10^(2m) + (ad + bc) * 10^m + bd
    resultado = ac * (10 ** (2 * m)) + ad_bc * (10 ** m) + bd
    
    return resultado

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
        (123456789, 987654321)
    ]
    
    for x, y in casos_teste:
        resultado = karatsuba(x, y)
        print(f"{x} × {y} = {resultado}")

if __name__ == "__main__":
    main()