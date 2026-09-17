from clientes import menu_clientes
from productos import menu_productos
from ventas import menu_ventas
from reportes import menu_reportes


def main():

    while True:

        print("\n============================================================")
        print("             SISTEMA DE GESTIÓN DE VENTAS")
        print("============================================================")

        print("1. Gestión de clientes")
        print("2. Gestión de productos")
        print("3. Gestión de ventas")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            menu_productos()

        elif opcion == "3":
            menu_ventas()

        elif opcion == "4":
            menu_reportes()

        elif opcion == "5":
            print("\nPrograma finalizado.")
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()