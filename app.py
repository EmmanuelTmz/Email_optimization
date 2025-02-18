import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from jinja2 import Template

# Cargar variables de entorno
load_dotenv()

def enviar_correo(destinatario, asunto, cuerpo):
    # Obtener credenciales del archivo .env
    remitente = os.getenv("EMAIL_USER")
    contrasena = os.getenv("EMAIL_PASS")
    
    # Configuración del servidor SMTP (Ejemplo con Gmail)
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    
    try:
        # Leer la plantilla HTML
        with open("templates/email_template.html", "r") as f:
            template_html = f.read()
        
        # Renderizar el HTML con Jinja2
        template = Template(template_html)
        contenido_html = template.render(asunto=asunto, cuerpo=cuerpo)
        
        # Crear mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(contenido_html, 'html'))

        # Conectar al servidor y enviar el correo
        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()  # Activar la encriptación
            servidor.login(remitente, contrasena)
            servidor.sendmail(remitente, destinatario, mensaje.as_string())
    except Exception as e:
        raise Exception(f"Error al enviar el correo: {str(e)}")
