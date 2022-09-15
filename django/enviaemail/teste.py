import smtplib
import ssl
from email.message import EmailMessage
import mysql.connector

# Definir função de extração SQL
con = mysql.connector.connect(host='3.89.36.150',
                            database='pye2122g1',
                            user='pye2122g1',
                            password='pye2122g1@25@ago')

cur = con.cursor()
sql_select_query = "SELECT pessoa_email FROM app1_pessoas WHERE id=(SELECT max(id) FROM app1_pessoas);"
cur.execute(sql_select_query)
destinatario = cur.fetchone()


# Define email sender and receiver
email_sender = "agendaieletronica@gmail.com"
email_password = "comyryethrahyexh"
email_receiver = destinatario

# Set the subject and body of the email
subject = 'Cadastro Confirmad0'
body = """

PARABÉNS, SEU CADASTRO FOI REALIZADO COM SUCESSO!

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())