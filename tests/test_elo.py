
from ratings.elo import elo_expected


def test_elo_scale_invariance():
    assert abs( elo_expected(d=100.0,f=400.) - elo_expected(d=50.0,f=200.) ) < 1e-4

