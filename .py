def hex_to_rgb(hex_color):
    # Elimina el símbolo "#" si está presente en el valor hexadecimal
    hex_color = hex_color.lstrip('#')

    # Convierte el valor hexadecimal a valores RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return (r, g, b)

# Solicita un valor hexadecimal al usuario
hex_color = input("Introduce un valor hexadecimal (por ejemplo, #FF00FF): ")

# Verifica si el valor hexadecimal es válido
if len(hex_color) == 7 and hex_color[0] == '#':
    try:
        rgb_values = hex_to_rgb(hex_color)
        print("Valores RGB:", rgb_values)
    except ValueError:
        print("El valor hexadecimal introducido no es válido.")
else:
    print("Por favor, introduce un valor hexadecimal válido en el formato #RRGGBB.")
