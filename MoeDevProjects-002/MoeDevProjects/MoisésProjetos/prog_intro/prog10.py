'''
Crie um programa que verifique se uma variável é do tipo booleano e imprima o
resultado.
'''
bool_str = input("Insira um valor para o teste (True ou False): ").strip().lower()
bool_con = None

if bool_str == 'true':
    bool_con = True
elif bool_str == 'false':
    bool_con = False

if isinstance(bool_con, bool):
    print("O valor é do tipo booleano")
else:
    print("O valor não é do tipo booleano")