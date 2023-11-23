import dataclasses


@dataclasses.dataclass
class GameState:
    current_buy_in: int


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        # parse game_state
        print(game_state)
        return 1

    def showdown(self, game_state):
        pass

