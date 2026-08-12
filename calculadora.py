#Pedir ao usuário um número
num1 = float (input("Digite um número: "))
num2 = float(input("Digite outro número: "))

#Pedir o usuário que escolha uma operação
operacao = input("Escolha uma operação (+, -, *, /): ")

if operacao == "+":
	resultado = num1 + num2
elif operacao == "-":
	resultado = num1 - num2
elif operacao == "*":
	resultado = num1 * num2
elif operacao == "/":
	resultado = num1 / num2
else:
	print("Operação Inválida")

#Imprimir o resultado
print("O resultado é: ", resultado)

#Perguntar ao usuário se ele quer continuar calculando ou sair
continuar = input("Deseja continuar calculando? (s/n): ")

if continuar == "s":
	while continuar  == "s":
		num1 = resultado
		num2 = float(input("Digite outro número: "))

		#Pedir ao usuário que escolha uma operação
		operacao = input("Escolha uma operação (+, -, *, /): ")
		if operacao == "+":
			resultado = num1 + num2
		elif operacao == "-":
			resultado = num1 - num2
		elif operacao == "*":
			resultado = num1 * num2
		elif operacao == "/":
			resultado = num1 / num2
		else:
			print("Operação Inválida")
		#Imprimir o resultado
		print("O resultado é: ", resultado)

		#Perguntar ao usuário se ele quer continuar calculando ou sair
		continuar = input("Deseja continuar calculando?(s/n): ")
	else:
		print("Até mais!")
