#Source: https://stackoverflow.com/questions/46270950/nameerror-variable-not-displaying-stored-text
if (salesavg < 5000):
    rank = "SAD SALESMEN"
    if (salesavg >= 5000 or salesavg <= 8000):
        rank = "LOW SALESMAN"
        if (salesavg >= 8001 or salesavg <= 9000):
            rank = "MID SALESMAN"
            if (salesavg >= 9001 or salesavg <= 10000):
                rank = "EXCELLENT SALESMAN"
                if (salesavg > 10000):
                   rank = "TOP SALESMAN"