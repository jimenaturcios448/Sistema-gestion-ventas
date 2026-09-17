from database import conectar


def mostrar_productos():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")
        lista = cursor.fetchall()

        print("\n============================================================")
        print("                    LISTA DE PRODUCTOS")
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


def registrar_producto():

    print("\n============================================================")
    print("                  REGISTRAR PRODUCTO")
    print("============================================================")

    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría: ").strip()

    if not nombre or not categoria:
        print("\n❌ Nombre y categoría son obligatorios.")
        return

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

    except ValueError:
        print("\n❌ Precio o stock inválido.")
        return

    if precio < 0:
        print("\n❌ El precio no puede ser negativo.")
        return

    if stock < 0:
        print("\n❌ El stock no puede ser negativo.")
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO productos
            (nombre, categoria, precio, stock)
            VALUES (%s, %s, %s, %s)
        """

        valores = (nombre, categoria, precio, stock)

        cursor.execute(sql, valores)
        conexion.commit()

        print("\n✅ Producto registrado correctamente.")

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al registrar producto:", error)


def actualizar_producto():

    mostrar_productos()

    try:
        id_producto = int(
            input("\nID del producto que deseas actualizar: ")
        )

    except ValueError:
        print("\n❌ ID inválido.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    if not nombre or not categoria:
        print("\n❌ Nombre y categoría son obligatorios.")
        return

    try:
        precio = float(input("Nuevo precio: "))
        stock = int(input("Nuevo stock: "))

    except ValueError:
        print("\n❌ Precio o stock inválido.")
        return

    if precio < 0 or stock < 0:
        print("\n❌ Precio y stock no pueden ser negativos.")
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
            UPDATE productos
            SET nombre = %s,
                categoria = %s,
                precio = %s,
                stock = %s
            WHERE id_producto = %s
        """

        valores = (
            nombre,
            categoria,
            precio,
            stock,
            id_producto
        )

        cursor.execute(sql, valores)
        conexion.commit()

        if cursor.rowcount > 0:
            print("\n✅ Producto actualizado correctamente.")
        else:
            print("\n❌ No se encontró ese producto.")

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al actualizar producto:", error)


def eliminar_producto():

    mostrar_productos()

    try:
        id_producto = int(
            input("\nID del producto que deseas eliminar: ")
        )

    except ValueError:
        print("\n❌ ID inválido.")
        return

    confirmar = input(
        "\n¿Seguro que deseas eliminar este producto? (s/n): "
    )

    if confirmar.lower() != "s":
        print("\nEliminación cancelada.")
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
            DELETE FROM productos
            WHERE id_producto = %s
        """

        cursor.execute(sql, (id_producto,))
        conexion.commit()

        if cursor.rowcount > 0:
            print("\n✅ Producto eliminado correctamente.")
        else:
            print("\n❌ No se encontró ese producto.")

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ No se puede eliminar el producto.")
        print("Puede estar relacionado con una venta.")
        print("Detalle:", error)


def menu_productos():

    while True:

        print("\n============================================================")
        print("                    GESTIÓN DE PRODUCTOS")
        print("============================================================")

        print("1. Ver productos")
        print("2. Registrar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Volver")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            registrar_producto()

        elif opcion == "3":
            actualizar_producto()

        elif opcion == "4":
            eliminar_producto()

        elif opcion == "5":
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")