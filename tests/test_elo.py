from ratings.elo import elo_expected, elo_update
# These tests are trivial for Elo but less so for other schemes


def test_elo_scale_invariance():
    assert abs( elo_expected(d=100.0,f=400.) - elo_expected(d=50.0,f=200.) ) < 1e-4


def test_elo_bounds():
    for d in [-1e10,0,1e10]:
        e = elo_expected(d=d)
        assert 0<=e<=1


def test_elo_sign():
    assert elo_expected(d=10)<0.5


def test_elo_update():
    w,b = elo_update(white_elo=500,black_elo=2500,points=1.0,k=100)
    w_check = 600
    assert abs(w-w_check)<0.1


if __name__=='__main__':
    test_elo_update()
    test_elo_bounds()
    test_elo_sign()
    test_elo_scale_invariance()