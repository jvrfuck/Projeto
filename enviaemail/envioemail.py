import smtplib
import ssl
from email.message import EmailMessage
import mysql.connector
from decouple import config

# Definir função de extração SQL
con = mysql.connector.connect(host=config("DBHOST"),
                            database=config("DBNAME"),
                            user=config("DBNAME"),
                            password=config("DBPASSWORD"))

cur = con.cursor()
sql_select_query = "SELECT pessoa_email FROM app1_pessoas WHERE id=(SELECT max(id) FROM app1_pessoas);"
cur.execute(sql_select_query)
destinatario = cur.fetchone()


# Define email sender and receiver
email_sender = config("EADRRESS")
email_password = config("EPASSWORD")
email_receiver = destinatario

# Set the subject and body of the email
subject = 'olhe seu NOVO AGENDAMENTO'
body = """

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