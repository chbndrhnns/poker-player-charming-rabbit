import logging

from pydantic import BaseModel

UPPER_BET_THRESHOLD = 101


class Player1(BaseModel):
    name: str
    bet: int


class Game(BaseModel):
    current_buy_in: int
    minimum_raise: int
    players: list[Player1]
    in_action: int
    small_blind: int

    def raise_amount(self):
        minimum_raise = self.current_buy_in - self.players[
            self.in_action].bet + self.minimum_raise
        print(f"Minimum raise: {minimum_raise}")
        return minimum_raise + self.small_blind

    def fold(self):
        ...

    def check(self):
        ...


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print(game_state)
        game = Game.model_validate(game_state)
        raise_amount = game.raise_amount()

        if raise_amount > UPPER_BET_THRESHOLD:
            print("'raise_amount' is larger than our threshold.")
            raise_amount = 0

        return raise_amount

    def showdown(self, game_state):
        pass
