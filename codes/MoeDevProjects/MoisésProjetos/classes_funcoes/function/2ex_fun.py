def soma(a,b):
    return a + b

def calculadora(a,b):
    return a+b,a-b,a*b,a/b if b !=0 else "Erro"

def main():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("Soma:", soma(a,b))
    print(f"calculadora: {calculadora(a,b)}")
    
main()