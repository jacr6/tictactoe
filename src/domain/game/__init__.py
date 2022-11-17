from multiprocessing import Process
from domain.infraAdapter import *
import uuid


class GameDomain(object):
    """ 
    Business Definition of TICTACTOE GAME\n
    Args:
        object (_type_): _description_
    """

    def __init__(self, player, game_id):
        """Constructor

        Args:
            player (_type_): _description_
        """
        self.infra = InfraDomain()

        if game_id is None:
            self.owner = player
            self.id = uuid.uuid1()
            self.players = [self.owner]
            self.persistence = self.infra.models.Game()
            self.persistence.owner = self.owner
            self.persistence.uuid = self.id
            self.persistence.save()
        else:
            self.persistence = self.infra.models.Game(uuid=game_id)
            self.owner = self.persistence.owner
            self.id = game_id
            self.players = [self.owner, player]
            self.persistence.guest = player
            self.persistence.save()
        self.started = False
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
        """to join into a game
        Args:
            uuid (_type_): _description_
        """
        if uuid == self.id:
            if self.match():
                self.play()
        pass

    def match(self):
        """validate if the players are completed

        Returns:
            _type_: _description_
        """
        return len(self.players) == 2

    def play(self):
        """to start the game
        """
        self.started = True
        Process(target=self.game_start).start()

    def game_start(self):
        """to start the game
        """
        while self.started:
            last = self.get_last()
            table = self.get_table()
            winner = self.check_winner(table)

    def get_last(self):
        """get the last move

        Returns:
            _type_: _description_
        """
        game_details = self.infra.models.GameDetail(uuid=self.id)
        last_player = game_details[-1].player
        return last_player == self.owner

    def get_table(self):
        """get table info to refresh frontend

        Returns:
            _type_: _description_
        """
        game_details = self.infra.models.GameDetail(uuid=self.id)
        self.coordinates = []
        for detail in game_details:
            self.coordinates.append([detail.coordinate, detail.player])
        return self.coordinates

    def check_winner(self, player):
        """to check winner

        Args:
            player (_type_): _description_
        """
        moves = self.infra.models.GameDetail(uuid=self.id, player=player)
        results = {}
        j = 0
        for i, move in enumerate(moves):
            if i == 2 or i == 4 or i == 6 or i == 8:
                j += 1
            if results[j] is None:
                results[j] = ""
            results[j] += str(move.coordinate)
        for result in results:
            if self.combinations.contains(result):
                self.infra.event.notify(f"WINER ON {self.id}")
                self.game_stop()

    def game_stop(self):
        """to stop the game
        """
        self.started = False

    def do_move(self, player, coordinate):
        """to move into the game

        Args:
            player (_type_): _description_
            coordinate (_type_): _description_
        """
        last = self.get_last()
        if last != player:
            game_detail = self.infra.models.GameDetail()
            game_detail.uuid = self.id
            game_detail.coordinate = coordinate
            game_detail.player = player
            game_detail.save()
            pass

    def share(self, guest):
        """sharing via email the game id to join

        Args:
            guest (_type_): _description_
        """
        self.infra.email.send(guest, self.id)
