import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_TO = os.getenv("EMAIL_TO")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('monitor_chamados.log'), logging.StreamHandler()]
)

def enviar_alerta_email(alertas):
    if not alertas:
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = f"🚨 {len(alertas)} ALERTA(S) - Chamados Críticos"

        corpo = """
        <html>
            <head>
                <style>
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    .critico { background-color: #ffdddd; }
                    .header { background-color: #ff0000; color: white; padding: 10px; }
                </style>
            </head>
            <body>
                <div class="header">
                    <h2>ALERTA DE CHAMADOS CRÍTICOS</h2>
                </div>
                <p>Os seguintes chamados requerem atenção imediata:</p>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Local</th>
                        <th>Técnico</th>
                        <th>Situação</th>
                        <th>Gravidade</th>
                        <th>Ação Tomada</th>
                        <th>Motivo</th>
                    </tr>
        """

        for alerta in alertas:
            classe = "critico" if alerta["gravidade"] == "Grave" else ""
            corpo += f"""
            <tr class="{classe}">
                <td>{alerta['id']}</td>
                <td>{alerta['local']}</td>
                <td>{alerta['tecnico']}</td>
                <td>{alerta['situacao']}</td>
                <td>{alerta['gravidade']}</td>
                <td>{alerta['acao']}</td>
                <td>{alerta['motivo']}</td>
            </tr>
            """

        corpo += f"""
                </table>
                <p><strong>Data da verificação:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
                <p><a href="{os.getenv('API_URL')}">Acessar Dashboard</a></p>
            </body>
        </html>
        """

        msg.attach(MIMEText(corpo, 'html'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info(f"Email de alerta enviado com {len(alertas)} alerta(s)")
    except Exception as e:
        logging.error(f"Falha ao enviar email: {e}")