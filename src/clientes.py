from database import conectar


def mostrar_clientes():

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes")
        lista = cursor.fetchall()

        print("\n============================================================")
        print("                    LISTA DE CLIENTES")
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


def registrar_cliente():

    print("\n============================================================")
    print("                  REGISTRAR CLIENTE")
    print("============================================================")

    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo electrónico: ").strip()

    if not nombre or not telefono or not email:
        print("\n❌ Todos los campos son obligatorios.")
        return

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO clientes
            (nombre, telefono, email)
            VALUES (%s, %s, %s)
        """

        valores = (nombre, telefono, email)

        cursor.execute(sql, valores)
        conexion.commit()

        print("\n✅ Cliente registrado correctamente.")

        cursor.close()
        conexion.close()

    except Exception as error:
        print("\n❌ Error al registrar cliente:", error)


def menu_clientes():

    while True:

        print("\n============================================================")
        print("                    GESTIÓN DE CLIENTES")
        print("============================================================")

        print("1. Ver clientes")
        print("2. Registrar cliente")
        print("3. Volver")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_clientes()

        elif opcion == "2":
            registrar_cliente()

        elif opcion == "3":
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")