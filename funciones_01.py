from data_stark import lista_personajes
from funciones_genericas import *

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def nombres_masculinos(lista:list)-> list:
    lista_filtrada = filtrar(lista, "genero", "M")
    heroes_masculinos = map_list(lambda heroe: f"{heroe['nombre']}", lista_filtrada)
    return heroes_masculinos

# lista = nombres_masculinos(lista_personajes)
# mostrar_lista(lista)

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def nombres_femeninos(lista:list)-> list:
    lista_filtrada = filtrar(lista, "genero", "F")
    heroes_femeninos = map_list(lambda heroe: f"{heroe['nombre']}", lista_filtrada)
    return heroes_femeninos

lista = nombres_femeninos(lista_personajes)
mostrar_lista(lista)