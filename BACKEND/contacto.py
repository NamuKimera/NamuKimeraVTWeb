from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('Sitios Web\NamuKimeraVTWeb\Contacto.html', methods=['post'])
def contacto():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    mensaje = data.get('mensaje')

    if not all([nombre, email, mensaje]):
        return jsonify({'success': False, 'message': 'Todos los campos son requeridos'}), 400

    success, message = enviar_email(nombre, email, mensaje)
    if success:
        return jsonify({'success': True, 'message': message}), 200
    else:
        return jsonify({'success': False, 'message': message}), 500

if __name__ == '__main__':
    app.run(debug=True)
