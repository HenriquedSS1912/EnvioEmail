from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


with open('template.html', 'r') as html:
    template = Template(html.read())
    data_now = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Henrique', data=data_now)

msg = MIMEMultipart()
msg['from'] = 'Herique da Silva'
msg['to'] = 'rike2807@gmail.com'
msg['subject'] = 'Atenção! Este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado...')
        print('Error: ', e)

    





