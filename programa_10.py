while True:
    foo = int(input("numero 1: "))
    bar = int(input("numero 2: "))
    tar = foo + bar
    print(foo,bar,tar)
    
    opcion = input("Continuar s/n:")
    if opcion == 'n':
        break
