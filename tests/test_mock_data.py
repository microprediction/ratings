import time
from ratings.simulation.generation import mock_data


def test_mock():
    df = mock_data(n_contestants=100, n_days=100)