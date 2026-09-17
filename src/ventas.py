from database import conectar


def mostrar_ventas():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM ventas")
        lista = cursor.fetchall()

        print("\n============================================================")
        print("                       LISTA DE VENTAS")
        print("============================================================")

        if not lista:
            print("No hay ventas registradas.")
        else:
            for venta in lista:
                print(
                    f"ID Venta: {venta[0]} | "
                    f"ID Cliente: {venta[1]} | "
                    f"Fecha: {venta[2]} | "
                    f"Total: ${float(venta[3]):.2f}"
                )

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al mostrar ventas:", error)


def mostrar_clientes():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes")
        lista = cursor.fetchall()

        print("\n============================================================")
        print("                       CLIENTES")
        print("============================================================")

        if not lista:
            print("No hay clientes registrados.")
        else:
            for cliente in lista:
                print(
                    f"ID: {cliente[0]} | "
                    f"Nombre: {cliente[1]} | "
                    f"Teléfono: {cliente[2]} | "
                    f"Correo: {cliente[3]}"
                )

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al mostrar clientes:", error)


def mostrar_productos():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        lista = cursor.fetchall()

        print("\n============================================================")
        print("                       PRODUCTOS")
        print("============================================================")

        if not lista:
            print("No hay productos registrados.")
        else:
            for producto in lista:
                print(
                    f"ID: {producto[0]} | "
                    f"Nombre: {producto[1]} | "
                    f"Categoría: {producto[2]} | "
                    f"Precio: ${float(producto[3]):.2f} | "
                    f"Stock: {producto[4]}"
                )

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al mostrar productos:", error)


def registrar_venta():

    print("\n============================================================")
    print("                    REGISTRAR VENTA")
    print("============================================================")

    mostrar_clientes()

    try:
        id_cliente = int(input("\nID del cliente: "))

    except ValueError:
        print("\n❌ ID de cliente inválido.")
        return

    conexion = None
    cursor = None

    try:

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT id_cliente
            FROM clientes
            WHERE id_cliente = %s
            """,
            (id_cliente,)
        )

        cliente = cursor.fetchone()

        if cliente is None:
            print("\n❌ No existe ese cliente.")
            return

        carrito = []
        total = 0

        while True:

            mostrar_productos()

            try:
                id_producto = int(
                    input("\nID del producto (0 para terminar): ")
                )

            except ValueError:
                print("\n❌ ID de producto inválido.")
                continue

            if id_producto == 0:
                break

            try:
                cantidad = int(input("Cantidad: "))

            except ValueError:
                print("\n❌ La cantidad debe ser un número entero.")
                continue

            if cantidad <= 0:
                print("\n❌ La cantidad debe ser mayor que cero.")
                continue

            cursor.execute(
                """
                SELECT nombre, precio, stock
                FROM productos
                WHERE id_producto = %s
                """,
                (id_producto,)
            )

            producto = cursor.fetchone()

            if producto is None:
                print("\n❌ No existe ese producto.")
                continue

            nombre = producto[0]
            precio = float(producto[1])
            stock = producto[2]

            if cantidad > stock:
                print(
                    f"\n❌ Stock insuficiente. "
                    f"Disponible: {stock}"
                )
                continue

            subtotal = precio * cantidad

            carrito.append({
                "id_producto": id_producto,
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            })

            total += subtotal

            print(
                f"\n✅ {nombre} agregado correctamente."
            )

            print(f"Subtotal: ${subtotal:.2f}")

            continuar = input(
                "\n¿Agregar otro producto? (s/n): "
            )

            if continuar.lower() != "s":
                break

        if not carrito:
            print("\n❌ No se agregaron productos.")
            return

        print("\n============================================================")
        print("                    RESUMEN DE VENTA")
        print("============================================================")

        for item in carrito:
            print(
                f"{item['nombre']} | "
                f"Cantidad: {item['cantidad']} | "
                f"Precio: ${item['precio']:.2f} | "
                f"Subtotal: ${item['subtotal']:.2f}"
            )

        print("------------------------------------------------------------")
        print(f"TOTAL: ${total:.2f}")

        confirmar = input(
            "\n¿Guardar esta venta? (s/n): "
        )

        if confirmar.lower() != "s":
            print("\nVenta cancelada.")
            return

        # Crear venta
        cursor.execute(
            """
            INSERT INTO ventas
            (id_cliente, fecha, total)
            VALUES (%s, NOW(), %s)
            """,
            (id_cliente, total)
        )

        id_venta = cursor.lastrowid

        # Registrar productos
        for item in carrito:

            cursor.execute(
                """
                INSERT INTO detalle_venta
                (id_venta, id_producto, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    id_venta,
                    item["id_producto"],
                    item["cantidad"],
                    item["precio"]
                )
            )

            cursor.execute(
                """
                UPDATE productos
                SET stock = stock - %s
                WHERE id_producto = %s
                """,
                (
                    item["cantidad"],
                    item["id_producto"]
                )
            )

        conexion.commit()

        print("\n============================================================")
        print("                  VENTA REGISTRADA")
        print("============================================================")

        print(f"ID de venta: {id_venta}")
        print(f"Total: ${total:.2f}")

    except Exception as error:

        if conexion:
            conexion.rollback()

        print("\n❌ Ocurrió un error al registrar la venta.")
        print("Detalle:", error)

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def menu_ventas():

    while True:

        print("\n============================================================")
        print("                       GESTIÓN DE VENTAS")
        print("============================================================")

        print("1. Ver ventas")
        print("2. Registrar venta")
        print("3. Volver")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_ventas()

        elif opcion == "2":
            registrar_venta()

        elif opcion == "3":
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")