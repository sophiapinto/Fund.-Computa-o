# Calcular raízes de uma equação do 2° Grau
# Tarefa 3
# Código by: Sarah Sophia Pinto
# Universidade Federal do Maranhão-UFMA
# Curso: BICT   2°período     Turma: 23456M123

#Pergunta base
print("Digite os coeficientes de uma equaçâo do 2° grau da forma: ax² + bx + c")

#coeficiente a 
a = int( input('Coeficiente a: ') )


if a==0:
        print("Se a=0, não é equação do segundo grau. Obrigada por executar meu código.")

else:
    b = int( input("Coeficiente b:   "))
    c = int( input("Coeficiente c:   "))
    delta= (b*2 - 4*a*c) #Discriminante ou delta
    
    
if delta < 0:
            print("Delta é menor que 0, não possui nenhuma raiz real. Obrigada por executar meu código.")
            
elif  delta==0:
            x1 = (-b + delta**(1/2)) / (2*a)
            print("Delta é igual a 0 , raíz 1 = ", x1)
            
else:
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    print ("As raízes da equação são:  ", x1 , "e" , x2)
    #O python vai calcular as raízes em forma de números complexos.
