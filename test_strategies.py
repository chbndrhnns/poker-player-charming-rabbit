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

        assert Player().has_good_pair(cards) is True

    def test_has_good_pairs__False(self):
        cards = [{'rank': '2', 'suit': 'spades'},
                       {'rank': '2', 'suit': 'spades'}]

        assert Player().has_good_pair(cards) is False
