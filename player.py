import json
import logging
from typing import Optional

import requests
from pydantic import BaseModel

UPPER_BET_THRESHOLD = 101


#
# wait out and don't raise while others are fighting
class Card(BaseModel):
    rank: str
    suit: str


class Player1(BaseModel):
    name: str
    bet: int
    stack: int
    hole_cards: Optional[str] #Optional[list[Card]]


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
    data = {'tournament_id': '655e6ea29c97ef0002da0843',
            'game_id': '655f51fb5485f700028038ee', 'round': 7, 'players': [
            {'name': 'Charming Rabbit', 'stack': 986, 'status': 'active', 'bet': 0,
             'hole_cards': [{'rank': 'Q', 'suit': 'hearts'},
                            {'rank': '2', 'suit': 'spades'}], 'time_used': 1983241,
             'version': 'Default Python folding player', 'id': 0},
            {'name': 'PokerGPT', 'stack': 2024, 'status': 'active', 'bet': 2,
             'time_used': 1994034, 'version': '5 with a test', 'id': 1},
            {'name': 'Green Rabbits', 'stack': 0, 'status': 'out', 'bet': 0,
             'time_used': 282888, 'version': '2 - with sysout', 'id': 2},
            {'name': 'The Semiprofessionals', 'stack': 984, 'status': 'active', 'bet': 4,
             'time_used': 1997195, 'version': 'Kotlin Player 0.0.1', 'id': 3}],
            'small_blind': 2, 'big_blind': 4, 'orbits': 1, 'dealer': 0,
            'community_cards': [], 'current_buy_in': 4, 'pot': 6, 'in_action': 0,
            'minimum_raise': 2, 'bet_index': 3}

    def get_our_data(self):
        for player in self.players:
            if player.name == 'Charming Rabbit':
                return player

    VERSION = "v 5 in progress"

    def call_ranking(self):
        cards = [{"rank": "5", "suit": "diamonds"},
                 {"rank": "6", "suit": "diamonds"},
                 {"rank": "7", "suit": "diamonds"},
                 {"rank": "7", "suit": "spades"},
                 {"rank": "8", "suit": "diamonds"},
                 {"rank": "9", "suit": "diamonds"}
                 ]
        data = f'cards={json.dumps(cards)}'
        response = requests.post("http://rainman.leanpoker.org/rank", data=data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
        return response.json()

    def check_pair(self, our_cards):
        return our_cards



    def betRequest(self, game_state):
        print(f"version: {self.VERSION} ")
        print(game_state)
        return 0
        in_action = game_state["in_action"]
        our_data = game_state["players"][in_action]
        #game = Game.model_validate(game_state)
        #our_data = game.get_our_data()
        do_i_have_pair = check_pair(our_data.hole_cards)
        #return our_data.stack

    def showdown(self, game_state):
        pass
