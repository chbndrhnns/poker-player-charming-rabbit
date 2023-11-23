import json
import logging

import requests
from pydantic import BaseModel

UPPER_BET_THRESHOLD = 101

#
#wait out and don't raise while others are fighting


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
    VERSION = "v 3 rank API call"

    def call_ranking(self):
        cards = [{"rank":"5","suit":"diamonds"},
    {"rank":"6","suit":"diamonds"},
    {"rank":"7","suit":"diamonds"},
    {"rank":"7","suit":"spades"},
    {"rank":"8","suit":"diamonds"},
    {"rank":"9","suit":"diamonds"}
]
        data = f'cards={json.dumps(cards)}'
        response = requests.post("http://rainman.leanpoker.org/rank", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return response.json()

    def betRequest(self, game_state):
        print(f"version: {self.VERSION} ")
        print(game_state)
        game = Game.model_validate(game_state)
        our_data = game.get_our_data()
        return our_data.stack

    def showdown(self, game_state):
        pass
