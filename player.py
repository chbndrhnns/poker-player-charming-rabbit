from pydantic import BaseModel


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
        return minimum_raise + self.small_blind

    def fold(self):
        ...

    def check(self):
        ...


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        game = Game.model_validate(game_state)
        return game.raise_amount()

    def showdown(self, game_state):
        pass
