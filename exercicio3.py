# pede imput do usuário e armazena na variável
num = int(input("Digite um número: "))

# verifica e imprime se a variável possui resto quuando dividida com a função de módulo(%)
# se possuir é impar SE NÃO é par
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
