from modulos_almacenamiento import cargar_datos, guardar_datos


def registrar_usuario():
    print("\n========== REGISTRO DE USUARIO ==========")

    datos = cargar_datos()
    datos.setdefault("usuarios", [])

    identificacion = input(
        "Número de identificación: "
    ).strip()

    if not identificacion:
        print("Error: la identificación es obligatoria.")
        return

    for usuario in datos["usuarios"]:
        if usuario.get("identificacion") == identificacion:
            print("Ya existe un usuario con esa identificación.")
            return

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico corporativo: ").strip()
    direccion = input("Dirección: ").strip()

    for usuario in datos["usuarios"]:
        if usuario.get("correo", "").lower() == correo.lower():
            print("Ese correo ya está registrado.")
            return

    rol = input(
        "Rol (Medico/Administrativo): "
    ).strip().lower()

    if rol == "medico":
        rol = "Medico"
    elif rol == "administrativo":
        rol = "Administrativo"
    else:
        print("Error: el rol debe ser Medico o Administrativo.")
        return

    contrasena = input("Contraseña: ").strip()

    if not all([
        nombres,
        apellidos,
        telefono,
        correo,
        direccion,
        contrasena
    ]):
        print("Error: todos los campos son obligatorios.")
        return

    nuevo_usuario = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "rol": rol,
        "contrasena": contrasena
    }

    datos["usuarios"].append(nuevo_usuario)
    guardar_datos(datos)

    print("\nUsuario registrado correctamente.")
    print("Nombre:", nombres, apellidos)
    print("Rol:", rol)
    print("Correo para iniciar sesión:", correo)