#Source: https://stackoverflow.com/questions/56621969/attribute-error-with-list-of-stock-tickers
file = 'techtickerlist.csv'
with open(file) as f:
    reader = csv.reader(f)
    technologyTickers = []
    for row in reader:
        technologyTickers.append(row[0])

def scrape(stock_list, interested, technicals):
    SuggestedStocks = []
    for each_stock in stock_list:
        try:
            technicals = scrape_yahoo(each_stock)
            condition_1 = float(technicals.get('Return on Equity',0).replace('%','').replace('N/A','-100').replace(',','')) > 25
            condition_2 = float(technicals.get('Trailing P/E',0).replace('N/A','0').replace(',','')) < 25
            condition_3 = float(technicals.get('Price/Book',0).replace('N/A','100')) <8
            condition_4 = float(technicals.get('Beta (3Y Monthly)',0).replace('N/A','100')) <1.1
            if condition_1 and condition_2 and condition_3 and condition_4:
                print(each_stock)
                SuggestedStocks.append(each_stock)  
                for ind in interested: 
                    print(ind + ": "+ technicals[ind])         
                print("------")
                time.sleep(1)   
        except ValueError:
                print('Value Error')
                return
                                              # Use delay to avoid getting flagged as bot
    #return technicals
    print(SuggestedStocks)


def main():

    stock_list = technologyTickers
    interested = ['Return on Equity', 'Revenue', 'Quarterly Revenue Growth','Trailing P/E', 'Beta (3Y Monthly)','Price/Book']
    technicals = {}

    tech = scrape(stock_list, interested, technicals)
    print(tech)