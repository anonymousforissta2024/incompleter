#Source: https://stackoverflow.com/questions/57343405/typeerror-unhashable-type-list-when-adding-a-count-variable-works-without
def add_entry(count,balance_list, Token1_balances, Token2_balances, Token3_balances,localtime):

   # check if in seen set
   if (count,Token1_balances, Token2_balances, Token3_balances,localtime) in seen:
       return balance_list

   # add to seen set
   seen.add(tuple([count,Token1_balances, Token2_balances, Token3_balances,localtime]))

   # append to results list
   balance_list.append({'count':count,Token1: Token1_balances, Token2: Token2_balances, Token3: Token3_balances,'time':localtime})

   return balance_list


def write_to_json(lst, fn):
    with open(fn, 'a', encoding='utf-8') as file:
        for item in lst:
            x = json.dumps(item, indent=4)
            file.write(x + '\n')


balance_list = []
seen = set()

if __name__ == '__main__':

  print('-'*40)   
  print(" Service Online and logging file has been established")
  print('-'*40)  

  n = 0 
  while True:
    time.sleep(throttleClient)
    localtime = time.asctime( time.localtime(time.time()) )
    minute = datetime.datetime.now().minute
    print('Local current time:',localtime,'CDT\n')
    if minute % throttleApi == 0:
     try:

        count = str(n + 1)
        balance_query   = p2p.getBalances()["result"]
        Token1_balances = str(balance_query[Token1])
        Token2_balances = str(balance_query[Token2])
        Token3_balances = str(balance_query[Token3])
        args1 = [count,Token1_balances, Token2_balances, Token3_balances,localtime]
        balance_list = add_entry(balance_list, *args1)  # add entry - SUCCESS  
        write_to_json(balance_list, 'balance.json') 
     except requests.exceptions.ConnectionError as e:
        print(ConnectionError)
        print('-'*20)
        print("Can't log balances due to connection error")
        pass
    else:
      pass           