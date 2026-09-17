from database import conectar


def reporte_ventas():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                v.id_ventas,
                c.nombre,
                v.fecha,
                v.total
            FROM ventas v
            INNER JOIN clientes c
                ON v.id_cliente = c.id_cliente
            ORDER BY v.id_ventas DESC
        """)

        lista = cursor.fetchall()

        print("\n============================================================")
        print("                    REPORTE DE VENTAS")
        print("============================================================")

        if not lista:
            print("No hay ventas registradas.")
        else:
            for venta in lista:
                print(
                    f"Venta: {venta[0]} | "
                    f"Cliente: {venta[1]} | "
                    f"Fecha: {venta[2]} | "
                    f"Total: ${float(venta[3]):.2f}"
                )

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al generar reporte:", error)


def reporte_productos_stock():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                id_producto,
                nombre,
                categoria,
                precio,
                stock
            FROM productos
            ORDER BY stock ASC
        """)

        lista = cursor.fetchall()

        print("\n============================================================")
        print("                  REPORTE DE INVENTARIO")
        print("============================================================")

        if not lista:
            print("No hay productos registrados.")
        else:
            for producto in lista:
                print(
                    f"ID: {producto[0]} | "
                    f"Producto: {producto[1]} | "
                    f"Categoría: {producto[2]} | "
                    f"Precio: ${float(producto[3]):.2f} | "
                    f"Stock: {producto[4]}"
                )

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al generar inventario:", error)


def reporte_total_ventas():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(total), 0)
            FROM ventas
        """)

        resultado = cursor.fetchone()

        total = float(resultado[0])

        print("\n============================================================")
        print("                    TOTAL DE VENTAS")
        print("============================================================")

        print(f"Total vendido: ${total:.2f}")

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al calcular total:", error)


def menu_reportes():

    while True:

        print("\n============================================================")
        print("                       REPORTES")
        print("============================================================")

        print("1. Reporte de ventas")
        print("2. Reporte de inventario")
        print("3. Total vendido")
        print("4. Volver")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            reporte_ventas()

        elif opcion == "2":
            reporte_productos_stock()

        elif opcion == "3":
            reporte_total_ventas()

        elif opcion == "4":
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")