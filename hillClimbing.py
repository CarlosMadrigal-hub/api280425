import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    # Validar que todas las ciudades en la ruta existan en coord
    for ciudad in ruta:
        if ciudad not in coord:
            raise ValueError(f"La ciudad '{ciudad}' no existe en las coordenadas proporcionadas.")
    
    # Calcular la distancia total de la ruta
    total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    # Añadir la distancia de regreso al punto inicial
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def hill_climbing(coord, ciudad_origen):
    # Validar que la ciudad inicial exista en coord
    if ciudad_origen not in coord:
        raise ValueError(f"La ciudad inicial '{ciudad_origen}' no existe en las coordenadas proporcionadas.")
    
    # Validar que haya al menos dos ciudades para calcular una ruta
    if len(coord) < 2:
        raise ValueError("Debe haber al menos dos ciudades en las coordenadas para calcular una ruta.")
    
    # Crear la ruta inicial aleatoria
    ruta = list(coord.keys())
    ruta.remove(ciudad_origen)
    random.shuffle(ruta)
    ruta.insert(0, ciudad_origen)  # Asegurar que la ciudad de origen sea la primera

    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta, coord)
        for i in range(1, len(ruta)):  # No intercambiar la ciudad de origen
            if mejora:
                break
            for j in range(1, len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_ruta(ruta_tmp, coord)
                    if dist < dist_actual:
                        mejora = True
                        ruta = ruta_tmp[:]
                        break
    return ruta