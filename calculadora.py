print("""
Según el número escriba lo que desee hacer:

1. Suma
2. Resta
3. Multiplicación""")

opcionDelMenu: input()

if opcionDelMenu == 1:
    print("Que números desea sumar?")
    numeroSumaUno: input()
    numeroSumaDos: input()
    resultadoDeLaSuma: numeroSumaUno + numeroSumaDos
    print(resultadoDeLaSuma)