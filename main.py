from validaciones import *
from funciones_genericas import *
from data_stark import lista_personajes
from funciones_stark import *


def iniciar(lista_personajes: list) -> None:
    while True:
        limpiar_pantalla()
        try:
            opcion = menu()
            match opcion:
                case "1":
                    nombres_superheroes(lista_personajes)
                case "2":
                    nombre_altura_todos(lista_personajes)
                case "3":
                    altura_maxima = heroe_mas_alto(lista_personajes)
                    imprimir_heroe_mas_alto(altura_maxima)
                    pausa()
                case "4":
                    heroe_mas_bajo(lista_personajes)
                case "5":
                    altura_promedio(lista_personajes)
                    print(f"La altura promedio de todos los héroes es: {altura_promedio:.2f}")
                case "6":
                    informar_bajo_alto(lista_personajes)
                case "7":
                    informar_liviano_pesado(lista_personajes)
                case "8":
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opción no válida, por favor ingrese una opción correcta.")
            continuar = input ("Presione enter para continuar...")
            system ("cls")
        except Exception as e:
            print(e)

formalizar_lista(lista_personajes)
iniciar(lista_personajes)
