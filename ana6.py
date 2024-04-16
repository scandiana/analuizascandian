nota1 = float(input('digite sua nota'))
nota2 = float(input('digite sua outra nota'))

media = (nota1+nota2) / 2

if media >=9:
   print (media,'nota A')
   
elif media >= 7.5 and media <= 9:
   print (media,'nota B')
   
elif media >= 6 and media <= 7.5:
    print (media, 'nota C')
    
elif media >= 4 and media <= 6:
    print (media,'nota d')
    
else:
    print (media, 'nota f')
