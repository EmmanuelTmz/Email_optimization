# Optimización de Envío de Correos con Python

Este proyecto permite enviar correos electrónicos de forma eficiente utilizando Python. Se hace uso de una cola de tareas (con `schedule`) para enviar correos de manera programada, evitando sobrecargar el servidor de correo y asegurando que los correos sean enviados de manera controlada.

## Requisitos

- Python 3.x
- Gmail (u otro servidor SMTP)
- Librerías Python: `smtplib`, `email`, `schedule`, `python-dotenv`

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/optimizacion-envio-correos.git
cd optimizacion-envio-correos
