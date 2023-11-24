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
    VERSION = "v 7 log bet"

    def has_pair(self, hole_cards):
        if hole_cards[0]["rank"] == hole_cards[1]["rank"]:
            return True
        return False

    def betRequest(self, game_state):
        bet = 0
        print(f"version: {self.VERSION} ")
        print(game_state)

        in_action = game_state["in_action"]
        our_data = game_state["players"][in_action]
        stack = our_data["stack"]

        hole_cards = our_data["hole_cards"]

        if self.has_pair(hole_cards):
            print("We have a pair")
            if hole_cards[0]["rank"] in ("10", "J", "Q", "K", "A"):
                print("We have a premium pair")
                bet = stack
        print(f"Our decision: {bet}")
        return bet

    def showdown(self, game_state):
        pass
