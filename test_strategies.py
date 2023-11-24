import pytest

from player import Player


class TestSuites:

    def test_has_suited__False(self):
        cards = [{'rank': 'Q', 'suit': 'hearts'},
                 {'rank': '2', 'suit': 'spades'}]

        assert Player().has_suited(cards) is False

    def test_has_suited__True(self):
        cards = [{'rank': 'Q', 'suit': 'spades'},
                 {'rank': '2', 'suit': 'spades'}]

        assert Player().has_suited(cards) is True

    def test_is_AKs__True(self):
        cards = [{'rank': 'K', 'suit': 'hearts'},
                 {'rank': 'A', 'suit': 'hearts'}]

        assert Player().is_AK(cards) is True

    def test_is_AKs__False(self):
        cards = [{'rank': '10', 'suit': 'hearts'},
                 {'rank': 'A', 'suit': 'hearts'}]

        assert Player().is_AK(cards) is False


class TestPairs:

    def test_has_pairs__True(self):
        cards = [{'rank': '2', 'suit': 'hearts'},
                 {'rank': '2', 'suit': 'spades'}]

        assert Player().has_pair(cards) is True

    def test_has_pairs__False(self):
        cards = [{'rank': 'Q', 'suit': 'spades'},
                 {'rank': '2', 'suit': 'spades'}]

        assert Player().has_pair(cards) is False

    def test_has_good_pair__True(self):
        cards = [{'rank': '10', 'suit': 'hearts'},
                 {'rank': '10', 'suit': 'spades'}]

        assert Player().has_high_pair(cards) is True

    def test_has_good_pairs__False(self):
        cards = [{'rank': '2', 'suit': 'spades'},
                 {'rank': '2', 'suit': 'spades'}]

        assert Player().has_high_pair(cards) is False


class TestRaisedPot:

    def test_false(self):
        gamestate = {"pot": 6, "small_blind": 2, "big_blind": 4}
        assert Player().is_raised_pot(gamestate) is False

    @pytest.mark.parametrize("state", [
        {"pot": 7, "small_blind": 2, "big_blind": 4},
    ])
    def test_true(self, state):
        assert Player().is_raised_pot(state) is True
