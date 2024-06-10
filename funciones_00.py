from funciones_genericas import *
from data_stark import lista_personajes
from validaciones import *

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def nombres_superheroes(lista: list)-> list:
    nombres = map_list(lambda heroe: heroe["nombre"], lista)
    return nombres

#Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def nombre_altura_todos(lista: list)-> list:
    lista_destino = map_list(lambda heroe: f"{heroe['nombre']} || Altura: {heroe['altura']:.2f}", lista_personajes)
    return lista_destino
    
#Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto(lista: list) -> dict:
    altura_maxima = calcular_maximo_dict(lista, "altura")
    return altura_maxima

#Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_bajo(lista: list)-> dict:
    altura_minima = calcular_minimo_dict(lista, "altura")
    return altura_minima

#Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def altura_promedio(lista: list)-> float:
    alturas = map_list(lambda heroe: heroe["altura"], lista) 
    altura_promedio = calcular_promedio(alturas)
    return altura_promedio

#Calcular e informar cual es el superhéroe más y menos pesado
def heroe_mas_pesado(lista: list)-> dict:
    peso_maximo = calcular_maximo_dict(lista, "peso")
    return peso_maximo

def heroe_mas_liviano(lista: list)-> dict:
    peso_minimo = calcular_minimo_dict(lista, "peso")
    return peso_minimo

def informar_liviano_pesado(lista: list)-> str:
    pesado = heroe_mas_pesado(lista)
    liviano = heroe_mas_liviano(lista)

    print(f"El superhéroe más pesado es '{pesado['nombre']}' con un peso de {pesado['peso']} \n"
          f"El superhéroe más liviano es '{liviano['nombre']}' con un peso de {liviano['peso']}")


