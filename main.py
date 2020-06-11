from imapclient import IMAPClient
from smtplib import *
import config
import pprint


def localizar():
    conn = IMAPClient(config.end_imap , use_uid=True)
    conn.login(config.user, config.passwd)    
    buscar = input('Digite o assunto do e-mail que deve ser Localizado? ')
    conn.select_folder('INBOX', readonly=True)
    pesquisa = conn.search('SUBJECT %s' % (buscar))
    resultado = conn.fetch(pesquisa, ['BODY[]'])
    pprint.pprint(resultado)
    conn.logout()

#localizar()

def enviar_email():
    assunto = input('Digite o Assunto do E-mail:')
    destinatario = input('Informe o e-mail Destino da Mensagem:')
    mensagem = input('Digite a Mensagem:')
    assunto_msg = 'Subject:'+ assunto
    msg = assunto_msg + '\n'+ mensagem
    smtpObj = SMTP(config.valor_smtp,config.porta)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(config.user,config.passwd)
    smtpObj.sendmail(config.user,destinatario,msg)
    smtpObj.quit()
    print('Mensagem enviada com sucesso!')

enviar_email()