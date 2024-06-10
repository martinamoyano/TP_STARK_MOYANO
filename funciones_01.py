from data_stark import lista_personajes
from funciones_genericas import *

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def nombres_genero(lista:list, genero)-> list:
    lista_filtrada = filtrar(lista, "genero", genero)
    nombres = map_list(lambda heroe: f"{heroe['nombre']}", lista_filtrada)
    return nombres

#Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mas_alto_genero(lista: list, genero)-> dict:
    lista_filtrada = filtrar(lista, "genero", genero)
    maximo = calcular_maximo_dict(lista_filtrada, "altura")
    return maximo 

def mas_bajo_genero(lista: list, genero)-> dict:
    lista_filtrada = filtrar(lista, "genero", genero)
    minimo = calcular_minimo_dict(lista_filtrada, "altura")
    return minimo 

#Recorrer la lista y determinar la altura promedio de los superhéroes de género M
def promedio_alturas_genero(lista:list, genero)-> float:
    lista_filtrada = filtrar(lista, "genero", genero)
    promedio = calcular_promedio_key(lista_filtrada, "altura")
    return promedio

def informar_nombres(lista:list):
    masculino_mas_alto = mas_alto_genero(lista, "M") #diccionario de datos del héroe M más alto
    femenina_mas_alta = mas_alto_genero(lista, "F") #diccionario de datos del héroe F más alto
    masculino_mas_bajo = mas_bajo_genero(lista, "M") #diccionario de datos del héroe M más bajo
    femenina_mas_baja = mas_bajo_genero(lista, "F") #diccionario de datos del héroe F más bajo

    print(f"El nombre del superhéroe más alto es '{masculino_mas_alto["nombre"]}' \n"
        f"El nombre de la superheroína más alta es '{femenina_mas_alta["nombre"]}' \n"
        f"El nombre del superhéroe más bajo es '{masculino_mas_bajo["nombre"]}' \n"
        f"El nombre de la superheroína más baja es '{femenina_mas_baja["nombre"]}' \n")

def contar_tipo(lista: list, key)-> dict:
    lista_tipos = mapear_campo(lista, key)
    tipos = set(lista_tipos)
    diccionario_tipos = {}
    for tipo in tipos:
        if tipo == "":
            diccionario_tipos["no tiene"] = 0
        else:
            diccionario_tipos[tipo] = 0
    for tipo in lista_tipos:
        if tipo == "":
            diccionario_tipos["no tiene"] += 1
        else:
            diccionario_tipos[tipo] += 1
    return diccionario_tipos

def mostrar_heroe (heroe: dict):
    """
    Imprime todos los datos de un heroe

    Args:
        heroe (dict): heroe a imprimir
    """
    print (f"Nombre: {heroe["nombre"]}\n"
           f"color ojos: {heroe["color_ojos"]}\n"
           f"color pelo: {heroe["color_pelo"]}\n"
           f"inteligencia: {heroe["inteligencia"]}\n")

def listar_segun_tipo(lista: list, criterio):
    ordenar_lista_campo(lista, criterio)
    for elemento in lista:
        mostrar_heroe (elemento)


