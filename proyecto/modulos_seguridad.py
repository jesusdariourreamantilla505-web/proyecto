from modulos_almacenamiento import cargar_datos


def iniciar_sesion():
    print("\n---------- INICIAR SESIÓN ----------")

    correo = input("Correo electrónico: ")
    contrasena = input("Contraseña: ")

    datos = cargar_datos()

    for usuario in datos["usuarios"]:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            print("Bienvenido", usuario["nombres"])
            return usuario

    print("Correo o contraseña incorrectos")
    return None