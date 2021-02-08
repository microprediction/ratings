# ratings
Elo ratings, and generalizations


    from ratings.elorating import elo_expected, elo_update
    elo_expected(d=234)
    new_white_rating, new_black_rating = elo_update(white_rating=1745,black_rating=1940,points=0.5)
    
