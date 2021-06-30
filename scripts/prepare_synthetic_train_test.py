import time
from ratings.simulation.generation import mock_data
from ratings.hereiam import TRAIN_CSV, TEST_CSV

if __name__=='__main__':
    st = time.time()
    df = mock_data(n_contestants=1000, n_days=1000)
    print(df)
    print(time.time()-st)
    print(len(df))
    df[:-30000].to_csv(TRAIN_CSV)
    df[-30000:].to_csv(TEST_CSV)