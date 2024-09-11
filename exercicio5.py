# pedeimput ao usuário do peso e armazena na variável "peso"
peso = float(input("Digite seu peso (em kg): "))

# pede o imput ao usuário da altura e armazena na variável "altura"
altura = float(input("Digite sua altura (em cm): "))

# Calcula o Índice de Massa Corporal (IMC) 
imc = peso / ((altura /100)** 2)

# Exibe o IMC calculado
print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")
