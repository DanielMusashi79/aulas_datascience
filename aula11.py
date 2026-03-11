def dividir(a,b):
    r = 0
    try:
        r = a / b
        return print(r)
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except:
        print("Erro inesperado. Foi mal!")
    finally:
        print("Função executada.")
    #return a / b

dividir(4,'d')

