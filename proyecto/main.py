from modulos_almacenamiento import cargar_datos, guardar_datos
from modulos_usuario import registrar_usuario
from modulos_seguridad import iniciar_sesion
from modulos_diagnostico import registrar_diagnostico
from modulos_historia_clinica import consultar_historia_clinica


def registrar_paciente():
    datos = cargar_datos()

    identificacion = input("Número de identificación: ").strip()
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()
    direccion = input("Dirección: ").strip()
    genero = input("Género: ").strip()
    estado_civil = input("Estado civil: ").strip()

    if not all([
        identificacion,
        nombres,
        apellidos,
        telefono,
        correo,
        direccion,
        genero,
        estado_civil
    ]):
        print("Error: todos los campos son obligatorios.")
        return

    datos.setdefault("pacientes", [])

    for paciente in datos["pacientes"]:
        if paciente.get("identificacion") == identificacion:
            print("Error: ya existe un paciente con esa identificación.")
            return

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

    print("Paciente registrado correctamente.")


def menu_principal(usuario):
    while True:
        rol = usuario.get("rol", "").strip().lower()

        print("\n" + "=" * 40)
        print("          CLÍNICA ACME")
        print("          MENÚ PRINCIPAL")
        print("=" * 40)
        print(f"Usuario conectado: {usuario.get('nombres', '')}")
        print(f"Rol: {rol.capitalize()}")
        print()

        if rol == "medico":
            print("1. Registrar diagnóstico")
            print("2. Consultar historia clínica")
            print("3. Cerrar sesión")

        elif rol == "administrativo":
            print("1. Registrar usuario")
            print("2. Registrar paciente")
            print("3. Registrar diagnóstico")
            print("4. Consultar historia clínica")
            print("5. Cerrar sesión")

        else:
            print("Error: el usuario no tiene un rol válido.")
            break

        print("=" * 40)
        opcion = input("Seleccione una opción: ").strip()

        if rol == "medico":
            if opcion == "1":
                registrar_diagnostico()

            elif opcion == "2":
                consultar_historia_clinica()

            elif opcion == "3":
                print("Sesión cerrada correctamente.")
                break

            else:
                print("Opción no válida. Intente nuevamente.")

        elif rol == "administrativo":
            if opcion == "1":
                registrar_usuario()
            elif opcion == "2":
                registrar_paciente()
            elif opcion == "3":
                print("La función de registrar diagnósticos está pendiente de integración.")
            elif opcion == "4":
                print("La consulta de historias clínicas está pendiente de integración.")
            elif opcion == "5":
                print("Sesión cerrada correctamente.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


def main():
    print("=" * 40)
    print("       BIENVENIDO A CLÍNICA ACME")
    print("=" * 40)

    while True:
        print("\nINICIO DE SESIÓN")

        usuario = iniciar_sesion()

        if usuario:
            menu_principal(usuario)
        else:
            print("Inicio de sesión fallido.")

        respuesta = input(
            "\n¿Desea intentar iniciar sesión nuevamente? (s/n): "
        ).strip().lower()

        if respuesta != "s":
            print("Gracias por utilizar Clínica ACME.")
            break


if __name__ == "__main__":
    main()