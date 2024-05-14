#Source: https://stackoverflow.com/questions/57560922/typeerror-function-object-is-not-iterable-when-i-am-not-calling-any-functions
import pandas as pd
from datetime import datetime, timedelta

data = ['2019-01-01']
only_onboarding = pd.DataFrame(data, columns = ['ClosedDate'])

cycle_times = pd.DataFrame;
today = datetime.today();
for i in range(today.month - 1):  # Regex Model: 2019-08-\d\d$
    regx = "";

    if (i + 1 < 10):
        regx = str(today.year) + '-0' + str(i + 1) + '-\d\d$';
    else:
        regx = str(today.year) + '-' + str(i + 1) + '-\d\d$';

of_month = only_onboarding['ClosedDate'].filter(lambda x: re.match(regx, x));