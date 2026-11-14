from datetime import datetime

from modulos_almacenamiento import cargar_datos, guardar_datos


def registrar_diagnostico():
    print("\n========== REGISTRAR DIAGNÓSTICO ==========")

    datos = cargar_datos()

    datos.setdefault("pacientes", [])
    datos.setdefault("diagnosticos", [])

    identificacion = input(
        "Número de identificación del paciente: "
    ).strip()

    paciente_encontrado = None

    for paciente in datos["pacientes"]:
        if paciente.get("identificacion") == identificacion:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("Error: no existe un paciente con esa identificación.")
        return

    nombres = paciente_encontrado.get("nombres", "")
    apellidos = paciente_encontrado.get("apellidos", "")

    print(f"\nPaciente: {nombres} {apellidos}")

    descripcion = input(
        "Descripción del diagnóstico: "
    ).strip()

    if not descripcion:
        print("Error: la descripción del diagnóstico es obligatoria.")
        return

    tratamiento = input(
        "Tratamiento recomendado: "
    ).strip()

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nuevo_diagnostico = {
        "identificacion_paciente": identificacion,
        "fecha": fecha_actual,
        "descripcion": descripcion,
        "tratamiento": tratamiento
    }

    datos["diagnosticos"].append(nuevo_diagnostico)

    guardar_datos(datos)

    print("\nDiagnóstico registrado correctamente.")