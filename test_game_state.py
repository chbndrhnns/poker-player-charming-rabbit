from player import Game, Player1, Player

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


def test_game_state():
    actual = Game.model_validate(data)
    assert actual.current_buy_in == 4


def test_minimum_raise_amount():
    actual = Game.model_validate(data)
    assert actual.raise_amount() == 8

def test_check_if_bet_is_above_threshold():
    other = Player1(name="other", bet=101)
    us = Player1(name="us", bet=50)
    actual = Game(players=[other, us], current_buy_in=0, in_action=0, minimum_raise=2, small_blind=10)
    assert actual.raise_amount() == 0

def test_call_ranking():
    response = Player().call_ranking()
    assert response == None

def test_check_pair():
    actual = Game.model_validate(data)
    response = Player().check_pair(actual.get_our_data().hole_cards)
    assert response == None