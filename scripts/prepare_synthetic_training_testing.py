# Adds posterior dividends to synthetic data ... can take awhile.
from ratings.hereiam import TRAIN_CSV, TRAINING_CSV, TEST_CSV, TESTING_CSV
import pandas as pd
from ratings.inference.inference import truncate, add_posterior_dividend, calibrate
from pprint import pprint


if __name__=='__main__':
    for (source,dest) in [ (TRAIN_CSV, TRAINING_CSV), (TEST_CSV,TESTING_CSV)]:
        print('Reading '+source)
        df = pd.read_csv(source)
        print('  calibrating ...')
        calib_df = truncate(df, n_performances=5000)
        calib_df, idio_std, ability_std, performance_std, empirical_std = calibrate(calib_df, loop=False)
        pprint({"idio":idio_std,'ability':ability_std,'performance':performance_std,'empirical':empirical_std})
        print('  calibration done. Adding posterior dividends ')
        df = add_posterior_dividend(df, ability_std = ability_std, idio_std=idio_std)
        print('  posterior dividends added')
        print(calib_df)
        calib_df.to_csv(dest)
        print('Saved '+dest)