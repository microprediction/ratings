from ratings.elo import elo_expected
# These tests are trivial for Elo but less so for other schemes


def test_elo_scale_invariance():
    assert abs( elo_expected(d=100.0,f=400.) - elo_expected(d=50.0,f=200.) ) < 1e-4


def test_elo_bounds():
    for d in [-1e10,0,1e10]:
        assert 0<elo_expected(d=d)<1


def test_elo_sign():
    assert elo_expected(d=10)<0.5