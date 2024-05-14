#Source: https://stackoverflow.com/questions/37044191/nameerror-name-var-not-defined-in-if-statement
for index, row in dfcodes.iterrows():
    # for each security code identify those with 3 down candles and narrowing raneg for first 3 days of 6 day set
    scode=row['Security_Code']

    tdate='2016-01-15'
    df=fetch_last(scode,tdate,6)
    dfreverse=df.sort('TradeDate', ascending=True)

    #look for 3 consecutive down candles with narrowing range and then 2 up candles
    dfdownbars=dfreverse.head(5)
    ncnt=1

    for index,row in dfdownbars.iterrows():
        otmp = row['Opening_Price']
        ctmp = row['Closing_Price']
        rtmp = abs(row['Opening_Price'] - row['Closing_Price'])
        dtmp = row['TradeDate']
        if ctmp<otmp and ncnt==1:
            o1 = otmp
            c1 = ctmp
            r1 = rtmp
            d1 = dtmp
            ncnt+=1
        elif ctmp<otmp and otmp<o1 and ctmp<c1 and rtmp<=r1 and ncnt==2:
            o2 = otmp
            c2 = ctmp
            r2 = rtmp
            d2 = dtmp
            ncnt += 1
        elif ctmp<otmp and otmp<o2 and rtmp<=r2 and ncnt==3:
            o3 = otmp
            c3 = ctmp
            r3 = rtmp
            d3 = dtmp
            ncnt += 1
        elif ctmp > otmp and ctmp > c3 and ncnt==4:  # first up candle after 3 downs
            o4 = otmp
            c4 = ctmp
            r4 = rtmp
            ncnt += 1
        else:
            break

    cnt -= 1