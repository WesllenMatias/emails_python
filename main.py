from imapclient import IMAPClient
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

localizar()