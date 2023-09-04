import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def envio_email():
    with open('emails.txt', 'r') as f:
        data = f.read()
        f.close()
    data = data.split('\n')
    message = """<html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <style>
                            
                            .divEmail {
                                display: flex;
                                flex-direction: column;
                                gap: 5px;
                            }
                            
                        </style>
                    </head>
                    <body>
                        <h3><strong>¡Aumenta la productividad de tu negocio sin contratar más empleados! Descubre el poder de la Automatización Robótica de Procesos (RPA) con nuestros BOTS</strong></h3>

                        <p>¿Te imaginas automatizar esas tareas repetitivas y tediosas que consumen el tiempo de tus empleados? Con nuestros BOTS de RPA, tus empleados pueden enfocarse en tareas más estratégicas y productivas, generando así una mayor rentabilidad para tu negocio.</p>

                        <h5><strong>Beneficios de nuestros BOTS:</strong></h5>
                        <ul>
                        <li>Interacción eficiente con Excel.</li>
                        <li>Envío y recepción de correos electrónicos.</li>
                        <li>Extracción de información de páginas web, como precios de productos, de forma ágil y precisa.</li>
                        <li>Integración con SAP u otros programas internos.</li>
                        <li>Realización de cualquier tarea que no requiera creatividad.</li>
                        </ul>
                        <p>Recuerda que nuestros BOTS <strong>no se enferman, no generan problemas laborales y no cometen errores.</strong> Son una solución confiable y efectiva para optimizar tus procesos.</p>

                        <p>No esperes más para liberar el potencial de tu negocio. ¡Si se puede describir, se puede automatizar!</p>
                        <p>Contáctanos para una demostración gratuita y personalizada.</p>

                        <p>¡Impulsa la eficiencia de tu empresa con nuestros <strong>BOTS</strong> de <strong>RPA!</strong></p>
                        
                        <p>- Email enviado desde BOT Spicy -</p>
                        
                        <img src="https://res.cloudinary.com/powchorba/image/upload/v1690604377/robotize_ezgdfh.jpg"/>
                    </body>
                </html>"""
    for email in data:
        print(email)
        try:
            msg = EmailMessage()
            msg['From'] = 'rpa.robotize@gmail.com'
            msg['To'] = email
            msg['Subject'] = 'Servicios de RPA'
            msg.set_content(message, subtype="html")
            email = email.replace(' ', '')
            smt = smtplib.SMTP('smtp.gmail.com', 587)
            smt.ehlo()
            smt.starttls()
            smt.login('rpa.robotize@gmail.com', 'qffadbewojkbleer')
            smt.sendmail('rpa.robotize@gmail.com', email, msg.as_string())
            smt.quit()
        except:
            print('[-] Error en envio de email')    


envio_email()
# <p><strong>Email:</strong> <u>inakielhaiek@gmail.com</u> o <u>pow.chorba.99@gmail.com</u></p>
# <p><strong>Teléfono:</strong> 11 5098-9839 o 11 3435-9691</p>