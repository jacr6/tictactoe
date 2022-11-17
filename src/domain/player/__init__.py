from ..game import *
from ..report import *


class PlayerDomain(object):
    def __init__(self, id):
        self.id = id
        pass

    def login(self, *args, **kwargs):
        pass

    def logout(self, *args, **kwargs):
        pass

    def buy_credits(self, *args, **kwargs):
        pass

    def register(self, *args, **kwargs):
        pass

    def unregister(self, *args, **kwargs):
        pass

    def forgot(self, *args, **kwargs):
        pass

    def join(self, *args, **kwargs):
        game_id = kwargs.get("game_id")
        self.game = GameDomain(self.id, game_id)
        self.game.join()
        pass

    def match(self, *args, **kwargs):
        pass

    def play(self, *args, **kwargs):
        pass

    def record(self, *args, **kwargs):
        pass

    def hello(self, *args, **kwargs):
        return "hello player"
