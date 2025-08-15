from flask import Flask, request, render_template, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Configuración del servidor de correo (ejemplo con Gmail)
# Es recomendable usar variables de entorno para credenciales
EMAIL_ADDRESS = 'tu_correo@gmail.com'
EMAIL_PASSWORD = 'tu_contraseña'

@app.route('/')
def index():
    return render_template('index.html')  # Muestra index.html en la página principal

@app.route('/contacto')  # Nueva ruta para el formulario de contacto
def contacto():
    return render_template('contacto.html')  # Muestra contacto.html

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email_remitente = request.form['email']
        mensaje_recibido = request.form['mensaje']

        # Crear el mensaje de correo electrónico
        msg = MIMEText(f"Nombre: {nombre}\nEmail: {email_remitente}\nMensaje: {mensaje_recibido}")
        msg['Subject'] = 'Nuevo Mensaje desde Formulario Web'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'tu_correo_destino@ejemplo.com' # El correo que recibirá el mensaje

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, 'tu_correo_destino@ejemplo.com', msg.as_string())
            # Redirigir a la página de contacto después de enviar el correo
            return redirect(url_for('contacto'))  # Redirige a la página de contacto
        except Exception as e:
            # Manejar el error (puedes mostrar un mensaje de error en la página de contacto)
            return f'Error al enviar el correo: {e}'
