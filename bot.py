import smtplib
from email.mime.text import MIMEText

from PyQt5.QtWidgets import *
from PyQt5 import uic



# variaveis fixas
sender = 'sender_email'
#email_list = []
#subject = 'Email Subject'
#message = 'Mensagem de test'
#body = 'Isto é apenas um teste para enviar um email. \n Para testar um bot. \n Escrito por:\n Bernardo Mamede \n Motcho inc.'


# email sender
#def bot_email():
#    msg = MIMEText(body)
#    msg['Subject'] = subject
#    msg['From'] = sender
    
    
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.starttls()
#    server.login(sender, 'znlzuluxvthmmcto')
    

#    for mail in email_list:
#        server.sendmail(sender, mail, msg.as_string())


class MyGUI(QMainWindow):
    
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('UI_mail_bot.ui', self)
        self.show()

        self.send.clicked.connect(self.get_email_values)

    
    def get_email_values(self):
        email_list_str = self.email_list.toPlainText()
        subject = self.subject.toPlainText()
        body = self.body.toPlainText()

        email_list = [email.strip() for email in email_list_str.split(',')]

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
    
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, 'need_code_from_gmail_app_passwords')
    

        for mail in email_list:
            server.sendmail(sender, mail, msg.as_string())


            print('User Input:', email_list, subject, body)




#pyqt5 app
def main():
    #inicializar app
    app = QApplication([])
    # propriedades de janela
    window = MyGUI()
    app.exec_()




if __name__ == '__main__':
    main()



