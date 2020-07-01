# Implementação de um algoritmo em Python
# Tarefa 2
# Código by: Sarah Sophia Pinto
#Universidade Federal do Maranhão-UFMA
#Curso: BICT 2°período  Turma: 23456M123


#Valores dos produtos
celular = 199.99
chaleira = 24.68
gnomo = 89.66
adesivos = 1.67
quantadesivos = 6
dolar = 5.36 #Foi adotado o valor de R$5.36 para dólar


#Valores das taxas 
frete = 18.34
iof = 6.38

#Regras de negócio
totalcompdolar = celular + chaleira + gnomo  + adesivos*quantadesivos + frete
totalcompreal = totalcompdolar * dolar
iof = totalcompreal * 0.0638

#Em caso de querer adicionar manualmente o valor da cotação do dólar no dia basta adicionar a linha abaixo e apagar a linha 12 do código.
#dolar = float (input ("Antes de iniciar o código, qual a cotação do dólar hoje?"))

#pergunta base
sabercompra = int (input( "Quer saber informações das compras feitas por Patryckson? Digite 1, se sim."))


if sabercompra == 1 :
    print ("O valor total da compra de Patryckson em dólar foi: USD ",  totalcompdolar, "." )
    print ("O valor da compra feita por Patryckson em real foi: R$ ", totalcompreal, "."  )
    print ("Patryckson pagou R$ " , iof, " em impostos de compras internacionais com cartão.")
    print ("Obrigada por executar meu código!")

else:
    print ("Você não quis saber informações das compras de  Patryckson! Obrigada por executar meu código!")





