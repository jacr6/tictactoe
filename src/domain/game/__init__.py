from multiprocessing import Process
from random import randint
from app.models import *
from domain.infra import *
import uuid


class GameDomain(object):
    def __init__(self, player):
        self.started = False
        self.infra = InfraDomain(id)
        self.app_label = ""
        self.owner = player
        self.players = [player]
        self.id = uuid.uuid1()
        self.combinations = [
            "123",
            "456",
            "789",
            "159",
            "357",
            "147",
            "258",
            "369"
        ]

    def join(self, uuid):
        if uuid == self.id:
            if self.match():
                self.play()
        pass

    def match(self):
        return len(self.players) == 2

    def play(self):
        self.started = True
        Process(target=self.game_start).start()

    def game_start(self):
        while self.started:
            res = self.validate_two_players()
            res = self.get_table()
            res = self.check_winner(res)

    def validate_two_players(self):
        res = self.validate_order()
        if res:
            return True
        return False

    def validate_order(self):
        game_details = GameDetail(uuid=self.id)
        last_player = game_details[-1].player
        return last_player == self.owner

    def do_move(self, player, coordinate):
        game_detail = GameDetail()
        game_detail.uuid = self.id
        game_detail.coordinate = coordinate
        game_detail.player = player
        game_detail.save()
        pass

    def get_table(self):
        game_details = GameDetail(uuid=self.id)
        self.coordinates = []
        for detail in game_details:
            self.coordinates.append([detail.coordinate, detail.player])
        return self.coordinates

    def share(self, guest):
        self.infra.email.send(guest, self.id)

    def check_winner(self, player):
        moves = GameDetail(uuid=self.id, player=player)
        results = {}
        j = 0
        for i, move in enumerate(moves):
            if i == 2 or i == 4 or i == 6 or i == 8:
                j+=1
            if results[j] is None:
                results[j] = ""
            results[j] += str(move.coordinate)
        for result in results:
            if self.combinations.contains(result):
                self.infra.event.notify(f"WIINER: {self.id}")
                self.game_stop()
                
    def game_stop(self):
        self.started = False