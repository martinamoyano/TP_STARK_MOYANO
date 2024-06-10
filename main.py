from validaciones import *
from funciones_genericas import *
from data_stark import lista_personajes
from funciones_00 import *
from funciones_01 import *

def menu()-> str:
    """Menú de opciones al usuario

    Returns:
        int: Devuelve la opción seleccionada
    """
    print("STARK INDUSTRIES \n"
        "--------------------------------------------------------\n"
        "1. Mostrar los nombres de todos los héroes.\n"
        "2. Mostrar nombres de todos los héroes masculinos. \n"
        "3. Mostrar nombres de todas las heroínas \n"
        "4. Mostrar los nombres de todos los héroes y sus alturas.\n"
        "5. Ver la altura del héroe más alto de todos.\n"
        "6. Ver la altura del héroe más bajo de todos.\n"
        "7. Ver altura del héroe masculino más alto \n"
        "8. Ver altura de la heroína más alta \n"
        "9. Ver altura del héroe masculino más bajo \n"
        "10. Ver altura de la heroína más baja \n"
        "11. Mostrar la altura promedio entre todos los héroes.\n"
        "12. Informar altura promedio de los héroes masculinos\n"   
        "13. Informar altura promedio de las heroínas \n"
        "14. Informar nombres de los héroes asociados a los items 7 al 10 \n"
        "15. Ver el nombre del héroe más alto y del más bajo.\n"
        "16. Mostrar el héroe más pesado y del más liviano.\n"    
        "17. Mostrar cantidad de héroes con cada tipo de color de ojos \n"
        "18. Mostrar cantidad de héroes con cada tipo de color de pelo \n"
        "19. Mostrar cantidad de héroes con cada tipo de inteligencia \n"
        "20. Listar todos los superhéroes agrupados por color de ojos \n"
        "21. Listar todos los superhéroes agrupados por color de pelo \n"
        "22. Listar todos los superhéroes agrupados por inteligencia \n"
        "23. Salir. \n"
        "--------------------------------------------------------\n"
        "  ")

    return input("Ingrese opción deseada (1-23): ")

def iniciar(lista: list) -> None:
    try:
        validar_lista(lista)
    
        while True:
            limpiar_pantalla()
            opcion = menu()
            print(" ")
            match opcion:
                case "1": #informa todos los nombres
                    lista_nombres = nombres_superheroes(lista)
                    mostrar_lista(lista_nombres)

                case "2": #informa nombres masculinos
                    lista_masculinos = nombres_genero(lista, "M")
                    mostrar_lista(lista_masculinos)

                case "3": #informa nombres femeninos
                    lista_femeninos = nombres_genero(lista, "F")
                    mostrar_lista(lista_femeninos)

                case "4": #informa nombres y alturas de todos
                    alturas_y_nombres = nombre_altura_todos(lista)
                    mostrar_lista(alturas_y_nombres)

                case "5": #calcula e informa altura máxima
                    altura_maxima = heroe_mas_alto(lista) #diccionario de datos del héroe más alto
                    print(f"El superhéroe más alto de todos mide {altura_maxima["altura"]}")

                case "6": #calcula e informa altura mínima
                    altura_minima = heroe_mas_bajo(lista) #diccionario de datos del héroe más bajo
                    print(f"El superhéroe más bajo de todos mide {altura_minima["altura"]}")

                case "7": #calcula e informa altura máxima de masculinos
                    masculino_mas_alto = mas_alto_genero(lista, "M") #diccionario de datos del héroe M más alto
                    print(f"El superhéroe masculino más alto mide {masculino_mas_alto["altura"]}")

                case "8": #calcula e informa altura máxima de femeninas
                    femenina_mas_alta = mas_alto_genero(lista, "F") #diccionario de datos del héroe F más alto
                    print(f"La superhéroina más alta mide {femenina_mas_alta["altura"]}")

                case "9": #calcula e informa altura minima de masculinos
                    masculino_mas_bajo = mas_bajo_genero(lista, "M") #diccionario de datos del héroe M más bajo
                    print(f"El superhéroe masculino más bajo mide {masculino_mas_bajo["altura"]}")

                case "10": #calcula e informa altura minima de femeninas
                    femenina_mas_baja = mas_bajo_genero(lista, "F") #diccionario de datos del héroe F más bajo
                    print(f"La superheroína más baja mide {femenina_mas_baja["altura"]}")

                case "11": # calcula e informa promedio de alturas
                    promedio = altura_promedio(lista)
                    print(f"La altura promedio de todos los superhéroes es: {promedio:.2f}")

                case "12": # calcula e informa promedio de alturas masculinas
                    promedio = promedio_alturas_genero(lista, "M")
                    print(f"La altura promedio de los superhéroes masculinos es: {promedio:.2f}")

                case "13": # calcula e informa promedio de alturas femeninas
                    promedio = promedio_alturas_genero(lista, "F")
                    print(f"La altura promedio de las superheroínas es: {promedio:.2f}")

                case "14": # informa nombres asociados a items (C-F)
                    informar_nombres(lista)

                case "15": #informa nombre del más alto y del más bajo
                    altura_maxima = heroe_mas_alto(lista) #diccionario de datos del héroe más alto
                    altura_minima = heroe_mas_bajo(lista) #diccionario de datos del héroe más bajo
                    print(f"El superhéroe más bajo de todos es '{altura_minima["nombre"]}' y el más alto '{altura_maxima["nombre"]}'")

                case "16": #calcula e informa héroe más y menos pesado
                    informar_liviano_pesado(lista)

                case "17": #informar superhéroes tienen cada tipo de color de ojos
                    tipos_ojo = contar_tipo(lista, "color_ojos")
                    mostrar_diccionario(tipos_ojo)
                
                case "18": #informar superhéroes tienen cada tipo de color de pelo
                    tipos_pelo = contar_tipo(lista, "color_pelo")
                    mostrar_diccionario(tipos_pelo)
                
                case "19": #informar superhéroes tienen cada tipo de inteligencia
                    tipo_inteligencia = contar_tipo(lista, "inteligencia")
                    mostrar_diccionario(tipo_inteligencia)

                case "20": #lista héroes por color de ojos
                    listar_segun_tipo(lista, "color_ojos")

                case "21": #lista héroes por color de pelo
                    listar_segun_tipo(lista, "color_pelo")

                case "22": #lista héroes por tipo de inteligencia
                    listar_segun_tipo(lista, "inteligencia")

                case "23": #salir
                    print("¡Gracias por usar nuestro programa!")
                    break

                case _:
                    print("Opción no válida, por favor ingrese una opción correcta (1-23) \n")

            pausa()
            limpiar_pantalla()
    except ValueError as e:
        print(e)

formalizar_lista(lista_personajes)
iniciar(lista_personajes)
