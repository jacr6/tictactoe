from multiprocessing import Process


class GameDomain(object):
    def __init__(self, *args):
        player1, player2 = args
        self.player1 = player1
        self.player2 = player2
        
        Process(target=self.get_table_state).start()
        pass

    def join(self, *args, **kwargs):
        pass

    def match(self, *args, **kwargs):
        pass

    def play(self, *args, **kwargs):
        pass

    def record(self, *args, **kwargs):
        pass

    def validate_two_players(self, player1, player2):
        res = validate_order(player1, player2)
        if res:
            return True
        return False
        pass

    def validate_order(self, player1, player2):
        return True
        pass

    def get_table_state(self):
        while True:
            res = self.get_table()
            res = self.check_winner(res)
            pass
        
    def do_move(self, player, coordinate):
        move = Move
        
    
    def get_table(self):
        pass
