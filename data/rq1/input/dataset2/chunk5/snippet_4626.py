#Source: https://stackoverflow.com/questions/52488617/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method
df = pd.DataFrame({'Date':[], 'Link':[], 'APR Rate':[]})
#cycle through links in array until it finds APR rates/fixed or variable using regex
for link in plcompetitors:
    cdate = datetime.date.today()
    sdate = str(cdate)
    l = r.get(link)
    l.encoding = 'utf-8'
    data = l.text
    soup = bs(data, 'html.parser')
    paragraph = soup.find_all(text=re.compile('[0-9]%'))
    for n in paragraph:
        matches = re.findall('(?i)\d+(?:\.\d+)?%\s*(?:to|-)\s*\d+(?:\.\d+)?%', n.string)
        try:
            irate = str(matches[0])
            df2 = pd.DataFrame({'Date':[cdate], 'Link':[link], 'APR Rate':[irate]})
            df = pd.concat([df, df2], join="inner")
            df.drop_duplicates(subset='Link', keep='first', inplace=True)
            s1 = df['APR Rate'].values.tolist()
            s1.insert(0, sdate)
        except IndexError:
            pass
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    spreadsheet_id = '1vk5uZQ-nJgTURH6P9Gq0QyyixsMN8e8hionS_ucko2g'
    range_ = "'Personal Loan'!B1:D"
    value_input_option = 'RAW'
    value_range_body = {
        "majorDimensions": "ROWS"
        ["values":
            s1
        ]
    }
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_,
                                                 valueInputOption=value_input_option, body=value_range_body)
    response = request.execute()
    pprint(response)

if __name__ == '__main__':
    main()