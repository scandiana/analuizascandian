a = float(input('diga o primeiro lado do triangulo'))
b = float(input('diga o segundo lado do triangulo'))
c = float(input('digite o terceiro lado do triangulo'))

triangulo = a+b>c and a+c>b and b+c>a

if triangulo == a==b and a == c:
   print(triangulo, "equilatero")

elif triangulo == a==b and a==c and c==b:
   print(triangulo, "isoceles")

elif triangulo != a==b and a==c and c==b:
   print (triangulo, 'escaleno')
   
else:
    print ('nao e triangulo')
