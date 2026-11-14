from modulos_almacenamiento import cargar_datos


def consultar_historia_clinica():
    datos = cargar_datos()

    identificacion = input(
        "Ingrese el número de identificación del paciente: "
    ).strip()

    pacientes = datos.get("pacientes", [])
    diagnosticos = datos.get("diagnosticos", [])

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente.get("identificacion") == identificacion:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("Error: no existe un paciente con esa identificación.")
        return

    print("\n" + "=" * 45)
    print("       HISTORIA CLÍNICA - CLÍNICA ACME")
    print("=" * 45)

    print(f"Identificación: {paciente_encontrado.get('identificacion', '')}")
    print(f"Nombres: {paciente_encontrado.get('nombres', '')}")
    print(f"Apellidos: {paciente_encontrado.get('apellidos', '')}")
    print(f"Teléfono: {paciente_encontrado.get('telefono', '')}")
    print(f"Correo: {paciente_encontrado.get('correo', '')}")
    print(f"Dirección: {paciente_encontrado.get('direccion', '')}")
    print(f"Género: {paciente_encontrado.get('genero', '')}")
    print(f"Estado civil: {paciente_encontrado.get('estado_civil', '')}")

    print("\nDIAGNÓSTICOS REGISTRADOS")
    print("-" * 45)

    encontrados = 0

    for diagnostico in diagnosticos:
        if diagnostico.get("identificacion_paciente") == identificacion:
            encontrados += 1
            print(f"\nDiagnóstico #{encontrados}")
            print(f"Fecha: {diagnostico.get('fecha', 'No registrada')}")
            print(f"Médico: {diagnostico.get('medico', 'No registrado')}")
            print(f"Descripción: {diagnostico.get('descripcion', '')}")
            print(f"Tratamiento: {diagnostico.get('tratamiento', '')}")

    if encontrados == 0:
        print("El paciente todavía no tiene diagnósticos registrados.")

    print("\n" + "=" * 45)