import random

example = {'tournament_id': '655e6ea29c97ef0002da0843',
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


class Player:
    VERSION = "v13 premium"

    def has_pair(self, hole_cards):
        print("Checking for pair...")
        if hole_cards[0]["rank"] == hole_cards[1]["rank"]:
            print("We have a pair")
            return True
        return False

    def has_suited(self, hole_cards):
        print("Checking for suited cards...")
        if hole_cards[0]["suit"] == hole_cards[1]["suit"]:
            print("We have suited")
            return True
        return False

    def betRequest(self, game_state):
        print(f"version: {self.VERSION} ")
        print(game_state)

        bet = 0
        our_data = self._get_our_data(game_state)
        hole_cards = our_data["hole_cards"]

        try:
            if self.is_raised_pot(game_state):
                if self.has_pair(hole_cards) and self.has_premium_pair(hole_cards):
                    bet = our_data["stack"]
            else:
                if self.need_bluff():
                    bet = our_data["stack"]
                if self.has_pair(hole_cards) and self.has_high_pair(hole_cards):
                    bet = our_data["stack"]
                elif self.has_suited(hole_cards) and self.is_AK(hole_cards):
                    bet = our_data["stack"]
        except:
            pass

        print(f"Our decision: {bet}")
        return bet

    def has_high_pair(self, hole_cards):
        print("Checking for high pair...")
        if hole_cards[0]["rank"] in ("10", "J", "Q", "K", "A"):
            print("We have a good pair")
            return True
        return False

    def has_premium_pair(self, hole_cards):
        print("Checking for premium pair...")
        if hole_cards[0]["rank"] in ("Q", "K", "A"):
            print("We have a premium pair")
            return True
        return False

    def is_AK(self, hole_cards):
        print("Checking for AK...")
        if {hole_cards[0]["rank"], hole_cards[1]["rank"]} == {"A", "K"}:
            print("is AK")
            return True
        return False

    def _get_our_data(self, game_state):
        our_data = game_state["players"][game_state["in_action"]]
        return our_data

    def showdown(self, game_state):
        pass

    def need_bluff(self, chance=0.05):
        print("Checking if bluff is needed...")
        val = random.randint(1, 100)
        if val < 5:
            print(f"Bluffing because we got {val}...")
            return True
        return False

    def is_raised_pot(self, game_state):
        cutoff_point = game_state["small_blind"] * 8
        print(f"Checking for raised pot (cutoff={cutoff_point})...")

        is_raised = game_state["pot"] > cutoff_point
        if is_raised:
            print(f"Pot is raised to {game_state['pot']}")
            return True
        return False
