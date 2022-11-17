from ..game import *
from ..report import *


class PlayerDomain(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self, id):
        """_summary_

        Args:
            id (_type_): _description_
        """        
        self.id = id
        pass 

    def buy_credits(self, *args, **kwargs):
        """_summary_
        """        
        pass
 
    def join(self, *args, **kwargs):
        """_summary_
        """        
        game_id = kwargs.get("game_id")
        self.game = GameDomain(self.id, game_id)
        self.game.join()
        pass
 
    def play(self, *args, **kwargs):
        """_summary_
        """        
        pass
 
    def hello(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return "hello player"
