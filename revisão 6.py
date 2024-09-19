peso = float(input("informe seu peso: "))
alt = float(input("informe sua altura: "))
imc = peso/(alt*alt)
if imc <= 18.5:
    print("abaixo do peso")
elif imc >= 18.6 and imc < 24.9:
    print("pesos ideal. PARABÉNS !")
elif imc >= 25.0 and imc > 29.9:
    print("levemente acima do peso !")
elif imc >= 30.0 and imc > 34.9:
    print("obesidade grau 1 !")
elif imc >= 35.0 and imc > 39.9:
    print("obesidade grau 2. severa !")
elif imc >= 40:
    print("obesidade grau 3. mórbida")
