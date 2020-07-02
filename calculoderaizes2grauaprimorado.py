# Calcular raízes de uma equação do 2° Grau
# Tarefa 4
# Código by: Sarah Sophia Pinto
# Universidade Federal do Maranhão-UFMA
# Curso: BICT   2°período     Turma: 23456M123


def coefi (a, b, c):
    delta= (b**2 - 4*a*c) #Discriminante ou delta
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)

    print('\nO valor da raíz da equação - x1: {0}'.format(x1))
    print('O valor da raíz da equação - x2: {0}'.format(x2))
    #Algumas vezes o python vai calcular as raízes em forma de números complexos.
    
    
while True:
        
        print('Calculando as raízes de uma equaçâo do 2° grau da forma: ax² + bx + c.\n')
        a = int (input("Digite um coeficiente a, não nulo:  "))
        if a==0:
            print("Se a=0, não é equação do segundo grau. Tente novamente. Obrigada por executar meu código.")
            
        else:
            b = int( input("Digite o coeficiente b:   "))
            c = int( input("Digite o coeficiente c:   "))
            print ("a =   ", a, "b=  ", b, "e c=   ",c)
        
            delta= (b**2 - 4*a*c) #Discriminante ou delta
            print ("delta =    ", delta)
            if delta < 0:
                print("Delta é menor que 0, não possui nenhuma raiz real. Obrigada por executar meu código.")
                import sys
                continua = 1
                continua = input("Deseja sair? Digite 1 se deseja sair.")
                if (continua == "1") :
                    sys.exit()
                    
            elif  delta==0:
                x1 = (-b + delta**(1/2)) / (2*a)
                continua = 1
                continua = input("Deseja sair? Digite 1 se deseja sair.")
                if (continua == "1") :
                    sys.exit()
          
            else:
                x1 = (-b + delta**(1/2)) / (2*a)
                x2 = (-b - delta**(1/2)) / (2*a)
                coefi(a,b,c)
                continua = input("Deseja sair? Digite 1 se deseja sair.")

if (continua == "1") :
            sys.exit()

