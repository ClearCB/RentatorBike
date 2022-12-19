import os
# Este modulo se va a encargar de crear el archivo demandado en la ruta especificada.

# Pasandole estos parámetros, conseguimos que cree un archivo con la información especificada.

def crearArchivo(contenido, ruta, nombre, tipo):

    ruta = os.path.relpath(ruta) # Definimos la ruta relativa 
    try:
        with open(f"{ruta}\\{nombre}.{tipo}","w", encoding="utf-8") as archivo: # Le asignamos los parametros detallados, creamos el archivo
            archivo.write(contenido) # Escribimos el contenido en el archivo
            print(f"El archivo '{nombre}.{tipo}' creado correctamente.")
    except FileNotFoundError: # Captamos una excepción en caso de que no encuentre el directorio.
        print("El directorio no existe, ejecuta correctamente el programa y vuelve a intentarlo.")
        return False