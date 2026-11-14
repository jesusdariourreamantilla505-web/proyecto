from modulos_almacenamiento import cargar_datos, guardar_datos


def registrar_paciente():
    print("\n////////// REGISTRO DE PACIENTE //////////")

    datos = cargar_datos()

    identificacion = input("Número de identificación: ")

    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("El paciente ya está registrado")
            return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Número de teléfono: ")
    correo = input("Correo electrónico: ")
    direccion = input("Dirección: ")
    genero = input("Género: ")
    estado_civil = input("Estado civil: ")

    nuevo_paciente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo_paciente)

    guardar_datos(datos)

    print("Paciente registrado correctamente")