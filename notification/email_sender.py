from logzero import logger
import smtplib
import settings


class EmailSender(object):
    def __init__(self):
        self.gmail_user = settings.EMAIL_USER
        self.gmail_password = settings.EMAIL_PASSWORD
        self.to = settings.SEND_TO_SPLITTED_BY_COMMA.split(',')
        self.send_from = 'Job Listener'
        self.subject = 'Job Status Notificator'

    def send(self, id_job: str, status_job):
        text = f'Job de Id {id_job} foi atualizado para o status {status_job}'
        email_text = f"""\
        From: Job Listener
        To: {self.to}
        Subject: {self.subject}
        {text}
        """
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.gmail_user, self.to, email_text)
            server.close()
            logger.info(f'Email send for job {id_job} with status {status_job}')

        except Exception as e:
            logger.error(f'Error trying to send email for job {id_job} with status {status_job}')
            raise Exception(str(e))
