from flask import Flask, jsonify, abort
from flask import make_response, request, url_for
import acesso

app = Flask(__name__)

'''
Esse arquivo contém uma funcao de envio de email.

A idéia é transformá-lo em um servidor, 
como os servidores controle_pessoas
e forum. Ele deve atender na porta 5051.

Ele deve ter um endpoint /mail/enviar/
que recebe um request do tipo POST,
com um JSON de 3 campos:
    to: uma lista de IDs de usuários
    subject: uma string de assunto
    texto: o texto da mensagem

Entao, ele consulta o servidor controle_pessoas,
para determinar os emails dessas pessoas,
e envia a mensagem.

Por ultimo, ele retorna o resultado, que pode ser
{response: True}
ou 
{response: False} e o erro,
que pode ser relativo ao servidor de email nao responder,
a um email ser invalido
ao servidor controle_pessoas nao responder
ou
ao servidor controle_pessoas nao ter achado uma ID
'''

'''
Esse codigo inicializa a conexao ao servico de email do google

Voce deve criar um email do gmail para completar os dados

Voce provavelmente tera problemas com acessar o gmail,
e eles serao resolvidos quando voce permitir acesso a
"aplicacoes inseguras", porque nosso cliente de email 
é meio tosquinho
'''
import smtplib
from email.message import EmailMessage
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("testeemailflask", "SenhaSegura")
'''
Essa funcao é um exemplo simplificado, e deverá ser alterada
'''

@app.route('/mail/enviar/<destinatario>', methods=['POST'])
def envia(destinatario):
    emails = request.get('to', None)
    #emails = acesso.retorna_email()
    msg = EmailMessage()
    msg.set_content('Esse eh um teste de email, enviado depois das 22h15')
    msg['Subject'] = 'Esse eh um teste de email'
    msg['From'] = 'testeemailflask'
    msg['To'] = "vic12hugo@hotmail.com"
    server.send_message(msg)
#    server.sendmail('testeemailflask',"vic12hugo@hotmail.com",msg.as_string())

    return "Message sent"

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=5051)

