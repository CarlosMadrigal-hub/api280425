from flask import Flask, request, jsonify, render_template
from hillClimbing import hill_climbing, evalua_ruta

app = Flask(__name__)

# Coordenadas de las ciudades
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener un archivo index.html en la carpeta templates

# Ruta para calcular la ruta óptima
@app.route('/ruta', methods=['GET'])
def obtener_ruta():
    # Obtener la ciudad inicial desde los parámetros de la solicitud
    ciudad_inicial = request.args.get('ciudad_inicial')
    print(f"Ciudad inicial recibida: {ciudad_inicial}")  # Depuración
    
    # Validar si se proporcionó la ciudad inicial
    if not ciudad_inicial:
        return jsonify({"error": "Debe proporcionar una ciudad inicial"}), 400

    # Validar si la ciudad inicial existe en las coordenadas
    if ciudad_inicial not in coord:
        return jsonify({"error": "La ciudad inicial no es válida"}), 400

    try:
        # Calcular la ruta óptima y la distancia total
        ruta = hill_climbing(coord, ciudad_inicial)
        distancia_total = evalua_ruta(ruta, coord)
        print(f"Ruta calculada: {ruta}")  # Depuración
        print(f"Distancia total: {distancia_total}")  # Depuración
    except Exception as e:
        print(f"Error: {e}")  # Depuración
        return jsonify({"error": str(e)}), 500

    # Devolver los datos en formato JSON
    return jsonify({
        "ruta_optima": ruta,
        "distancia_total": distancia_total
    })

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)