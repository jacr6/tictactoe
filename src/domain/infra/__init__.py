from domain.infra.email import EmailInfra
from domain.infra.event import EventInfra
from domain.infra.log import LogInfra


class InfraDomain(object):
    def __init__(self) -> None:
        self.email = EmailInfra()
        self.event = EventInfra()
        self.logs = LogInfra()
        pass