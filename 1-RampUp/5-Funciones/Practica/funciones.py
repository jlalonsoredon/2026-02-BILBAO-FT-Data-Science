import math

def area_cuadrado(lado):
    return(lado ** 2)

def area_triangulo(base, altura):
    return((base * altura) / 2)

def area_circulo(radio):
    return(math.pi * (radio ** 2))


def fibonacci(num):
    i = 1
    serie_fi = [1, 1]
    while len(serie_fi) < num:
        numero_fi = serie_fi[-1] + serie_fi[-2]
        serie_fi.append(numero_fi)
    return(numero_fi)


def constructor_frase(*args):
    frase = ""
    for i in args:
        frase = frase + " " + i
    return(frase)

def edit_list(list, comand, elemet):
    if comand == "add":
        list.append(elemet)
    elif comand == "remove":
        list.remove(elemet)
    return(list)

def conta_caracteres(texto):
    diccionario = {}
    for letra in texto:
        letra_min = letra.lower()
        if letra_min in diccionario:
            diccionario[letra_min] += 1
        else:
            diccionario[letra_min] = 1
    return(diccionario)

def conta_letras(texto, letra):
    cont = 0
    for carater in texto:
        if carater.lower() == letra.lower():
            cont +=1
    return(cont)

def num_mayor(num1, num2):
    if num1 < num2:
        return("El num2 es mayor")
    elif num1 > num2:
        return("el num1 es mayor")
    return("num1 y num2 son iguales")

def piramide(num_filas):
    for i in range(num_filas, 0, -1):
        #recorre la cuenta atras de 5 a 1 y se le asigna a otro rango que tambien va acia atras de i a 1
        for j in list(range(i, 0, -1)):
            #imprime el rango de j sin salto de linea redefiniendo el parametro end a un espacio 
            print(j, end=" ")
        # al finalizar el bucle de j, se imprime un salto de linea para separar cada cuenta atras más en end 
        # por defecto para hacer un doble salto de linea mas similar a un formato de cuenta atras tradicional a ejemlplo:
        print("\n")
        
def dias_semana(int):
    semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    return semana[int-1]