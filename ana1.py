ps = float(input('digite seu peso'))
al = float(input('digite sua altura'))
imc = ps/ al*al

if imc < 18.5:
    print (imc,'abaixo do peso normal')

elif imc > 18.5 and imc< 24.9:
    print (imc,'peso normal')

elif imc > 25.0 and imc < 29.9:
    print (imc,'excesso de peso')

elif imc > 30.0 and imc < 34.9:
    print (imc,'obesidade classe 1')

elif imc > 35.0 and imc < 39.9:
    print (imc, 'obesidade classe 2')

else:
    imc >= 40.0
    print (imc,'obesidade classe 3')