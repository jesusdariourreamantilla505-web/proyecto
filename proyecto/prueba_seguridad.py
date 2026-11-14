from modulos_seguridad import iniciar_sesion

usuario = iniciar_sesion()

if usuario is not None:
    print("Acceso permitido")
    print("Nombre:", usuario["nombres"])
    print("Rol:", usuario["rol"])
else:
    print("Acceso denegado")