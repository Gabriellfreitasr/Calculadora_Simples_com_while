while True:
    num1 = input("Digite um valor: ")
    num2 = input("Digite outro valor: ")
    operador = input("Digite um operador (+, -, / ou *) ")

    try:
        num1_f = float(num1)
        num2_f = float(num2)

    except:
        print("Um ou ambos númneros digitados são inválidos! ")

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Digite um operador válido! ")

    if len(operador) > 1:
        print("Escolha apenas um operador")

    if operador == "+":
        total = num1_f + num2_f
        print(f"O resultado da soma de {num1_f} + {num2_f} é de: {total}")

    elif operador == "-":
        total = num1_f - num2_f
        print(f"O resultado da subtração de {num1_f} - {num2_f} é de: {total}")

    elif operador == "/":
        total = num1_f / num2_f
        print(f"O resultado da divisão de {num1_f} / {num2_f} é de: {total:.2f}")

    elif operador == "*":
        total = num1_f * num2_f
        print(f"O resultado da multiplicação de {num1_f} * {num2_f} é de: {total:.2f}")

    obs = int(input("Deseja fazer outra Operação [1] ? Ou Sair [2]: "))

    if obs == 1:
        print("Nova Operação")
        continue

    elif obs == 2:
        print("Saindo...")
        break

    else:
        print("Resultado Inválido")
