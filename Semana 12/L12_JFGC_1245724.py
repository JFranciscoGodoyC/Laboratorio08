print('Semana No. 12: Ejercicio 1')
n=0
while n>=0 and n<=4:
    print('Elija la opción a calcular')
    print('1)Sumatoria, 2)Factorial, 3)Tablas de Multiplicar, 4)Número perfecto')
    n = int(input())
    match(n):
        case 1:
            N=0
            while N<=0:
                print('Ingrese un número entero positivo:')
                N = int(input())
                if N<0:
                    print('El número ingresado debe ser entero positivo')
            sumatoria = 0
            for i in range(1, N+1):
                sumatoria+=i
            print('La sumatoria es: ' , sumatoria)
            print()

        case 2:
            N=0
            while N<=0:
                print('Ingrese un número entero positivo:')
                N = int(input())
                if N<0:
                    print('El número ingresado debe ser entero positivo')
            factorial = 1
            for i in range(1, N+1):
                factorial+=i
            print('El factorial es: ' , factorial)
            print()
        
        case 3:
            for i in range(1,11):
                for j in range(1,11):
                    print(i*j, "\t", end= " ")
                print()
        
        case 4:
            N=0
            while N<=0:
                print('Ingrese un número entero positivo:')
                N = int(input())
                if N<0:
                    print('El número ingresado debe ser entero positivo') 
            acumulador=0
            for i in range(1,N):
                if N%i==0:
                    acumulador+= i
            if N==acumulador:
                print('Es perfecto')
                print()
            else:
                print('No es perfecto')
                print()
