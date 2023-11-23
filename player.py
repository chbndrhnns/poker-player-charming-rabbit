import logging

from pydantic import BaseModel

UPPER_BET_THRESHOLD = 101


class Player1(BaseModel):
    name: str
    bet: int
    stack: int


class Game(BaseModel):
    current_buy_in: int
    minimum_raise: int
    players: list[Player1]
    in_action: int
    small_blind: int

    def raise_amount(self):
        return 10000

    def fold(self):
        ...

    def check(self):
        ...

    def get_our_data(self):
        for player in self.players:
            if player.name == 'Charming Rabbit':
                return player


class Player:
    VERSION = "v 2 immediate all in"
    print(VERSION)

    def betRequest(self, game_state):
        print(game_state)
        game = Game.model_validate(game_state)
        our_data = game.get_our_data()
        return our_data.stack

    def showdown(self, game_state):
        pass
