import smtplib
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'server'
smtp_ssl_port = port server
# username ou email para logar no servidor
username = 'your username'
password = 'your password'

from_addr = 'your email address'
to_addrs = ['the email who you want to send']

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEText('Esta é uma mensagem teste do Python.')
message['subject'] = 'Mensagem teste'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()