from modulos_almacenamiento import cargar_datos, guardar_datos

datos = cargar_datos()

print(datos)

guardar_datos(datos)

print("Los datos se guardaron correctamente.")