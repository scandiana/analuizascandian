valor = float(input('digite o valor do produto'))
taxa_desconto = float(input('digite a porcentagem'))

valor_desconto = valor * (taxa_desconto / 100)

valor_final = valor - valor_desconto
print (valor_final)