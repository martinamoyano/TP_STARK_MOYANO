from funciones_genericas import *
from data_stark import lista_personajes
from validaciones import *

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def nombres_superheroes(lista: list)-> None:
    nombres = mapear_campo(lista, "nombre")
    mostrar_lista(nombres)

#Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def nombre_altura_todos(lista: list)-> None:
    lista_destino = map_list(lambda heroe: f"{heroe['nombre']} || Altura: {float(heroe['altura']):.2f}", lista_personajes)
    mostrar_lista(lista_destino)
    
#Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto(lista: list) -> float:
    alturas = mapear_campo(lista, "altura")
    altura_maxima = calcular_maximo(alturas)
    return altura_maxima

def imprimir_heroe_mas_alto(altura_maxima: float) -> None:
    print(f"La altura del héroe más alto es: {altura_maxima:.2f}")


#Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_bajo(lista: list)-> float:
    alturas = mapear_campo(lista, "altura")
    altura_minima = calcular_minimo(alturas)
    return altura_minima


#Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def altura_promedio(lista: list)-> float:
    alturas = mapear_campo(lista, "altura")
    altura_promedio = calcular_promedio(alturas)
    return altura_promedio

def heroe_mas_alto(lista: list) -> None:
    altura_maxima = max([float(heroe['altura']) for heroe in lista])
    

def altura_promedio(lista: list) -> None:
    alturas = [float(heroe['altura']) for heroe in lista]
    altura_promedio = sum(alturas) / len(alturas)
    return altura_promedio



#Informar cual es el nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def nombre_mas_alto(lista: list)-> str:
    altura_maxima = heroe_mas_alto(lista)
    nombre_heroe_maximo = buscar_dato_dict(lista, "altura", altura_maxima)["nombre"]
    return nombre_heroe_maximo

def nombre_mas_bajo(lista: list)-> str:
    altura_minima = heroe_mas_bajo(lista)
    nombre_heroe_minimo = buscar_dato_dict(lista, "altura", altura_minima)["nombre"]
    return nombre_heroe_minimo

def informar_bajo_alto(lista: list)-> str:
    print(f"El superhéroe más bajo es '{nombre_mas_bajo(lista)}' y el más alto es '{nombre_mas_alto(lista)}'")



#Calcular e informar cual es el superhéroe más y menos pesado
def heroe_mas_pesado(lista: list)-> dict:
    peso_maximo = calcular_maximo_dict(lista, "peso")
    dict_pesado = {"nombre": peso_maximo["nombre"], "peso": peso_maximo["peso"]}
    return dict_pesado

def heroe_mas_liviano(lista: list)-> dict:
    peso_minimo = calcular_minimo_dict(lista, "peso")
    dict_liviano = {"nombre": peso_minimo["nombre"], "peso": peso_minimo["peso"]}
    return dict_liviano

def informar_liviano_pesado(lista: list)-> str:
    mas_pesado = heroe_mas_pesado(lista)
    mas_liviano = heroe_mas_liviano(lista)

    print(f"El superhéroe más pesado es '{mas_pesado['nombre']}' con un peso de {mas_pesado['peso']} \n"
          f"El superhéroe más liviano es '{mas_liviano['nombre']}' con un peso de {mas_liviano['peso']}")


def menu()-> str:
    """Menú de opciones al usuario

    Returns:
        int: Devuelve la opción seleccionada
    """
    print("STARK INDUSTRIES \n"
        "--------------------------------------------------------\n"
        "1. Mostrar los nombres de todos los héroes.\n"
        "2. Mostrar los nombres de los héroes y sus alturas.\n"
        "3. Ver la altura del héroe más alto.\n"
        "4. Ver la altura del héroe más bajo.\n"
        "5. Mostrar la altura promedio entre todos los héroes.\n"
        "6. Ver el nombre del héroe más alto y del más bajo.\n"
        "7. Mostrar el héroe más pesado y del más liviano.\n"
        "8. Salir. \n"
        "--------------------------------------------------------\n"
        "  ")

    return input("Ingrese opción deseada: ")