from infra.mailsender import MailSender


class EmailInfra(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self) -> None:
        """_summary_
        """
        self.mail_sender = MailSender()        
        pass
    def send(self, guest, id):
        """_summary_

        Args:
            guest (_type_): _description_
            id (_type_): _description_
        """
        self.mail_sender.send_email("text")        
        pass