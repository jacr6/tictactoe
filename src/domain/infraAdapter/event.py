from infra.consumer import Consumer
from infra.publisher import Publisher


class EventInfra(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self) -> None:
        """_summary_
        """        
        self.consumer = Consumer()
        self.publisher = Publisher()
        
    def notify(self, msg):
        """_summary_
        """        
        self.publisher.publish(msg)