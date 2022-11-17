from domain.infraAdapter.email import EmailInfra
from domain.infraAdapter.event import EventInfra
from domain.infraAdapter.log import LogInfra
import infra.models as models

class InfraDomain(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self) -> None:
        self.email = EmailInfra()
        self.event = EventInfra()
        self.logs = LogInfra()
        self.models = models
        pass