#Source: https://stackoverflow.com/questions/55629181/calibration-and-holdout-data-attributeerror-int-object-has-no-attribute-n
from lifetimes.utils import calibration_and_holdout_data

summary_cal_holdout = calibration_and_holdout_data(df2, 'person_id', 'effective_date',
                                        calibration_period_end='2017-12-31',
                                        observation_period_end='2018-12-31')

print(summary_cal_holdout.head())