from multiprocessing import Process
from app.models import *
from domain.infra import *


class GameDomain(object):
    def __init__(self, *args):
        player = args
        self.game = Game()
        self.id = self.game
        self.player = player
        self.infra = InfraDomain(id)
        self.players = Game.where(id=id)
        pass

    def join(self, *args, **kwargs):
        if self.match():
            self.play()
        pass

    def match(self):
        return len(self.players) == 2

    def play(self, *args, **kwargs):
        Process(target=self.get_table_state).start()
        pass

    def get_table_state(self):
        while True:
            res = self.validate_two_players()
            res = self.get_table()
            res = self.record()
            res = self.check_winner(res)
            pass

    def record(self):
        pass

    def validate_two_players(self):
        res = self.validate_order()
        if res:
            return True
        return False

    def validate_order(self):
        return True

    def do_move(self, player, coordinate):
        game_detail = GameDetail()
        pass

    def get_table(self):
        pass
