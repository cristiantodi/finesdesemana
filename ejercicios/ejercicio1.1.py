print("CUAL VALOR SERA EL MAS ALTO")

num1 = int(input("INGRESAR NUMERO 1:  "))
num2 = int(input("INGRESAR NUMERO 2:  "))

def DevuelveMax (n1, n2):
    if n1>n2:
        print("NUMERO 1 MAYOR QUE NUMERO 2")
    elif n1<n2:
        print("NUMERO 2 MAYOR QUE NUMERO 1")
    else:
        print("LOS DOS NUMEROS SON IGUALES")
        
DevuelveMax(num1, num2)