# TODO: Once core is its own package, move these tests.  They're here currently
# so that they can be easily run by the Django test runner.

from unittest import TestCase

from core.runner import Result, ResultType, run_game
from noughtsandcrosses import game


class RunGameTests(TestCase):
    def test_bot1_wins(self):
        # X | O | X
        # --|---|--
        # O | X | O
        # --|---|--
        # X | . | .

        result = run_game(game, get_next_move_1, get_next_move_1)

        expected_result = Result(
            result_type=ResultType.COMPLETE,
            score=1,
            move_list=[0, 1, 2, 3, 4, 5, 6],
            traceback=None,
        )

        self.assertEqual(result, expected_result)

    def test_bot2_wins(self):
        # . | X | O
        # --|---|--
        # X | O | X
        # --|---|--
        # O | . | .

        result = run_game(game, get_next_move_2, get_next_move_2)

        expected_result = Result(
            result_type=ResultType.COMPLETE,
            score=-1,
            move_list=[1, 2, 3, 4, 5, 6],
            traceback=None,
        )

        self.assertEqual(result, expected_result)

    def test_draw(self):
        # X | X | O
        # --|---|--
        # O | O | X
        # --|---|--
        # X | X | O

        result = run_game(game, get_next_move_3, get_next_move_4)

        expected_result = Result(
            result_type=ResultType.COMPLETE,
            score=0,
            move_list=[0, 2, 1, 3, 5, 4, 6, 8, 7],
            traceback=None,
        )

        self.assertEqual(result, expected_result)


def get_next_move_1(board):
    """Return first available move."""

    available_moves = game.available_moves(board)
    return available_moves[0]


def get_next_move_2(board):
    """Return second available move."""

    available_moves = game.available_moves(board)
    return available_moves[1]


def get_next_move_3(board):
    """Return player X move to ensure draw."""

    available_moves = game.available_moves(board)
    for move in [0, 1, 5, 6, 7]:
        if move in available_moves:
            return move


def get_next_move_4(board):
    """Return player O move to ensure draw."""

    available_moves = game.available_moves(board)
    for move in [2, 3, 4, 8]:
        if move in available_moves:
            return move
